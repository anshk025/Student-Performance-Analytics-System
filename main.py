"""
Student Performance Analytics System
Author: Ansh (GitHub: anshk025)
Course: EWB Courses | Python with AI
Project Title: Student Performance Analytics System
Technology Stack: Python, NumPy, Pandas

This is the main entry point for running the Student Performance Analytics System.
It loads student records from students.csv, processes calculations using NumPy and Pandas,
and outputs clean, comprehensive performance analytics.
"""

import sys
from functions import (
    load_dataset,
    calculate_totals_and_averages,
    assign_grades,
    evaluate_pass_fail,
    calculate_overall_class_summary,
    calculate_subject_performance,
    get_top_performers,
    calculate_pass_fail_statistics,
    calculate_department_performance,
)


def print_header(title):
    print("=" * 80)
    print(f" {title.upper()} ".center(80, "="))
    print("=" * 80)


def print_subheader(title):
    print("\n" + "-" * 80)
    print(f"  {title}")
    print("-" * 80)


def run_pipeline():
    print_header("Student Performance Analytics System")
    print(" Developed for EWB Courses | Python with AI Assignment")
    print(" Author: Ansh | GitHub: https://github.com/anshk025/Student-Performance-Analytics-System")
    print("=" * 80)

    # -------------------------------------------------------------
    # Step 1 & 2: Load the Dataset
    # -------------------------------------------------------------
    print_subheader("STEP 1 & 2: DATASET LOADING AND INSPECTION")
    try:
        raw_df = load_dataset("students.csv")
        print(f"[+] Dataset loaded successfully from 'students.csv'.")
        print(f"[+] Total Student Records Found: {len(raw_df)}")
        print(f"[+] Columns: {', '.join(raw_df.columns.tolist())}\n")
    except Exception as e:
        print(f"[!] Error loading dataset: {e}")
        sys.exit(1)

    # -------------------------------------------------------------
    # Step 3: Process the Data
    # -------------------------------------------------------------
    print_subheader("STEP 3: DATA PROCESSING (NUMPY & PANDAS)")
    print("[-] Calculating Total Marks & Average Marks using NumPy...")
    processed_df = calculate_totals_and_averages(raw_df)

    print("[-] Assigning Letter Grades based on defined grading criteria...")
    processed_df = assign_grades(processed_df)

    print("[-] Evaluating Pass/Fail status based on subject cutoffs (>=40) and attendance (>=75%)...")
    processed_df = evaluate_pass_fail(processed_df)

    print("[+] Data processing complete.\n")

    # Display Processed Student Records Table
    display_cols = [
        "Student_ID",
        "Name",
        "Department",
        "Math_Marks",
        "Science_Marks",
        "English_Marks",
        "Total_Marks",
        "Average_Marks",
        "Grade",
        "Attendance_Percentage",
        "Status",
    ]
    print("Processed Student Scorecards:")
    print(processed_df[display_cols].to_string(index=False))

    # -------------------------------------------------------------
    # Step 4: Perform Analysis & Answer Practical Questions
    # -------------------------------------------------------------
    print_subheader("STEP 4: PRACTICAL QUESTIONS & EXECUTIVE SUMMARY")

    class_summary = calculate_overall_class_summary(processed_df)
    subject_summary_df, best_subject = calculate_subject_performance(processed_df)
    pass_fail_stats = calculate_pass_fail_statistics(processed_df)
    top_3_students = get_top_performers(processed_df, top_n=3)

    print(f" 1. Overall Class Average Marks : {class_summary['class_average']:.2f} / 100")
    print(f" 2. Student with Highest Average: {class_summary['top_student']} (Score: {class_summary['highest_average']}%)")
    print(f" 3. Student with Lowest Average : {class_summary['lowest_student']} (Score: {class_summary['lowest_average']}%)")
    print(f" 4. Subject with Best Average   : {best_subject}")
    print(f" 5. Pass/Fail Student Count     : Passed: {pass_fail_stats['passed_count']} ({pass_fail_stats['pass_percentage']}%) | Failed: {pass_fail_stats['failed_count']} ({pass_fail_stats['fail_percentage']}%)")

    # Overall Class Performance Metrics
    print_subheader("OVERALL CLASS PERFORMANCE (NUMPY COMPUTED)")
    print(f" * Total Enrolled Students : {class_summary['total_students']}")
    print(f" * Class Mean Average      : {class_summary['class_average']}")
    print(f" * Class Median Score      : {class_summary['class_median']}")
    print(f" * Standard Deviation      : {class_summary['class_std_dev']}")
    print(f" * Highest Score           : {class_summary['highest_average']} ({class_summary['top_student']})")
    print(f" * Lowest Score            : {class_summary['lowest_average']} ({class_summary['lowest_student']})")

    # Subject-Wise Breakdown
    print_subheader("SUBJECT-WISE PERFORMANCE ANALYSIS")
    print(subject_summary_df.to_string(index=False))

    # Pass / Fail Detailed Analysis
    print_subheader("PASS / FAIL CRITERIA EVALUATION")
    print("Criteria:")
    print("  1. Minimum 40 marks in each individual subject (Math, Science, English).")
    print("  2. Minimum 75% overall attendance.")
    print("\nSummary:")
    print(f"  * Students Passed: {pass_fail_stats['passed_count']} / {pass_fail_stats['total_students']} ({pass_fail_stats['pass_percentage']}%)")
    print(f"  * Students Failed: {pass_fail_stats['failed_count']} / {pass_fail_stats['total_students']} ({pass_fail_stats['fail_percentage']}%)")

    failed_students = processed_df[processed_df["Status"] == "Fail"][
        ["Student_ID", "Name", "Department", "Attendance_Percentage", "Remark"]
    ]
    if not failed_students.empty:
        print("\nBreakdown of Unsuccessful Candidates & Underlying Reasons:")
        print(failed_students.to_string(index=False))

    # Top-Performing Students Showcase
    print_subheader("TOP 3 PERFORMING STUDENTS")
    for rank, (_, row) in enumerate(top_3_students.iterrows(), start=1):
        print(
            f" Rank #{rank}: {row['Name']} (ID: {row['Student_ID']}) | Dept: {row['Department']} | "
            f"Total: {row['Total_Marks']} | Avg: {row['Average_Marks']}% | Grade: {row['Grade']} | Attendance: {row['Attendance_Percentage']}%"
        )

    # Department-Wise Performance Breakdown
    print_subheader("DEPARTMENT-WISE PERFORMANCE SUMMARY")
    dept_df = calculate_department_performance(processed_df)
    print(dept_df.to_string(index=False))

    print("\n" + "=" * 80)
    print(" Analytics Pipeline Completed Successfully ".center(80, "="))
    print("=" * 80 + "\n")


def main():
    run_pipeline()


if __name__ == "__main__":
    main()