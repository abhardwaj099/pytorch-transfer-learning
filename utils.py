from pathlib import Path

def getFiles(path):
        files = [x for x in Path(path).rglob("*") if x.is_file()]
        return files

def getLabel(file_path):
    file_path = str(file_path.resolve())
    number = file_path.split("\\")[6]
    switcher = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    return switcher.get(number)
    # print(number)


if __name__=='__main__':
    file = getFiles("./images_copy")[15678]
    print(getLabel(file))