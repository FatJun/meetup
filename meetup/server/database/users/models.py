from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    username = fields.CharField(max_length=100, unique=True)
    hashed_password = fields.CharField(max_length=100)
    is_active = fields.BooleanField(default=True)

    telegram_chat_id = fields.IntField(null=True, default=None)
    registered_in_telegram = fields.BooleanField(default=False)

    meets = fields.ManyToManyRelation['models.Meet']
    own_meets = fields.ForeignKeyRelation['models.Meet']

    class PydanticMeta:
        exclude = ["hashed_password"]

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
