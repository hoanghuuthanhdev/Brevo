from fastapi import FastAPI
from app.routers import example_router, brevo_router, trigger_router

app = FastAPI(title="Brevooo API")

app.include_router(example_router.router)
app.include_router(brevo_router.router)
app.include_router(trigger_router.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Brevooo API"}
