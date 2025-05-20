import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help ="echo is string")
args = parser.parse_args()
print(args.echo)