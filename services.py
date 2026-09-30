
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models import Billing, Patient, Doctor, Appointment


def create_billing(db: Session, data):

    patient = db.query(Patient).filter(
        Patient.id == data.patient_id
    ).first()

    if not patient:
        raise HTTPException(404, "Patient not found")

    doctor = db.query(Doctor).filter(
        Doctor.id == data.doctor_id
    ).first()

    if not doctor or not doctor.is_active:
        raise HTTPException(400, "Doctor not found or inactive")

    appointment = None

    if data.appointment_id:
        appointment = db.query(Appointment).filter(
            Appointment.id == data.appointment_id
        ).first()

        if not appointment:
            raise HTTPException(404, "Appointment not found")

        if appointment.patient_id != data.patient_id:
            raise HTTPException(400, "Patient does not match appointment")

        if appointment.doctor_id != data.doctor_id:
            raise HTTPException(400, "Doctor does not match appointment")

        if appointment.status == "cancelled":
            raise HTTPException(400, "Cannot bill cancelled appointment")

        existing = db.query(Billing).filter(
            Billing.appointment_id == data.appointment_id,
            Billing.is_active == True
        ).first()

        if existing:
            raise HTTPException(409, "Billing already exists")

    total = data.consultation_fee + data.additional_charges

    billing = Billing(
        patient_id=data.patient_id,
        doctor_id=data.doctor_id,
        appointment_id=data.appointment_id,
        consultation_fee=data.consultation_fee,
        additional_charges=data.additional_charges,
        total_amount=total,
        payment_status=data.payment_status,
        payment_mode=data.payment_mode,
        is_active=True
    )

    db.add(billing)
    db.commit()
    db.refresh(billing)

    return billing


def get_billing(db: Session, billing_id: int):
    billing = db.query(Billing).filter(
        Billing.id == billing_id,
        Billing.is_active == True
    ).first()

    if not billing:
        raise HTTPException(404, "Billing not found")

    return billing
