import argparse_subcommand as ap_sub

meaning = "some help text for the subcommand"

def add_arguments(parser: ap_sub.ArgumentParser): 
	pass

def execute(args: ap_sub.Namespace): 
	print(args)
