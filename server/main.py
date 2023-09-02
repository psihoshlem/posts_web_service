from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/posts")
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

if __name__=="__main__":
    uvicorn.run("main:app",host="0.0.0.0", port=8000, reload=True)