# Mission 2 — become comfortable with the terminal

## 1. task / objective
learn basic terminal commands, practice creating and editing files safely, understand flags and pipes, and check Homebrew package manager

## 2. work completed
- practiced 9 basic terminal commands for files and folders
- created `terminal-practice` folder and practiced writing, appending, copying, and renaming files
- checked flags (`-l`, `-a`, `-h`) and pipes (`|` with `head`)
- checked Homebrew version and package list

---

### task 2.1 — explore basic terminal operations

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the current working directory | The terminal output displayed `/Users/[redacted]/Desktop/digital-detective-8440` |
| **Directory listing (`ls`)** | Lists the visible files and folders in the target directory | Displayed the directory names (`mission-00-setup`, `terminal-practice`, etc.) in multi-column format |
| **Detailed listing (`ls -l`)** | Displays the directories and folders whith their permissions, link count, owner, group, byte size, and last modified date | `-rw-r--r--`, byte counts, dates, and names cleanly aligned |
| **Change directory (`cd ..` / `cd`)** | Navigates to a specified target directory or parent directory | Navigating to parent `cd ..` shifted working directory to `/Users/[redacted]/Desktop` and returning via `cd digital-detective-8440` brouoght me back to the previous path |
| **Create directory (`mkdir`)** | Generates one or more new directories at the specified path | A new folder naned `termnia practice` got formed |
| **Create empty file (`touch`)** | Used to create a new file | An empty file `practice.txt` got created |
| **Copy file (`cp`)** | copies a file to a new name or location | `cp practice.txt backup.txt` made a copy while keeping the original |
| **Move / rename file (`mv`)** | moves or renames a file | `mv backup.txt renamed_backup.txt` renamed the file |
| **Display file contents (`cat`)** | prints file text on the screen | `cat practice.txt` showed both lines on the terminal |

---

### task 2.2 — practise file changes safely
inside `terminal-practice`:
1. created `practice.txt` with line 1 using `>`
   ```bash
   echo "mission 2 terminal practice: line 1 initialized" > practice.txt
   ```
2. added line 2 without erasing line 1 using `>>`
   ```bash
   echo "appending second line of notes without overwriting" >> practice.txt
   ```
3. checked the file with `cat practice.txt`
4. made a copy `cp practice.txt backup.txt` and renamed it `mv backup.txt renamed_backup.txt`

#### questions answered:
- **difference between replacing a file's contents and adding text to the end:**
  `>` replaces everything inside the file. `>>` adds new text to the end without deleting old lines
- **difference between copying a file and moving a file:**
  `cp` makes a duplicate so both files exist. `mv` moves or renames the file so the old name is gone
- **what information does the current-directory display provide:**
  `pwd` shows the full path of the folder you are currently in starting from `/`
- **why is a directory-listing operation useful:**
  `ls` lets you see what files and folders are inside, check if a new file was created, and view permissions and sizes

---

### task 2.3 — understand flags and pipes
- **flags (`ls` vs `ls -lah`):**
  - `ls` shows only normal file names
  - `ls -lah` shows more details: `-l` gives permissions, owner, size, and date; `-a` shows hidden files starting with `.`; `-h` shows sizes in KB or MB instead of bytes
- **pipes (`ls -la | head -n 5`):**
  - the pipe symbol `|` sends the output of the command on the left directly into the command on the right
  - `ls -la` lists all files with details, and `head -n 5` prints only the first 5 lines of that list

---

### task 2.4 — understand package managers
- **Homebrew check:**
  - version: `Homebrew 7.0.12`
  - some installed packages: `git`, `python@3.14`, `htop`, `node`, `sqlite`, `ffmpeg`
- **why package managers are useful:**
  a package manager makes it easy to install, update, and remove software from the terminal. it also handles required dependencies automatically and keeps tools updated with one command

---

## 3. commands / tools used
- `pwd`, `ls`, `ls -l`, `ls -lah`: checking current path and listing files
- `cd`, `mkdir`: moving between folders and making folders
- `touch`, `echo`, `cat`: making files, writing text, and viewing text
- `cp`, `mv`: copying and renaming files
- `|`, `head`: piping output and showing top lines
- `brew --version`, `brew list`: checking Homebrew

## 4. my understanding
terminal commands give fast control over files and folders. redirection (`>`, `>>`) and pipes (`|`) let you save text and connect commands together easily

## 5. difficulties faced
remembering which flags to combine for hidden files and readable sizes (`-lah`)

## 6. how i resolved them
checked `man ls` to see what each flag does

## 7. evidence / files
- `terminal-practice/practice.txt`
- `terminal-practice/renamed_backup.txt`
- `evidence/mission-02/terminal_session.txt`

## 8. commit details
- commit message: `complete terminal and file management mission`
- branch: `main`
- status: committed and pushed to github
