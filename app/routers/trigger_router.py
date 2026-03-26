from fastapi import APIRouter, HTTPException
from app.schemas.trigger_schema import BaseTriggerRequest, AgentTradeTriggerRequest
from app.services.email_trigger_service import email_trigger_service
from app.schemas.brevo_schema import BrevoEmailResponse

router = APIRouter(prefix="/triggers", tags=["email-triggers"])

@router.post("/welcome", response_model=BrevoEmailResponse)
async def trigger_welcome_email(request: BaseTriggerRequest):
    """
    Trigger a welcome email to a new user.
    """
    return await email_trigger_service.send_welcome_email(request.email, request.name)

@router.post("/api-reminder", response_model=BrevoEmailResponse)
async def trigger_api_reminder(request: BaseTriggerRequest):
    """
    Trigger an API connection reminder email.
    """
    return await email_trigger_service.send_api_reminder(request.email, request.name)

@router.post("/agent-trade", response_model=BrevoEmailResponse)
async def trigger_agent_trade(request: AgentTradeTriggerRequest):
    """
    Trigger an agent trade notification email.
    """
    return await email_trigger_service.send_agent_trade_notification(
        request.email, 
        request.name, 
        request.agent_name, 
        request.trade_percentage
    )

@router.post("/onboarding-reminder", response_model=BrevoEmailResponse)
async def trigger_onboarding_reminder(request: BaseTriggerRequest):
    """
    Trigger an onboarding reminder email.
    """
    return await email_trigger_service.send_onboarding_reminder(request.email, request.name)
