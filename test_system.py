"""
Unit Tests for Student Performance Analytics System
Validates reusable analytical functions, NumPy calculations, grading rules, and pass/fail logic.
"""

import unittest
import pandas as pd
import numpy as np
from functions import (
    load_dataset,
    calculate_totals_and_averages,
    determine_grade,
    assign_grades,
    evaluate_pass_fail,
    calculate_overall_class_summary,
    calculate_subject_performance,
    get_top_performers,
    calculate_pass_fail_statistics,
    calculate_department_performance,
)


class TestStudentPerformanceAnalytics(unittest.TestCase):

    def setUp(self):
        # Sample test dataframe with realistic values
        self.sample_data = pd.DataFrame([
            {
                "Student_ID": 1,
                "Name": "Alice",
                "Department": "CS",
                "Math_Marks": 90,
                "Science_Marks": 95,
                "English_Marks": 85,
                "Attendance_Percentage": 90,
            },
            {
                "Student_ID": 2,
                "Name": "Bob",
                "Department": "Mech",
                "Math_Marks": 35,
                "Science_Marks": 60,
                "English_Marks": 70,
                "Attendance_Percentage": 80,
            },
            {
                "Student_ID": 3,
                "Name": "Charlie",
                "Department": "Civil",
                "Math_Marks": 80,
                "Science_Marks": 85,
                "English_Marks": 75,
                "Attendance_Percentage": 70,  # Below 75%
            },
            {
                "Student_ID": 4,
                "Name": "Diana",
                "Department": "CS",
                "Math_Marks": 50,
                "Science_Marks": 55,
                "English_Marks": 45,
                "Attendance_Percentage": 85,
            },
        ])

    def test_determine_grade(self):
        self.assertEqual(determine_grade(90), "A")
        self.assertEqual(determine_grade(85), "A")
        self.assertEqual(determine_grade(75), "B")
        self.assertEqual(determine_grade(70), "B")
        self.assertEqual(determine_grade(60), "C")
        self.assertEqual(determine_grade(55), "C")
        self.assertEqual(determine_grade(45), "D")
        self.assertEqual(determine_grade(40), "D")
        self.assertEqual(determine_grade(39.9), "F")

    def test_calculate_totals_and_averages(self):
        res = calculate_totals_and_averages(self.sample_data)
        # Alice: 90 + 95 + 85 = 270, avg = 90.0
        self.assertEqual(res.loc[0, "Total_Marks"], 270)
        self.assertEqual(res.loc[0, "Average_Marks"], 90.0)
        # Bob: 35 + 60 + 70 = 165, avg = 55.0
        self.assertEqual(res.loc[1, "Total_Marks"], 165)
        self.assertEqual(res.loc[1, "Average_Marks"], 55.0)

    def test_assign_grades(self):
        df_calc = calculate_totals_and_averages(self.sample_data)
        res = assign_grades(df_calc)
        self.assertEqual(res.loc[0, "Grade"], "A")
        self.assertEqual(res.loc[1, "Grade"], "C")
        self.assertEqual(res.loc[2, "Grade"], "B")
        self.assertEqual(res.loc[3, "Grade"], "D")

    def test_evaluate_pass_fail(self):
        res = evaluate_pass_fail(self.sample_data)
        # Alice passed all criteria
        self.assertEqual(res.loc[0, "Status"], "Pass")
        # Bob failed Math (35 < 40)
        self.assertEqual(res.loc[1, "Status"], "Fail")
        self.assertIn("Failed in Math", res.loc[1, "Remark"])
        # Charlie low attendance (70 < 75)
        self.assertEqual(res.loc[2, "Status"], "Fail")
        self.assertIn("Low Attendance", res.loc[2, "Remark"])
        # Diana passed all
        self.assertEqual(res.loc[3, "Status"], "Pass")

    def test_overall_class_summary(self):
        df_calc = calculate_totals_and_averages(self.sample_data)
        summary = calculate_overall_class_summary(df_calc)
        self.assertEqual(summary["total_students"], 4)
        self.assertEqual(summary["highest_average"], 90.0)
        self.assertEqual(summary["lowest_average"], 50.0)
        self.assertIn("Alice", summary["top_student"])

    def test_subject_performance(self):
        subj_df, best = calculate_subject_performance(self.sample_data)
        self.assertEqual(len(subj_df), 3)
        self.assertIn(best, ["Math", "Science", "English"])

    def test_dataset_loading(self):
        df = load_dataset("students.csv")
        self.assertGreaterEqual(len(df), 20)
        required_cols = {"Student_ID", "Name", "Department", "Math_Marks", "Science_Marks", "English_Marks", "Attendance_Percentage"}
        self.assertTrue(required_cols.issubset(set(df.columns)))


if __name__ == "__main__":
    unittest.main()
