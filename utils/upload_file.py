import os

def handle_upload(file) -> None: 
     if not os.path.exists(UPLOAD_FOLDER): 
         os.makedirs(UPLOAD_FOLDER) 
     file.save(os.path.join(UPLOAD_FOLDER, file.filename))