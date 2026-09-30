
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum


class PaymentStatus(str, Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"


class PaymentMode(str, Enum):
    cash = "cash"
    card = "card"
    upi = "upi"


class BillingCreate(BaseModel):
    patient_id: int
    doctor_id: int
    appointment_id: Optional[int] = None
    consultation_fee: float
    additional_charges: float = 0
    payment_status: PaymentStatus = PaymentStatus.pending
    payment_mode: Optional[PaymentMode] = None


class BillingUpdate(BaseModel):
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    appointment_id: Optional[int] = None
    consultation_fee: Optional[float] = None
    additional_charges: Optional[float] = None
    payment_status: Optional[PaymentStatus] = None
    payment_mode: Optional[PaymentMode] = None


class BillingResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_id: Optional[int]
    consultation_fee: float
    additional_charges: float
    total_amount: float
    payment_status: PaymentStatus
    payment_mode: Optional[PaymentMode]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
