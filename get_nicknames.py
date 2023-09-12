def return_only_nicknames(raw_data: list) -> list:
    return [person['nickname'] for person in raw_data]