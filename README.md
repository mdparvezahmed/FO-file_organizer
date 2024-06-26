﻿# File Organizer

This Python script organizes files in a specified folder based on their file extensions. It categorizes files into different folders according to their types such as images, videos, documents, etc.

## How to Use

1. **Requirements**: This script requires Python 3.x to be installed on your system.

2. **Setup**:

   - Clone this repository or download the `file_organizer.py` file.
   - Ensure Python is installed on your system.

3. **Usage**:

   - Open your terminal or command prompt.
   - Navigate to the directory where the `file_organizer.py` file is located.
   - Run the script using the following command:
     ```
     python organizer.py [source_folder]
     ```
     Replace `[source_folder]` with the path to the folder you want to organize. If no source folder is provided, the script will use the current directory.
   - Or copy the file_organizer.py file to the folder you want to organize: -Run the script using the following command:
     ```
     python file_organizer.py
     ```

4. **Customization**:

   - You can customize the file extensions and folder paths according to your needs by modifying the `file_extensions` and `folder_paths` dictionaries in the script.

5. **Example**:

This will organize the files in the specified source folder based on their types into respective folders.

6. **Note**:

- Ensure that the source folder contains files that you want to organize.
- Make sure to review the script and understand how it works before running it on important data.

## Supported File Types

- **Image Files**: `.jpg`, `.jpeg`, `.png`, `.gif`
- **Video Files**: `.mp4`, `.avi`, `.mkv`
- **Document Files**: `.txt`, `.doc`, `.docx`, `.pdf`, `.xls`, `.xlsx`, `.ppt`, `.pptx`
- **Compressed Files**: `.zip`, `.rar`, `.tar`, `.tar.gz`, `.7z`
- **Audio Files**: `.mp3`, `.wav`, `.ogg`, `.flac`, `.aac`, `.wma`, `.m4a`, `.opus`, `.aiff`, `.ape`, `.amr`, `.midi`, `.pcm`, `.alac`, `.webm`, `.3gp`, `.mka`, `.aa`, `.au`, `.ra`, `.vox`, `.gsm`, `.mogg`, `.sln`, `.dss`, `.ds2`, `.wv`, `.tta`, `.mpc`, `.mod`, `.s3m`, `.xm`, `.it`, `.mo3`
- **Windows Software Files**: `.exe`, `.dll`, `.iso`
- **Other Files**: `.html`, `.htm`, `.css`, `.js`, `.csv`, `.xml`, `.json`, `.sql`, `.log`
