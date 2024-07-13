from typing import Dict, List, TypeVar

import peewee
from peewee import ModelSelect

from database.common.models import db, ModelBase, History
# from ..common.models import db


T = TypeVar('T')


def _update_history(user_id, first_name, response):

    with db.atomic():
        history_entry = History.get(History.user_id == user_id)
        history_entry.first_name = first_name
        history_entry.response = response
        try:
            history_entry.save()
        except peewee.IntegrityError:
            print('IntegrityError')


def _store_date(db: db, model: T, *data: List[Dict]) -> None:
    """ Функция записи данных, которая сохраняет данные в базу данных """

    with db.atomic():
        model.insert_many(*data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    """ Функция чтения данных, которая извлекает данные из базы данных """

    with db.atomic():
        response = model.select(*columns)

    return response


class CRUDInterface():
    """ Интерфейс базы данных """

    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data


if __name__ == '__main__':
    _update_history()
    _store_date()
    _retrieve_all_data()
    CRUDInterface()
