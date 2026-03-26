from fastapi import APIRouter
from app.services import example_service
from app.schemas.example_schema import ExampleSchema

router = APIRouter(prefix="/example", tags=["example"])

@router.get("/", response_model=ExampleSchema)
async def get_example():
    return example_service.get_example_data()
