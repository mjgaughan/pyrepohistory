import argparse

from lib import cloning, commit_analysis

parser = argparse.ArgumentParser(description="repository search")

parser.add_argument("repolink", help="The repository hosting")

args = parser.parse_args()

print(args.repolink)
temp_repo, temp_repo_path = cloning.temp_clone(args.repolink)
commit_analysis.commit_analysis(temp_repo)
delete = cloning.delete_clone(temp_repo_path)

