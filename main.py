# from fastapi import FastAPI,Body,Depends
# from pydantic import BaseModel
# from typing import Annotated
# import uvicorn

# class Post(BaseModel):
#     title : str
#     content : str

# app = FastAPI()

# async def common_parameters(q:str ,skip: int = 0, limit:int = 100 ):
#     print("Here!!!!!!!!!")
#     return {"q":q,"skip":skip,"limit":limit}

# @app.get("/blogs")
# async def blogs(params: Annotated[dict,Depends(common_parameters)]):
#     return {"results":[1,2,3,4,5]}

# @app.post("/create-post")
# async def create(post:Post = Body()):
#     return post

# @app.get("/{slug}")
# async def root(slug: int,is_public: bool = True):
#     return {"message": f"Hello {slug}! "}

# uvicorn.run(app)
