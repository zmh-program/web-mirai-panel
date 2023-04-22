import os
from flask import send_file

UPLOADS_FOLDER = 'uploads'

def handle_upload(file):
    if not os.path.exists(UPLOADS_FOLDER):
        os.makedirs(UPLOADS_FOLDER)
    filename = file.filename
    file.save(os.path.join(UPLOADS_FOLDER, filename))
