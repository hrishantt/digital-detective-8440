# Mission 4 — how programs run

## 1. task / objective
write and run a simple Python program, and understand how compilers and interpreters run code

## 2. work completed
- created `hello.py` inside `mission-04-programs`
- ran it from terminal using `python3 hello.py`, output was `Hello from Python`
- made a simple table comparing compiler and interpreter

---

### task 4.1 — create and run a Python program
- **file:** `mission-04-programs/hello.py`
- **code:**
  ```python
  print("Hello from Python")
  ```
- **command to run:**
  ```bash
  python3 hello.py
  ```
- **what i observed:**
  ```text
  Hello from Python
  ```

---

### task 4.2 — compare compiler and interpreter

| point | compiler |interpreter| 
| :--- | :--- | :--- |
| **when translation happens** | translates all code at once before running | translates line by line while running |
| **typical output** | makes an executable file (like .exe) | gives direct output on the screen |
| **one example** | C or C++ | Python |
| **one advantage** | program runs very fast | easy to test and find bugs |

#### simple explanation:
a compiler converts the entire code into machine language before the program starts, making it run faster. an interpreter reads and runs the code line by line at runtime without making a separate file. compiled code is faster for big apps, but interpreted code is easier for testing and writing programs quickly. Python first creates bytecode and then runs it using the Python interpreter

---

## 3. commands / tools used
- `python3`: used to run the Python script
- text editor: used to write the code

## 4. my understanding
computers do not understand human language. they need a compiler or interpreter to change our code into binary instructions that the CPU can execute

## 5. difficulties faced
understanding if Python is compiled or interpreted

## 6. how i resolved them
found out that Python does both: it first compiles to bytecode, then interprets it

## 7. evidence / files
- `mission-04-programs/hello.py`: Python program file

## 8. commit details
- commit message: `add hello program and compare compiler and interpreter`
- branch: `main`
- status: committed and pushed to github
