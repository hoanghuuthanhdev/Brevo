import httpx
from app.config.settings import settings
from app.schemas.brevo_schema import BrevoEmailRequest, BrevoEmailResponse
from fastapi import HTTPException

class BrevoService:
    def __init__(self):
        self.api_key = settings.BREVO_API_KEY
        self.api_url = settings.BREVO_API_URL

    async def send_transactional_email(self, email_data: BrevoEmailRequest) -> BrevoEmailResponse:
        headers = {
            "api-key": self.api_key,
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        
        async with httpx.AsyncClient() as client:
            try:
                payload = email_data.model_dump(exclude_none=True)
                response = await client.post(
                    self.api_url,
                    json=payload,
                    headers=headers,
                    timeout=10.0
                )
                
                if response.status_code not in [201, 202]:
                    # Capture more detail if available
                    error_detail = response.text
                    try:
                        error_json = response.json()
                        error_detail = error_json.get("message", response.text)
                    except:
                        pass
                    raise HTTPException(
                        status_code=response.status_code,
                        detail=f"Brevo API error ({response.status_code}): {error_detail}"
                    )
                
                return BrevoEmailResponse(**response.json())
            
            except httpx.RequestError as exc:
                # Provide a more descriptive error message
                error_msg = f"Network error while connecting to Brevo: {type(exc).__name__}"
                if hasattr(exc, 'args') and exc.args:
                    error_msg += f" - {exc.args[0]}"
                raise HTTPException(
                    status_code=500,
                    detail=error_msg
                )
            except Exception as exc:
                raise HTTPException(
                    status_code=500,
                    detail=f"Internal error in email service: {str(exc) or type(exc).__name__}"
                )

brevo_service = BrevoService()
