# 💸 Expense Analysis Dashboard

An interactive **Streamlit dashboard** to analyze your expenses.  
It provides:
- 📊 **KPIs**: Total Spent & Top Spending Category  
- 🥧 **Monthly Expense Pie Charts**  
- 📋 **Top 10 Highest Expenses Table**  
- 📈 **Top 10 Highest Expenses Bar Chart (Side by Side with Table)**  

---

## 📂 Required CSV Format

Your file **must have these columns exactly**:

| Date       | Category   | Amount |
|------------|-----------|--------|
| 2024-01-05 | Food      | 2000   |
| 2024-01-15 | Rent      | 8000   |

- **Date** → format: `YYYY-MM-DD`  
- **Category** → text (e.g. Food, Rent, Transport)  
- **Amount** → numeric  

---

## ⚙️ Setup & Run Instructions

### 1️⃣ Clone or Download Project
```bash
git clone <your-repo-link>
cd <project-folder>

```
```bash
conda create -n expensedash python=3.8 -y

```

```bash
conda activate expensedash
```
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```

