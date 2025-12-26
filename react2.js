import requests

TOKEN = "ghp_your_personal_access_token"
OWNER = "your-org-or-username"
REPO = "your-repo"

url = f"https://api.github.com/repos/{OWNER}/{REPO}/installation"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json",
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("GitHub App installed:")
    print("App ID:", data["app_id"])
else:
    print("No GitHub App installed or insufficient permissions")
