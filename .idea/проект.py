import datetime

import matplotlib.pyplot
import matplotlib.pyplot as plt
import datetime
import sys
import io
from PyQt6 import uic
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QPushButton, QBoxLayout

con = sqlite3.connect('Weather')
cur = con.cursor()
result = cur.execute("""SELECT * FROM weather""").fetchall()
con.close()


class Constructor(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('interface.ui', self)
        self.pushButton1.clicked.connect(self.run_T)
        self.pushButton2.clicked.connect(self.run_P)
        self.pushButton3.clicked.connect(self.run_U)
        self.pushButton4.clicked.connect(self.run_DD)
        self.pushButton5.clicked.connect(self.run_Ff)
        self.pushButton6.clicked.connect(self.run_W1)
        self.pushButton.clicked.connect(self.gist_T)
        self.pushButton_7.clicked.connect(self.condition)
        self.pushButton_2.clicked.connect(self.gist_P)
        self.pushButton_3.clicked.connect(self.gist_U)
        self.pushButton_5.clicked.connect(self.gist_Ff)

    def run_T(self):
        if self.lineEdit_9.text() == '':
            self.lineEdit.setText('error')
        else:
            for i in result:
                n = result.index(i)
                if i[0][:10] == self.lineEdit_9.text():
                    data = result[n][1]
                    break
            self.lineEdit.setText(data)

    def run_P(self):
        if self.lineEdit_10.text() == '':
            self.lineEdit_2.setText('error')
        else:
            for i in result:
                n = result.index(i)
                if i[0][:10] == self.lineEdit_10.text():
                    data = result[n][2]
                    break
            self.lineEdit_2.setText(data)

    def run_U(self):
        if self.lineEdit_9.text() == '':
            self.lineEdit_3.setText('error')
        else:
            for i in result:
                n = result.index(i)
                if i[0][:10] == self.lineEdit_11.text():
                    data = result[n][3]
                    break
            self.lineEdit_3.setText(data)

    def run_DD(self):
        if self.lineEdit_12.text() == '':
            self.lineEdit_4.setText('error')
        else:
            for i in result:
                n = result.index(i)
                if i[0][:10] == self.lineEdit_12.text():
                    data = result[n][4]
                    break
            self.lineEdit_4.setText(data)

    def run_Ff(self):
        if self.lineEdit_13.text() == '':
            self.lineEdit_5.setText('error')
        else:
            for i in result:
                n = result.index(i)
                if i[0][:10] == self.lineEdit_13.text():
                    data = result[n][5]
                    break
            self.lineEdit_5.setText(data)

    def run_W1(self):
        if self.lineEdit_14.text() == '':
            self.lineEdit_6.setText('error')
        else:
            for i in result:
                n = result.index(i)
                if i[0][:10] == self.lineEdit_14.text():
                    data = result[n][6]
                    break
            if data != '':
                self.lineEdit_6.setText(data)
            else:
                self.lineEdit_6.setText('Осадков нет')

    def mean_T(self):
        condition1 = self.lineEdit_25.text()
        condition2 = self.lineEdit_28.text()
        if condition1 == '' or condition2 == '':
            return 'error'
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [float(i[1].replace(',', '.')) for i in result[n2:n1]]
            text = round(sum(sps) / len(sps), 1)
            return str(text)

    def mean_P(self):
        condition1 = self.lineEdit_25.text()
        condition2 = self.lineEdit_28.text()
        if condition1 == '' or condition2 == '':
            return 'error'
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [float(i[2].replace(',', '.')) for i in result[n2:n1]]
            text = round(sum(sps) / len(sps), 1)
            return str(text)

    def mean_U(self):
        condition1 = self.lineEdit_25.text()
        condition2 = self.lineEdit_28.text()
        if condition1 == '' or condition2 == '':
            return 'error'
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [int(i[3].replace(',', '.')) for i in result[n2:n1]]
            text = round(sum(sps) / len(sps), 1)
            return str(text)

    def mean_Ff(self):
        condition1 = self.lineEdit_25.text()
        condition2 = self.lineEdit_28.text()
        if condition1 == '' or condition2 == '':
            return 'error'
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [int(i[5].replace(',', '.')) for i in result[n2:n1]]
            text = round(sum(sps) / len(sps), 1)
            return str(text)

    def condition(self):
        if self.Combobox.currentText() == 'Температуры':
            self.lineEdit_27.setText(self.mean_T())
        elif self.Combobox.currentText() == 'Атмосферного давления':
            self.lineEdit_27.setText(self.mean_P())
        elif self.Combobox.currentText() == 'Относительной влажногсти':
            self.lineEdit_27.setText(self.mean_U())
        elif self.Combobox.currentText() == 'Скорости ветра':
            self.lineEdit_27.setText(self.mean_Ff())

    def gist_T(self):
        condition1 = self.lineEdit_7.text()
        condition2 = self.lineEdit_8.text()
        if condition1 == '' or condition2 == '':
            self.lineEdit_7.setText('error')
            self.lineEdit_8.setText('error')
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [float(i[1].replace(',', '.')) for i in result[n2:n1]]
            plt.hist(sps)
            plt.show()

    def gist_P(self):
        condition1 = self.lineEdit_15.text()
        condition2 = self.lineEdit_16.text()
        if condition1 == '' or condition2 == '':
            self.lineEdit_15.setText('error')
            self.lineEdit_16.setText('error')
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [float(i[2].replace(',', '.')) for i in result[n2:n1]]
            plt.hist(sps)
            plt.show()

    def gist_U(self):
        condition1 = self.lineEdit_17.text()
        condition2 = self.lineEdit_18.text()
        if condition1 == '' or condition2 == '':
            self.lineEdit_17.setText('error')
            self.lineEdit_18.setText('error')
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [int(i[3].replace(',', '.')) for i in result[n2:n1]]
            plt.hist(sps)
            plt.show()

    def gist_Ff(self):
        condition1 = self.lineEdit_21.text()
        condition2 = self.lineEdit_22.text()
        if condition1 == '' or condition2 == '':
            self.lineEdit_21.setText('error')
            self.lineEdit_22.setText('error')
        else:
            for i in result[1::]:
                if i[0][:10] == condition1:
                    n1 = result.index(i)
                elif i[0][:10] == condition2:
                    n2 = result.index(i)
            sps = [int(i[5].replace(',', '.')) for i in result[n2:n1]]
            plt.hist(sps)
            plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Constructor()
    ex.show()

    sys.exit(app.exec())
