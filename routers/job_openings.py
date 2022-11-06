from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import database, models, schema 

router = APIRouter(
	prefix='/job_openings',
	tags=['job_openings']
)


@router.get('/')     # query parameters for filtering
def get_all_openings(db : Session = Depends(database.get_db), type : str = None, location :str = None, experience:str = None):
	openings = db.query(models.Job_openings)

	if type != None:
		openings = openings.filter(models.Job_openings.job_type == type)

	if experience != None:
		openings = openings.filter(models.Job_openings.experience == experience)

	if location != None:
		openings = openings.filter(models.Job_openings.location == location)
		
	
	return openings.all()


@router.get('/{id}')
def get_opening(id:int, db : Session = Depends(database.get_db)):
	opening = db.query(models.Job_openings).filter(models.Job_openings.job_id == id).first()

	if not opening:
		return False
	
	return opening

@router.delete('/delete/{id}')
def delete_opening(id:int, db : Session = Depends(database.get_db)):
	opening = db.query(models.Job_openings).filter(models.Job_openings.job_id == id).first()

	if not opening:
		return False
	
	db.delete(opening)
	db.commit()
	

@router.post('/add_opening')
def add_new_opening(request:schema.Job_openings, db : Session = Depends(database.get_db)):
	opening = models.Job_openings(
		title = request.title,
		department = request.department,
		experience = request.experience,
		location = request.location,
		job_type = request.job_type,
		responsibilities = request.responsibilities,
		requirements = request.requirements
	)

	db.add(opening)
	db.commit()
	db.refresh(opening)


