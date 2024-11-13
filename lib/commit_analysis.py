import git 
import os
import shutil

def commit_analysis(repo):
    for commit in repo.iter_commits():
        commit_info = {
            'commit_hash': commit.hexsha,
            'author_name': commit.author.name,
            'author_email': commit.author.email,
            'date': commit.committed_datetime,
            'message': commit.message
        }
        # some more effort to get this information
        commit_info['branches'] = repo.git.branch("--contains", commit_info['commit_hash'])
        #diff information
        diffs = commit.diff(commit.parents[0] if commit.parents else git.NULL_TREE, create_patch=True)
        commit_info['diff_info'] = diff_analysis(diffs)
        print(commit_info)

def diff_analysis(diffs):
    diff_objects = []
    for diff in diffs:
        diff_info = {
            'lines_added' : diff.diff.decode("utf-8").count('\n+'),
            'lines_deleted' : diff.diff.decode("utf-8").count('\n-'), 
            'file' : diff.b_path,
        }
        diff_objects.append(diff_info)
    return diff_objects