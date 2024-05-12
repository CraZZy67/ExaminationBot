import json

from aiogram.fsm.state import StatesGroup, State


class AddChannel(StatesGroup):
    id = State()

    @staticmethod
    def add_json_channels(id_: int, full_name: str):
        with open("data/channels.json", "r", encoding="utf-8") as file:
            len_channel = len(json.loads(file.read()))

        if len_channel != 0:
            with open("data/channels.json", "r", encoding="utf-8") as file:
                update_obj = json.loads(file.read())
                update_obj[f"{len_channel + 1}"] = {"full_name": full_name, "id": id_}

            with open("data/topics.json", "r", encoding="utf-8") as file:
                update_obj_top = json.loads(file.read())
                update_obj_top[f"{len_channel + 1}"] = []

        with open("data/channels.json", "w", encoding="utf-8") as file:
            if len_channel != 0:
                json.dump(update_obj, file, indent=4)
            else:
                json.dump({f"{len_channel + 1}": {"full_name": full_name, "id": id_}}, file, indent=4)

        with open("data/topics.json", "w", encoding="utf-8") as file:
            if len_channel != 0:
                json.dump(update_obj_top, file, indent=4)
            else:
                json.dump({f"{len_channel + 1}": []}, file, indent=4)


class AddTopic(StatesGroup):
    link = State()

    @staticmethod
    def add_json_topic(link: str, number_channel: str):

        with open("data/topics.json", "r", encoding="utf-8") as file:
            json_ = json.loads(file.read())
        len_json_list = len(json_[number_channel])
        json_[number_channel].append({"id": len_json_list + 100, "link": link})

        with open("data/topics.json", "w", encoding="utf-8") as file:
            json.dump(json_, file, indent=4)

        return len_json_list + 100
