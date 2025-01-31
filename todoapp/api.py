from ninja import NinjaAPI
from django.shortcuts import get_object_or_404
from .models import todoapp  # Ensure the correct model name
from typing import List
from pydantic import BaseModel

api = NinjaAPI()



class todoappSchema(BaseModel):
    title: str
    description: str = None
    completed: bool

class todoappOutSchema(todoappSchema):
    id: int

    class Config:
        from_attributes = True  # Allow from_orm to work

@api.post("/todoapp/", response=todoappOutSchema)
def create_todoapp(request, data: todoappSchema):
    todoapp_instance = todoapp.objects.create(**data.dict())  # Correct model name
    return todoappOutSchema.from_orm(todoapp_instance)  # Use from_orm method

@api.get("/todoapp/", response=List[todoappOutSchema])
def list_todoapp(request):
    return todoapp.objects.all() 

@api.get("/todoapp/{todoapp_id}/", response=todoappOutSchema)
def get_todoapp(request, todoapp_id: int):
    todoapp_instance = get_object_or_404(todoapp, id=todoapp_id)  
    return todoapp_instance

@api.put("/todoapp/{todoapp_id}/", response=todoappOutSchema)
def update_todoapp(request, todoapp_id: int, data: todoappSchema):
    todoapp_instance = get_object_or_404(todoapp, id=todoapp_id) 
    for attr, value in data.dict().items():
        if value is not None:  # Optionally check for None before updating
            setattr(todoapp_instance, attr, value)
    todoapp_instance.save()
    return todoapp_instance

@api.delete("/todoapp/{todoapp_id}/")
def delete_todoapp(request, todoapp_id: int):
    todoapp_instance = get_object_or_404(todoapp, id=todoapp_id)  # Correct model name
    todoapp_instance.delete()
    return {"success": True}
