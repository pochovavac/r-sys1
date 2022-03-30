import base64
from github import Github
from pprint import pprint

username = "pochovavac"
g = Github()
user = g.get_user(username)

print("---------------ZOZNAM REPOZITAROV--------------")
for repo in user.get_repos():
    print(repo)
print("---------------ZOZNAM COMMITOV V REPOZITARI R-SYS1---------------------------")

repo = g.get_repo('pochovavac/r-sys1')
for commit in repo.get_commits():
    print(commit.files)
print("-----------------------------------------------------------------------------")
