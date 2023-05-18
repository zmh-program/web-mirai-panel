import os

def handle_upload(file) -> str:
    try:
        if file.filename == 'session.token':
            save_folder = os.path.join(os.getcwd(), 'gocqhttp')
        else:
            save_folder = os.path.join(os.getcwd(), 'upload')

        if not os.path.exists(save_folder):
            os.makedirs(save_folder)

        file.save(os.path.join(save_folder, file.filename))
        
        return "File uploaded successfully"  
    except Exception as e:
        return f"Error: {e}"  

