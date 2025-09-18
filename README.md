# Accuknox Django Trainee Assignment

This repository contains answers to the Django Signals and Python Custom Class tasks.

---

## Directory Structure

```
django_accuknox_assignment/
├── signals_q1.py
├── signals_q2.py
├── signals_q3.py
├── rectangle.py
└── README.md
```

---

## Django Signals

### Question 1: Are signals synchronous or asynchronous?
- **Answer:** By default, Django signals are executed **synchronously**.
- **Proof:** Run `signals_q1.py`.  
  It will block execution for 5 seconds inside the signal handler before continuing.

```bash
python signals_q1.py
```

---

### Question 2: Do signals run in the same thread?
- **Answer:** Yes, Django signals run in the **same thread** as the caller.
- **Proof:** Run `signals_q2.py`.  
  It will print the thread ID of the caller and the signal handler — they are the same.

```bash
python signals_q2.py
```

---

### Question 3: Do signals run in the same transaction?
- **Answer:** Yes, signals run in the **same database transaction** by default.
- **Proof:** Run `signals_q3.py`.  
  The signal raises an exception inside a transaction, which rolls back the object creation.

```bash
python signals_q3.py
```

---

## Custom Python Class

### Rectangle Class
- Located in `rectangle.py`.
- Implements iteration over a rectangle instance to yield length first and then width.

**Example:**
```bash
python rectangle.py
```

**Output:**
```
{'length': 10}
{'width': 5}
```

---

## Notes
- These scripts are for demonstration only and not production-ready.
- Make sure you have Django installed (`pip install django`) before running the signal demos.
