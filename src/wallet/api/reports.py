from fastapi import APIRouter, UploadFile, File, Depends, BackgroundTasks
from starlette.responses import StreamingResponse

from wallet.models.auth import User
from wallet.services.auth import get_current_user
from wallet.services.reports import ReportsService

router = APIRouter(
    prefix='/reports',
)


@router.post('/import-csv', tags=['reports'])
def import_csv(
        background_tasks: BackgroundTasks,
        file: UploadFile = File(...),
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends()
):
    background_tasks.add_task(reports_service.import_csv, user.id, file.file)


@router.get('/export-csv', tags=['reports'])
def export_csv(
        user: User = Depends(get_current_user),
        reports_service: ReportsService = Depends()
):
    report = reports_service.export_csv(user.id)
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        }
    )
