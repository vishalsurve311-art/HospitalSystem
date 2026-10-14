# Hospital Management System (HMS)

A clean, modular, and lightweight CLI-based Hospital Management System built in Python with SQLite for complete data persistence. This system provides core clinical administrative workflows, including patient intake, medical staff directory management, appointment scheduling, and automated billing.

---

## Table of Contents

1. [Overview](https://www.google.com/search?q=%23overview)
2. [Key Features](https://www.google.com/search?q=%23key-features)
3. [Architecture & Database Schema](https://www.google.com/search?q=%23architecture--database-schema)
4. [File Structure](https://www.google.com/search?q=%23file-structure)
5. [Prerequisites & Requirements](https://www.google.com/search?q=%23prerequisites--requirements)
6. [Installation & Setup](https://www.google.com/search?q=%23installation--setup)
7. [Usage Guide](https://www.google.com/search?q=%23usage-guide)
8. [Sample CLI Workflow](https://www.google.com/search?q=%23sample-cli-workflow)
9. [Future Enhancements](https://www.google.com/search?q=%23future-enhancements)

---

## Overview

Small clinics and healthcare facilities often require a simple, dependable tool to track basic operations without the overhead of heavy enterprise enterprise-resource-planning (ERP) platforms.

This system uses Python’s built-in `sqlite3` library, eliminating the need to set up, configure, or maintain external database servers like MySQL or PostgreSQL. The local SQLite database (`hospital.db`) initializes automatically when the application runs for the first time.

---

## Key Features

* **Patient Records Management:** Register patients with unique identification IDs, demographic details (name, age, gender), and contact numbers. View all active patient profiles at any time.


* **Doctor Directory:** Maintain staff records detailing names, medical specializations (e.g., Cardiology, General Practice), and consultation fees.


* **Appointment Scheduling:** Connect patients to specific doctors with defined dates (YYYY-MM-DD). System defaults to current date if left blank.


* **Billing & Invoicing:** Generate itemized, clean text invoices linking patient visits with doctor fees automatically.


* **Zero External Dependencies:** Built purely with Python’s standard library.


* **Persistent Storage:** All data writes directly to `hospital.db` on disk, persisting data between app sessions.



---

## Architecture & Database Schema

The database consists of three relational tables linked by foreign keys:

### 1. `patients`

| Column | Type | Description |
| --- | --- | --- |
| `id` | `INTEGER` | Primary key, Auto-incremented unique ID |
| `name` | `TEXT` | Patient's full name |
| `age` | `INTEGER` | Age in years |
| `gender` | `TEXT` | Patient's gender (`M`, `F`, `Other`) |
| `contact` | `TEXT` | Phone or emergency contact details |

### 2. `doctors`

| Column | Type | Description |
| --- | --- | --- |
| `id` | `INTEGER` | Primary key, Auto-incremented staff ID |
| `name` | `TEXT` | Doctor's full name |
| `specialty` | `TEXT` | Area of expertise (e.g., Dermatology, Cardiology) |
| `consultation_fee` | `REAL` | Base fee charged per consultation |

### 3. `appointments`

| Column | Type | Description |
| --- | --- | --- |
| `id` | `INTEGER` | Primary key, Unique appointment ID |
| `patient_id` | `INTEGER` | Foreign key referencing `patients(id)` |
| `doctor_id` | `INTEGER` | Foreign key referencing `doctors(id)` |
| `date` | `TEXT` | Scheduled date in `YYYY-MM-DD` format |
| `status` | `TEXT` | Default: `'Scheduled'` |

---

## File Structure

```text
hospital-management-system/
│
├── hospital_system.py        # Core application source code
├── hospital.db               # SQLite database file (created automatically on first run)
└── README.md                 # Project documentation and guide

```

---

## Prerequisites & Requirements

* **Python Version:** Python 3.7 or higher


* **Operating System:** Platform independent (Windows, macOS, Linux)
* **Dependencies:** None (Uses built-in standard modules: `sqlite3`, `datetime`)



---

## Installation & Setup

1. **Extract Archive:**
Extract your downloaded `hospital_management_system.zip` file to a folder of your choice.


2. **Open Terminal / Command Prompt:**
Navigate into the project directory:
```bash
cd path/to/hospital-management-system

```


3. **Verify Python Installation:**
```bash
python --version
# or
python3 --version

```


4. **Launch Application:**
Execute the core script:
```bash
python hospital_system.py

```


*(Upon first execution, `hospital.db` is generated automatically in the directory).*

---

## Usage Guide

The interactive terminal menu allows you to navigate the operations via options `1` through `8`:

1. **Register New Patient:** Prompt for name, age, gender, and contact details. Prints assigned patient ID.


2. **List All Patients:** Displays formatted overview of all registered patient entries.


3. **Register New Doctor:** Prompt for doctor name, area of specialization, and consultation fee amount.


4. **List All Doctors:** Lists all available doctors, their specialty, and billing rates.


5. **Schedule Appointment:** Enter Patient ID, Doctor ID, and target consultation date (`YYYY-MM-DD`).


6. **View All Appointments:** Lists all booked appointments showing patient names, attending doctors, dates, and statuses.


7. **Generate Invoice / Bill:** Input appointment ID to calculate and format a consultation bill.


8. **Exit:** Safely terminates the CLI session.



---

## Sample CLI Workflow

### Registering Doctor & Patient:

```text
=== HOSPITAL MANAGEMENT SYSTEM ===
Select an option (1-8): 1
Enter Patient Name: Alice Walker
Enter Age: 32
Enter Gender (M/F/Other): F
Enter Contact Number: +1-555-0199

[+] Patient registered successfully! Assigned ID: 1

Select an option (1-8): 3
Enter Doctor Name: Gregory House
Enter Specialty: Diagnostic Medicine
Enter Consultation Fee: 150.00

[+] Doctor registered successfully! Assigned ID: 1

```

### Scheduling & Billing:

```text
Select an option (1-8): 5
Enter Patient ID: 1
Enter Doctor ID: 1
Enter Date (YYYY-MM-DD) [Leave blank for today]: 2026-10-15

[+] Appointment booked successfully! Appointment ID: 1

Select an option (1-8): 7
Enter Appointment ID for Invoice: 1

========================================
           HOSPITAL INVOICE
========================================
Invoice ID       : INV-0001
Date             : 2026-10-15
Patient Name     : Alice Walker
Doctor Name      : Gregory House
Consultation Fee : $150.00
----------------------------------------
Total Amount Due : $150.00
========================================

```

---

## Future Enhancements

* Export reports and invoices directly to formatted PDF files.
* Add patient diagnosis history and prescription records.
* Introduce room/bed allocation and ward tracking.
* Build a graphical user interface (GUI) using Tkinter, PyQt, or a web dashboard via Flask/FastAPI.
