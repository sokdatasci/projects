# Shift & Tip Calculator 🕒💸

This is a Python-based mini program for managing daily worker shifts and calculating fair tip distribution based on hours worked. Designed for small businesses, casinos, or restaurants, the tool handles employee roles, shift types, and day-by-day logs exported to Excel.

---

## 🔧 Features (In Progress)

- [x] Record daily shifts for multiple employees
- [x] Handle different roles (e.g., Manager, Cashier, Houseman)
- [x] Support shift types: Daytime, Evening, Graveyard
- [x] Export shift data to Excel (`.xlsx`)
- [x] Load structured Excel sheets for each day
- [x] Calculate total weekly hours per worker
- [ ] Automatically distribute tips proportionally
- [ ] Summarize and export tip distributions
- [ ] Link to employee master sheet via Employee ID

---

## 🧠 Example Use Case

1. You fill out a daily shift Excel file (`data/2025-08-05.xlsx`) with:
   - Name
   - Role
   - Shift Type
   - Start & End times

2. The script calculates hours worked for each employee

3. A summary groups hours by name, role, or shift type

4. Total weekly tips can be distributed automatically based on time worked

---

## 📁 Project Structure

shift-tip-calculator/
├── data/
│ ├── 2025-08-05.xlsx # Daily shift logs
│ ├── employees.xlsx # Employee master list (with roles)
│ └── tip_distribution.xlsx # Output file (future)
├── src/
│ ├── shift_calculator.py # Main logic for shifts and summary
│ └── create_daily_shifts.py # Script to generate example Excel files
├── README.md
└── requirements.txt

---

## 📦 Requirements

- Python 3.8+
- pandas
- openpyxl

Install with:

```bash
pip install -r requirements.txt
