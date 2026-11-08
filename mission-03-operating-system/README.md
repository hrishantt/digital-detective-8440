# Mission 3 — Understand the operating system

## 1. Task / objective
The objective of this mission is to examine how the operating system coordinates computing resources by inspecting OS release metrics, active user identity, storage volume utilization, running process states, file path resolution (absolute vs. relative), and POSIX file access permissions.

## 2. Work completed
- Inspected the host operating system platform, hardware architecture, and kernel version using `sw_vers` and `uname`.
- Determined active session user identity and POSIX privilege groups using `whoami` and `id` while ensuring all personal identifiers were sanitized.
- Evaluated disk filesystem storage distribution using `df -h`.
- Analyzed real-time CPU, thread, and memory load metrics using a snapshot of `top`.
- Explained process lifecycle concepts, the role of Process Identifiers (PID), and identified real process instances.
- Clarified the distinction between absolute and relative file system paths with repository examples.
- Analyzed POSIX file permissions (`rwx`), identified owner access rights on a practice file, and summarized the core responsibilities of an operating system.

---

### Task 3.1 — Explore your operating system
All outputs were collected via Terminal and sanitized according to the privacy rules.

| Information explored | What it tells you | Your observation (privacy-safe) |
| :--- | :--- | :--- |
| **Operating system / system details** | Identifies the commercial OS product name, release version, kernel version, and processor instruction set architecture. | macOS version 27.2 (Build 26B123), Darwin Kernel Version 27.2.0, running on an `arm64` (Apple Silicon 64-bit) architecture. |
| **Current account identity** | Displays the username and numeric user identifier (UID) under which processes in this shell session execute, along with assigned group memberships (GID). | User: `[redacted]` (UID: 501), Primary Group: `staff` (GID: 20). |
| **Available and used storage** | Shows mounted file systems, total capacity, used storage, free space available, and filesystem utilization percentage. | Root filesystem (`/dev/disk3s1s1`) mounted on `/System/Volumes/Data`: Total size 460 GiB, 13 GiB used on system volume, 326 GiB available, 4% capacity utilization. |
| **System activity snapshot** | Displays a real-time monitor of total running processes, execution states (running/sleeping), thread counts, system load averages, CPU utilization breakdown, and physical RAM distribution. | 751 total processes (3 running, 748 sleeping), 3226 threads; Load averages: 2.64, 1.90, 1.70; CPU: ~3.9% user, 11.1% sys, 85.8% idle; Memory: 15 GB active/used, 196 MB unused. |

---

### Task 3.2 — Understand processes
- **What is a process?**
  A process is a program in active execution. When a program binary stored on secondary storage (SSD) is launched, the operating system kernel creates an execution context for it in volatile memory (RAM). This context includes dedicated virtual memory address space (text segment, data segment, call stack, and heap), processor register states, program counter, and open resource handles (file descriptors and sockets).
- **What does the PID column represent?**
  The PID (Process Identifier) is a unique non-negative integer assigned sequentially by the operating system kernel to identify and track each distinct active process. The OS uses PIDs to route signals (e.g., termination signals `SIGTERM` or `SIGKILL`), manage process hierarchies (parent and child processes via PPID), and schedule CPU time slices.
- **Two examples of processes running on this computer:**
  1. **User Application Process:** `Google Chrome` (or `VS Code`), an interactive user-space application process with its own PID, rendering web pages and managing background tabs.
  2. **System Background Daemon:** `launchd` (PID 1), the foundational macOS initialization daemon responsible for bootstrapping user sessions and managing system daemons and background services.

---

### Task 3.3 — Understand paths and permissions
- **Difference between an Absolute Path and a Relative Path:**
  - **Absolute Path:** A fully qualified file specification starting from the file system root (`/`). It unambiguously locates a resource regardless of the shell's current working directory.
    - *Example from repository:* `/Users/[redacted]/Desktop/digital-detective-8440/terminal-practice/practice.txt`
  - **Relative Path:** A path defined relative to the current working directory, using navigational references such as `.` (current directory) and `..` (parent directory).
    - *Example from repository:* When standing in the project root, the relative path to the practice file is `terminal-practice/practice.txt`; when inside `terminal-practice`, the relative path to the root README is `../README.md`.

- **File Permissions Analysis:**
  Inspected `terminal-practice/practice.txt` using `ls -l`:
  ```text
  -rw-r--r--  1 [redacted]  staff  101 Nov  9 02:20 practice.txt
  ```
  - **Permission Triad:**
    - Owner permissions: `rw-` (Read and Write permitted; Execute denied).
    - Group permissions: `r--` (Read-only permitted; Write and Execute denied).
    - Others permissions: `r--` (Read-only permitted; Write and Execute denied).
  - **Owner Rights:** The owner (`[redacted]`) can view/read the file and edit/modify its contents, but cannot execute it as a standalone script or binary.

| Permission | Meaning | Example |
| :--- | :--- | :--- |
| **r — Read** | Allows a file's contents to be read or inspected; on a directory, allows listing its filenames. | Opening a text file or viewing source code. |
| **w — Write** | Allows a file to be modified, edited, appended, or truncated; on a directory, allows creating and deleting files. | Saving changes in a text editor or appending lines with `>>`. |
| **x — Execute** | Allows a file to be executed as an executable binary or script; on a directory, allows traversing/entering it (`cd`). | Running a compiled executable or shell script (`./run.sh`). |

---

### Task 3.4 — Explain operating-system responsibilities
The operating system serves as the foundational resource manager between hardware components and user applications.

| OS responsibility | Your explanation | Example |
| :--- | :--- | :--- |
| **Process management** | Controls the creation, scheduling, execution, inter-process communication, and termination of processes, allocating CPU time slices via preemptive multitasking. | The OS scheduler switches execution between a web browser, code editor, and music player thousands of times per second. |
| **Memory management** | Allocates, tracks, and isolates virtual memory pages across physical RAM and disk swap spaces, preventing processes from interfering with or corrupting each other's memory. | Allocating 4 GB of RAM to a video editing program and cleanly reclaiming all allocated pages back to the free pool when closed. |
| **Device management** | Manages communication with peripheral hardware devices using device drivers, interrupt handlers, and input/output request queues. | Handling keyboard scan interrupts, translating trackpad gestures, or streaming audio buffers to a connected Bluetooth headset. |
| **File management** | Organizes data storage into logical hierarchical trees of directories and files, managing block allocation, metadata, paths, and caching on persistent storage. | The APFS file system locating physical storage blocks on the NVMe SSD and retrieving the contents of `README.md`. |
| **User interface / shell** | Provides a visual GUI or command-line CLI interface allowing users and administrators to issue instructions and control system behavior. | The macOS graphical Finder interface and the Zsh command-line Terminal shell. |
| **Security and permissions** | Enforces access controls, user authorization boundaries, cryptographic safeguards, and privilege separation to protect system integrity and privacy. | Preventing standard user accounts from modifying root system binaries in `/System` without elevated administrative authentication. |

---

## 3. Commands / tools used
- `sw_vers`, `uname -smr`: OS release and kernel architecture inspection.
- `whoami`, `id`: User identity and security group verification.
- `df -h`: Filesystem disk capacity and usage analysis.
- `top -l 1`: Operating system load, task state, and memory snapshot.
- `ls -l`: POSIX file permission inspection.

## 4. My understanding
The operating system acts as the master coordinator of the computer. By abstracting raw silicon into structured processes, virtual memory address spaces, POSIX permission systems, and hierarchical filesystems, it provides an isolated, reliable environment where multiple competing programs can execute concurrently without crashing the hardware or compromising security.

## 5. Difficulties faced
Interpreting the dense multi-column output generated by macOS `top`, particularly the distinction between wired, active, compressed, and unused physical memory.

## 6. How I resolved them
Consulted the macOS `top` man page (`man top`) to understand that macOS utilizes aggressive memory caching, meaning "unused" memory is kept low intentionally while "compressed" memory avoids disk paging to maximize performance.

## 7. Evidence / files
- `evidence/mission-03/system_info.txt`: Sanitized system release, user identity, disk usage, and top process monitor logs.

## 8. Commit details
- Commit message: `Document operating system and file management`
- Branch: `main`
- Status: Staged and committed locally.
