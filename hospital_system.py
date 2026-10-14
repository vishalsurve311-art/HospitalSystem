"""
Hospital Management System
A clean, modular terminal-based application with SQLite storage.
"""

import sqlite3
from datetime import datetime

DATABASE_NAME = "hospital.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        gender TEXT,
        contact TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialty TEXT,
        consultation_fee REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS appointments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER,
        doctor_id INTEGER,
        date TEXT,
        status TEXT DEFAULT 'Scheduled',
        FOREIGN KEY(patient_id) REFERENCES patients(id),
        FOREIGN KEY(doctor_id) REFERENCES doctors(id)
    )
    """)

    conn.commit()
    conn.close()


def add_patient(name, age, gender, contact):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO patients (name, age, gender, contact) VALUES (?, ?, ?, ?)",
        (name, age, gender, contact),
    )
    conn.commit()
    pid = cursor.lastrowid
    conn.close()
    return pid


def list_patients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return patients


def add_doctor(name, specialty, fee):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO doctors (name, specialty, consultation_fee) VALUES (?, ?, ?)",
        (name, specialty, fee),
    )
    conn.commit()
    did = cursor.lastrowid
    conn.close()
    return did


def list_doctors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return doctors


def schedule_appointment(patient_id, doctor_id, date_str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointments (patient_id, doctor_id, date) VALUES (?, ?, ?)",
        (patient_id, doctor_id, date_str),
    )
    conn.commit()
    appt_id = cursor.lastrowid
    conn.close()
    return appt_id


def list_appointments():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
        a.id,
        p.name AS patient_name,
        d.name AS doctor_name,
        d.specialty,
        a.date,
        a.status
    FROM appointments a
    JOIN patients p ON a.patient_id = p.id
    JOIN doctors d ON a.doctor_id = d.id
    ORDER BY a.date DESC
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records


def generate_bill(appointment_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    SELECT 
        a.id AS appt_id,
        p.name AS patient_name,
        d.name AS doctor_name,
        d.consultation_fee,
        a.date
    FROM appointments a
    JOIN patients p ON a.patient_id = p.id
    JOIN doctors d ON a.doctor_id = d.id
    WHERE a.id = ?
    """
    cursor.execute(query, (appointment_id,))
    record = cursor.fetchone()
    conn.close()

    if not record:
        return "Appointment not found."

    bill = (
        "\n" + "=" * 40 + "\n"
        "           HOSPITAL INVOICE\n"
        + "=" * 40 + "\n"
        f"Invoice ID       : INV-{record['appt_id']:04d}\n"
        f"Date             : {record['date']}\n"
        f"Patient Name     : {record['patient_name']}\n"
        f"Doctor Name      : {record['doctor_name']}\n"
        f"Consultation Fee : ${record['consultation_fee']:.2f}\n"
        + "-" * 40 + "\n"
        f"Total Amount Due : ${record['consultation_fee']:.2f}\n"
        + "=" * 40 + "\n"
    )
    return bill


def main_menu():
    init_db()
    while True:
        print("\n" + "=" * 35)
        print("    HOSPITAL MANAGEMENT SYSTEM")
        print("=" * 35)
        print("1. Register New Patient")
        print("2. List All Patients")
        print("3. Register New Doctor")
        print("4. List All Doctors")
        print("5. Schedule Appointment")
        print("6. View All Appointments")
        print("7. Generate Invoice / Bill")
        print("8. Exit")
        print("=" * 35)

        choice = input("Select an option (1-8): ").strip()

        if choice == "1":
            name = input("Enter Patient Name: ").strip()
            age = int(input("Enter Age: ") or 0)
            gender = input("Enter Gender (M/F/Other): ").strip()
            contact = input("Enter Contact Number: ").strip()
            pid = add_patient(name, age, gender, contact)
            print(f"\n[+] Patient registered successfully! Assigned ID: {pid}")

        elif choice == "2":
            patients = list_patients()
            print("\n--- Patient Records ---")
            if not patients:
                print("No patients registered yet.")
            for p in patients:
                print(f"ID: {p['id']} | Name: {p['name']} | Age: {p['age']} | Gender: {p['gender']} | Contact: {p['contact']}")

        elif choice == "3":
            name = input("Enter Doctor Name: ").strip()
            spec = input("Enter Specialty (e.g. Cardiology, General): ").strip()
            fee = float(input("Enter Consultation Fee: ") or 0.0)
            did = add_doctor(name, spec, fee)
            print(f"\n[+] Doctor registered successfully! Assigned ID: {did}")

        elif choice == "4":
            doctors = list_doctors()
            print("\n--- Doctor Directory ---")
            if not doctors:
                print("No doctors registered yet.")
            for d in doctors:
                print(f"ID: {d['id']} | Dr. {d['name']} | Specialty: {d['specialty']} | Fee: ${d['consultation_fee']:.2f}")

        elif choice == "5":
            try:
                pid = int(input("Enter Patient ID: "))
                did = int(input("Enter Doctor ID: "))
                date_str = input("Enter Date (YYYY-MM-DD) [Leave blank for today]: ").strip()
                if not date_str:
                    date_str = datetime.now().strftime("%Y-%m-%d")
                aid = schedule_appointment(pid, did, date_str)
                print(f"\n[+] Appointment booked successfully! Appointment ID: {aid}")
            except ValueError:
                print("\n[!] Invalid input. IDs must be integers.")

        elif choice == "6":
            appts = list_appointments()
            print("\n--- Appointments Schedule ---")
            if not appts:
                print("No appointments found.")
            for a in appts:
                print(f"Appt ID: {a['id']} | Date: {a['date']} | Patient: {a['patient_name']} | Doctor: Dr. {a['doctor_name']} ({a['specialty']}) | Status: {a['status']}")

        elif choice == "7":
            try:
                aid = int(input("Enter Appointment ID for Invoice: "))
                print(generate_bill(aid))
            except ValueError:
                print("\n[!] Invalid Appointment ID.")

        elif choice == "8":
            print("\nThank you for using the Hospital Management System. Goodbye!")
            break
        else:
            print("\n[!] Invalid option. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main_menu()
