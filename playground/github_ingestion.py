import requests

headers = {
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2026-03-10',
    'User-Agent': 'panda-docs-qa-graphrag'
}

response = requests.get('https://api.github.com/repos/pandas-dev/pandas/issues', headers=headers)

with open('./artifacts/example_issues.json', 'w') as f:
    f.write(json.dumps(response.json(), indent=4))
