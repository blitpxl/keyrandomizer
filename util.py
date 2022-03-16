from PyQt5.QtCore import QFile, QIODevice


def open_qt_resource(url):
    file = QFile(url)
    file.open(QIODevice.ReadOnly)
    bytes_content = file.readAll()
    content = bytes(bytes_content).decode("utf-8")
    return content


def clean(string: str):
    string = string.split(",")
    string = [char for char in string if char and char != " "]
    string = [char.strip() for char in string]
    string = str(string).replace("[", "").replace("]", "").replace("'", "")
    return string
