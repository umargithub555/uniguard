from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime
from enum import Enum

class RoleEnum(str, Enum):
    admin = "admin"
    user = "user"

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role: RoleEnum = RoleEnum.user

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    
    class Config:
        from_attributes = True



# class VehicleBase(BaseModel):
#     plate_number: str
#     model: str
#     color: str

# class VehicleCreate(VehicleBase):
#     pass

# class VehicleResponse(VehicleBase):
#     id: int
#     user_id: int
    
#     class Config:
#         from_attributes = True

class AccessStatusEnum(str, Enum):
    pending = "Pending"
    granted = "Granted"
    denied = "Denied"

class AccessLogBase(BaseModel):
    user_id: int
    vehicle_id: int
    status: AccessStatusEnum = AccessStatusEnum.pending

class AccessLogCreate(AccessLogBase):
    pass

class AccessLogResponse(AccessLogBase):
    id: int
    entry_time: datetime
    exit_time: Optional[datetime] = None
    
    class Config:
        from_attributes = True




class UserDataBase(BaseModel):
    name:str
    email : EmailStr
    phone_number : str
    cnic:str
    registration_number:str
    face_embedding:str
    plate_number:str
    model:Optional[str] = None
    color:Optional[str] = None


class UserDataCreate(UserDataBase):
    pass

class UserDataResponse(UserDataBase):
    id:int


    class Config:
        from_attributes = True

class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
