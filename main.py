import argparse
import sys
import os
import datetime
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'lib')))
from lib import cloning, commit_analysis
from lib import primary_language as pl

def repo_lifecycle(vcs_link, from_date, to_date):
    """
    Parameters:
        vcs_link (str): Version control system link of the repository.
        from_date (datetime): The start date for commit analysis.
        to_date (datetime): The end date for commit analysis.
    """
    try:
        #download the repository
        temp_repo, temp_repo_path = cloning.temp_clone(vcs_link)
        project_name = vcs_link.split('/')[-1]
        project_owner = vcs_link.split('/')[-2]

        # collect data on prior commits
        commits_array = commit_analysis.commit_analysis(temp_repo, from_date, to_date)
        commits_df = pd.DataFrame.from_records(commits_array)
        #commits_df.to_csv(project_owner + "_" + project_name + "_" + from_date.strftime('%Y-%m-%d') + "_" + 'now.csv', index=False)
        print(commits_df.columns)

        # TODO: using the corresponding hash, checkout the project at that date
        # TODO: rename the project repository to reflect hash specificity

        # program/code analysis of the project at a specific point in time
        language_breakdown = pl.language_sizes(temp_repo_path) #breakdown is in terms of LoC
        print(language_breakdown)
        # TODO: here goes the linter/analysis implementation 

    except Exception as e:
        print(f"An error occurred: {e}")
    #clean up
    finally:
        delete = cloning.delete_clone(temp_repo_path)

if __name__ == "__main__":
    #setting the defaults for the test run
    parser = argparse.ArgumentParser(description="repository search")
    parser.add_argument("repolink", help="The repository hosting")
    args = parser.parse_args()
    cst = datetime.timezone(datetime.timedelta(hours=-6))
    from_date = datetime.datetime(2024, 11, 10, 1, 52, 32, tzinfo=cst)
    to_date = datetime.datetime(2024, 11, 15, 1, 52, 32, tzinfo=cst)
    #getting the information for the search
    repo_lifecycle(args.repolink, from_date, to_date)