# from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
# from fastapi.responses import JSONResponse
# from sqlalchemy.orm import Session
# from ..database import get_db
# from ..utils.video_processor import VideoProcessor
# import logging

# router = APIRouter()

# @router.post("/process-gate-video")
# async def process_gate_video(
#     video: UploadFile = File(...),
#     image: UploadFile = File(None),  # Make the image optional
#     db: Session = Depends(get_db)
# ):
#     # Validate video content type
#     allowed_video_types = {'video/mp4', 'video/avi', 'video/quicktime'}
#     if video.content_type not in allowed_video_types:
#         return JSONResponse(
#             status_code=400,
#             content={"detail": f"Invalid video file type. Allowed types: {', '.join(allowed_video_types)}"}
#         )
    
#     # Validate image content type if provided
#     if image is not None:
#         allowed_image_types = {'image/jpeg', 'image/png', 'image/jpg'}
#         if image.content_type not in allowed_image_types:
#             return JSONResponse(
#                 status_code=400,
#                 content={"detail": f"Invalid image file type. Allowed types: {', '.join(allowed_image_types)}"}
#             )
    
#     try:
#         # Read the video file
#         video_bytes = await video.read()
        
#         # Check if video is empty
#         if not video_bytes:
#             return JSONResponse(
#                 status_code=400,
#                 content={"detail": "Empty video file"}
#             )
            
#         # Read the image file if provided
#         image_bytes = None
#         if image is not None:
#             image_bytes = await image.read()
            
#             # Check if image is empty
#             if not image_bytes:
#                 return JSONResponse(
#                     status_code=400,
#                     content={"detail": "Empty image file"}
#                 )
            
#         # Process the video and image
#         processor = VideoProcessor(db)
#         result = processor.process_video(video_bytes, image_bytes)
        
#         if "error" in result:
#             return JSONResponse(
#                 status_code=400,
#                 content={"detail": result["error"]}
#             )
        
#         return JSONResponse(content=result)
        
#     except Exception as e:
#         logging.error(f"Video processing error: {str(e)}")
#         return JSONResponse(
#             status_code=500,
#             content={"detail": "Internal server error during video processing"}
#         )









from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import Optional
from ..database import get_db
from ..utils.video_processor import VideoProcessor
import logging

router = APIRouter()

@router.post("/process-gate-video")
async def process_gate_video(
    gate_video: UploadFile = File(...),
    face_video: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db)
):
    # Validate gate video content type
    allowed_video_types = {'video/mp4', 'video/avi', 'video/quicktime'}
    if gate_video.content_type not in allowed_video_types:
        return JSONResponse(
            status_code=400,
            content={"detail": f"Invalid video file type. Allowed types: {', '.join(allowed_video_types)}"}
        )
    
    # Validate face video content type if provided
    if face_video is not None:
        if face_video.content_type not in allowed_video_types:
            return JSONResponse(
                status_code=400,
                content={"detail": f"Invalid face video file type. Allowed types: {', '.join(allowed_video_types)}"}
            )
    
    try:
        # Read the gate video file
        gate_video_bytes = await gate_video.read()
        
        # Check if gate video is empty
        if not gate_video_bytes:
            return JSONResponse(
                status_code=400,
                content={"detail": "Empty gate video file"}
            )
            
        # Read the face video file if provided
        face_video_bytes = None
        if face_video is not None:
            face_video_bytes = await face_video.read()
            
            # Check if face video is empty
            if not face_video_bytes:
                return JSONResponse(
                    status_code=400,
                    content={"detail": "Empty face video file"}
                )
            
        # Process the videos
        processor = VideoProcessor(db)
        result = processor.process_video(gate_video_bytes, face_video_bytes)
        
        # Structure the response to match what the Streamlit app expects
        # response = {
        #     "all_plates": result.get("all_plates", []),
        #     "access_granted": result.get("access_granted", False),
        #     "confidence": result.get("confidence", 0)
        # }
        
        # # Add face recognition results if face video was provided
        # if face_video is not None:
        #     response["face_match"] = result.get("face_match", False)
        #     response["face_confidence"] = result.get("face_confidence", 0)
        
        # # Add vehicle and user details if access is granted
        # if response["access_granted"]:
        #     response["details"] = {
        #         "vehicle_info": {
        #             "plate_number": result.get("plate_number", "N/A"),
        #             "model": result.get("model", "N/A"),
        #             "color": result.get("color", "N/A")
        #         },
        #         "user_info": {
        #             "name": result.get("user_name", "N/A"),
        #             "email": result.get("user_email", "N/A")
        #         }
        #     }
        
        # return JSONResponse(content=response)
        

        if "error" in result:
            return JSONResponse(
                status_code=400,
                content={"detail": result["error"]}
            )
        
        return JSONResponse(content=result)



    except Exception as e:
        logging.error(f"Gate video processing error: {str(e)}")
        return JSONResponse(
            status_code=500,
            content={"detail": f"Internal server error during video processing: {str(e)}"}
        )

