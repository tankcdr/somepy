# Robotic Arm Package Sorter

## **Objective**

This repository contains a function that sorts packages into the correct stack based on their **dimensions** (width, height, and length) and **mass**. It simulates a scenario where a robotic arm in Thoughtful's robotic automation factory dispatches packages to appropriate stacks.

---

## **Problem Statement**

The function sorts packages using the following criteria:

- A package is **bulky** if:
  - Its **volume** (Width x Height x Length) is greater than or equal to **1,000,000 cm³**, **OR**
  - Any of its dimensions (Width, Height, Length) is greater than or equal to **150 cm**.
- A package is **heavy** if its **mass** is greater than or equal to **20 kg**.

### **Sorting Rules**

- **STANDARD**: Packages that are **not bulky** and **not heavy**.
- **SPECIAL**: Packages that are **either bulky** or **heavy** (but not both).
- **REJECTED**: Packages that are **both bulky** and **heavy**.

---

## **How to Run**

### Prerequisites:

- Python 3.x installed on your system.

### Steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/robotic-arm-package-sorter.git
   cd robotic-arm-package-sorter
   ```

2. Run the Python script:

   ```bash
   python package_sorter.py
   ```

3. Verify the output for the predefined test cases.

---

## **Code Structure**

The main function `sort()` determines the stack based on the provided inputs:

- **Inputs**:

  - `width` (int): Width of the package in cm.
  - `height` (int): Height of the package in cm.
  - `length` (int): Length of the package in cm.
  - `mass` (int): Mass of the package in kg.

- **Output**:
  - Returns one of the following strings: `STANDARD`, `SPECIAL`, or `REJECTED`.

### **Example Usage**

#### **Code**

```python
    print(sort(100, 50, 200, 30))  # REJECTED (Both bulky and heavy)
    print(sort(150, 150, 150, 25)) # REJECTED (Both bulky and heavy)
    print(sort(50, 50, 50, 10))    # STANDARD (Neither bulky nor heavy)
    print(sort(100, 100, 100, 20)) # REJECTED (Both bulky and heavy)
    print(sort(10, 10, 10, 5))     # STANDARD (Neither bulky nor heavy)
    print(sort(200, 50, 50, 15))   # SPECIAL (Bulky but not heavy)
```

#### **Output**

```
REJECTED
REJECTED
STANDARD
REJECTED
STANDARD
SPECIAL
```

