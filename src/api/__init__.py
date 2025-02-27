from .auths import auth_router as auth
from .question_bank import question_router as question 
from .organizations import organization_router as orgnazition
from fastapi import APIRouter


main_router = APIRouter()

main_router.include_router(auth)
main_router.include_router(question)
main_router.include_router(orgnazition)