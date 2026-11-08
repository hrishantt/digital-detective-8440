# Mission 0 — Create your GitHub workspace

## 1. Task / objective
The objective of this mission is to establish a well-structured project workspace, verify essential local developer tools (Git and Python 3), initialize a local Git repository named `digital-detective-8440`, establish the standardized folder layout required for all subsequent missions, and connect it to a public GitHub repository.

## 2. Work completed
- Decided on the repository name based on the convention `digital-detective-` followed by the last four digits of the USN: `digital-detective-8440`.
- Verified installed versions of Python 3 and Git using the Terminal.
- Created the project directory `/Users/hrishant/Desktop/digital-detective-8440` on macOS.
- Created all mandatory subdirectories and files:
  - `README.md` (root repository documentation and navigation)
  - `mission-00-setup/README.md`
  - `mission-01-computer-basics/README.md`
  - `mission-02-terminal/README.md`
  - `mission-03-operating-system/README.md`
  - `mission-04-programs/README.md`
  - `mission-05-numbers-data/README.md`
  - `mission-05-numbers-data/number_converter.py`
  - `mission-06-git-github/README.md`
  - `mission-07-networking/README.md`
  - `mission-08-final-report/README.md`
  - `evidence/` directory for safe outputs and logs.
- Linked the local repository to the remote public repository at `https://github.com/hrishantt/digital-detective-8440.git`.

## 3. Commands / tools used
- `git --version`: Checked the installed Git version (`git version 2.56.0`).
- `python3 --version`: Verified the installed Python 3 interpreter version (`Python 3.14.7`).
- `mkdir`: Created the mission directory structure and the `evidence` directory.
- `touch`: Created initial placeholder markdown files and Python script templates.
- `git init`: Initialized the local Git version control repository.
- `git remote add origin https://github.com/hrishantt/digital-detective-8440.git`: Connected local repository to GitHub.
- `git branch -M main`: Renamed primary branch to `main`.

## 4. My understanding
- **What is a Git repository?**
  A Git repository is a digital storage database managed by the Git version control system. It tracks the complete historical timeline of changes made to files within a project. Instead of manually creating duplicate copies (e.g., "project_v1", "project_final"), Git records granular snapshots (commits), allowing users to track progression, revert changes if errors arise, and collaborate seamlessly across branches.
- **Why is the folder structure organized by mission?**
  Organizing the repository into distinct mission folders ensures modularity, clean documentation separation, and systematic progress tracking. Each mission represents an independent module of computer science investigation—from hardware fundamentals and OS processes to networking and data encoding. A modular structure allows instructors to review and grade each milestone individually while keeping project code, shell experiments, and reports cleanly isolated.

## 5. Difficulties faced
Configuring the remote tracking branch and ensuring authentication between the local terminal and the GitHub repository without exposing sensitive personal tokens or credentials.

## 6. How I resolved them
Verified the remote URL using `git remote -v`, ensured macOS Keychain handled credential caching securely, and confirmed the default branch was set to `main` before pushing.

## 7. Evidence / files
- `mission-00-setup/README.md`
- Root directory structure listing with all mission folders and `evidence/` directory.

## 8. Commit details
- Commit message: `Set up Digital Detective mission structure`
- Branch: `main`
- Remote status: Pushed to `https://github.com/hrishantt/digital-detective-8440`
