# Mission 5 — numbers and data

## 1. task / objective
convert numbers between decimal, binary and hex by hand, check answers with Python, build a number converter script, and learn how text is stored

## 2. work completed
- solved all 7 number conversions showing simple steps
- checked all answers using Python built-in functions
- created and tested `number_converter.py` with 4 test numbers
- checked ASCII codes for letters and explained why text encoding is needed
---

### task 5.1 — convert numbers by hand

| question | your working and answer |
| :--- | :--- |
| **convert decimal 13 to binary** | 13 ÷ 2 = 6, rem 1<br>6 ÷ 2 = 3, rem 0<br>3 ÷ 2 = 1, rem 1<br>1 ÷ 2 = 0, rem 1<br>read from bottom to top:<br>**answer:** **1101** |
| **convert decimal 25 to binary** | 25 ÷ 2 = 12, rem 1<br>12 ÷ 2 = 6, rem 0<br>6 ÷ 2 = 3, rem 0<br>3 ÷ 2 = 1, rem 1<br>1 ÷ 2 = 0, rem 1<br>read from bottom to top:<br>**answer:** **11001** |
| **convert binary 1010 to decimal** | (1 × 8) + (0 × 4) + (1 × 2) + (0 × 1)<br>= 8 + 0 + 2 + 0<br>**answer:** **10** |
| **convert binary 1101 to decimal** | (1 × 8) + (1 × 4) + (0 × 2) + (1 × 1)<br>= 8 + 4 + 0 + 1<br>**answer:** **13** |
| **convert hexadecimal A to decimal** | in hex, A stands for 10<br>**answer:** **10** |
| **convert hexadecimal 1F to decimal** | (1 × 16) + (15 × 1)<br>= 16 + 15<br>**answer:** **31** |
| **convert binary 1111 to hexadecimal** | 1111 in decimal = 8 + 4 + 2 + 1 = 15<br>15 in hex is F<br>**answer:** **F** (or 0xF) |

---

### task 5.2 — verify using Python

| expression tested | result | matches manual calculation? |
| :--- | :--- | :---: |
| `bin(13)` | `'0b1101'` | **yes** |
| `bin(25)` | `'0b11001'` | **yes** |
| `int('1010', 2)` | `10` | **yes** |
| `int('1101', 2)` | `13` | **yes** |
| `int('A', 16)` | `10` | **yes** |
| `int('1F', 16)` | `31` | **yes** |
| `hex(0b1111)` | `'0xf'` | **yes** |

all manual calculations matched Python output

---

### task 5.3 — build a small number converter
- **file:** `mission-05-numbers-data/number_converter.py`
- **how to run:**
  ```bash
  python3 mission-05-numbers-data/number_converter.py
  ```
- **test results:**

| test number | binary output | hexadecimal output |
| :---: | :--- | :--- |
| **13** | `0b1101` | `0xd` |
| **25** | `0b11001` | `0x19` |
| **42** | `0b101010` | `0x2a` |
| **255** | `0b11111111` | `0xff` |

#### what the Python functions do:
- `int()`: changes user input text into a number
- `bin()`: turns a number into binary with `0b` in front
- `hex()`: turns a number into hex with `0x` in front

---

### task 5.4 — how is text stored?
- **ASCII decimal codes:**
  - uppercase letter **A**: **65**
  - lowercase letter **a**: **97**
- **why computers need an encoding standard to store text:**
  computers can only store numbers (0 and 1). they cannot store letters directly, so they need a table like ASCII or UTF-8 that matches each letter with a number
- **example of character not in basic ASCII:**
  the Indian rupee symbol **₹** or Hindi letter **क**

---

## 3. commands / tools used
- `python3`: ran the script and tested functions in Python terminal
- `bin()`, `hex()`, `int()`, `ord()`: built-in functions for conversions

## 4. my understanding
computers work only with 0 and 1 (binary). hex is used because it is much shorter and easier for humans to read than long binary strings

## 5. difficulties faced
no major difficulties

## 6. how i resolved them
not applicable

## 7. evidence / files
- `mission-05-numbers-data/number_converter.py`: number converter code
- `evidence/mission-05/converter_test_output.txt`: test outputs

## 8. commit details
- commit message: `build number converter and finish mission 5`
- branch: `main`
- status: committed and pushed to github
