from git import Repo
import tempfile
import os

def get_local_repo(path="."):
    return Repo(path)

def get_remote_repo(url):
    temp_dir = tempfile.mkdtemp()
    repo = Repo.clone_from(url, temp_dir)
    return repo, temp_dir

def extract_commits(repo):
    commits = list(repo.iter_commits())
    print(f"Found {len(commits)} commits")
    return commits