# Mission 4 — How programs run

## 1. Task / objective
The objective of this mission is to write and execute a standalone Python program, observe program execution via the command line, and analyze the architectural differences between compiled and interpreted programming language execution models.

## 2. Work completed
- Authored the script `hello.py` inside `mission-04-programs/`.
- Successfully executed `hello.py` from the command line using `python3`, observing the output `Hello from Python`.
- Constructed an in-depth comparison matrix evaluating compilers versus interpreters across execution timing, typical output products, real-world examples, and advantages.
- Composed a synthesized analysis explaining how modern high-level languages execute.

---

### Task 4.1 — Create and run a Python program
- **File:** `mission-04-programs/hello.py`
- **Program Code:**
  ```python
  print("Hello from Python")
  ```
- **Execution Command:**
  ```bash
  python3 hello.py
  ```
- **Observed Terminal Output:**
  ```text
  Hello from Python
  ```

---

### Task 4.2 — Compare compiler and interpreter

| Point | Compiler | Interpreter |
| :--- | :--- | :--- |
| **When translation / execution happens** | Translates the entire high-level source code into native machine code or intermediate binary ahead of time (at compile time), prior to program execution. | Translates and executes source code dynamically statement-by-statement or line-by-line during runtime. |
| **Typical output** | Produces a standalone, executable binary file (e.g., Mach-O on macOS, ELF on Linux, `.exe` on Windows) or bytecode binary (`.class`). | Does not generate a standalone machine-executable binary; outputs directly to standard output/execution environment at runtime. |
| **One example** | **C / C++** (`clang` / `gcc`), **Rust** (`rustc`), or **Go** (`go build`). | **Python** (`cpython`), **JavaScript** (browser engine / Node.js), or **Ruby**. |
| **One advantage** | **Optimal execution speed and performance:** Because machine code is pre-generated and heavily optimized before execution, compiled binaries run directly on the CPU without translation overhead. | **Portability and rapid development:** Source code can run directly on any target system with the interpreter installed, facilitating immediate testing and interactive debugging without build cycles. |

#### Synthesis & Explanation:
A compiler translates source code into native machine code in advance before program execution begins, producing an independent binary artifact that executes directly on the computer hardware with maximum computational efficiency. In contrast, an interpreter processes instructions dynamically at runtime, translating statements on the fly and executing them immediately without a mandatory pre-compilation phase. While compiled programs deliver superior raw execution performance and earlier syntax validation, interpreted environments provide developers with unmatched flexibility, cross-platform portability, and rapid iteration. Notably, modern languages such as Python often employ a hybrid design: source code is first compiled into intermediate bytecode (`.pyc`), which is subsequently interpreted by the Python Virtual Machine (PVM).

---

## 3. Commands / tools used
- `python3`: Invoked the CPython 3.14.7 runtime interpreter to execute `hello.py`.
- Text editor: Created and edited the Python source code file.

## 4. My understanding
Software cannot be understood directly by silicon hardware in its high-level textual form. The choice between compilation and interpretation represents an engineering trade-off: compilation optimizes for runtime execution speed and system resource efficiency, whereas interpretation optimizes for developer iteration velocity, portability, and rapid debugging.

## 5. Difficulties faced
Understanding whether Python is purely an interpreted language or whether it involves a compilation stage.

## 6. How I resolved them
Researched Python execution internals to discover that CPython compiles source text into bytecode instructions prior to execution by the bytecode interpreter virtual machine.

## 7. Evidence / files
- `mission-04-programs/hello.py`: Python program file containing `print("Hello from Python")`.
- Terminal output observation confirming successful execution.

## 8. Commit details
- Commit message: `Compare compilers and interpreters`
- Branch: `main`
- Status: Staged and committed locally.
