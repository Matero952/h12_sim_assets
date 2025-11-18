if __name__ == "__main__":
    import os
    import json
    import pprint
    foo = {}
    foo["assets"] = {}
    for path in os.scandir("assets"):
        print(path)
        print(type(path))
        foo["assets"][f"{path.name}"] = {}
        for file in os.scandir(path):
            print(file)
            foo["assets"][f"{path.name}"][file.name.split(".")[1] + "_file"] = file.name
    pprint.pprint(foo)
    with open("asset_manifest.json", "w") as f:
        json.dump(foo, f, indent=4)
        # f.write(json.dump(foo, indent=4))
