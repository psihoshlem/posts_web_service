from fastapi import APIRouter

from db_functions.posts_funcs import (
    get_posts_from_db,
    add_post
)

router = APIRouter()

@router.get("/posts")
async def get_posts():
    posts: list[str, str] = get_posts_from_db()
    return posts