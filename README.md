# Python Projects Repository

This repository contains a collection of Python projects developed as part of academic coursework, practice challenges, and hands-on learning activities.

## About
The projects in this repository focus on strengthening core Python concepts such as:
- Data types and variables
- Conditional statements
- String manipulation
- Basic input/output handling
- Problem-solving using logical thinking

Each project is implemented using simple and clear Python code, following standard programming practices and academic guidelines.

## Day-wise Progress

### Day 1: User Profile Validator
- **Focus**: Basic input validation.
- **Features**: Validates Full Name (checked for spaces), Email (standard format), Mobile (10 digits), and Age (range 18-60).

### Day 2: Smart ID & Credential Validator
- **Focus**: String manipulation and pattern matching.
- **Features**: 
  - **Student ID**: Validates format (e.g., CSE-123).
  - **Email**: Checks for `.edu` domain.
  - **Password**: Ensures it starts with an uppercase letter and contains at least one digit.
  - **Referral Code**: Validates prefix and symbol requirements.

### Day 3: Student Marks Evaluator
- **Focus**: List handling and conditional logic.
- **Features**: Categorizes marks into Excellent, Very Good, Good, etc., using logic based on whether the student's name length is even or odd.

### Day 4: Activity Score Risk Analyzer
- **Focus**: Data categorization and filtering.
- **Features**: Sorts scores into Low, Medium, High, and Critical risk categories. Applies personalized filtering (removing specific risk levels) based on the parity of the last digit of the Register Number.

### Day 5: Resource Request Personalizer
- **Focus**: Advanced filtering and personalization rules.
- **Special Metrics**:
  - **L value**: The length of the user's name (excluding spaces).
  - **PLI Value**: Calculated as `L % 3`.
- **Applied Rules (Personalization)**:
  - If `PLI == 0`: All **Low Demand** requests are removed.
  - If `PLI == 1`: All **High Demand** requests are removed.
  - If `PLI == 2`: Both **Low** and **High Demand** requests are removed (keeping only Moderate).

### Day 6: Transaction Risk Categorizer
- **Focus**: Data categorization and risk assessment.
- **Features**: 
  - Categorizes transactions into Normal, Large, High Risk, and Invalid based on their amounts.
  - Calculates total value and number of valid transactions.
  - Determines a final risk level (Low, Moderate, High Risk) based on the total high-risk transaction count and overall transaction value.

### Day 8: Student Performance Analytics
- **Focus**: Data analysis using Pandas, NumPy, and Math.
- **Features**: 
  - **Data Generation**: Creates a dataset of students with marks, attendance, and assignment scores.
  - **Metrics Calculation**: Computes average scores and a custom **Performance Index** using vectorized NumPy operations.
  - **Classification**: Categorizes students into Top Performer, Good, and Average based on their overall average.
  - **Statistical Insights**: Extracts mean marks, peak performance values, and logarithmic distributions of scores.

### Day 9: Electronics Store Inventory Copy Behavior
- **Focus**: Shallow vs. Deep Copy mechanisms in memory management.
- **Features**:
  - Demonstrates how nested object references are shared in shallow copies.
  - Implements a deep copy using the `copy` module for complete data isolation.
  - Applies a personalized 10% discount and stock update logic based on register number modulo operations.
  - Compares value integrity between original and modified copies.

### Day 10: Academic Data Drift & Copy Behavior Analyzer
- **Focus**: Advanced Data Analysis and mutation tracking using NumPy and Pandas.
- **Features**:
  - **Data Simulation**: Generates structured academic records for 12 students.
  - **Mutation Tracking**: Applies a square-root-based mathematical transformation to marks and monitors "Data Drift."
  - **Statistical Insights**: Computes mean, median, standard deviation, and Min-Max normalization using vectorized operations.
  - **Classification**: Categorizes performance shifts (Stable, Minor, or Critical Drift) based on statistical thresholds.
  - **Tabular Reporting**: Utilizes Pandas DataFrames for clear comparison between original, shallow, and deep-copied datasets.

---
