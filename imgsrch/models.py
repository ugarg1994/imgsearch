#from django.db import models
from mongoengine import *
#from djangotoolbox.fields import ListField

class ImageDB(Document):
    img_name = StringField(required=True)
    image_url = StringField(max_length=200)
    keywords = ListField(StringField(max_length=30))