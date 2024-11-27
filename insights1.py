# -*- coding: utf-8 -*-
"""insights1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YycM3-cecGIjU4q0hrAEFJM9kRC5bEBU
"""

import streamlit as st
import pandas as pd

# Streamlit App
st.title("Family Financial Insights")

# Sidebar for file upload
st.sidebar.subheader("Upload Excel File")
uploaded_file = st.sidebar.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file:
    # Load Excel file into a DataFrame
    try:
        family_spending = pd.read_excel(uploaded_file)
        st.sidebar.success("File uploaded successfully!")

        # Ensure necessary columns exist in the uploaded file
        required_columns = ['Family ID', 'Income', 'Savings', 'Monthly Expenses',
                            'Loan Payments', 'Credit Card Spending', 'Financial Goals Met (%)', 'Final Score']
        if not all(col in family_spending.columns for col in required_columns):
            st.error(f"The uploaded file must contain the following columns: {', '.join(required_columns)}")
        else:
            # Generate recommendations
            def generate_recommendations(row):
                recommendations = []
                score = row['Final Score']

                # Savings recommendations
                savings_ratio = row['Savings'] / row['Income'] if row['Income'] > 0 else 0
                if savings_ratio < 0.2:
                    recommendations.append(f"Increase savings by 5% to improve your score by {min(10, 100 - score)} points.")

                # Expenses recommendations
                expense_ratio = row['Monthly Expenses'] / row['Income'] if row['Income'] > 0 else 0
                if expense_ratio > 0.7:
                    recommendations.append(f"Reduce discretionary spending by 10% to improve your score by {min(8, 100 - score)} points.")

                # Loan payments recommendations
                loan_ratio = row['Loan Payments'] / row['Income'] if row['Income'] > 0 else 0
                if loan_ratio > 0.3:
                    recommendations.append(f"Explore options to reduce loan payments to improve your score by {min(7, 100 - score)} points.")

                # Credit card spending recommendations
                credit_ratio = row['Credit Card Spending'] / row['Income'] if row['Income'] > 0 else 0
                if credit_ratio > 0.15:
                    recommendations.append(f"Reduce credit card spending to improve your score by {min(5, 100 - score)} points.")

                # Financial goals recommendations
                if row['Financial Goals Met (%)'] < 80:
                    recommendations.append(f"Make a concrete plan to achieve financial goals to improve your score by {min(6, 100 - score)} points.")

                return recommendations

            family_spending['Recommendations'] = family_spending.apply(generate_recommendations, axis=1)

            # Sidebar for Family Selection
            st.sidebar.subheader("Select a Family")
            selected_family_id = st.sidebar.selectbox("Family ID", family_spending['Family ID'])

            # Display details and recommendations for the selected family
            if selected_family_id:
                selected_family = family_spending[family_spending['Family ID'] == selected_family_id].iloc[0]

                st.subheader(f"Details for Family ID: {selected_family_id}")
                st.write(f"**Income:** {selected_family['Income']}")
                st.write(f"**Savings:** {selected_family['Savings']}")
                st.write(f"**Monthly Expenses:** {selected_family['Monthly Expenses']}")
                st.write(f"**Loan Payments:** {selected_family['Loan Payments']}")
                st.write(f"**Credit Card Spending:** {selected_family['Credit Card Spending']}")
                st.write(f"**Financial Goals Met (%):** {selected_family['Financial Goals Met (%)']}")
                st.write(f"**Final Score:** {selected_family['Final Score']}")

                st.subheader("Recommendations")
                for recommendation in selected_family['Recommendations']:
                    st.write(f"- {recommendation}")

    except Exception as e:
        st.error(f"An error occurred while reading the Excel file: {e}")
else:
    st.sidebar.info("Please upload an Excel file to get started.")