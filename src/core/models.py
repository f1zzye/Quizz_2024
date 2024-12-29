from django.db import models


class BaseModel(models.Model):
    create_datetime = models.DateTimeField(null=True, auto_now_add=True)
    last_update = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True
