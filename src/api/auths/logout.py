from fastapi import APIRouter, Response, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select  
from src.settings.base import get_db  
from src.auth.utils import get_current_user  
from src.model import User

router = APIRouter()

@router.put("/logout")
async def logout(
    current_user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(select(User).filter(User.id == current_user.id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    
    user.disabled = True
    await db.commit()


