import argparse_subcommand as ap_sub
import sys

def main(argv: list[str]):

	explanation = "My Little Helpers: a collection of small utility programs" 
	parser = ap_sub.ArgumentParser(epilog=explanation)
	parser.scan("subcmds.gitac", "subcmds.lsnew")
	args = parser.parse_args(argv[1:])
	parser.execute_subcommand(args)

if __name__ == '__main__':
	main(sys.argv)
