import os
import shutil
import sys



def move_files(source_folder,folder_paths,  file_extensions):
    files = os.listdir(source_folder)

    for file in files:
        for category, extensions in file_extensions.items():
            for extension in extensions:
                if file.endswith(extension):
                    source_path = os.path.join(source_folder,file)
                    direction_path = os.path.join(source_folder,folder_paths[category],file)
                    # print(source_path)
                    # print(direction_path)

                    shutil.move(source_path, direction_path)
                    print(f"'{file}' has been moved to '{folder_paths[category]}'.")
                    break

                # else:
                #     direction_path = os.path.join("/Others",file)
                #     shutil.move(source_path, direction_path)
                #     break
                    
def make_dirs(source_folder, folder_paths):

    for folder in folder_paths.values():
        nepat = os.path.join(source_folder, folder)
        if not os.path.exists(nepat):
            os.makedirs(nepat)
            print(f"Folder '{folder}' created successfully.")




if __name__ == "__main__":
    if len(sys.argv)>1:
        print(len(sys.argv))
        source_folder = sys.argv[1]
        
    else:
        source_folder = "."




file_extensions = {
    "Image Files": [".jpg", ".jpeg", ".png", ".gif"],
    "Video Files": [".mp4", ".avi",".mkv"],
    "Document Files": [".txt", ".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Compressed Files": [".zip", ".rar", ".tar", ".tar.gz", ".7z"],
    "Audio Files": [".mp3", ".wav", ".ogg", ".flac", ".aac", ".wma", ".m4a", ".opus", ".aiff", ".ape", ".amr", ".midi", ".pcm", ".alac", ".webm", ".3gp", ".mka", ".aa", ".au", ".ra", ".vox", ".gsm", ".mogg", ".sln", ".dss", ".ds2", ".wv", ".tta", ".mpc", ".mod", ".s3m", ".xm", ".it", ".mo3"],
    "Windows Software Files": [".exe", ".dll", ".iso"],
    "Other Files": [".html", ".htm", ".css", ".js", ".csv", ".xml", ".json", ".sql", ".log"]
}


folder_paths = {
    "Image Files": "Images",
    "Video Files": "Videos",
    "Document Files": "Documents",
    "Compressed Files": "Compressed_files",
    "Audio Files": "Audios",
    "Windows Software Files": "Softwares",
    "Other Files": "Others"
}


make_dirs(source_folder, folder_paths)
move_files(source_folder,folder_paths, file_extensions)


