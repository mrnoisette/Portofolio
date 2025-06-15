from fastapi import APIRouter
from github import Github

github_router = APIRouter()  # <-- crée un router à utiliser dans main.py

github = Github()
user = github.get_user("mrnoisette")

@github_router.get("/repos")
def ObtenirRepos():
    repos_data = []
    for repo in user.get_repos():
        commits = repo.get_commits()
        repos_data.append({
            "name": repo.name,
            "url": repo.html_url,
            "description": repo.description,
            "language": repo.language,
            "stars": repo.stargazers_count,
            "updated": repo.updated_at.isoformat(),
            "commits": commits.totalCount,  # nombre total de commits
        })
    return repos_data
