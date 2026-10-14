# Hospital Management System

A simple, lightweight, and complete Python console application for managing hospital records using SQLite.

## Features
- **Patient Management**: Register patients and list all registered patient details.
- **Doctor Management**: Add doctors with specialty details and consultation fees.
- **Appointment Scheduling**: Link patients and doctors with appointment dates.
- **Billing & Invoicing**: Automatically calculate and generate formatted bills based on doctor consultation fees.
- **Persistent Storage**: Uses a local SQLite database (`hospital.db`), requiring no extra database configuration or external servers.

## Requirements
- Python 3.7 or higher (No third-party packages needed — uses standard library `sqlite3` and `datetime`).

## How to Run
1. Open your terminal or command prompt.
2. Navigate to the extracted folder.
3. Run:
   ```bash
   python hospital_system.py
   ```
