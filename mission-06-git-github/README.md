# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of this mission is to understand distributed version control workflows using Git and GitHub, master repository inspection and staging lifecycle states, create and isolate work in a dedicated feature branch (`update-about`), simulate and explain the collaborative Pull Request (PR) review process, and compile a comprehensive Git command glossary.

## 2. Work completed
- Inspected the repository lifecycle states (working directory, index/staging area, commit history) using `git status` and `git log`.
- Created an isolated feature branch named `update-about` using `git switch -c update-about`.
- Modified the root `README.md` to add a new section titled `## My Learning` detailing core system concepts learned.
- Committed the changes on the `update-about` branch and simulated/executed the Pull Request integration into `main` via merge commit.
- Documented the conceptual role and industrial necessity of branching and Pull Requests in collaborative software teams.
- Authored a nine-part Git command glossary explaining standard daily Git operations.

---

### Task 6.1 — Understand the basic Git workflow
The Git workflow separates local modifications into distinct lifecycle stages before they become immutable repository history.

| Git operation | What it does in your own words |
| :--- | :--- |
| **Check repository status (`git status`)** | Queries the working directory and staging index, displaying which branch is checked out, which files have been modified or deleted, and which untracked files are not yet managed by Git. |
| **Stage selected changes (`git add <file>`)** | Moves specific modified or newly created files from the working tree into Git's staging area (index), curating exactly what will be included in the next commit snapshot. |
| **Create a commit (`git commit -m "..."`)** | Permanently records the staged changes as a new, immutable snapshot in the local Git repository database, attaching author metadata, timestamp, and a descriptive log message. |
| **View commit history (`git log`)** | Displays a chronological list of commits in the repository history, showing unique commit hashes (SHA-1/SHA-256), author information, dates, and commit messages. |

#### Difference between Staging a change and Committing it:
- **Staging (`git add`):** Staging acts as an intermediate workbench or drafting phase. A developer might modify ten files in their local workspace while debugging, but only want to package five related files into a specific logical unit of work. Staging lets the developer selectively curate and review changes before recording them.
- **Committing (`git commit`):** Committing takes that curated staging area and permanently seals it as a cryptographic snapshot in the repository's permanent history. Once committed, the changes are assigned a permanent hash ID, cannot be accidentally overwritten, and can be referenced, branched, or reverted at any point in the future.

---

### Task 6.2 — Create and use a branch
1. Created and checked out a dedicated feature branch:
   ```bash
   git switch -c update-about
   ```
2. Opened the root `README.md` and added the `## My Learning` section covering hardware abstraction, command-line control, and data uniformity.
3. Verified the status of the branch:
   ```bash
   git status
   ```
4. Staged the modified file and created a dedicated commit on the feature branch:
   ```bash
   git add README.md
   git commit -m "Add My Learning section to root README on update-about branch"
   ```

---

### Task 6.3 — Create a Pull Request (PR) Workflow
- **What is a Branch?**
  A branch in Git is an independent, lightweight pointer to a commit in the repository timeline. Branching enables developers to diverge from the primary production codebase (`main`) to develop new features, experiment with designs, or fix bugs in complete isolation. Work on a branch does not destabilize or interfere with the working code on `main`.
- **What is a Pull Request (PR)?**
  A Pull Request (or Merge Request) is a collaborative development practice popularized by platforms like GitHub. It serves as a formal request to merge changes from a feature branch into the target base branch (typically `main`). A PR provides a web-based code review interface displaying unified diffs, automated continuous integration (CI) test results, and discussion threads where team members can audit code quality, suggest improvements, and ensure alignment before merging.
- **Why are branches and Pull Requests essential when people collaborate?**
  In modern software engineering teams, multiple engineers write code concurrently on the same codebase. Without branches, commits would constantly collide, causing merge conflicts, overwriting unreleased features, and risking production crashes. Pull Requests enforce code review standards, peer accountability, security checks, and ensure that only verified, tested code enters the main release branch.
- **PR Status:**
  The `update-about` branch was created and committed locally. In accordance with the assignment guidelines, the branch was merged into the local `main` branch via a dedicated merge commit (`Merge branch 'update-about' into main (Pull Request simulation)`), updating `main` with the latest learnings while keeping the branch history intact.

---

### Task 6.4 — Build your Git command glossary

1. **Initialise a repository (`git init`):** Creates an empty Git version control repository or re-initializes an existing one by generating a hidden `.git` metadata tracking folder.
2. **Check status (`git status`):** Shows the current branch name, untracked files, modified files, and files staged for the upcoming commit.
3. **Stage changes (`git add <path>`):** Moves specified file changes from the working tree into the Git index/staging area in preparation for committing.
4. **Commit changes (`git commit -m "<msg>"`):** Takes an immutable snapshot of all currently staged files and saves it to the local repository log with author metadata and message.
5. **View history (`git log`):** Lists past commits in chronological order, displaying their unique commit hashes, author details, dates, and messages.
6. **Create or list branches (`git branch`):** Displays all local branch names when run without arguments, or creates a new branch pointer when supplied with a branch name.
7. **Switch branches (`git switch <branch>` / `git checkout <branch>`):** Shifts HEAD and updates files in the working directory to match the specified branch state.
8. **Publish changes (`git push <remote> <branch>`):** Uploads committed local branch snapshots to a remote repository server (such as GitHub) to update the remote branch.
9. **Retrieve remote changes (`git pull` / `git fetch`):** Downloads new commits, branches, and tags from a remote repository and merges them into the active local branch.

---

## 3. Commands / tools used
- `git switch -c`: Created and branched into `update-about`.
- `git status`, `git diff`: Monitored working tree modifications.
- `git add`, `git commit`: Staged and recorded changes.
- `git switch main`, `git merge`: Navigated back to `main` and merged the branch.
- `git log --graph --oneline`: Inspected the commit graph structure.

## 4. My understanding
Git separates file states into three primary trees: the Working Directory (sandbox files on disk), the Staging Area / Index (curated changeset), and the Repository Commit History (immutable object database). Branches are simply movable pointers to commit objects, making branching and merging practically instantaneous and safe.

## 5. Difficulties faced
Understanding the difference between fast-forward merges and three-way merge commits when integrating branches.

## 6. How I resolved them
Used the `--no-ff` (no fast-forward) flag during merging to ensure an explicit merge commit was generated, documenting that the work originated from the `update-about` branch.

## 7. Evidence / files
- `mission-06-git-github/README.md`: Complete workflow explanations, PR analysis, and nine-command glossary.
- Root `README.md`: Updated with `## My Learning` section from the branch.

## 8. Commit details
- Commit message: `Complete Git and GitHub collaboration mission`
- Branch: `main`
- Status: Staged and committed locally.
