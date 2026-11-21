# Mission 3 — understand the operating system

## 1. task / objective
check how the operating system works, see running processes, check disk space, learn about file paths and permissions

## 2. work completed
- checked OS version and details using `sw_vers` and `uname`
- checked active user account using `whoami` and `id`
- checked available disk space using `df -h`
- checked running processes and CPU usage using `top`
- explained processes, PIDs, file paths, and file permissions

---

### task 3.1 — explore your operating system

| information explored | what it tells you | your observation (privacy-safe) |
| :--- | :--- | :--- |
| **operating system / system details** | name and version of OS | macOS version 27.2, arm64 |
| **current account identity** | logged in user and group | user: `[redacted]`, group: `staff` |
| **available and used storage** | total, used and free disk space | total 460 GiB, used 13 GiB, free 326 GiB |
| **system activity snapshot** | running tasks and CPU use | 751 processes, CPU is mostly idle (~85%) |

---

### task 3.2 — understand processes
- **what is a process?**
  a process is simply a program that is currently running on the computer
- **what does the PID column represent?**
  PID means process ID. it is a unique number given by the OS to identify each running program
- **two examples of processes running on this computer:**
  1. `Google Chrome` (application used for browsing)
  2. `launchd` (background system process that starts other services)

---

### task 3.3 — understand paths and permissions
- **difference between an absolute path and a relative path:**
  - **absolute path:** full path starting from the root `/`
    - *example:* `/Users/[redacted]/Desktop/digital-detective-8440/terminal-practice/practice.txt`
  - **relative path:** path starting from the folder you are currently in
    - *example:* `terminal-practice/practice.txt`

- **file permissions for `practice.txt`:**
  checked using `ls -l`:
  ```text
  -rw-r--r--  1 [redacted]  staff  101 Nov 20 18:19 practice.txt
  ```
  - owner permissions are `rw-` (read and write allowed, run not allowed)
  - group permissions are `r--` (only read allowed)
  - others permissions are `r--` (only read allowed)
  - owner can read and edit the file, but cannot execute it

| permission | meaning | example |
| :--- | :--- | :--- |
| **r — read** | allows reading file contents | opening a text file |
| **w — write** | allows changing or editing file | saving changes to a file |
| **x — execute** | allows running a program or opening a folder | running a script |

---

### task 3.4 — explain operating-system responsibilities

| OS responsibility | your explanation | example |
| :--- | :--- | :--- |
| **process management** | starts, runs and stops programs | switching between browser and text editor |
| **memory management** | shares RAM between open apps | giving RAM to a game while playing |
| **device management** | controls hardware like mouse, screen, keyboard | taking clicks from a mouse |
| **file management** | stores and organizes files on disk | saving a file on the SSD |
| **user interface / shell** | lets the user talk to the computer | terminal or desktop screen |
| **security and permissions** | protects files and stops unauthorized access | asking password before installing software |

---

## 3. commands / tools used
- `sw_vers`, `uname`: to see OS name and kernel
- `whoami`, `id`: to see user name and ID
- `df -h`: to see disk space in GB
- `top -l 1`: to see CPU and memory usage
- `ls -l`: to see file permissions

## 4. my understanding
the operating system is the main program that manages the whole computer. it controls the hardware, shares RAM and CPU between apps, and keeps files safe

## 5. difficulties faced
understanding the output of `top` command because it has too many numbers

## 6. how i resolved them
read the top man page and focused only on CPU and memory summary at the top

## 7. evidence / files
- `evidence/mission-03/system_info.txt`: saved terminal output

## 8. commit details
- commit message: `complete operating system and permissions mission`
- branch: `main`
- status: committed and pushed to github
