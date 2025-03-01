# from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
# from sqlalchemy.orm import Session
# from typing import List
# import numpy as np
# import io
# import base64
# from ..database import get_db
# from ..models import Vehicle, User
# from ..schemas import VehicleCreate, VehicleResponse
# from ..utils.dependencies import get_current_user

# router = APIRouter()

# @router.post("/", response_model=VehicleResponse)
# def create_vehicle(
#     vehicle: VehicleCreate,
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     # Check if vehicle with plate number already exists
#     db_vehicle = db.query(Vehicle).filter(Vehicle.plate_number == vehicle.plate_number).first()
#     if db_vehicle:
#         raise HTTPException(status_code=400, detail="Vehicle with this plate number already registered")
    
#     new_vehicle = Vehicle(
#         plate_number=vehicle.plate_number,
#         model=vehicle.model,
#         color=vehicle.color,
#         user_id=current_user.id
#     )
#     db.add(new_vehicle)
#     db.commit()
#     db.refresh(new_vehicle)
#     return new_vehicle

# @router.get("/", response_model=List[VehicleResponse])
# def read_vehicles(
#     skip: int = 0,
#     limit: int = 100,
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     if current_user.role == "admin":
#         vehicles = db.query(Vehicle).offset(skip).limit(limit).all()
#     else:
#         vehicles = db.query(Vehicle).filter(Vehicle.user_id == current_user.id).offset(skip).limit(limit).all()
#     return vehicles

# @router.get("/{plate_number}", response_model=VehicleResponse)
# def read_vehicle(
#     plate_number: str,
#     # current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     vehicle = db.query(Vehicle).filter(Vehicle.plate_number == plate_number).first()
#     if not vehicle:
#         raise HTTPException(status_code=404, detail="Vehicle not found")
    
#     # if current_user.role != "admin" and vehicle.user_id != current_user.id:
#     #     raise HTTPException(status_code=403, detail="Not authorized to access this vehicle")
    
#     return vehicle

# @router.delete("/{vehicle_id}")
# def delete_vehicle(
#     vehicle_id: int,
#     current_user: User = Depends(get_current_user),
#     db: Session = Depends(get_db)
# ):
#     vehicle = db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
#     if not vehicle:
#         raise HTTPException(status_code=404, detail="Vehicle not found")
    
#     if current_user.role != "admin" and vehicle.user_id != current_user.id:
#         raise HTTPException(status_code=403, detail="Not authorized to delete this vehicle")
    
#     db.delete(vehicle)
#     db.commit()
#     return {"detail": "Vehicle deleted successfully"}





