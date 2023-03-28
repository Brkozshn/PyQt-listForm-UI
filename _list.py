from PyQt5 import QtWidgets
import sys
from _listForm import Ui_MainWindow
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #load Students
        self.loadStudents()

        #add New Student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        #edit Student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        #delete Student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        #Up
        self.ui.btnUp.clicked.connect(self.upStudent)

        #Down
        self.ui.btnDown.clicked.connect(self.downStudent)

        #Sort
        self.ui.btnSort.clicked.connect(self.sortStudents)

        #Exit
        self.ui.btnExit.clicked.connect(self.close)

    def editStudent(self):
        index = self.ui.listitems.currentRow()   #index no gelir.
        item = self.ui.listitems.item(index)    #indexe karşılık değer gelir.

        if item is not None:
            text, ok = QInputDialog.getText(self,"Edit Student","Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)


    def addStudent(self):
        currentIndex = self.ui.listitems.currentRow()
        text, ok = QInputDialog.getText(self,"New Student","Student Name")
        if ok and text is not None:
            self.ui.listitems.insertItem(currentIndex,text)

    def loadStudents(self):
        self.ui.listitems.addItems(['Ahmet','Ali','Çınar'])
        self.ui.listitems.setCurrentRow(1)

    def removeStudent(self):
        index = self.ui.listitems.currentRow()  # index no gelir.
        item = self.ui.listitems.item(index)  # indexe karşılık değer gelir.
        if item is None:
            return

        q = QMessageBox.question(self, "Remove Student", "Do you want to remove the student: " + item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.listitems.takeItem(index)
            del item


    def upStudent(self):
        index = self.ui.listitems.currentRow()
        if index >= 1:
            item = self.ui.listitems.takeItem(index)
            self.ui.listitems.insertItem(index-1,item)  #bir önceki indexe yerleştiririz.
            self.ui.listitems.setCurrentItem(item)


    def downStudent(self):
        index = self.ui.listitems.currentRow()
        if index < self.ui.listitems.count() - 1:
            item = self.ui.listitems.takeItem(index)
            self.ui.listitems.insertItem(index + 1, item)  # bir sonraki indexe yerleştiririz.
            self.ui.listitems.setCurrentItem(item)

    def sortStudents(self):
        self.ui.listitems.sortItems()

    def close(self):
        quit()



def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()