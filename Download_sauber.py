import os
import shutil

# Erstelle die Namen der Ordner, die die verschiedenen Dateitypen enthalten sollen
folder_names = {
    '.jpg': 'Bilder',
    '.jpeg': 'Bilder',
    '.png': 'Bilder',
    '.gif': 'Bilder',
    '.bmp': 'Bilder',
    '.tiff': 'Bilder',
    '.mp4': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.wmv': 'Videos',
    '.pdf': 'PDF',
    '.mp3': 'Musik',
    '.wav': 'Musik',
    '.aac': 'Musik',
    '.flac': 'Musik'
}

# Pfad zum Download-Ordner auf Windows
download_path = os.path.join(os.path.expanduser("~"), "Downloads")

# Durchsuche alle Dateien im Download-Ordner
for filename in os.listdir(download_path):
    # Ignoriere Ordner und versteckte Dateien
    if os.path.isdir(os.path.join(download_path, filename)) or filename.startswith('.'):
        continue

    # Holen Sie die Dateierweiterung und den Namen des Dateityps
    extension = os.path.splitext(filename)[1]
    folder_name = folder_names.get(extension, 'Andere')

    # Erstelle den Ordner, wenn er noch nicht vorhanden ist
    folder_path = os.path.join(download_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Kopiere die Datei in den entsprechenden Ordner
    file_path = os.path.join(download_path, filename)
    new_file_path = os.path.join(folder_path, filename)
    shutil.move(file_path, new_file_path)

print("Fertig!")
