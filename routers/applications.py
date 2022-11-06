from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database, models ,schema


router = APIRouter(
    prefix='/applications',
    tags=['applications']
)

@router.get('/{jobID}')
def get_application(jobID:str, db: Session = Depends(database.get_db)):
    obj = db.query(models.Applications).filter(models.Applications.job_id == jobID).all()
    if not obj:
        return []
    
    return obj


@router.put('/status/{appID}')
def change_status(request:schema.Modify_status, appID:int, db: Session = Depends(database.get_db)):
    obj = db.query(models.Applications).filter(models.Applications.app_id == appID).first()
    if not obj:
        return False

    obj.status = request.new_status
   
    db.commit()
    db.refresh(obj)


@router.post('/apply')
def apply(request:schema.Applications, db: Session = Depends(database.get_db)):
    obj = models.Applications(
        job_id = request.job_id,
        name = request.name,
        experience = request.experience,
        current_org = request.current_org,
        current_title = request.current_title,
        university = request.university,
        cv = request.cv,
        status = request.status,
        email = request.email
    )

    db.add(obj)
    db.commit()
    db.refresh(obj)
    


@router.delete('/delete/{appID}')
def delete_application(appID:int, db: Session = Depends(database.get_db)):
    obj = db.query(models.Applications).filter(models.Applications.app_id == appID).first()
    if not obj:
        return False
    
    db.delete(obj)
    db.commit()
    # db.refresh(obj)