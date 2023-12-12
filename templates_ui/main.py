# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1475, 872)
        MainWindow.setMinimumSize(QSize(1024, 720))
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"backround-color: #a4b0be;\n"
"color: #ffffff;\n"
"}\n"
"")
        MainWindow.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        MainWindow.setInputMethodHints(Qt.ImhNone)
        self.realization_menu = QAction(MainWindow)
        self.realization_menu.setObjectName(u"realization_menu")
        self.receipt_of_goods_menu = QAction(MainWindow)
        self.receipt_of_goods_menu.setObjectName(u"receipt_of_goods_menu")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.main_menu = QMenuBar(MainWindow)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setGeometry(QRect(0, 0, 1475, 22))
        self.main_menu.setStyleSheet(u"")
        self.documents_menu = QMenu(self.main_menu)
        self.documents_menu.setObjectName(u"documents_menu")
        self.documents_menu.setStyleSheet(u"")
        self.documents_for_buyers_menu = QMenu(self.documents_menu)
        self.documents_for_buyers_menu.setObjectName(u"documents_for_buyers_menu")
        self.documents_by_suppliers_menu = QMenu(self.documents_menu)
        self.documents_by_suppliers_menu.setObjectName(u"documents_by_suppliers_menu")
        self.guids_menu = QMenu(self.main_menu)
        self.guids_menu.setObjectName(u"guids_menu")
        MainWindow.setMenuBar(self.main_menu)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.main_menu.addAction(self.documents_menu.menuAction())
        self.main_menu.addAction(self.guids_menu.menuAction())
        self.documents_menu.addAction(self.documents_for_buyers_menu.menuAction())
        self.documents_menu.addAction(self.documents_by_suppliers_menu.menuAction())
        self.documents_for_buyers_menu.addAction(self.realization_menu)
        self.documents_by_suppliers_menu.addAction(self.receipt_of_goods_menu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u043e\u0440\u0433\u043e\u0432\u043b\u044f \u0438 \u0441\u043a\u043b\u0430\u0434", None))
        self.realization_menu.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.receipt_of_goods_menu.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435 \u0422\u0426\u041c", None))
        self.documents_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.documents_for_buyers_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u043f\u043e \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044f\u043c", None))
        self.documents_by_suppliers_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043a\u0443\u043c\u0435\u043d\u0442\u044b \u043f\u043e \u043f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a\u0430\u043c", None))
        self.guids_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0440\u0430\u0432\u043e\u0447\u043d\u0438\u043a", None))
    # retranslateUi

