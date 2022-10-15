
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5 import QtGui


class FenPrincipale(QMainWindow):
     def __init__(self):
         super(FenPrincipale, self).__init__()
         self.setWindowIcon(QtGui.QIcon('logo-azpetite.jpeg'))
         self.navigateur = QWebEngineView()
         self.navigateur.setUrl(QUrl('http://google.com'))
         self.setCentralWidget(self.navigateur)
         self.showMaximized()


           #navbar:
         navbar = QToolBar()
         self.addToolBar(navbar)

         accueil_btn = QAction('Accueil', self)
         accueil_btn.triggered.connect(self.url_accueil)
         navbar.addAction(accueil_btn)

         retour_btn = QAction('Retour', self)
         retour_btn.triggered.connect(self.navigateur.back)
         navbar.addAction(retour_btn)

         rafraichir_btn = QAction('Rafraichir', self)
         rafraichir_btn.triggered.connect(self.navigateur.reload)
         navbar.addAction(rafraichir_btn)

         avancer_btn = QAction('Avancer', self)
         avancer_btn.triggered.connect(self.navigateur.forward)
         navbar.addAction(avancer_btn)

         self.url_bar = QLineEdit()
         self.url_bar.returnPressed.connect(self.navigation)
         navbar.addWidget(self.url_bar)

         self.navigateur.urlChanged.connect(self.update_url)

     def url_accueil(self):
         self.navigateur.setUrl(QUrl('http://google.com'))

     def navigation(self):
         url = self.url_bar.text()
         self.navigateur.setUrl(QUrl(url))

     def update_url(self,url):
        self.url_bar.setText(url.toString())



app = QApplication(sys.argv)
QApplication.setApplicationName('Azuro')
fenetre = FenPrincipale()
app.exec()

