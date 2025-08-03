import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="Expense Analysis Dashboard", layout="wide")
st.title("💸 Expense Analysis Dashboard")

# Show Required Format
st.markdown("""
### 📌 Required CSV Format  
Your file **must have these columns** exactly with same names:
- **Date** (format: YYYY-MM-DD)
- **Category** (text, e.g. Food, Rent, Transport)
- **Amount** (numeric)
""")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your expenses CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        # Validation
        required_cols = ['Date', 'Category', 'Amount']
        if not all(col in df.columns for col in required_cols):
            st.error(f"❌ CSV must contain: {required_cols}")
            st.stop()

        # Data cleaning
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        df = df.dropna(subset=['Date', 'Amount'])
        df['Month'] = df['Date'].dt.strftime('%b')

        # Sorted data
        df_sorted = df.sort_values(by='Amount', ascending=False)

        # KPIs
        total_spent = df['Amount'].sum()
        top_category = df.groupby('Category')['Amount'].sum().idxmax()
        top_value = df.groupby('Category')['Amount'].sum().max()

        col1, col2 = st.columns(2)
        col1.metric("💰 Total Spent", f"{total_spent:,.2f}")
        col2.metric("🏆 Top Category", f"{top_category} ({top_value:,.2f})")

        st.markdown("---")

        # Pie Charts
        st.subheader("📅 Monthly Expense Breakdown")
        monthly = df.groupby(['Month', 'Category'])['Amount'].sum().unstack(fill_value=0)
        colors = ['#a8dadc','#f4a261','#e9c46a','#90be6d','#f08080','#b5ead7']

        cols = st.columns(2)
        for i, month in enumerate(monthly.index):
            values = monthly.loc[month]
            fig, ax = plt.subplots(figsize=(4,4))
            wedges, texts = ax.pie(values, startangle=90, colors=colors)
            total = values.sum()
            labels = [f"{cat}: {val/total*100:.1f}%" for cat, val in zip(values.index, values)]
            ax.legend(wedges, labels, title="Category", loc="center left", bbox_to_anchor=(1,0,0.5,1))
            ax.set_title(f"{month} Expenses")
            cols[i % 2].pyplot(fig)

        st.markdown("---")

        
        st.subheader("📊 Top 10 Highest Expenses")
        col_left, col_right = st.columns(2)

        # Table in left column
        col_left.dataframe(df_sorted[['Date', 'Category', 'Amount']].head(10))

        # Bar Chart in right column
        top10 = df_sorted.head(10)
        fig, ax = plt.subplots(figsize=(6,4))
        ax.barh(top10['Category'], top10['Amount'], color='#90be6d')
        ax.invert_yaxis()
        ax.set_xlabel("Amount")
        ax.set_ylabel("Category")
        ax.set_title("Top 10 Expenses by Category")
        col_right.pyplot(fig)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

else:
    st.info("👆 Please upload a CSV file with columns: Date, Category, Amount")
