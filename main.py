import argparse
import sys
import os
import datetime
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
from lib import cloning, commit_analysis
from lib import primary_language as pl

#TODO: functionalize this

parser = argparse.ArgumentParser(description="repository search")

parser.add_argument("repolink", help="The repository hosting")

args = parser.parse_args()

print(args.repolink)
#download the repository
cst = datetime.timezone(datetime.timedelta(hours=-6))
temp_repo, temp_repo_path = cloning.temp_clone(args.repolink)
# collect data on prior commits
commits_array = commit_analysis.commit_analysis(temp_repo, datetime.datetime(2024, 1, 1, 1, 52, 32, tzinfo=cst))
commits_df = pd.DataFrame.from_records(commits_array)
print(commits_df.columns)
#roll the repo back to the date that you want 
# TODO: get the max datetime less than the specified date 
# TODO: using the corresponding hash, checkout the project at that date
# TODO: rename the project repository to reflect hash specificity
# program/code analysis of the project at a specific point in time
language_breakdown = pl.language_sizes(temp_repo_path) #breakdown is in terms of LoC
print(language_breakdown)
# TODO: here goes the linter/analysis implementation 
#clean up
delete = cloning.delete_clone(temp_repo_path)

