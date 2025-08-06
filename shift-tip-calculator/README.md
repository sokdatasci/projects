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

```
shift-tip-calculator/
├── data/                          # All Excel files (input/output)
│   ├── employees.xlsx             # Master employee list (with IDs, roles)
│   ├── 2025-08-05.xlsx            # Example daily shift sheet (no date column)
│   └── tip_distribution.xlsx      # Future: calculated tips output
│
├── src/                           # All source code
│   ├── shift_calculator.py        # Adds shifts, calculates hours, exports
│   ├── create_daily_shifts.py     # Script to generate test Excel files
│   └── tip_distributor.py         # (Planned) Tip calculation logic
│
├── requirements.txt               # Dependencies: pandas, openpyxl
├── README.md                      # Project overview, setup, and usage
└── .gitignore                     # (Optional) Ignoring cache/temp files
```

---

## 📦 Requirements

- Python 3.8+
- pandas
- openpyxl

Install with:

```bash
pip install -r requirements.txt
