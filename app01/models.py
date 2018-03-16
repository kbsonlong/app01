# coding: utf8
from app01 import app,db
import datetime
db.init_app(app)

class Post(db.Document):
    title = db.StringField(max_length=255, required=True)
    slug = db.StringField(max_length=255, required=True, unique=True)
    abstract = db.StringField()
    raw_content = db.StringField(required=True)
    pub_time = db.DateTimeField()
    update_time = db.DateTimeField()
    author = db.StringField()
    category = db.StringField(max_length=64)
    tags = db.ListField(db.StringField(max_length=30))


    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        if not self.pub_time:
            self.pub_time = now
        self.update_time = now

        return super(Post, self).save(*args, **kwargs)