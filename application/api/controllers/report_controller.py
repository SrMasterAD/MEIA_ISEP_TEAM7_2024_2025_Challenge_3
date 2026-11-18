from fastapi import APIRouter, Depends, HTTPException

from application.api.services import report_service
from application.api.utils.token_utils import get_current_user_id_from_token
from fastapi import UploadFile, File


router = APIRouter(tags=["Report Generation"])


@router.post("/report")
async def generate_report(image: UploadFile = File(...), user_id: int = Depends(get_current_user_id_from_token)):
    try:
        return await report_service.generate_report(image, user_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
