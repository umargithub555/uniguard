from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from .security import verify_token

<<<<<<< HEAD
async def get_current_user(email: str = Depends(verify_token), db: Session = Depends(get_db)):
=======
async def get_current_user(db: Session = Depends(get_db), email: str = Depends(verify_token)):
>>>>>>> 9d5ba82d98f1c663ea9ad1fb235f1d31d64cbbcd
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

async def get_admin_user(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Insufficient permissions"
        )
    return current_user