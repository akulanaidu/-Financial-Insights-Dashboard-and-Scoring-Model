import streamlit as st
import pandas as pd

# Streamlit App
st.title("Family Financial Insights and Scoring")

# Sidebar for file upload
st.sidebar.subheader("Upload Excel File")
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file:
    try:
        # Load the uploaded Excel file into a DataFrame
        family_spending = pd.read_excel(uploaded_file)
        st.sidebar.success("File uploaded successfully!")
        
        # Ensure necessary columns exist in the uploaded file
        required_columns = ['Income', 'Savings', 'Monthly Expenses', 'Loan Payments', 'Credit Card Spending', 'Financial Goals Met (%)']
        if not all(col in family_spending.columns for col in required_columns):
            st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
        else:
            # Function to calculate score based on the financial data
            def calculate_score(row):
                score = 100  # Start with a perfect score
                
                # Savings: if savings are less than 20% of income, reduce score
                savings_ratio = row['Savings'] / row['Income'] if row['Income'] > 0 else 0
                if savings_ratio < 0.2:
                    score -= 10  # Deduct 10 points if savings are low
                
                # Expenses: if monthly expenses are more than 70% of income, reduce score
                expense_ratio = row['Monthly Expenses'] / row['Income'] if row['Income'] > 0 else 0
                if expense_ratio > 0.7:
                    score -= 15  # Deduct 15 points if expenses are high
                
                # Loan Payments: if loan payments are more than 30% of income, reduce score
                loan_ratio = row['Loan Payments'] / row['Income'] if row['Income'] > 0 else 0
                if loan_ratio > 0.3:
                    score -= 20  # Deduct 20 points if loan payments are high
                
                # Credit Card Spending: if credit card spending is more than 15% of income, reduce score
                credit_ratio = row['Credit Card Spending'] / row['Income'] if row['Income'] > 0 else 0
                if credit_ratio > 0.15:
                    score -= 10  # Deduct 10 points if credit card spending is high
                
                # Financial Goals: if financial goals are not met, reduce score
                if row['Financial Goals Met (%)'] < 80:
                    score -= 10  # Deduct 10 points if less than 80% of goals are met
                
                return score

            # Apply the scoring function to each row
            family_spending['Predicted Score'] = family_spending.apply(calculate_score, axis=1)

            st.subheader("Data with Predicted Scores")
            st.write(family_spending)

            # Family Selection
            st.sidebar.subheader("Select a Family")
            if 'Family ID' in family_spending.columns:
                selected_family_id = st.sidebar.selectbox("Family ID", family_spending['Family ID'])
                
                # Ensure the selected family ID works with loc
                selected_family = family_spending.loc[family_spending['Family ID'] == selected_family_id]
                
                if not selected_family.empty:
                    st.subheader(f"Details for Family ID: {selected_family_id}")
                    st.write(f"**Predicted Score:** {selected_family['Predicted Score'].values[0]}")
                    st.write(selected_family)
                else:
                    st.error("No data found for the selected Family ID.")
            else:
                st.error("The uploaded file does not contain a 'Family ID' column.")
    
    except Exception as e:
        st.error(f"An error occurred while reading the Excel file: {e}")
else:
    st.sidebar.info("Please upload an Excel file to get started.")
