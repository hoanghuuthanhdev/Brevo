from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "Brevooo"
    API_V1_STR: str = "/api/v1"
    
    # Brevo Configuration
    BREVO_API_KEY: str = ""
    BREVO_API_URL: str = "https://api.brevo.com/v3/smtp/email"
    
    DEFAULT_SENDER_EMAIL: str = "noreply@brevooo.com"
    DEFAULT_SENDER_NAME: str = "Brevooo Team"
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
