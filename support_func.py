def pars_json_to_list(json: dict):
    result_string = ""
    for k, v in json.items():
        result_string += f"{k}. {v["full_name"]}\n--------------\n"
    return result_string


def sort(json: dict):
    sorted_json = {}
    count = 1
    for k, v in json.items():
        sorted_json[count] = v
        count += 1
    return sorted_json


