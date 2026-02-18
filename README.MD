# CLOUDFIDE Junior Data Engineer

## Task: Virtual Columns in Pandas DataFrame

The goal of this task was to implement an `add_virtual_column` function that takes an existing pandas DataFrame, a mathematical expression (the `role`), and a new column name, then returns a new DataFrame with the computed column appended.

---

## My Approach

I chose to solve this using **plain Python string methods** without any external libraries beyond pandas. I wanted the logic to be simple, readable, and easy to follow step by step.

### How the function works

The function runs through these steps in order:

**1. Validate existing column names**

Before doing anything, I check that every column name in the DataFrame only contains letters and underscores. I do this by looping through each character using Python's built-in `str.isalpha()` method combined with a check for `_`. If any column has a hyphen, number, or special character, the function immediately returns an empty DataFrame.

**2. Validate the new column name**

The same character-by-character check is applied to the `new_column` argument. For example, `"label3"` would fail because `"3"` is not a letter or underscore.

**3. Find the operator**

I loop through the `role` string looking for `+`, `-`, or `*`. If none of these are found, the expression is invalid and an empty DataFrame is returned.

**4. Split the expression**

Once the operator is found, I use `str.split(operator)` to break the expression into a first and second column name. For example, `"label_one * label_two"` split on `"*"` gives `["label_one ", " label_two"]`. I then use `.strip()` to remove any surrounding spaces.

**5. Validate the parsed column names**

The same label validation is applied to both the left and right column names extracted from the expression.

**6. Check columns exist in the DataFrame**

Even if the column names are valid strings, they must actually exist in the DataFrame. If either is missing, an empty DataFrame is returned.

**7. Compute and return the result**

Finally, I apply the operation on the two columns and attach the result as a new column on a copy of the original DataFrame (using `df.copy()` to avoid modifying the original).

---

## How to Run the Tests

### Requirements

```bash
pip install pandas pytest
```

### Run

```bash
pytest 'test_virtual_column 1.py' -v
```

---

## Project Structure

```
├── solution.py       # solution to the task
├── test_virtual_column 1.py      # Unit tests provided as part of the task to test solution
├── .gitignore      # keep the repository clean from system files
└── README.md         # This file

```
## Result Screenshot
<img width="984" height="480" alt="Image" src="https://github.com/user-attachments/assets/076c615e-9f17-4424-bb48-f13445e24602" />