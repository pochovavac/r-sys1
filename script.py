import base64

from github import Github
from pprint import pprint

Priecinok = Github().get_user("pochovavac")

for Repozitare in Priecinok.get_repos():
    print(Repozitare)

