from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from app.restauration.moteur import MoteurRestauration
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('WEEGER Studio'); self.resize(900,650); self.dossier=''
        w=QWidget(); self.setCentralWidget(w); l=QVBoxLayout(w)
        t=QLabel('WEEGER Studio'); t.setAlignment(Qt.AlignCenter); l.addWidget(t)
        b=QPushButton('📂 Choisir un dossier'); b.clicked.connect(self.choisir_dossier); l.addWidget(b)
        self.cb_restauration=QCheckBox('Restaurer les photos'); self.cb_restauration.setChecked(True); l.addWidget(self.cb_restauration)
        self.cb_description=QCheckBox('Générer les descriptions'); self.cb_description.setChecked(True); l.addWidget(self.cb_description)
        self.cb_ocr=QCheckBox('OCR'); l.addWidget(self.cb_ocr)
        self.cb_rename=QCheckBox('Renommer'); l.addWidget(self.cb_rename)
        self.cb_doublons=QCheckBox('Détecter les doublons'); l.addWidget(self.cb_doublons)
        run=QPushButton('▶ Lancer'); run.clicked.connect(self.lancer); l.addWidget(run)
        self.progress=QProgressBar(); l.addWidget(self.progress)
        self.journal=QTextEdit(); self.journal.setReadOnly(True); l.addWidget(self.journal)
    def choisir_dossier(self):
        d=QFileDialog.getExistingDirectory(self,'Choisir un dossier')
        if d: self.dossier=d; self.journal.append(f'Dossier sélectionné : {d}')
    def lancer(self):
        if not self.dossier:
            self.journal.append('Aucun dossier sélectionné.'); return
        self.journal.clear(); self.journal.append('Recherche des photos...\n')
        m=MoteurRestauration(self.dossier); photos=m.recuperer_photos()
        self.progress.setMaximum(max(len(photos),1))
        if not photos: self.journal.append('Aucune photo trouvée.'); return
        for i,p in enumerate(photos,1):
            self.journal.append(f'{i}. {p.name}'); self.progress.setValue(i)
        self.journal.append(f'\n{len(photos)} photo(s) trouvée(s).')
