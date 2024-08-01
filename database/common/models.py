import peewee as pw

db = pw.SqliteDatabase('passwords.db')


class Password(pw.Model):
    """ Модель для хранения сгенерированных паролей """

    password = pw.CharField()
    user_id = pw.IntegerField()

    class Meta:
        database = db


class Game(pw.Model):
    """ Модель для хранения данных игры """

    user_id = pw.IntegerField()
    number = pw.IntegerField()
    attempts = pw.IntegerField()

    class Meta:
        database = db
