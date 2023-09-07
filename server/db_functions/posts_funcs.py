from sqlalchemy import create_engine, desc
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
        posts = session.query(Post).order_by(desc(Post.created_at)).all()
    json_posts = []
    for post in posts:
        json_posts.append(
            {
                "id": post.id,
                "title": post.title,
                "text": post.text,
                "date": get_str_date(post.created_at)
            }
        )
    return json_posts


def add_post_to_db(title: str, text: str):
    new_post = Post(title=title, text=text)
    with DBSession() as session:
        session.add(new_post)
        session.commit()


def delete_post_db(id):
    with DBSession() as session:
        post = session.query(Post).filter_by(id=id).first()
        session.delete(post)
        session.commit()


def edit_post_db(id, post):
    with DBSession() as session:
        post_to_update = session.query(Post).filter_by(id=id).first()
        post_to_update.title = post.title
        post_to_update.text = post.text
        session.commit()