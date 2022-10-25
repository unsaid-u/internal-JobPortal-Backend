from pydantic import BaseModel


class Job_openings(BaseModel):
	title : str
	department : str
	experience : str
	location : str
	job_type : str
	responsibilities : str
	requirements : str


class Applications(BaseModel):
	name : str
	experience : str
	job_id : str
	current_org : str
	current_title : str
	university : str
	cv : str
	status : str
	email : str

class Modify_status(BaseModel):
	new_status: str