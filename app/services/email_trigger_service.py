import os
from typing import List, Optional
from app.services.brevo_service import brevo_service
from app.schemas.brevo_schema import BrevoEmailRequest, EmailSender, EmailRecipient
from app.config.settings import settings

class EmailTriggerService:
    def __init__(self):
        self.default_sender = EmailSender(
            name=settings.DEFAULT_SENDER_NAME,
            email=settings.DEFAULT_SENDER_EMAIL
        )
        self.template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")

    def _load_template(self, filename: str) -> str:
        with open(os.path.join(self.template_dir, filename), "r", encoding="utf-8") as f:
            return f.read()

    def _get_html_content(self, title: str, content: str) -> str:
        base = self._load_template("base.html")
        return base.replace("{{ app_name }}", settings.APP_NAME) \
                   .replace("{{ title }}", title) \
                   .replace("{{ content }}", content)

    async def send_welcome_email(self, to_email: str, name: str):
        subject = f"Welcome to {settings.APP_NAME}, {name}!"
        template = self._load_template("welcome.html")
        content = template.format(name=name, APP_NAME=settings.APP_NAME)
        html_content = self._get_html_content("Welcome aboard!", content)
        
        request = BrevoEmailRequest(
            sender=self.default_sender,
            to=[EmailRecipient(email=to_email, name=name)],
            subject=subject,
            htmlContent=html_content
        )
        print(f"[EmailTriggerService] Sending welcome email to {to_email}...")
        try:
            response = await brevo_service.send_transactional_email(request)
            print(f"[EmailTriggerService] Successfully sent email. MessageId: {response.messageId}")
            return response
        except Exception as e:
            print(f"[EmailTriggerService] Failed to send email: {str(e)}")
            raise e


    async def send_api_reminder(self, to_email: str, name: str):
        subject = "Action Required: Connect your API to start trading"
        template = self._load_template("api_reminder.html")
        content = template.format(name=name, APP_NAME=settings.APP_NAME)
        html_content = self._get_html_content("Connect your API", content)
        
        request = BrevoEmailRequest(
            sender=self.default_sender,
            to=[EmailRecipient(email=to_email, name=name)],
            subject=subject,
            htmlContent=html_content
        )
        return await brevo_service.send_transactional_email(request)

    async def send_agent_trade_notification(self, to_email: str, name: str, agent_name: str, trade_percentage: float):
        subject = f"Alert: Agent {agent_name} just made a trade!"
        template = self._load_template("agent_trade.html")
        content = template.format(name=name, agent_name=agent_name, trade_percentage=trade_percentage)
        html_content = self._get_html_content("New Trade Notification", content)
        
        request = BrevoEmailRequest(
            sender=self.default_sender,
            to=[EmailRecipient(email=to_email, name=name)],
            subject=subject,
            htmlContent=html_content
        )
        return await brevo_service.send_transactional_email(request)

    async def send_onboarding_reminder(self, to_email: str, name: str):
        subject = "Friendly Reminder: Complete your onboarding"
        template = self._load_template("onboarding_reminder.html")
        content = template.format(name=name, APP_NAME=settings.APP_NAME)
        html_content = self._get_html_content("Finish your setup", content)
        
        request = BrevoEmailRequest(
            sender=self.default_sender,
            to=[EmailRecipient(email=to_email, name=name)],
            subject=subject,
            htmlContent=html_content
        )
        return await brevo_service.send_transactional_email(request)

email_trigger_service = EmailTriggerService()
