from pydantic import BaseModel, EmailStr
from typing import Optional

class BaseTriggerRequest(BaseModel):
    email: EmailStr
    name: str

class AgentTradeTriggerRequest(BaseTriggerRequest):
    agent_name: str
    trade_percentage: float
