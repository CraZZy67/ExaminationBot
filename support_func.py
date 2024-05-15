import json


def pars_json_to_list(json_: dict):
    result_string = ""
    for k, v in json_.items():
        result_string += f"{k}. {v['full_name']}\n--------------\n"
    return result_string


def sort(json_: dict):
    sorted_json = {}
    count = 1
    for k, v in json_.items():
        sorted_json[count] = v
        count += 1
    return sorted_json


def exam_len(type_: str):
    with open(f"{type_}.json", "r", encoding="utf-8") as file:
        json_len = len(json.loads(file.read()))

    return True if json_len > 0 else False


def len_topics_current_channel(number_channel: str):
    with open(f"data/topics.json", "r", encoding="utf-8") as file:
        json_ = json.loads(file.read())

    len_ = len(json_[number_channel])
    return True if len_ > 0 else False


def list_for_topics(number: str):
    with open("data/topics.json", "r", encoding="utf-8") as file:
        json_ = json.loads(file.read())

    spec_list = json_[number]
    result_string = ""
    count = 1

    for i in spec_list:
        result_string += f"{count}. {i['link']}\n--------------\n"
        count += 1
    return result_string


def examination_json_inf(list_: list):
    with open("data/topics.json", "r", encoding="utf-8") as file:
        required_link = json.loads(file.read())[list_[0]][int(list_[1]) - 100]["link"]

    with open("data/channels.json", "r", encoding="utf-8") as file:
        chat_full_name = json.loads(file.read())[list_[0]]["full_name"]

    with open("data/channels.json", "r", encoding="utf-8") as file:
        chat_id = json.loads(file.read())[list_[0]]["id"]

    result_string_if = ("Здравствуйте, это бот проверки на спам пользователей, "
                        f"чтобы дочитать продолжение, подпишитесь на канал: https://t.me/{chat_full_name}. ")
    result_string_else = (f"Вы успешно прошли проверку. Благодарим за подписку! "
                          f"Продолжение рассказа: {required_link}")
    return {"id": chat_id, "strings": [result_string_if, result_string_else]}
