from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_functions.db_models import Post
from db_functions.db_config import user, password, host, db_name
from db_functions.utils import get_str_date

engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}/{db_name}", echo=False
)

DBSession = sessionmaker(bind=engine)


def get_posts_from_db():
    with DBSession() as session:
        posts = session.query(Post).all()
    json_posts = []
    for post in posts:
        json_posts.append(
            {
                "title": post.title,
                "text": post.text,
                "date": get_str_date(post.created_at)
            }
        )
    return json_posts


def add_post(title: str, text: str):
    new_post = Post(title=title, text=text)
    with DBSession() as session:
        session.add(new_post)
        session.commit()

if __name__=="__main__":
    print(get_posts_from_db())