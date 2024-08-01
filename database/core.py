from database.common.models import db, Password, Game

db.connect()
db.create_tables([Password, Game], safe=True)
