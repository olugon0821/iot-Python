character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
}

for key, value in character.items():
    if key == "name" or key == "level":
        print(key, ":", value)
    elif key == "items":
        for item_key, item_value in character["items"].items():
            print(item_key, ":", item_value)
    elif key == "skill":
        for skill in value:
            print(key, ":", skill)
