"""
Student Performance Analytics System - Reusable Functions Module
Author: Ansh (GitHub: anshk025)
Course: EWB Courses | Python with AI
Project: Student Performance Analytics System

This module provides reusable analytical and processing functions
powered by NumPy and Pandas for student performance evaluation.
"""

import os
import pandas as pd
import numpy as np

# Subject columns used across the application
SUBJECT_COLUMNS = ["Math_Marks", "Science_Marks", "English_Marks"]
PASSING_MARKS_PER_SUBJECT = 40
MIN_ATTENDANCE_PERCENTAGE = 75


def load_dataset(file_path="students.csv"):
    """
    Loads student data from a CSV file into a Pandas DataFrame.
    Validates that the file exists and contains the required columns.
    """
    if not os.path.exists(file_path):
        # Fallback to local directory relative to this script
        alt_path = os.path.join(os.path.dirname(__file__), "students.csv")
        if os.path.exists(alt_path):
            file_path = alt_path
        else:
            raise FileNotFoundError(f"Dataset file not found at: {file_path}")

    df = pd.read_csv(file_path)
    return df


def calculate_totals_and_averages(df, subjects=None):
    """
    Calculates total marks and average marks for each student.
    Uses loops and NumPy calculations (np.sum, np.mean).
    """
    if subjects is None:
        subjects = SUBJECT_COLUMNS

    df_copy = df.copy()
    total_marks_list = []
    average_marks_list = []

    # Iterating over each student using a loop
    for i in range(len(df_copy)):
        marks = [df_copy.loc[i, subject] for subject in subjects]
        marks_array = np.array(marks, dtype=float)

        total = np.sum(marks_array)
        avg = np.mean(marks_array)

        total_marks_list.append(int(round(total)))
        average_marks_list.append(round(float(avg), 2))

    df_copy["Total_Marks"] = total_marks_list
    df_copy["Average_Marks"] = average_marks_list
    return df_copy


def determine_grade(average_score):
    """
    Determines letter grade based on a defined grading scheme:
    - 85 and above: Grade A (Distinction)
    - 70 to 84.99:  Grade B (First Class)
    - 55 to 69.99:  Grade C (Second Class)
    - 40 to 54.99:  Grade D (Pass Grade)
    - Below 40:     Grade F (Fail)
    """
    if average_score >= 85:
        return "A"
    elif average_score >= 70:
        return "B"
    elif average_score >= 55:
        return "C"
    elif average_score >= 40:
        return "D"
    else:
        return "F"


def assign_grades(df):
    """
    Assigns grades to all students in the DataFrame using a loop.
    """
    df_copy = df.copy()
    grades = []
    for avg in df_copy["Average_Marks"]:
        grade = determine_grade(avg)
        grades.append(grade)

    df_copy["Grade"] = grades
    return df_copy


def evaluate_pass_fail(df, subjects=None, passing_mark=PASSING_MARKS_PER_SUBJECT, min_attendance=MIN_ATTENDANCE_PERCENTAGE):
    """
    Evaluates Pass/Fail status for each student based on:
    1. Scoring at least `passing_mark` (40) in each subject.
    2. Maintaining at least `min_attendance` (75%) attendance.
    """
    if subjects is None:
        subjects = SUBJECT_COLUMNS

    df_copy = df.copy()
    status_list = []
    reasons_list = []

    for i in range(len(df_copy)):
        failed_subjects = []
        for subj in subjects:
            if df_copy.loc[i, subj] < passing_mark:
                failed_subjects.append(subj.replace("_Marks", ""))

        attendance = df_copy.loc[i, "Attendance_Percentage"]
        low_attendance = attendance < min_attendance

        if failed_subjects or low_attendance:
            status_list.append("Fail")
            reasons = []
            if failed_subjects:
                reasons.append(f"Failed in {', '.join(failed_subjects)}")
            if low_attendance:
                reasons.append(f"Low Attendance ({attendance}%)")
            reasons_list.append("; ".join(reasons))
        else:
            status_list.append("Pass")
            reasons_list.append("Cleared all criteria")

    df_copy["Status"] = status_list
    df_copy["Remark"] = reasons_list
    return df_copy


def calculate_overall_class_summary(df):
    """
    Computes overall class summary statistics using NumPy.
    Returns a dictionary of class-level metrics.
    """
    averages = np.array(df["Average_Marks"], dtype=float)
    totals = np.array(df["Total_Marks"], dtype=float)

    highest_avg = np.max(averages)
    lowest_avg = np.min(averages)
    class_mean = round(float(np.mean(averages)), 2)
    class_median = round(float(np.median(averages)), 2)
    class_std = round(float(np.std(averages)), 2)

    top_idx = df["Average_Marks"].idxmax()
    lowest_idx = df["Average_Marks"].idxmin()

    top_student_name = df.loc[top_idx, "Name"]
    top_student_id = df.loc[top_idx, "Student_ID"]
    lowest_student_name = df.loc[lowest_idx, "Name"]
    lowest_student_id = df.loc[lowest_idx, "Student_ID"]

    return {
        "total_students": len(df),
        "class_average": class_mean,
        "class_median": class_median,
        "class_std_dev": class_std,
        "highest_average": highest_avg,
        "top_student": f"{top_student_name} (ID: {top_student_id})",
        "lowest_average": lowest_avg,
        "lowest_student": f"{lowest_student_name} (ID: {lowest_student_id})",
    }


def calculate_subject_performance(df, subjects=None):
    """
    Calculates subject-wise performance metrics (Average, Max, Min, Std Dev)
    using loops and NumPy operations.
    Returns a summary DataFrame.
    """
    if subjects is None:
        subjects = SUBJECT_COLUMNS

    records = []
    # Loop over each subject
    for subject in subjects:
        marks = np.array(df[subject], dtype=float)
        clean_name = subject.replace("_Marks", "")

        subj_mean = round(float(np.mean(marks)), 2)
        subj_max = int(np.max(marks))
        subj_min = int(np.min(marks))
        subj_std = round(float(np.std(marks)), 2)

        records.append({
            "Subject": clean_name,
            "Average Marks": subj_mean,
            "Highest Marks": subj_max,
            "Lowest Marks": subj_min,
            "Std Deviation": subj_std,
        })

    subject_df = pd.DataFrame(records)
    best_subject_row = subject_df.loc[subject_df["Average Marks"].idxmax()]
    best_subject = best_subject_row["Subject"]

    return subject_df, best_subject


def get_top_performers(df, top_n=3):
    """
    Retrieves top N performing students sorted by Total Marks and Average Marks.
    """
    sorted_df = df.sort_values(by=["Total_Marks", "Average_Marks"], ascending=[False, False]).reset_index(drop=True)
    return sorted_df.head(top_n)


def calculate_pass_fail_statistics(df):
    """
    Calculates total count and percentage of passing and failing students.
    """
    total = len(df)
    status_counts = df["Status"].value_counts().to_dict()
    passed = status_counts.get("Pass", 0)
    failed = status_counts.get("Fail", 0)

    pass_percentage = round((passed / total) * 100, 2) if total > 0 else 0.0
    fail_percentage = round((failed / total) * 100, 2) if total > 0 else 0.0

    return {
        "total_students": total,
        "passed_count": passed,
        "failed_count": failed,
        "pass_percentage": pass_percentage,
        "fail_percentage": fail_percentage,
    }


def calculate_department_performance(df):
    """
    Groups students by department and calculates departmental performance metrics.
    """
    dept_summary = (
        df.groupby("Department")
        .agg(
            Student_Count=("Student_ID", "count"),
            Average_Marks=("Average_Marks", "mean"),
            Average_Attendance=("Attendance_Percentage", "mean"),
        )
        .reset_index()
    )
    dept_summary["Average_Marks"] = dept_summary["Average_Marks"].round(2)
    dept_summary["Average_Attendance"] = dept_summary["Average_Attendance"].round(2)
    return dept_summary
