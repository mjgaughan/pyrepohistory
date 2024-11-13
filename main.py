import argparse

from lib import cloning, commit_analysis

parser = argparse.ArgumentParser(description="repository search")

parser.add_argument("repolink", help="The repository hosting")

args = parser.parse_args()

print(args.repolink)
temp_repo, temp_repo_path = cloning.temp_clone(args.repolink)
commits_dict = commit_analysis.commit_analysis(temp_repo)
# TODO: here goes static/dynamic analysis of the code base for each commit
delete = cloning.delete_clone(temp_repo_path)

