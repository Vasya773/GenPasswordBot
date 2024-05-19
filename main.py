# from loader import bot
import handlers
from database.common.models import History, db
from keyboards.reply import menu
from database.core import crud
from site_API.core import site_api, url, headers, params

# from utils.set_bot_commands import set_default_commands


db_write = crud.create()
db_read = crud.retrieve()

fact_by_number = site_api.get_math_fact()
fact_by_date = site_api.get_date_fact()

response = fact_by_number('GET', url, headers, params, 5,  timeout=3)
response = response.json()
data = [{'number': response.get('number'), 'message': response.get('text')}]

db_write(db, History, data)

response = fact_by_date('GET', url, headers, params, '6', '21',  timeout=3)
response = response.json()
data = [{'number': response.get('year'), 'message': response.get('text')}]

db_write(db, History, data)

retrieved = db_read(db, History, History.number, History.message)

for elem in retrieved:
    print(elem.number, elem.message)

# if __name__ == '__main__':
#     # set_default_commands(bot)
#     bot.infinity_polling()
