# The Digital Detective: Explore Your Computer • Build a Mini System Report

## Diwali Independent Learning Assignment
- **Student Name:** Hrishant
- **USN Reference:** Ends in `8440`
- **GitHub Repository:** [digital-detective-8440](https://github.com/hrishantt/digital-detective-8440)
- **Host Environment:** macOS 27.2 (ARM64 Apple Silicon), Zsh Shell, Python 3.14.7, Git 2.56.0

---

## 1. Project Introduction & Purpose
**The Digital Detective** is a comprehensive, practical computer science investigation designed to explore how computer systems function from the hardware layer up to network communication. Spanning nine distinct missions, this assignment examines hardware architecture, operating system internals, command-line operations, programming language execution models, numerical representations, distributed version control, and internet networking.

Every mission has been completed in strict chronological sequence, documented within its own dedicated mission folder using the mandatory standardized outline, backed by authentic empirical evidence, and recorded with dedicated Git commits.

---

## 2. Topics Explored
1. **Computer Fundamentals & The IPOS Cycle:** Input, Processing, Output, and Storage workflows; hardware/software categorization; embedded computer systems.
2. **Terminal Navigation & Command-Line File Management:** Directory inspection, non-destructive file operations, Unix flags, stream pipelines (`|`), and package managers (Homebrew).
3. **Operating System Architecture & Permissions:** Kernel metrics, CPU/memory resource monitoring, process lifecycles, PIDs, absolute vs. relative path resolution, POSIX access permissions (`rwx`), and OS responsibilities.
4. **How Programs Run:** Ahead-of-time (AOT) compilers versus runtime interpreters, bytecode execution, and Python program execution.
5. **Number Systems & Data Representation:** Manual step-by-step mathematical conversions between decimal, binary, and hexadecimal; programmatic verification; interactive Python CLI converter; ASCII and UTF-8 text encoding.
6. **Version Control with Git & GitHub:** Repository lifecycle states, staging vs. committing, branching (`update-about`), Pull Request simulation, and a daily Git command glossary.
7. **Computer Networks & Web Communication:** Network topologies (LAN, MAN, WAN), DNS resolution, packet switching, routers, client-server models, and the 7-step lifecycle of an HTTP/TLS web request.
8. **Final System Audit & Quality Assurance:** Comprehensive repository review, verification checklist, and submission audit.

---

## 3. Mission Navigation Index

| Mission | Focus Area | Status | Documentation Link |
| :---: | :--- | :---: | :--- |
| **Mission 0** | Repository and workspace setup | Completed | [mission-00-setup/README.md](mission-00-setup/README.md) |
| **Mission 1** | Computer fundamentals and IPOS | Completed | [mission-01-computer-basics/README.md](mission-01-computer-basics/README.md) |
| **Mission 2** | Terminal and file management | Completed | [mission-02-terminal/README.md](mission-02-terminal/README.md) |
| **Mission 3** | Operating system, processes and permissions | Completed | [mission-03-operating-system/README.md](mission-03-operating-system/README.md) |
| **Mission 4** | How programs run (Compiler vs Interpreter) | Completed | [mission-04-programs/README.md](mission-04-programs/README.md) |
| **Mission 5** | Number systems, Python and text encoding | Completed | [mission-05-numbers-data/README.md](mission-05-numbers-data/README.md) |
| **Mission 6** | Git, GitHub, branches and Pull Requests | Completed | [mission-06-git-github/README.md](mission-06-git-github/README.md) |
| **Mission 7** | Computer networks and web communication | Completed | [mission-07-networking/README.md](mission-07-networking/README.md) |
| **Mission 8** | Final review and submission report | Completed | [mission-08-final-report/README.md](mission-08-final-report/README.md) |

---

## 4. Instructions for Running the Python Programs

### A. Number Converter (`number_converter.py`)
The number converter prompts for a positive decimal integer and computes its binary and hexadecimal representations.

1. Navigate to the mission directory:
   ```bash
   cd mission-05-numbers-data
   ```
2. Execute the script using Python 3:
   ```bash
   python3 number_converter.py
   ```
3. Enter any positive decimal number (e.g. `13`, `25`, `42`, or `255`) when prompted:
   ```text
   ===================================
          DIGITAL NUMBER CONVERTER      
   ===================================
   Enter a positive decimal integer: 25

   --- Conversion Results ---
   Decimal (Base 10):     25
   Binary (Base 2):       0b11001
   Hexadecimal (Base 16): 0x19
   ===================================
   ```

### B. Hello Program (`hello.py`)
1. Navigate to the mission directory:
   ```bash
   cd mission-04-programs
   ```
2. Run the script:
   ```bash
   python3 hello.py
   ```
   *Expected Output:* `Hello from Python`

---

## 5. Summary of Key Learnings
- **Hardware-Software Abstraction:** The IPOS model demonstrates how low-level physical keystrokes and electronic interrupts are handled by the OS kernel, mediated through memory buffers in RAM, and persisted to non-volatile SSD storage blocks.
- **Terminal Control and Composability:** Command-line operations and Unix pipelines (`|`) provide a direct mechanism to query system metrics, inspect processes, and process data streams efficiently in memory without intermediate files.
- **Data Uniformity Across Systems:** Underneath programming languages and character encodings, all data and instructions are fundamentally stored as binary bits (0s and 1s), efficiently expressed in hexadecimal for human inspection and translated seamlessly by compilers and interpreters.
- **Collaborative Engineering Discipline:** Git version control provides safety, accountability, and traceability. Isolating features into branches and reviewing them through Pull Requests ensures stability across team codebases.
- **Network Protocol Layering:** From local LANs to global WANs, internet communication functions through layered protocols: DNS resolves names to IP addresses, routers forward packets through dynamic packet switching, and client-server architectures power the modern web.

---

## 6. Git Commit Protocol & Workflow Discipline
In strict adherence to assignment requirements:
- Each mission was completed, verified, and documented independently before beginning subsequent tasks.
- Dedicated, meaningful commit messages were authored for every mission milestone.
- All mission folders include their own complete `README.md` following the mandatory 8-part section template.

---

## 7. Privacy & Sanitization Policy
To comply with the assignment security rules, all personally identifiable information (including local machine account usernames, hardware MAC/serial numbers, Wi-Fi SSIDs, internal IP addresses, and authentication tokens) has been sanitized and replaced with `[redacted]` across all markdown files and terminal output logs.
