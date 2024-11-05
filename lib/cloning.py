import git 
import os
import shutil

def temp_clone(vcs_link):
    temp_location = "tmp/"
    os.makedirs(temp_location)
    repo_path = temp_location
    repo = git.Repo.clone_from(vcs_link, repo_path)
    for commit in repo.iter_commits():
        print("---------------------")
        print(f'Commit: {commit.hexsha}')
        print(f'Author: {commit.author.name}')
        print(f'Author Email: {commit.author.email}')
        print(f'Date: {commit.committed_datetime}')
        print(f'Message: {commit.message}')

        diffs = commit.diff(commit.parents[0] if commit.parents else git.NULL_TREE, create_patch=True)
        for diff in diffs:
            lines_added = diff.diff.decode("utf-8").count('\n+')
            lines_deleted = diff.diff.decode("utf-8").count('\n-')
            print(f'File: {diff.b_path}')
            print(f'Lines Added: {lines_added}')
            print(f'Lines Deleted: {lines_deleted}')

    if os.path.exists(temp_location):
        shutil.rmtree(temp_location)
        print('Temporary clone has been deleted.')