from fastapi import APIRouter
from pydantic import BaseModel

from db_functions.posts_funcs import (
    get_posts_from_db,
    add_post_to_db,
    delete_post_db,
    edit_post_db
)

class Post(BaseModel):
    title: str 
    text: str

router = APIRouter()

@router.get("/posts")
async def get_posts():
    posts: list[str, str] = get_posts_from_db()
    return posts


@router.post("/posts")
async def create_post(post: Post):
    try:
        add_post_to_db(post.title, post.text)
        return 
    except Exception as err:
        print(err)
        return
    
@router.delete("/posts/{id}")
async def delete_post(id: int):
    delete_post_db(id)
    return

@router.put("/posts/{id}")
async def edit_post(id: int, post: Post):
    edit_post_db(id, post)
    return