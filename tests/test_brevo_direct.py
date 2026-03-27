import httpx
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

async def test_brevo():
    api_key = os.getenv("BREVO_API_KEY")
    sender_email = os.getenv("DEFAULT_SENDER_EMAIL")
    sender_name = os.getenv("DEFAULT_SENDER_NAME")
    
    # Use a test recipient (you can change this to your own for testing)
    recipient_email = "hoanghuuthanhdev@gmail.com" 
    
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    
    payload = {
        "sender": {"name": sender_name, "email": sender_email},
        "to": [{"email": recipient_email, "name": "Test Recipient"}],
        "subject": "Test Email from Brevooo Script",
        "htmlContent": "<html><body><h1>It works!</h1><p>This is a test email sent from a script.</p></body></html>"
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=headers)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_brevo())
