# Project Documentation: Student Performance Analytics System

**Course:** EWB Courses | Python with AI  
**Assignment:** Python Project Assignment  
**Student Name:** Ansh  
**GitHub Repository:** [https://github.com/anshk025/Student-Performance-Analytics-System](https://github.com/anshk025/Student-Performance-Analytics-System)  
**Submission Deadline:** 15 October 2026 (on or before)  

---

## 1. Project Title
**Student Performance Analytics System**  
A Python-based academic data analytics system engineered using NumPy and Pandas to inspect student evaluation records, compute essential metrics, enforce grading criteria, evaluate pass/fail standing, and generate comprehensive departmental and subject-wise performance intelligence.

* **Student:** Ansh
* **GitHub Username:** anshk025
* **Target Repository:** https://github.com/anshk025/Student-Performance-Analytics-System

---

## 2. Objective
In educational administration, evaluation data encompasses diverse parameters—subject scores, attendance percentages, department distributions, and overall grade benchmarks. Calculating these values manually for large batches introduces high likelihood of clerical errors and delays in publishing results.

The primary objectives of this system are:
1. **Automate Grade & Performance Processing:** Read raw student records and compute total marks, averages, and letter grades without manual intervention.
2. **Implement Dual-Condition Evaluation:** Enforce institutional regulations requiring both a minimum score in all subjects ($\ge 40$) and an adequate attendance record ($\ge 75\%$).
3. **Generate Actionable Academic Insights:** Answer critical administrative queries:
   * Which student has the highest average?
   * Which student has the lowest average?
   * What is the overall class performance and spread?
   * Which subject reflects the highest and lowest student comprehension?
   * How many students passed or failed, and what were the exact grounds for failure?
4. **Demonstrate Core Python Concepts:** Exhibit the practical application of loops, functions, variables, Pandas DataFrame manipulation, and NumPy vector arithmetic.

---

## 3. Technologies Used
* **Python 3:** Core programming language utilizing procedural and functional paradigms.
* **NumPy (`numpy`):** Employed for statistical computations:
  * `np.mean()`: Arithmetic mean for averages.
  * `np.sum()`: Total marks summation.
  * `np.median()`: Median distribution calculation.
  * `np.std()`: Standard deviation to quantify dispersion.
  * `np.min()`, `np.max()`: Extreme value identification.
* **Pandas (`pandas`):** Used for tabular data management:
  * `pd.read_csv()`: CSV ingestion.
  * `DataFrame` slicing, masking, and column assignment.
  * `value_counts()`: Frequency distribution.
  * `groupby().agg()`: Departmental aggregations.
* **Unittest (`unittest`):** Comprehensive unit tests verifying computational accuracy.
* **Git & GitHub:** Version control and public repository hosting.

---

## 4. Dataset Description
The dataset is curated in [`students.csv`](students.csv) with 20 student entries reflecting realistic scores and attendance patterns across four engineering departments: Computer Science, Electronics, Mechanical, and Civil.

### Schema:
* `Student_ID`: Unique integer identifier (101 to 120).
* `Name`: Student full name.
* `Department`: Engineering department.
* `Math_Marks`: Score in Mathematics (out of 100).
* `Science_Marks`: Score in Science (out of 100).
* `English_Marks`: Score in English (out of 100).
* `Attendance_Percentage`: Attendance attendance percentage (out of 100%).

---

## 5. Implementation Details

The project is structured modularly:
* **`functions.py`**: Houses reusable logic, data processing routines, and statistical calculators.
* **`main.py`**: Orchestrates data loading, invokes processing functions, and outputs structured reports.
* **`test_system.py`**: Unit tests verifying all functions against synthetic test scenarios.
* **`students.csv`**: Source data file.

### Step-by-Step Execution:
1. **Data Ingestion (`load_dataset`):**
   Loads `students.csv` into a Pandas DataFrame and checks for existence.
2. **Totals & Averages Calculation (`calculate_totals_and_averages`):**
   Uses a `for` loop to iterate across students, converts individual subject marks into a NumPy array, and calls `np.sum()` and `np.mean()`.
3. **Grade Assignment (`assign_grades` & `determine_grade`):**
   * Grade A: $\ge 85\%$
   * Grade B: $70\% - 84.99\%$
   * Grade C: $55\% - 69.99\%$
   * Grade D: $40\% - 54.99\%$
   * Grade F: $< 40\%$
4. **Pass/Fail Assessment (`evaluate_pass_fail`):**
   Applies logic requiring subject cutoff $\ge 40$ in all 3 subjects AND attendance $\ge 75\%$. Populates a `Remark` column highlighting reasons for failure.
5. **Statistical Synthesis:**
   Calculates class metrics, subject metrics, top performers, and departmental aggregates.

---

## 6. Key Features
1. **Dynamic Path Handling:** Automatically resolves file paths relative to script directory.
2. **Detailed Failure Diagnostic:** Reports exact subjects failed or low attendance percentage.
3. **Comprehensive Subject Analytics:** Mean, Max, Min, and Standard Deviation per subject.
4. **Leaderboard Ranking:** Top 3 students with complete profile details.
5. **Departmental Breakdown:** Average marks and attendance comparisons per department.
6. **Automated Unit Tests:** Full test suite verifying grading, averages, and filtering rules.

---

## 7. Output & Results Summary

### Practical Answers to Core Assignment Questions:
* **Overall Class Average:** `71.02%`
* **Student with Highest Average:** Ananya Iyer (ID: 104) with `94.33%`
* **Student with Lowest Average:** Rahul Gupta (ID: 111) with `44.67%`
* **Subject with Best Average:** English (`72.35` average)
* **Pass / Fail Count:** Passed: 15 (75.0%) | Failed: 5 (25.0%)

### Top 3 Students:
1. **Rank #1:** Ananya Iyer (ID: 104, Computer Science) — Total: 283, Avg: 94.33%, Grade: A
2. **Rank #2:** Isha Bansal (ID: 116, Civil) — Total: 272, Avg: 90.67%, Grade: A
3. **Rank #3:** Meera Joshi (ID: 110, Electronics) — Total: 270, Avg: 90.00%, Grade: A

---

## 8. Final Outcome
The Student Performance Analytics System was successfully constructed and validated. It satisfies all assignment mandates without utilizing superfluous machine learning libraries, focusing strictly on core Python, NumPy, and Pandas principles taught in the course.

---

## 9. Challenges & Learning
* **Challenge:** Maintaining strict evaluation standards (e.g. failing students who scored high marks overall but failed a single subject or attendance).
  * **Solution:** Designed dual conditional evaluation with diagnostic notes to ensure transparency.
* **Challenge:** Platform-agnostic terminal formatting on Windows machines.
  * **Solution:** Replaced non-standard Unicode characters with standard ASCII characters.
* **Learning:** Deepened understanding of combining Pandas DataFrames with NumPy numerical functions and adopting modular design principles.

---

## 10. GitHub Repository
* **URL:** [https://github.com/anshk025/Student-Performance-Analytics-System](https://github.com/anshk025/Student-Performance-Analytics-System)
