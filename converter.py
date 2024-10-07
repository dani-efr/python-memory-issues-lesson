import ijson


def convert():
    # TODO: read the data.json file and convert it to a simple readable table
    with open("data.json", "r") as file:
        # meta, data
        objects = ijson.items(file, "data.item")
        for obj in objects:
            print(obj)
