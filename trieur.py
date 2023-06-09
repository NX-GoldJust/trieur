#Import :

import os, shutil


img = ["png", "jpeg", "jpg", "webp", "bmp", "tif", "svg", "ico"]

video = ["mkv", "mp4", "avi", "mov", "wmv", "gif"]


doc = ["txt", "pdf", "odt", "doc", "docx", "xps", "rtf", "xml"]


audio = ["mp3", "wav", "ogg", "wma", "mid", "acc", "flac", "alac", "aiff", "dsd"]
app = ["exe"]

nom_dossier = ["Images", "Vidéo", "Documents", "Audios", "Dossiers", "Autres", "Applications"]


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
                    
trie(img, "Images")
trie(video, "Vidéo")
trie(doc, "Documents")
trie(audio, "Audios")
trie(app, "Applications")
#Dossier :
restant = os.listdir()
for c in restant:
    if os.path.isdir(c):
        if not os.path.exists("Dossiers/"+c) and c not in nom_dossier:
            
            shutil.copytree(dirs_exist_ok=True, src=c, dst="Dossiers")
            try:
                shutil.rmtree(c)
            except:
                pass
    else:
        if not os.path.exists("Autres/"+c) and os.path.basename(__file__) != c:
            shutil.copyfile(c, "Autres/"+c)
            os.remove(c)
        


