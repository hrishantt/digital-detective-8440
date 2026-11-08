# Mission 2 — Become comfortable with the Terminal

## 1. Task / objective
The objective of this mission is to master essential command-line interface (CLI) navigation, safely perform file and directory manipulation operations inside a dedicated workspace, analyze Unix flags and command pipelining, and explore package manager functionality on macOS.

## 2. Work completed
- Conducted practical command-line exercises for nine standard operations: directory display, listing, detailed inspection, navigation, folder creation, file creation, file copying, file renaming/moving, and content inspection.
- Created an isolated `terminal-practice` directory within the assignment repository to safely perform file mutations without impacting system directories.
- Demonstrated non-destructive file appending (`>>`) versus destructive truncation (`>`), file duplication (`cp`), and renaming (`mv`).
- Analyzed command modification flags (`-l`, `-a`, `-h`) and Unix pipeline composition using `|` and `head`.
- Inspected Homebrew package manager status, recorded installed packages, and summarized package management benefits.

---

### Task 2.1 — Explore basic Terminal operations
All operations were executed sequentially from within the project workspace.

| Operation / command name | What it does | What I observed |
| :--- | :--- | :--- |
| **Current-directory display (`pwd`)** | Prints the absolute, full pathname of the current working directory starting from root (`/`). | The terminal output displayed `/Users/[redacted]/Desktop/digital-detective-8440`. |
| **Directory listing (`ls`)** | Lists the visible files and folders residing in the target directory. | Displayed the directory names (`mission-00-setup`, `terminal-practice`, etc.) in multi-column format. |
| **Detailed listing (`ls -l`)** | Formats directory contents with file attributes: permissions, link count, owner, group, byte size, and last modified date. | Columns displayed `-rw-r--r--`, byte counts, dates, and names cleanly aligned. |
| **Change directory (`cd ..` / `cd`)** | Navigates the active shell session to a specified target directory or parent directory. | Navigating to parent `cd ..` shifted working directory to `/Users/[redacted]/Desktop`; returning via `cd digital-detective-8440` restored the context. |
| **Create directory (`mkdir`)** | Generates one or more new directories at the specified path. | Executed `mkdir terminal-practice`; confirmed directory creation immediately using `ls`. |
| **Create empty file (`touch`)** | Creates a 0-byte file if it does not exist, or updates access and modification timestamps if it exists. | `touch practice.txt` created an empty file ready for data entry. |
| **Copy file (`cp`)** | Duplicates the contents of a source file into a new destination file path. | `cp practice.txt backup.txt` produced an identical second file while preserving the original. |
| **Move / rename file (`mv`)** | Moves a file between paths or renames it in place within the directory table. | `mv backup.txt renamed_backup.txt` updated the filename; `backup.txt` no longer appeared in the directory. |
| **Display file contents (`cat`)** | Concatenates and streams the raw contents of one or more text files to standard output (`stdout`). | `cat practice.txt` output the two lines of text stored inside directly to the console. |

---

### Task 2.2 — Practise file changes safely
Inside the dedicated practice directory `terminal-practice`:
1. Created `practice.txt` with line 1 using output redirection:
   ```bash
   echo "Mission 2 Terminal Practice: Line 1 initialized." > practice.txt
   ```
2. Appended line 2 without overwriting line 1 using the append redirection operator:
   ```bash
   echo "Appending second line of notes without overwriting." >> practice.txt
   ```
3. Verified the file contents with `cat practice.txt`:
   ```text
   Mission 2 Terminal Practice: Line 1 initialized.
   Appending second line of notes without overwriting.
   ```
4. Created a backup copy:
   ```bash
   cp practice.txt backup.txt
   ```
5. Renamed the backup copy:
   ```bash
   mv backup.txt renamed_backup.txt
   ```

#### Analysis Questions:
- **What is the difference between replacing a file's contents and adding text to the end?**
  - **Replacing (`>`):** The standard output redirection operator opens the destination file in truncate mode. If the file already contains data, its length is instantly reset to zero bytes, discarding all prior content before writing new data.
  - **Adding text (`>>`):** The append redirection operator opens the target file in append mode, moving the write pointer to the very end of the file (EOF). New data is appended after the existing bytes, leaving previous content completely intact.
- **What is the difference between copying a file and moving a file?**
  - **Copying (`cp`):** Allocates new storage blocks on disk, duplicates all data bytes from the source to the target, and creates a separate directory entry. Both the original file and new file exist independently.
  - **Moving (`mv`):** On the same filesystem volume, moving updates only the directory pointer (inode reference) without duplicating physical data blocks on disk. The file now exists solely at the new destination/name, and the old path is removed.
- **What information does the current-directory display provide?**
  The `pwd` (print working directory) command reveals the full, canonical absolute path from the root directory (`/`) to the active working location. This orientates the user within the operating system tree, preventing unintended modifications to wrong folders.
- **Why is a directory-listing operation useful?**
  A directory listing (`ls`) allows the user to inspect directory contents, verify whether previous file creation/copy commands succeeded, check exact filenames and extensions, inspect file size and timestamp metadata, and verify read/write/execute permissions.

---

### Task 2.3 — Understand flags and pipes
- **Directory Listing Flag Comparison:**
  - Standard command: `ls`
    - Displays only visible filenames in simple tabular format without supplementary metadata.
  - Enhanced command: `ls -lah`
    - `-l` (long listing): Produces detailed multi-column format showing permissions (`drwxr-xr-x`), link counts, owner, group, file sizes, and modification timestamps.
    - `-a` (all): Reveals hidden files and folders that begin with a dot (`.`), such as `.` (current directory), `..` (parent directory), `.DS_Store`, and `.git`.
    - `-h` (human-readable): Converts raw byte values into human-readable size units (e.g., `101B`, `4.0K`, `2.5M`), significantly easing manual inspection.
- **Pipes and Command Chaining:**
  - Command: `ls -la | head -n 5`
  - **What the pipe symbol (`|`) does:** The Unix pipe acts as an inter-process communication channel in memory. It redirects the standard output (`stdout`) of the command on its left directly into the standard input (`stdin`) of the command on its right, eliminating the need to write intermediate temporary files to disk.
  - **Left side (`ls -la`):** Generates a comprehensive, detailed directory stream containing all files and metadata.
  - **Right side (`head -n 5`):** Reads the incoming stream from `ls -la` and prints only the first 5 lines (the total block header and top directory entries), discarding the remaining stream.

---

### Task 2.4 — Understand package managers
- **Homebrew Check:**
  - Homebrew is installed on this macOS system.
  - Verified version: `Homebrew 7.0.12`
  - Sample packages managed: `git`, `python@3.14`, `htop`, `ca-certificates`, `coreutils`, `node`, `sqlite`, `ffmpeg`.
- **Why Package Managers are Useful:**
  A package manager is an automated software management utility that centralizes installing, configuring, upgrading, and removing command-line tools and software packages. It automatically calculates and resolves complex dependency graphs, ensuring required shared libraries are installed with matching compatibility. Additionally, package managers enhance security and reproducibility by enabling one-command system-wide audits and updates (`brew upgrade`) without requiring manual source compilation or scattered web downloads.

---

## 3. Commands / tools used
- `pwd`, `ls`, `ls -l`, `ls -lah`: Directory path and file listing inspection.
- `cd`, `mkdir`: Navigation and practice folder creation.
- `touch`, `echo`, `cat`: File creation, text redirection, appending, and content inspection.
- `cp`, `mv`: File duplication and renaming.
- `|` (pipe), `head`: Stream composition and line filtering.
- `brew --version`, `brew list`: Package manager inspection.

## 4. My understanding
The command-line interface provides precise, programmatic control over the operating system. Mastery of Unix streams, input/output redirection (`>`, `>>`), pipeline composition (`|`), and path navigation enables developers to automate repetitive workflows, inspect system state transparently, and maintain clean separation of concerns.

## 5. Difficulties faced
Remembering the exact combination of flags for human-readable long listings with hidden files (`-lah`).

## 6. How I resolved them
Consulted the manual page using `man ls` to verify that `-l`, `-a`, and `-h` can be combined into a single compound flag argument.

## 7. Evidence / files
- `terminal-practice/practice.txt`: Dual-line practice file created and appended.
- `terminal-practice/renamed_backup.txt`: Duplicated and renamed backup file.
- `evidence/mission-02/terminal_session.txt`: Sanitized log of terminal commands and output.

## 8. Commit details
- Commit message: `Complete Terminal and file management mission`
- Branch: `main`
- Status: Staged and committed locally.
