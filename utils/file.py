import os

files = {
    "session.token": "gocqhttp",
}


def path_safe(*segments: str) -> str:
    path = os.path.join(*segments)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def upload(file) -> bool:
    try:
        file.save(os.path.join(
            path_safe(files.get(file.filename, 'upload')),
            file.filename,
        ))
        return True
    except Exception:
        return False
