from pydantic import BaseModel, EmailStr
from typing import List, Optional

class EmailSender(BaseModel):
    name: Optional[str] = None
    email: EmailStr

class EmailRecipient(BaseModel):
    name: Optional[str] = None
    email: EmailStr

class BrevoEmailRequest(BaseModel):
    sender: EmailSender
    to: List[EmailRecipient]
    subject: str
    htmlContent: str
    textContent: Optional[str] = None

class BrevoEmailResponse(BaseModel):
    messageId: str
