import git

def get_prs(repo_path):
    """
    Parameters:
        repo_path (str): path to the cloned git repository
    RETURNS:
        prs (array of dicts): array of dictionary objects with prs, opened and closed
    """
    repo = git.Repo(repo_path)
    repo.remote().fetch('refs/pull/*/head:refs/pull/*/head')
    results = repo.remote().fetch('refs/pull/*/merge:refs/pull/*/merge')

    pr_refs = [ref for ref in repo.refs if ref.name.startswith('refs/pull/')]
    print(pr_refs)
    for ref in pr_refs:
        print(ref)
    '''
    #repo.git.fetch('origin', 'refs/pull/*/head:refs/pull/*/head')
    #repo.git.fetch('origin', 'refs/pull/*/merge:refs/pull/*/merge')

    #pr_refs = [ref for ref in repo.refs if ref.name.startswith('refs/pull/')]

    print(pr_refs)
    prs = []
    for ref in pr_refs:
        print(ref)
    '''

if __name__ == "__main__":
    repo_path = '../../../hipcheck'
    get_prs(repo_path)