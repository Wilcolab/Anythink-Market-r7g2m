from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

database_url = os.environ["DATABASE_URL"].replace("postgres://", "postgresql://")

user_insert_statement = text(
    """INSERT INTO users(username, email, salt, bio, hashed_password) VALUES(:username, :email, :salt, :bio, :hashed_password)"""
)
select_last_user_id = text("""SELECT * FROM users ORDER BY id DESC LIMIT 1""")
item_statement = text(
    """INSERT INTO items(slug, title, description, seller_id) VALUES(:slug, :title, :description, :seller_id)"""
)
select_last_item_id = text("""SELECT * FROM items ORDER BY id DESC LIMIT 1""")
comment_statement = text(
    """INSERT INTO comments(body, seller_id, item_id) VALUES(:body, :seller_id, :item_id)"""
)

engine = create_engine(database_url, echo=True)

with engine.connect() as connect:
    for i in range(100):
        random_user = f'user_{i}'
        user = {
            "username": random_user,
            "email": f"{random_user}@mail.com",
            "salt": "abc_123",
            "bio": f"{random_user} bio",
            "hashed_password": f"super_secuere_{i}"
        }
        connect.execute(user_insert_statement, **user)
        result = connect.execute(select_last_user_id)
        
        result = connect.execute(select_last_user_id).one()
        generated_user_id = result.id

        item = {
            "slug": f"slug-{random_user}",
            "title": f"title{i}",
            "description": f"desc{i}",
            "seller_id": generated_user_id,
        }
        connect.execute(item_statement, **item)

        item_result = connect.execute(select_last_item_id).one()
        generated_item_id = item_result.id
        
        comment = {
            "body": f"comment{i}",
            "seller_id": generated_user_id,
            "item_id": generated_item_id,
        }
        connect.execute(comment_statement, **comment)