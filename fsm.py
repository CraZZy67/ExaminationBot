import json

from aiogram.fsm.state import StatesGroup, State

from support_func import sort


class AddChannel(StatesGroup):
    id = State()

    @staticmethod
    def add_json_channels(id_: int, full_name: str):
        with open("channels.json", "r", encoding="utf-8") as file:
            len_ = len(json.loads(file.read()))

        if len_ != 0:
            with open("channels.json", "r", encoding="utf-8") as file:
                update_obj = json.loads(file.read())
                update_obj[f"{len_ + 1}"] = {"full_name": full_name, "id": id_}

        with open("channels.json", "w", encoding="utf-8") as file:
            if len_ != 0:
                json.dump(update_obj, file, indent=4)
            else:
                json.dump({f"{len_ + 1}": {"full_name": full_name, "id": id_}}, file, indent=4)


class DelChannel(StatesGroup):
    number = State()

    @staticmethod
    def del_json_channel(number: str):
        with open("channels.json", "r", encoding="utf-8") as file:
            json_obj = json.loads(file.read())
            json_obj.pop(number)
            sorted_json = sort(json_obj)

        with open("channels.json", "w", encoding="utf-8") as file:
            json.dump(sorted_json, file, indent=4)
