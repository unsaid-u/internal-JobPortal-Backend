from fastapi import FastAPI
from db import database, models
from routers import  applications, job_openings
from db import models
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

models.Base.metadata.create_all(database.engine)


app.include_router(applications.router)
app.include_router(job_openings.router)

@app.get('/')
def welcome():
    return {'Welcome' : 'Job Portal'}

