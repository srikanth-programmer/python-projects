# Question : https://roadmap.sh/projects/github-user-activity
"""
Key Considerations:

1. Use only prebuilt packages
2. Validate github username and api call status

"""

import json
import urllib.request
import urllib.error
import sys


def fetch_github_activity(username: str):
    url = f"https://api.github.com/users/{username}/events"

    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Python CLI App",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2026-03-10",
        },
    )
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = response.read().decode("utf-8")
                return json.loads(data)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"Error username {username} not found")
        elif e.code == 403:
            print("Error: API rate limit exceeded or Access forbidden")
        else:
            print(f"HTTP Error occured: {e.code} - {e.reason}")
        # program closed due to failure
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"Network error: Failed to reach server {e.reason}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexcepted error occured: {e}")
        sys.exit(1)


def format_events(event):
    event_type = event.get("type", "Unknown Type")
    repo_name = event.get("repo", {}).get("name", "unknown repository")
    payload = event.get("payload", {})

    match event_type:
        case "PushEvent":
            commit_count = len(payload.get("commits", []))
            return f"- Pushed {commit_count} commit(s) to {repo_name}"
        case "IssuesEvent":
            action = payload.get("action", "modified")
            return f"- {action.capitalize()} an issue in {repo_name}"
        case "WatchEvent":
            return f"- Starred {repo_name}"
        case "CreateEvent":
            ref_type = payload.get("ref_type", "repository")
            return f"- Created a {ref_type} in {repo_name}"
        case "ForkEvent":
            return f"- Forked {repo_name}"
        case "IssueCommentEvent":
            action = payload.get("action", "created")
            return f"- {action.capitalize()} a comment on an issue in {repo_name}"
        case "PullRequestEvent":
            action = payload.get("action", "opened")
            return f"- {action.capitalize()} a pull request in {repo_name}"
        case _:
            # Fallback for other event types
            event_name = event_type.replace("Event", "") if event_type else "Unknown"
            return f"- Perform action '{event_name}' on {repo_name}"


def main():
    if len(sys.argv) < 2:
        print("Usage: python github_activity.py <username>")
        sys.exit(1)
    username = sys.argv[1].strip()

    if not username:
        print("Error: Username cannot be empty")

    print(f"Fetching recent activity for '{username}...\n")
    events = fetch_github_activity(username)

    if not events:
        print(f"No recent activity found for '{username}")
        return
    # display up to 10 most recent events

    for event in events[:10]:
        print(format_events(event))


if __name__ == "__main__":
    main()
