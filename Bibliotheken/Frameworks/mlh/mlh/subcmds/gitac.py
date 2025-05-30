import argparse_subcommand as ap_sub

meaning = "some help text for the subcommand"

def add_arguments(parser: ap_sub.ArgumentParser): 
	parser.add_argument("-m", "--message", help="Commit message")
	parser.add_argument("file", nargs="+", help="List of files")


def execute(args: ap_sub.Namespace): 
	print(args)
