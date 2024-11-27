# -Financial-Insights-Dashboard-and-Scoring-Model
Model Logic Explanation:
# 1. Data Loading and Exploration:
#    - Loads the dataset using pandas.
#    - Displays basic information (data types, missing values, summary statistics).
#    - Visualizes data distributions and relationships using histograms, pair plots, and correlation matrices.
#    - Explores categorical features if any.

# 2. Feature Engineering and Data Preprocessing:
#   - Converts 'Transaction Date' to datetime objects.
#   - Aggregates data by family to analyze family-level financial patterns (e.g. total spending, income, savings, etc.)
#   - Calculates a 'Financial Score' for each family based on several financial metrics using a weighted scoring system.
#       - The higher the score, the better the financial situation of the family.

# 3. Financial Score Calculation:
#   - `calculate_financial_score` function computes a financial score between 0 and 100 for each family.
#   - The function uses weighted averages of various financial indicators:
#     - Savings-to-Income Ratio
#     - Monthly Expenses as % of Income
#     - Loan Payments as % of Income
#     - Credit Card Spending
#     - Spending Category Distribution (essential vs. discretionary spending)
#     - Financial Goals Met (%)
#   - Each indicator has assigned weights based on its significance.


# 4. Recommendations Generation:
#   - The `generate_recommendations` function provides personalized recommendations based on the calculated financial score and individual financial metrics.

# 5. Insights Visualization:
#    - Visualizes spending distribution across categories.
#    - Creates bar chart to compare family-wise financial scores.
#    - Generates line plots of member-wise spending trends over time.
#    - Visualizes spending breakdown by family using stacked bar chart.

# 6. AI/ML for Prediction:
#  - Utilizes Linear Regression, Random Forest, and Decision Tree models to predict next month's expenses.
#  - The model uses income, savings, monthly expenses, loan payments, and credit card spending as input features.
#  - Predicts next month's expenses/savings trends using trained models.

# 7. Model Evaluation:
#    - Evaluates the linear regression, Random Forest, and Decision Tree model performance using the mean squared error (MSE).  Lower MSE indicates better prediction accuracy.
