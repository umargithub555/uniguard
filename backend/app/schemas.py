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
    password: Optional[str]
    plate_number:str
    model:Optional[str] = None
    color:Optional[str] = None
    face_embedding:str


class UserDataCreate(UserDataBase):
    pass

class UserDataResponse(UserDataBase):
    id:int
    
    password: Optional[str] = None 


    class Config:
        from_attributes = True

<<<<<<< HEAD
class ChangePasswordRequest(BaseModel):
    current_password: str
    new_password: str
=======



class UserSearch(BaseModel):
    cnic:str


class NormalUserResponse(BaseModel):
    name:str
    phone_number:str
    registration_number:str
    plate_number:str
    color:str
    email:EmailStr
    cnic:str
    model:str
>>>>>>> 6f608e5c4446d738f31a016d411b41bfe54ed80c
