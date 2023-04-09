from sqlalchemy import create_engine

from repositories.users import UsersRepository
from repositories.items import ItemsRepository
from repositories.comments import CommentsRepository
import random
import string
from core.config import get_app_settings


database_url = get_app_settings().database_url.replace("postgres://", "postgresql://")


engine = create_engine(database_url, echo=True)
letters = string.ascii_lowercase
with engine.connect() as connect:
    user_repository = UsersRepository(connect)
    items_repository = ItemsRepository(connect)
    comments_repository = CommentsRepository(connect)
    
    for i in range(100):
        random_username = ''.join(random.choice(letters) for i in range(24))
        user = user_repository.create_user(username=random.choice(),email= f'{random_username}@mail.com',password= 'super_secure')
        
        item = items_repository.create_item(
            slug=f'slug-{random_username}',
            title=f'Title-{i}',
            description=f'Description-{i}',
            seller=user,
            body=f'Body {i}',
            image=f'image_{i}',
            tags=f'Tags--->{i}',
        )
        comments = comments_repository.create_comment_for_item(body=f'body---{i}', item=item, user=user)
    