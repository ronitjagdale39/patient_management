from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import json
from schema.schema import Patient,PatientUpdate

app2=FastAPI()

    
filename='/Users/rony/Documents/DJANGO/FastAPI/app2/files/patients.json'
def save_data(data):
    with open(filename,'w') as f:
        json.dump(data,f)
def load_json():
    with open(filename,'r') as f:
        data1=json.load(f)
        return data1
@app2.get('/')    
def home():
    return {"Patient Management system"
    }
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
@app2.post('/create')
def Create(patient:Patient):
    data=load_json()
    if patient.id in data:
        raise HTTPException(status_code=400,detail="The Patient already exists  in the database.")
    data[patient.id]=patient.model_dump(exclude={'id'})
    save_data(data)
    return JSONResponse(status_code=200,content={
        'message':'Data entered successfully '
    })
@app2.put("/patientupdate/{patient_id}")
def update_patient(patient_id: str, patient: PatientUpdate):
    data = load_json()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    updates = patient.model_dump(
    exclude_unset=True,
    exclude_none=True
    )

    if not updates:
        raise HTTPException(status_code=400, detail="No fields provided for update")

   
    for key, value in updates.items():
        data[patient_id][key] = value

    save_data(data)

    return {
        "message": "Patient updated successfully",
        "patient_id": patient_id,
        "updated_data": data[patient_id]
    }
@app2.delete('/delete')
def Delete(patient_id :str ,patient:Patient):
    data=load_json()
    if patient_id in data:
        del data[patient_id]
        save_data(data)
    else:
        raise HTTPException(status_code=400,detail="particular id not has any entry")      
    return JSONResponse(status_code=200,content={
        'message':f"successfully deleted the details of {patient_id}"
    })  
    
