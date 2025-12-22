from pydantic import BaseModel,Field,field_validator,computed_field,validate_email
from typing import List ,Tuple ,Dict ,Annotated,Optional,Literal
class Patient(BaseModel):
    id:Annotated[str,Field(...,description='enter your patient id here:',examples=['P001'])]
    name:Annotated[str,Field(...,description="enter u r name (maximum 50 characters..):",max_length=50)]
    city:Annotated[str,Field(...,description="enter your city name :",examples=['Mumbai'])]
    age:Annotated[int ,Field(...,description="enter the age :")]
    gender:Annotated[Literal['male','female','others'],Field(...,description="Enter u r gender :")]
    height:Annotated[float,Field(...,gt=0,description='Enter u r height in meters')]
    
    weight:Annotated[float,Field(...,gt=0,description='Enter u r weight in kgs ')] 
    @field_validator('city')
    @classmethod
    def Cityy(cls,value:str):
        value=value.strip().title()
        return value
    @computed_field
    @property
    def bmi(self)->float:
        bmi=round((self.weight/self.height**2),2)  
        return bmi
    @computed_field
    @property
    def verdict(self)->str:
        if self.bmi<=18.5:
            return "underweight"
        elif 18.5<self.bmi<40:
            return "Normal"
        else:
            return "Obese"
        
    