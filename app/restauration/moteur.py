from pathlib import Path
EXTENSIONS=['.jpg','.jpeg','.png','.tif','.tiff','.bmp']
class MoteurRestauration:
    def __init__(self,dossier):
        self.dossier=Path(dossier)
    def recuperer_photos(self):
        photos=[]
        for f in self.dossier.iterdir():
            if f.suffix.lower() in EXTENSIONS:
                photos.append(f)
        return sorted(photos)
