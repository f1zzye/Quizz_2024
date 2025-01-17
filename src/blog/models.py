import datetime

from django.utils.formats import date_format
from mongoengine import (
    Document, StringField, DateTimeField, ReferenceField, ListField, EmbeddedDocumentField, EmbeddedDocument
)

class Blog(EmbeddedDocument):
    name = StringField(max_length=255)
    text = StringField()
    author = StringField(max_length=255)

class Entry(Document):
    blog = ListField(EmbeddedDocumentField(Blog))
    timestamp = DateTimeField(default=datetime.datetime.now)
    headline = StringField(max_length=255)

