# Mission 6 — Git and GitHub

## 1. task / objective
learn basic Git workflow, create a branch, work with Pull Requests, and make a Git command glossary

## 2. work completed
- checked Git status, staging, committing and log
- made a new branch named `update-about`
- added `## My Learning` to root `README.md` on the new branch and committed it
- merged the branch into `main`
- wrote a short 9-command Git glossary

---

### task 6.1 — understand the basic Git workflow

| Git operation | what it does in your own words |
| :--- | :--- |
| **check repository status (`git status`)** | shows which files are changed, staged, or untracked |
| **stage selected changes (`git add `)** | picks which changed files to include in the next commit |
| **create a commit (`git commit `)** | permanently saves the staged changes with a message |
| **view commit history (`git log`)** | shows the list of past commits with their date and message |

#### difference between staging and committing:
- **staging (`git add`):** like putting files in a box before packing it. you pick what you want to save
- **committing (`git commit`):** like taping the box and sealing it. it saves the snapshot permanently in Git history

--- 

### task 6.2 — create and use a branch
1. made and switched to new branch:
   ```bash
   git switch -c update-about
   ```
2. edited root `README.md` and added `## My Learning` section
3. checked status using `git status`
4. staged and committed the change:
   ```bash
   git add README.md
   git commit -m "Add My Learning section to root README on update-about branch"
   ```

---

### task 6.3 — create a Pull Request (PR) workflow
- **what is a branch?**
  a branch is a separate workspace. you can make changes and test new things without breaking the `main` code
- **what is a Pull Request (PR)?**
  a Pull Request is asking other team members to review your branch code on GitHub before adding it to `main`
- **why are branches and Pull Requests useful when working together?**
  they stop team members from overwriting each other's work and let everyone review changes before they go live
- **PR status:**
  branch `update-about` was created, committed, and merged into `main`

---

### task 6.4 — build your Git command glossary

1. **`git init`:** creates a new local Git repository in the folder
2. **`git status`:** shows changed, staged, and untracked files
3. **`git add`:** moves files to the staging area
4. **`git commit`:** saves staged changes with a commit message
5. **`git log`:** shows the list of past commits
6. **`git branch`:** lists existing branches or creates a new one
7. **`git switch`:** switches between branches
8. **`git push`:** uploads local commits to GitHub
9. **`git pull`:** downloads new commits from GitHub

---

## 3. commands / tools used
- `git status`, `git add`, `git commit`: basic workflow
- `git switch -c`, `git merge`: branching and merging
- `git log `: checking commit history

## 4. my understanding
Git helps you keep track of all changes in your project so you can go back if you make a mistake. branches let you try things safely

## 5. difficulties faced
understanding how to merge a branch without losing history

## 6. how i resolved them
used `git merge` with a descriptive message to show the branch was combined into `main`

## 7. evidence / files
- `mission-06-git-github/README.md`: this notes file
- root `README.md`: updated with `## My Learning`

## 8. commit details
- commit message: `complete git and github mission`
- branch: `main`
- status: committed and pushed to github
