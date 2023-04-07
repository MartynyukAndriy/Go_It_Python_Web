from commands import search_tag, search_tags, search_name
from mongoengine import disconnect


if __name__ == "__main__":
    while True:
        command = input("Type a command as 'command: search'\n>>> ")
        to_do = command.split(":")[0].strip()
        search = command.split(":")[1].strip()
        if to_do in ["tag", "tags", "name"]:
            if to_do == "tag":
                print(search_tag(search))
            elif to_do == "tags":
                tags = [tag.strip() for tag in search.split(",")]
                print(search_tags(tags))
            else:
                print(search_name(search))
        elif to_do == "exit":
            break
        else:
            print("Wrong command")

    disconnect()
