from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from ..database import get_db
from ..models import AccessLog, User, UserData
from ..schemas import AccessLogCreate, AccessLogResponse
from ..utils.dependencies import get_current_user, get_admin_user

router = APIRouter()

@router.post("/", response_model=AccessLogResponse)
def create_access_log(
    access_log: AccessLogCreate,
    current_user: User = Depends(get_admin_user),
    db: Session = Depends(get_db)
):
    # Verify vehicle exists (using UserData table)
    vehicle = db.query(UserData).filter(UserData.id == access_log.vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    # Verify user exists
    user = db.query(User).filter(User.id == access_log.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    new_log = AccessLog(
        user_id=access_log.user_id,
        vehicle_id=access_log.vehicle_id,
        entry_time=datetime.utcnow(),
        status=access_log.status
    )
    db.add(new_log)
    db.commit()
    db.refresh(new_log)
    return new_log

@router.get("/", response_model=List[AccessLogResponse])
def read_access_logs(
    skip: int = 0,
    limit: int = 100,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current_user.role.name == "admin":
        logs = db.query(AccessLog).offset(skip).limit(limit).all()
    else:
        logs = db.query(AccessLog).filter(AccessLog.user_id == current_user.id).offset(skip).limit(limit).all()
    return logs

@router.patch("/{log_id}/exit")
def record_exit(
    log_id: int,
    current_user: User = Depends(get_admin_user),  # Only admins can update exit times
    db: Session = Depends(get_db)
):
    log = db.query(AccessLog).filter(AccessLog.id == log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Access log not found")
    
    if log.exit_time:
        raise HTTPException(status_code=400, detail="Exit already recorded for this entry")
    
    log.exit_time = datetime.utcnow()
    db.commit()
    db.refresh(log)
    return {"detail": "Exit time recorded successfully"}