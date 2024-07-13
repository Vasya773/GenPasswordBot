from datetime import datetime

import peewee as pw


db = pw.SqliteDatabase('info.db')


class ModelBase(pw.Model):
    """ Базовый класс модели, который инициализирует базу данных """

    created_at = pw.DateField(default=datetime.now)

    class Meta():
        database = db


class History(ModelBase):
    """ Класс модели, который расширяет базовый класс """

    user_id = pw.AutoField(primary_key=True)
    first_name = pw.CharField()
    response = pw.TextField()
