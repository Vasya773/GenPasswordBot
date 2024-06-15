from datetime import datetime

import peewee as pw

db = pw.SqliteDatabase('info.db')


class ModelBase(pw.Model):
    """ Базовый класс модели, который определяет базу данных """

    created_at = pw.DateField(default=datetime.now)

    class Meta():
        database = db


class History(ModelBase):
    """ Класс модели, который расширяет базовый класс """

    city = pw.TextField()
