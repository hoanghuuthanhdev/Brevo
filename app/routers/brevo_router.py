from fastapi import APIRouter
from app.schemas.brevo_schema import BrevoEmailRequest, BrevoEmailResponse
from app.services.brevo_service import brevo_service

router = APIRouter(prefix="/brevo", tags=["brevo"])

@router.post("/send-email", response_model=BrevoEmailResponse)
async def send_email(email_data: BrevoEmailRequest):
    """
    Send a transactional email using Brevo API.
    """
    return await brevo_service.send_transactional_email(email_data)
