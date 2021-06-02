from github import Github
import os
import datetime
# project_name = "TFCloud_2.8"

Users = {'xmonader': '@xmonader',
       'AhmedHanafy725': '@ahmedhanafy725',
       'rkhamis': '@rThursday',
       'hossnys': '@samir_hosny',
       'PeterNashaat': '@PeterNashaat',
       'ranatrk': '@ranatrk',
       'abom': '@abomdev',
       'saeedr': '@ramez_saeed',
       'arahmanhamdy': '@mr_conflict',
       'Hamdy': '@hamdy_farag',
       'waleedhammam': '@Waleedhammam',
       'muhamadazmy':  '@muhamadazmy',
       'OmarElawady': '@oElawady',
       'dmahmouali': '@dmahmou',
       'MElborolossy': '@melborolossy',
       'RafyAmgadBenjamin': '@RafyBenjamin',
       'ashraffouda': '@ashraffouda',
       'mhost39': '@mhost39',
       'samaradel': '@adelsamar',
       'sameh-farouk': '@sameh_farouk',

       }

github_token = "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" #os.environ.get("GITHUB_TOKEN")

def get_projects(org):
    project_name = os.environ.get("PROJECT_NAME")
    print(">>>>>>>>>>>>>>>>>>>", project_name)
    all_projects = org.get_projects()
    for p in all_projects:
        if p.name == "TFCloud_2.8":
            return p
    return 0

def get_column(project, column_name):
    for col in project.get_columns():
        if col.name == column_name:
            return col
    return 0
    
g = Github(login_or_token=github_token, per_page=100)
org = g.get_organization("threefoldtech")
project = get_projects(org)
in_progress_column = get_column(project, "In progress")

cards = in_progress_column.get_cards()

def get_status():
    msg = []
    needs_update = {}
    for card in cards:
        issue = card.get_content()

        today = datetime.datetime.weekday(datetime.datetime.today())
        if today in range(0, 4):
            # yesterday was a workday
            update_time = datetime.datetime.now() - datetime.timedelta(days=1)
        elif today == 6:
            update_time = datetime.datetime.now() - datetime.timedelta(days=3)
        else:
            return []

        for assignee in issue.assignees:
            needs_update.setdefault(assignee.login, [])
            needs_update[assignee.login].append(issue)
        for comment in issue.get_comments(since=update_time):
            if issue in needs_update[comment.user.login]:
                needs_update[comment.user.login].remove(issue)
    
    for ass, issue in needs_update.items():
        if(issue):
            msg.append(f"{Users[ass]} please update status for [{issue[0].title}]({issue[0].html_url})")
    return msg
