# Mission 1 — Know your computer

## 1. Task / objective
The objective of this mission is to understand the fundamental architecture of modern computing systems through the Input-Processing-Output-Storage (IPOS) model. This involves tracing a real-world computing workflow through each hardware stage, categorizing commonly used hardware components and software types (system, application, and utility software), and analyzing embedded computer systems encountered in daily life.

## 2. Work completed
- Detailed a comprehensive IPOS trace for the activity: *Writing and saving a source code file in a code editor*.
- Constructed an analysis table classifying five hardware devices and four software categories.
- Analyzed three everyday standalone embedded computer systems (ATM, Smart Traffic Controller, and Gaming Console), identifying their primary purpose, specific input mechanisms, and real-time outputs.
- Documented key conceptual insights on hardware-software synergy and operating system abstraction.

---

### Task 1.1 — Trace one activity using IPOS
**Chosen Activity:** Typing and saving a Python script (`hello.py`) in Visual Studio Code on macOS.

| Stage | What happens in your example? | Possible hardware / component |
| :--- | :--- | :--- |
| **Input** | The user presses alphanumeric and control keys on the keyboard. Each keypress closes a mechanical/scissor switch circuit, which the keyboard microcontroller translates into a scan code and sends via USB/Bluetooth interrupt signals to the system. | Built-in scissor-switch keyboard, multi-touch trackpad |
| **Processing** | The Central Processing Unit (CPU) receives the hardware interrupt, decodes the scan codes into UTF-8 characters via the operating system event queue, allocates dynamic memory in RAM for the text buffer, and instructs the Graphics Processing Unit (GPU) to rasterize the text glyphs for display. | Apple M-series SoC (CPU cores, RAM controller, GPU) |
| **Output** | The GPU drives the internal display matrix, rendering the updated text editor window with syntax highlighting in real time at 60/120 Hz, giving immediate visual feedback of each typed character. | Liquid Retina LED display panel |
| **Storage** | When the user triggers the Save command (`Cmd + S`), the editor initiates an OS write system call. The OS file system driver coordinates with the storage controller to commit the file buffer from volatile RAM across the NVMe bus into persistent NAND flash memory blocks. | High-speed NVMe Solid State Drive (SSD) |

#### How the activity moves from input to output and storage:
1. **Physical Event to Digital Signal:** Physical finger pressure is converted into digital scan codes by the keyboard controller.
2. **Interrupt & CPU Handling:** The CPU halts lower-priority background tasks briefly to service the hardware interrupt, handing the raw key code to the macOS I/O Kit and window server.
3. **Buffer Management:** The text editor application updates its in-memory document buffer allocated within volatile system RAM.
4. **Visual Feedback Loop (Output):** Concurrently, the display pipeline rasterizes the fonts and refreshes the frame buffer, updating the monitor pixels so the user sees the characters instantly.
5. **Persistent Serialization (Storage):** Upon invoking the save action, data moves across the high-speed internal bus from volatile memory (RAM) to non-volatile secondary storage (SSD), ensuring the file remains intact even after the computer is shut down.

---

### Task 1.2 — Identify hardware and software
The computer operates through an integrated ecosystem of physical hardware and layered software applications.

| Item / software name | Hardware or software? | Software type (if applicable) | Purpose |
| :--- | :--- | :--- | :--- |
| **Apple M-Series SoC / CPU** | Hardware | Not applicable | Executes machine instructions, performs arithmetic and logic computations, and coordinates data flow between system buses. |
| **Liquid Retina Display** | Hardware | Not applicable | Provides high-resolution visual output of the graphical user interface, text editors, terminal sessions, and application windows. |
| **NVMe Solid State Drive (SSD)** | Hardware | Not applicable | Provides non-volatile, persistent digital storage for files, libraries, user configurations, and the operating system. |
| **Integrated Multi-Touch Trackpad** | Hardware | Not applicable | Captures physical touch gestures and pointer movements to enable precise spatial user interaction with GUI elements. |
| **macOS (Darwin Kernel)** | Software | Operating system software | Manages system hardware resources, schedules CPU tasks, handles memory allocation, and enforces security and permissions. |
| **Visual Studio Code** | Software | Application software | Provides an integrated developer environment for writing, editing, debugging, and navigating source code files. |
| **Homebrew** | Software | Utility software | Automates the discovery, installation, dependency resolution, updating, and uninstallation of developer command-line packages. |
| **Activity Monitor / Disk Utility** | Software | Utility software | Diagnoses hardware health, inspects active processes, monitors memory pressure, and manages storage disk partitions. |

---

### Task 1.3 — Computer systems around you
Computing devices extend far beyond general-purpose personal computers and laptops. Dedicated embedded computing systems automate everyday infrastructure:

| System | Main purpose | One input | One output |
| :--- | :--- | :--- | :--- |
| **Automated Teller Machine (ATM)** | Enables self-service banking transactions such as cash withdrawals, fund transfers, and balance inquiries. | Numeric PIN entered via the encrypted physical PIN pad, or chip card inserted into the EMV smartcard reader. | Physical banknotes accurately counted and dispensed through the motorized shutter slot, accompanied by a printed transaction receipt. |
| **Smart Traffic Light Controller** | Optimizes road intersection vehicle flow and pedestrian crossing safety using dynamic interval scheduling. | Electromagnetic inductive loop sensor embedded in the roadway tarmac detecting the metal chassis of waiting vehicles. | High-illumination LED signal lenses switching states (Red, Yellow, Green) and acoustic pedestrian beepers. |
| **PlayStation 5 Gaming Console** | Executes real-time 3D simulation rendering, interactive physics, spatial audio, and game state networking. | DualSense wireless controller inputs (analog thumbstick displacement and trigger potentiometer pressure). | 4K 60/120fps video frame stream delivered over HDMI to a display, along with dynamic haptic feedback vibrations in the controller. |

---

## 3. Commands / tools used
- Markdown editor and text processor for structured table creation.
- macOS System Information (`system_profiler`) for hardware component identification.

## 4. My understanding
- **The IPOS Cycle:** Every digital transaction follows a predictable path: input devices convert human or physical stimuli into binary electrical signals; the CPU and RAM process and transform this data; output devices convert processed digital information into human-perceivable signals; and non-volatile storage guarantees persistence across power cycles.
- **Hardware vs Software Layers:** Hardware provides raw physical computation and storage capabilities, but remains dormant without software. Operating system software acts as the critical intermediary, virtualizing complex hardware abstractions so application software can perform user-facing tasks safely without direct hardware manipulation.

## 5. Difficulties faced
Distinguishing strictly between utility software and application software, particularly for developer tools like package managers that bridge system maintenance and application workflows.

## 6. How I resolved them
Clarified definitions: application software directly assists the user in achieving external end-user goals (such as text editing or web browsing), whereas utility software is dedicated to maintaining, configuring, optimizing, or supporting the computer system infrastructure itself.

## 7. Evidence / files
- `mission-01-computer-basics/README.md`: Complete IPOS workflow trace, hardware/software taxonomy table, and embedded computing systems analysis.

## 8. Commit details
- Commit message: `Complete computer basics and IPOS mission`
- Branch: `main`
- Status: Staged and committed locally to `main`.
