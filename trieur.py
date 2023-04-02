#Import :

import os, shutil


img = ["png", "jpeg", "jpg", "webp", "bmp", "tif", "svg", "ico"]

video = ["mkv", "mp4", "avi", "mov", "wmv"]


doc = ["txt", "pdf", "odt", "doc", "docx", "xps", "rtf", "xml"]


audio = ["mp3", "wav", "ogg", "wma", "mid", "acc", "flac", "alac", "aiff", "dsd"]


nom_dossier = ["Images", "Vidéo", "Documents", "Audios", "Dossiers"]


for a in nom_dossier:
    if not os.path.exists(a):
        os.mkdir(a)


def trie(format: list, dossier: str):
    all = os.listdir()
    for fichier in all:
        if os.path.isfile(fichier):
            ext = fichier.split(".")
            if ext[len(ext)-1] in format:
                if not os.path.exists(dossier+"/"+fichier):
                    shutil.copyfile(fichier, dossier+"/"+fichier)
                    os.remove(fichier)