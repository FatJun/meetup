from tortoise import fields
from tortoise.models import Model


class Meet(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    description = fields.CharField(max_length=500)
    start_at = fields.DatetimeField()
    created = fields.DatetimeField(auto_now_add=True)
    creator = fields.ForeignKeyField("models.User", related_name="meet")
    members = fields.ManyToManyField("models.User", related_name="meets")

    def __repr__(self):
        return self.name
