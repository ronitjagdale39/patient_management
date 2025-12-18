from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
import json

app2=FastAPI()

filename='patients.json'
def load_json():
    with open(filename,'r') as f:
        data1=json.load(f)
        return data1
@app2.get('/home')    
def home():
    return "helloooo frndssss"
@app2.get('/patient/{patient_id}')
def Show(patient_id:str):
    data=load_json()
    if patient_id not in data:
        return HTTPException(status_code=400,detail="patients not found of this id ...")
    else:
        return data[patient_id]
@app2.get('/sort')
def Ordering(sort_by:str=Query(...,description='on what basisu wanna sort by : height,weight and bmi'),order:str=Query('asc',description="what do u wanna order it by ascending or descendding")):
    valid_teams=['height','weight','bmi']
    if sort_by not in valid_teams:
        raise HTTPException(status_code=400,detail=f"enter btw {valid_teams}")
    if order not in ['asc' ,'desc']:
        raise HTTPException(status_code=400,detail='only asc or desc allowed ')
    data=load_json()  
    sorting=True if order=='desc' else False  
    sort=sorted(data.values(),key=lambda x : x.get(sort_by,0),reverse=sorting)
    return sort