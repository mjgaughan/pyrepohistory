import argparse
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
from lib import cloning, commit_analysis
from lib import primary_language as pl

parser = argparse.ArgumentParser(description="repository search")

parser.add_argument("repolink", help="The repository hosting")

args = parser.parse_args()

print(args.repolink)
temp_repo, temp_repo_path = cloning.temp_clone(args.repolink)
commits_dict = commit_analysis.commit_analysis(temp_repo)
# TODO: here goes static/dynamic analysis of the code base for each commit
language_breakdown = pl.language_sizes(temp_repo_path)
#
print(language_breakdown)
delete = cloning.delete_clone(temp_repo_path)

