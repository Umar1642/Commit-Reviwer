from review_commits.git_handler import get_local_repo, get_remote_repo, extract_commits
from review_commits.llm import review_commit
from review_commits.reporter import generate_report
from review_commits.server import server_report
import os
import time

def logs(commit, review):
    print(f"\nCommit: {commit.hexsha[:7]}")
    print(f"Author: {commit.author.name}")
    print(f"Message:   {commit.message.strip()}")
    print(f"Rating:    {review['rating']}")
    print(f"Reasoning: {review['reasoning']}")


def run_llm(repo, repo_name):
    raw_commits = extract_commits(repo)
    print(f"\n Found {len(raw_commits)} commits. Reviewing commits...")

    data = []
    for i, commit in enumerate(raw_commits):
        print(f"Reviewing {commit.hexsha[:7]}... ({i+1}/{len(raw_commits)})")
 
        review = review_commit(commit_message=commit.message.strip(), commit_hash=commit.hexsha[:7], author=commit.author.name, date=str(commit.authored_datetime))
        logs(commit, review)


        data.append({
            "hash": commit.hexsha[:7],
            "author": commit.author.name,
            "date": str(commit.authored_datetime),
            "message": commit.message.strip(),
            "review": review
        })

        if i < len(raw_commits):
            print("Waiting to avoid rate limit...")
            time.sleep(3) # need this or else get rate limited
    
    report_path = generate_report(repo_name=repo_name, commits=data)
    server_report(report_path)


def local_repo():
    repo_path = input("Please enter the repo's file path on your local machine:\n").strip().strip('"').strip("'")
    repo = get_local_repo(repo_path)
    repo_name = os.path.basename(repo_path)
    print(f"Repo name {repo_name}")
    run_llm(repo, repo_name)


def remote_repo():
    url = input("Enter the GitHub URL: ")
    repo, temp_dir = get_remote_repo(url)
    repo_name = url.rstrip("/").split("/")[-1]
    run_llm(repo, repo_name)

def main():
    while True:
        print("\n" + "-"*50)
        print("   Welcome to your Git Commit Reviewer")
        print("-"*50)
        print("   1. Local Repo")
        print("   2. Remote Repo")
        print("-"*50)

        choice = input("\n Select option: ")
        
        if choice == "1":
            local_repo()
        elif choice == "2":
            remote_repo()
        else:
            print("Invalid Option, try again")
            continue
        input("\n Press Enter to continue...")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n Error: {e}")
