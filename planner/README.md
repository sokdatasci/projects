# 🗓️ Personal Planner (Python + Pandas)

This is a custom planner built using Python and pandas. It allows you to track:
- 📚 Class schedules
- ✅ Personal tasks & to-do items
- 📆 Appointments

Designed for use in VS Code, this tool stores data in CSV files and runs entirely offline.

---

## 📁 Project Structure

```
planner_project/
├── planner.py           # Main application logic
├── data/                # Folder for CSV files
│   ├── tasks.csv
│   ├── classes.csv
│   └── appointments.csv
├── README.md            # Project info and usage
└── requirements.txt     # Python dependencies
```

---

## 🚀 How to Run

1. Clone or download the project folder.
2. Open it in VS Code.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the planner:

```bash
python planner.py
```

---

## 🔧 Features (in progress)

- Add new tasks to your to-do list
- Create a recurring class schedule
- Record appointments and events
- Save and load data from CSV files
- (Planned) View tasks by date, filter by priority, interactive menu

---

## 📦 Dependencies

- `pandas`
- `openpyxl` (for Excel compatibility, optional)
