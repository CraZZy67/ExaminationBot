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

    if json_len > 0:
        return True
    elif json_len == 0:
        return False


def len_topics_current_channel(number_channel: str):
    with open(f"secondary/topics.json", "r", encoding="utf-8") as file:
        json_ = json.loads(file.read())

    len_ = len(json_[number_channel])
    if len_ > 0:
        return True
    else:
        return False


def list_for_topics(number: str):
    with open("secondary/topics.json", "r", encoding="utf-8") as file:
        json_ = json.loads(file.read())

    spec_list = json_[number]
    result_string = ""
    count = 1

    for i in spec_list:
        result_string += f"{count}. {i['link']}\n--------------\n"
        count += 1
    return result_string
