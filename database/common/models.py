from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('info.db')


class ModelBase(pw.Model):
    created_at = pw.DateField(default=datetime.now())

    class Meta():
        database = db


class History(ModelBase):
    city = pw.TextField()
