import asyncio
import os
from dotenv import load_dotenv
from app.services.email_trigger_service import email_trigger_service
from app.config.settings import settings

load_dotenv()

async def test_trigger_service():
    # Set the same recipient you used for the direct test
    recipient_email = "hoanghuuthanhdev@gmail.com"
    recipient_name = "Thanh Hoang"
    
    print(f"Testing send_welcome_email for {recipient_email}...")
    try:
        response = await email_trigger_service.send_welcome_email(recipient_email, recipient_name)
        print(f"Response: {response}")
    except Exception as e:
        print(f"Error in send_welcome_email: {e}")

if __name__ == "__main__":
    asyncio.run(test_trigger_service())
