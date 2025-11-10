import argparse_subcommand as ap_sub
import ast
import os
import inspect

meaning = "Zeigt an, welcher Anteil der möglichen AST-Knotentypen in den Dateien vorkommt."

def add_arguments(parser: ap_sub.ArgumentParser): 
	parser.add_argument("-v", "--verbose", action="store_true" ,help="Zeigt eine detaillierte Analyse der Knotenarten an")
	parser.add_argument("filename", nargs="+", help="List of files")

def execute(args):
	filenames = args.filename
	verbose = getattr(args, "verbose", getattr(args, "v", False))

	used_types = used_nodetypes(args)

	g = groups_with_unknown()
	all_types = all_nodetypes()
	covered_union = set().union(*g.values())
	missing = all_types - covered_union
	extra   = covered_union - all_types
	overlaps = []
	keys = list(g)
	for i in range(len(keys)):
		for j in range(i+1, len(keys)):
			o = g[keys[i]] & g[keys[j]]
			if o:
				overlaps.append((keys[i], keys[j], sorted(o)))

	assert not missing and not extra and not overlaps, (
		f"Fehlt: {sorted(missing)} | Zuviel: {sorted(extra)} | "
		f"Überschneidungen: {overlaps}"
	)


	if args.verbose:
		gdict = groups_with_unknown_and_extras()
		order = ["basic","expressions","statements","definitions","other",
				"ignore","deprecated","abstract","undocumented","unknown"]
		print("Fraction of possible node types that occured per node type group:")
		total_u = total_n = 0
		for i, g in enumerate(order, 1):
			members = gdict.get(g, set())
			u = len(used_types & members)
			n = len(members)
			if n == 0:
				pct = 0
			else:
				pct = u / n * 100
				total_u += u; total_n += n
			print(f"{i:>2} {g.capitalize():<11}: {u:>2} / {n:<3} {pct:>3.0f}%")
		if total_n:
			print(f"   TOTAL: {total_u:>2} / {total_n:<3} {(total_u/total_n*100):>3.0f}%")

		unknown_members = gdict.get("unknown", set())
		if unknown_members:
			print("\nUnknown node types (not covered by any group):")
			for name in sorted(unknown_members):
				print(f"  - {name}")

	all_types = all_nodetypes()
	used_percentage = (len(used_types) / len(all_types) * 100) if all_types else 0
	print(f"Verwendeter Anteil der Knotenarten: {used_percentage:.2f}%")
    
def all_nodetypes() -> set[str]:
    raw = {
        name for name, obj in ast.__dict__.items()
        if inspect.isclass(obj) and issubclass(obj, ast.AST) and not name.startswith("_")
    }
    classes = {n: getattr(ast, n) for n in raw}

    ignore = {n for n, c in classes.items() if issubclass(c, ast.mod)}
    if "FunctionType" in raw:   # ggf. versionsabhängig vorhanden
        ignore.add("FunctionType")

    deprecated = {"Suite", "Index", "ExtSlice", "Param", "AugLoad", "AugStore"} & raw

    abstract = {n for n in raw if n == "AST" or n.islower()}  

    undocumented = {n for n in raw if not getattr(getattr(ast, n), "__doc__", None)}
    undocumented -= (ignore | deprecated | abstract)  
    return raw - ignore - deprecated - abstract - undocumented


def nodetypes(pythontext: str) -> set[str]:

	try: 
		tree = ast.parse(pythontext)
		return {type(node).__name__ for node in ast.walk(tree)}
	except SyntaxError as e:
		print(f"Syntaxfehler in Datei: {e.filename}, Zeile {e.lineno}, Fehler: {e.msg}")
		return set()

def used_nodetypes(args):
    filenames = args.filename
    used_types = set()
    
    for filename in filenames:
        if not filename.endswith('.py'):
            print(f"Warnung: Datei {filename} ist keine Python-Datei und wird übersprungen")
            continue
        
        if not os.path.exists(filename):
            print(f"Warnung: Datei {filename} existiert nicht.")
            continue
        
        with open(filename, 'r') as pyfile:
            pythontext = pyfile.read()
            used_types.update(nodetypes(pythontext))
            
    return used_types


groups = {
    "basic": ["Literal", "Name"],
    "expressions": ["BinOp", "Call", "Compare"],
    "statements": ["If", "While", "For"],
    "definitions": ["FunctionDef", "ClassDef"],
    "other": ["Match", "TypeAnnotation", "AsyncFunctionDef"]
}

def categorize_node_types(node: ast.AST) -> str:
    
    for group, node_types in groups.items():
        if type(node).__name__ in node_types:
            return group
    return "other"

def analyze_file(filename: str):
   
    with open(filename, "r") as f:
        tree = ast.parse(f.read())
        
    used_types_in_file = {type(n).__name__ for n in ast.walk(tree)}
    group_counts = {g: 0 for g in groups}
    
    for g, node_names in groups.items():
        group_counts[g] = len(used_types_in_file.intersection(node_names))
        
    return group_counts

def build_groups() -> dict[str, set[str]]:
    names = all_nodetypes()
    classes: dict[str, type[ast.AST]] = {n: getattr(ast, n) for n in names}

    definitions = {"FunctionDef", "AsyncFunctionDef", "ClassDef"} & names

    statements = {n for n, c in classes.items() if issubclass(c, ast.stmt)} - definitions

    basic = {
        "Name", "Constant", "Attribute", "Subscript", "Starred",
        "List", "Tuple", "Set", "Dict", "JoinedStr", "FormattedValue",
    } & names

    expressions = {n for n, c in classes.items() if issubclass(c, ast.expr)} - basic

    covered = definitions | statements | basic | expressions
    other = names - covered

    return {
        "basic": basic,
        "expressions": expressions,
        "statements": statements,
        "definitions": definitions,
        "other": other,
    }



def groups_with_unknown() -> dict[str, set[str]]:
    base = build_groups()
    covered = set().union(*base.values()) if base else set()
    base["unknown"] = all_nodetypes() - covered
    return base



def groups_with_unknown() -> dict[str, set[str]]:
    base = build_groups()  # <-- statt aus dem globalen 'groups'
    covered = set().union(*base.values()) if base else set()
    base["unknown"] = all_nodetypes() - covered
    return base

def split_unknown(unknown: set[str]) -> dict[str, set[str]]:

    classes: dict[str, type[ast.AST]] = {
        name: obj for name, obj in ast.__dict__.items()
        if inspect.isclass(obj) and issubclass(obj, ast.AST)
    }

    ignore = {n for n, c in classes.items() if issubclass(c, ast.mod)} & unknown

    if "FunctionType" in unknown:
        ignore.add("FunctionType")

    deprecated_known = {"Suite", "Index", "ExtSlice", "Param", "AugLoad", "AugStore"} & unknown

    abstract = {n for n in unknown if n == "AST" or n.islower()}  # AST oder kleingeschriebene Basen wie mod/stmt/expr/…

    undocumented = unknown - ignore - deprecated_known - abstract

    return {
        "ignore": ignore,
        "deprecated": deprecated_known,
        "abstract": abstract,
        "undocumented": undocumented,
    }
    
def groups_with_unknown_and_extras() -> dict[str, set[str]]:
    base = build_groups()
    covered = set().union(*base.values()) if base else set()
    unknown = all_nodetypes() - covered
    extras = split_unknown(unknown)

    for k, s in extras.items():
        base[k] = s

    base["unknown"] = all_nodetypes() - set().union(*base.values())
    return base