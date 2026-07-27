# GitHub User Activity CLI

A simple Python command-line tool that fetches and displays recent public GitHub activity for a given username.

## Features

- Retrieves the latest public events from the GitHub API
- Shows up to 10 recent activities
- Supports common event types such as pushes, issues, stars, forks, pull requests, and comments
- Uses only Python's standard library

## Requirements

- Python 3.8 or newer
- Internet access to reach the GitHub API

## Usage

Run the script with a GitHub username:

```bash
python github_activity.py <username>
```

### Example

```bash
python github_activity.py octocat
```

## Example Output

```text
Fetching recent activity for 'octocat'...
- Pushed 2 commit(s) to octocat/example-repo
- Opened a pull request in octocat/example-repo
- Starred octocat/example-repo
```

## Error Handling

The script provides clear messages for common issues, including:

- Username not found (404)
- API rate limit or access forbidden (403)
- Network errors

## Project Files

- `github_activity.py` - Main CLI script

## Notes

This tool uses the public GitHub Events API and only shows activity that is publicly available.
