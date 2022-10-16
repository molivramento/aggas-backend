import ormar
from db import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = 'users'

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128)
    sub: str = ormar.String(max_length=64)
