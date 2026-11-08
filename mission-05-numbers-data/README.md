# Mission 5 — Numbers and data

## 1. Task / objective
The objective of this mission is to understand fundamental digital data representation principles, perform and document manual conversions between decimal (base 10), binary (base 2), and hexadecimal (base 16) numeral systems, verify the calculations programmatically using Python, develop a standalone CLI base converter program, and examine how character encoding standards represent textual information.

## 2. Work completed
- Worked through seven manual number conversions step by step using repeated division and place-value expansion.
- Verified all manual mathematical results using built-in Python conversion functions (`bin()`, `hex()`, `int()`).
- Developed and tested `number_converter.py` inside `mission-05-numbers-data/`, executing test runs across multiple positive decimal values.
- Investigated ASCII and UTF-8 text encoding standards, identified standard decimal character codes, and explained the role of encoding tables.

---

### Task 5.1 — Convert numbers by hand
All steps, remainders, and positional weights are detailed below:

| Question | Your working and answer |
| :--- | :--- |
| **Convert decimal 13 to binary** | **Method: Successive Division by 2**<br>• $13 \div 2 = 6$, remainder **1**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1**<br>Reading remainders from bottom to top (most significant to least significant bit):<br>**Answer:** $\mathbf{1101_2}$<br>*Check:* $(1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 8 + 4 + 0 + 1 = 13_{10}$. |
| **Convert decimal 25 to binary** | **Method: Successive Division by 2**<br>• $25 \div 2 = 12$, remainder **1**<br>• $12 \div 2 = 6$, remainder **0**<br>• $6 \div 2 = 3$, remainder **0**<br>• $3 \div 2 = 1$, remainder **1**<br>• $1 \div 2 = 0$, remainder **1**<br>Reading remainders from bottom to top:<br>**Answer:** $\mathbf{11001_2}$<br>*Check:* $(1 \times 2^4) + (1 \times 2^3) + (0 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) = 16 + 8 + 0 + 0 + 1 = 25_{10}$. |
| **Convert binary 1010 to decimal** | **Method: Positional Weight Expansion**<br>• Position 3: $1 \times 2^3 = 1 \times 8 = 8$<br>• Position 2: $0 \times 2^2 = 0 \times 4 = 0$<br>• Position 1: $1 \times 2^1 = 1 \times 2 = 2$<br>• Position 0: $0 \times 2^0 = 0 \times 1 = 0$<br>Sum: $8 + 0 + 2 + 0 = 10$<br>**Answer:** $\mathbf{10_{10}}$ |
| **Convert binary 1101 to decimal** | **Method: Positional Weight Expansion**<br>• Position 3: $1 \times 2^3 = 1 \times 8 = 8$<br>• Position 2: $1 \times 2^2 = 1 \times 4 = 4$<br>• Position 1: $0 \times 2^1 = 0 \times 2 = 0$<br>• Position 0: $1 \times 2^0 = 1 \times 1 = 1$<br>Sum: $8 + 4 + 0 + 1 = 13$<br>**Answer:** $\mathbf{13_{10}}$ |
| **Convert hexadecimal A to decimal** | **Method: Base-16 Place Value**<br>In hexadecimal, the digits are $0$–$9$ followed by $\text{A}=10, \text{B}=11, \text{C}=12, \text{D}=13, \text{E}=14, \text{F}=15$.<br>• Position 0: $\text{A} \times 16^0 = 10 \times 1 = 10$<br>**Answer:** $\mathbf{10_{10}}$ |
| **Convert hexadecimal 1F to decimal** | **Method: Base-16 Place Value Expansion**<br>• Position 1: $1 \times 16^1 = 16$<br>• Position 0: $\text{F} \times 16^0 = 15 \times 1 = 15$<br>Sum: $16 + 15 = 31$<br>**Answer:** $\mathbf{31_{10}}$ |
| **Convert binary 1111 to hexadecimal** | **Method: Direct 4-bit Binary-to-Hex Grouping**<br>• Binary nibble $1111_2$ evaluates to:<br>$(1 \times 8) + (1 \times 4) + (1 \times 2) + (1 \times 1) = 8 + 4 + 2 + 1 = 15_{10}$.<br>• In hexadecimal, the decimal value 15 corresponds to the symbol **F**.<br>**Answer:** $\mathbf{F_{16}}$ (or $\text{0xF}$) |

---

### Task 5.2 — Verify using Python
Executed in the Python 3 interactive shell environment (`python3`):

| Expression tested | Result | Matches manual calculation? |
| :--- | :--- | :---: |
| `bin(13)` | `'0b1101'` | **Yes** ($1101_2$) |
| `bin(25)` | `'0b11001'` | **Yes** ($11001_2$) |
| `int('1010', 2)` | `10` | **Yes** ($10_{10}$) |
| `int('1101', 2)` | `13` | **Yes** ($13_{10}$) |
| `int('A', 16)` | `10` | **Yes** ($10_{10}$) |
| `int('1F', 16)` | `31` | **Yes** ($31_{10}$) |
| `hex(0b1111)` | `'0xf'` | **Yes** ($\text{F}_{16}$) |

All manual calculations match Python's internal radix conversions.

---

### Task 5.3 — Build a small number converter
- **Script:** `mission-05-numbers-data/number_converter.py`
- **Execution:**
  ```bash
  python3 mission-05-numbers-data/number_converter.py
  ```
- **Test Results:**

| Test number | Binary output | Hexadecimal output |
| :---: | :--- | :--- |
| **13** | `0b1101` | `0xD` |
| **25** | `0b11001` | `0x19` |
| **42** | `0b101010` | `0x2A` |
| **255** | `0b11111111` | `0xFF` |

#### Explanation of Python conversion functions used:
- `int(string_input)`: Parses a string representation of digits into a base-10 Python integer object. When passed an optional second argument (e.g., `int('1010', 2)`), it parses the string according to the specified radix base.
- `bin(integer_value)`: Converts an integer to its binary equivalent string formatted with the standard `0b` prefix (e.g., `13` becomes `'0b1101'`).
- `hex(integer_value)`: Converts an integer to its lowercase hexadecimal equivalent string prefixed with `0x` (e.g., `25` becomes `'0x19'`). Slicing or string formatting (e.g., `hex(...).upper()`) formats the hex digits in uppercase.

---

### Task 5.4 — How is text stored?
- **ASCII Decimal Codes:**
  - **Uppercase letter 'A':** Decimal **65** (Binary: `01000001`, Hex: `0x41`). Verified in Python using `ord('A')`.
  - **Lowercase letter 'a':** Decimal **97** (Binary: `01100001`, Hex: `0x61`). Verified in Python using `ord('a')`.
  - *Observation:* Lowercase letters are offset from uppercase letters by exactly 32 ($2^5$), meaning toggling the 6th bit shifts between cases.
- **Why computers need an encoding standard to store text:**
  Computers cannot natively understand human alphabet characters, punctuation, or symbols; hardware registers and storage circuits only store binary state voltages representing 0s and 1s. A character encoding standard defines a standardized dictionary mapping each character glyph to a unique numeric code point, guaranteeing that text written on one machine is read and rendered identically across different operating systems, networks, and applications.
- **Example of a character not part of basic ASCII:**
  - The Indian Rupee currency sign **₹** (Unicode code point `U+20B9`, UTF-8 byte sequence `0xE2 0x82 0xB9`), or the Hindi Devanagari character **अ** (`U+0905`), or the emoji **🚀** (`U+1F680`). Standard ASCII is strictly limited to 7 bits (128 characters from 0 to 127), which accommodates only basic English letters, digits, and control codes.

---

## 3. Commands / tools used
- `python3`: Interactive shell verification and execution of `number_converter.py`.
- Built-in functions: `bin()`, `hex()`, `int()`, `ord()`, `chr()`.
- Text editor for script authoring.

## 4. My understanding
Number systems represent different lenses for viewing the same underlying quantity. While humans use base 10 (decimal) due to historical anatomical convention, digital electronic circuits rely on base 2 (binary) because transistors switch between two discrete voltage levels (on/off). Hexadecimal (base 16) acts as a human-friendly shorthand for binary, where each hexadecimal digit cleanly maps to exactly four binary bits (one nibble), enabling compact representation of memory addresses and byte streams.

## 5. Difficulties faced
Handling lowercase versus uppercase hexadecimal formatting conventions in Python's default `hex()` output.

## 6. How I resolved them
Used Python string manipulation (`.upper()`) and slicing to present the hexadecimal digits cleanly as `0xD`, `0x19`, and `0xFF`.

## 7. Evidence / files
- `mission-05-numbers-data/number_converter.py`: Complete Python number converter script.
- `evidence/mission-05/converter_test_output.txt`: Captured test execution log for inputs 13, 25, 42, and 255.

## 8. Commit details
- Commit message: `Build number converter and practise data representation`
- Branch: `main`
- Status: Staged and committed locally.
