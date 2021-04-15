from github import Github
import os


github_token = os.environ.get("GITHUB_TOKEN")

def get_prs_title(prs, repo_name):
    prs_title= [f">>>>>> {repo_name} PRs >>>>>>\n"]
    for pr in prs:
        prs_title.append(f"{pr.title}: {pr.html_url} \n")
    return prs_title

g = Github(login_or_token=github_token, per_page=100)
r = g.get_repo("threefoldtech/js-sdk")

all_prs_sdk = r.get_pulls('open')
prs_sdk = get_prs_title(all_prs_sdk, "SDK")

r = g.get_repo("threefoldtech/js-ng")
all_prs_jsng = r.get_pulls('open')
prs_jsng = get_prs_title(all_prs_jsng, "jsng")

r = g.get_repo("threefoldtech/vdc-solutions-charts")
all_prs_charts = r.get_pulls('open')
prs_charts = get_prs_title(all_prs_charts, "vdc-solutions-charts")
