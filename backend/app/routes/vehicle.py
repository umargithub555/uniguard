from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..models import UserData, User
from ..schemas import UserDataResponse
from ..utils.dependencies import get_current_user

router = APIRouter()

@router.get("/{vehicle_id}", response_model=UserDataResponse)
def read_vehicle(
    vehicle_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Get the vehicle (UserData) by ID
    vehicle = db.query(UserData).filter(UserData.id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    # Check permissions (admin or vehicle owner)
    if current_user.role.name != "admin" and vehicle.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to access this vehicle")
    
    return vehicle
