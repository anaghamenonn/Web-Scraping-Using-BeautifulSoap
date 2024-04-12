import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore

req = requests.get("https://www.geeksforgeeks.org/")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title

print(soup.get_text())