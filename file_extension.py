def main():
    file_name = input("File name: ").strip().lower()
    
    extensions = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
    }
    
    for ext, media_type in extensions.items():
        if file_name.endswith(ext):
            print(media_type)
            return
    
    print("application/octet-stream")


    main()
