from fastapi import APIRouter

router = APIRouter()

@router.get("/posts")
async def get_posts():
    return [
        {
            "title": "title1",
            "text": "text1",
            "date": "01.01.2001"
        },
        {
            "title": "title2",
            "text": "text2",
            "date": "01.01.2001"
        },
        {
            "title": "title3",
            "text": "text3",
            "date": "01.01.2001"
        },
        {
            "title": "title4",
            "text": "text4",
            "date": "01.01.2001"
        },
        {
            "title": "title5",
            "text": "text5",
            "date": "01.01.2001"
        },
    ]