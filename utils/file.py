import os

files = {
    "session.token": "gocqhttp",
}


def upload(file) -> bool:
    try:
        path = os.path.join(os.getcwd(), files.get(file.filename, 'upload'))
        if not os.path.exists(path):
            os.makedirs(path)
        file.save(os.path.join(path, file.filename))
        return True
    except Exception:
        return False
