
Hospital Management System – Billing Module

Project Overview

This project is a Hospital Management System backend developed using FastAPI.

The Billing Module is added as the next enhancement to manage patient billing, payments, revenue reports, validation, authorization, and database transactions.

Technologies Used

- Python 3.9+
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite / PostgreSQL
- JWT Authentication
- Uvicorn
- Swagger UI

Billing Module

The Billing module connects:

- Doctors
- Patients
- Appointments
- Billing
- Payments

Billing Fields

Field| Description
id| Unique billing ID
patient_id| Patient foreign key
doctor_id| Doctor foreign key
appointment_id| Optional appointment foreign key
consultation_fee| Doctor consultation fee
additional_charges| Additional charges
total_amount| Automatically calculated amount
payment_status| pending / paid / cancelled
payment_mode| cash / card / upi
is_active| Soft delete status
created_at| Billing creation time
updated_at| Last update time

Business Rules

The application validates the following rules:

1. Patient must exist.
2. Doctor must exist.
3. Doctor must be active.
4. Appointment is optional.
5. If an appointment is provided:
   - It must belong to the same patient.
   - It must belong to the same doctor.
   - It must not be cancelled.
6. Duplicate billing for the same appointment is prevented.
7. "total_amount" is automatically calculated.

Total Amount

total_amount = consultation_fee + additional_charges

Billing APIs

Create Billing

POST /billings

Creates a new billing record after validating the patient, doctor, and appointment.

Get Billing

GET /billings/{billing_id}

Returns a billing record using its ID.

Patient Billings

GET /patients/{patient_id}/billings

Returns all billing records for a patient.

Doctor Billings

GET /doctors/{doctor_id}/billings

Returns billing records related to a doctor.

Update Billing

PUT /billings/{billing_id}

Updates the complete billing information.

Partial Update

PATCH /billings/{billing_id}

Updates selected billing fields.

Delete Billing

DELETE /billings/{billing_id}

Performs a soft delete by setting:

is_active = false

The billing record is not permanently removed from the database.

---

Billing Reports

The project also supports billing reports and filtering.

Filters

Billing records can be filtered using:

- Payment status
- Doctor ID
- Patient ID
- From date
- To date

Pagination

List APIs support pagination using parameters such as:

?page=1&limit=10

Revenue Report

GET /reports/revenue

Example:

GET /reports/revenue?doctor_id=1&from=2024-01-01&to=2024-01-31

The report provides revenue information based on the selected doctor and date range.

Revenue can be calculated:

- Per doctor
- Per day
- Within a specific date range

---

Authorization

JWT-based role authorization is implemented.

Admin

Admin has full access to billing APIs.

Create
View
Update
Delete
Reports

Doctor

Doctors can view billing records related to their patients.

Doctors cannot delete billing records.

Unauthorized operations return:

403 Forbidden

---

Transactions & Data Consistency

Database transactions are used to maintain billing consistency.

When creating a billing record with an appointment:

Create Billing
      ↓
Update Appointment Status
      ↓
Commit Transaction

If any operation fails:

Rollback Transaction

This prevents partial data from being saved.

Database-level constraints are also used where required to maintain data integrity.

---

Billing Flow

Patient
   ↓
Doctor
   ↓
Appointment
   ↓
Create Billing
   ↓
Validate Patient & Doctor
   ↓
Validate Appointment
   ↓
Calculate Total Amount
   ↓
Save Billing
   ↓
Update Appointment
   ↓
Commit Transaction

Example Billing

{
    "patient_id": 1,
    "doctor_id": 2,
    "appointment_id": 5,
    "consultation_fee": 500,
    "additional_charges": 100,
    "payment_status": "pending",
    "payment_mode": "upi"
}

The system automatically calculates:

Total Amount = 500 + 100
             = 600

---

Error Handling

The API returns appropriate HTTP status codes.

Status Code| Meaning
200| Successful request
201| Billing created
400| Invalid request
401| Authentication required
403| Unauthorized access
404| Resource not found
409| Duplicate billing
500| Internal server error

---

Swagger Documentation

FastAPI provides interactive API documentation.

Start the application:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

Use Swagger to test:

- Billing APIs
- Patient billing APIs
- Doctor billing APIs
- Revenue reports
- Authentication and authorization

---

Project Structure

hospital-management/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py
├── crud.py
├── routers/
│   ├── doctors.py
│   ├── patients.py
│   ├── appointments.py
│   └── billings.py
│
├── requirements.txt
├── .gitignore
└── README.md

---

Installation

Clone the repository:

git clone <your-github-repository-url>

Go to the project directory:

cd hospital-management

Install dependencies:

pip install -r requirements.txt

Run the application:

uvicorn main:app --reload

Open Swagger:

http://127.0.0.1:8000/docs

---

Testing

Billing APIs can be tested using:

- Swagger UI
- Postman

The submission includes screenshots showing the Billing APIs and their responses.

---

GitHub Submission

The repository contains:

- FastAPI source code
- Billing model
- Billing APIs
- Validation and business rules
- Role-based authorization
- Revenue reports
- Pagination and filtering
- Database transactions
- Swagger/Postman testing
- README documentation

Author

Karteek

Python / Backend Developer
