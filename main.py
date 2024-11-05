import argparse

from lib import cloning

parser = argparse.ArgumentParser(description="repository search")

parser.add_argument("repolink", help="The repository hosting")

args = parser.parse_args()

print(args.repolink)
cloning.temp_clone(args.repolink)

