from fastapi import APIRouter

page_router=APIRouter()

@page_router.get("/")
async def home():
    return {"message":"we are in home page"}

@page_router.get("/about")
async def about():
    return {"message":"We are in about page"}
