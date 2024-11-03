from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QInputDialog,QLineEdit,QFileDialog, QProgressDialog, QMessageBox
import calculate_l5
import calculate_l8
import reg_analysis

object1 = calculate_l5.Calculate_NDVI_L5

object2 = calculate_l8.Calculate_NDVI_LST_L8

object3 = reg_analysis.Calculate_Regression_Analysis

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName("Dialog")
        self.resize(884, 681)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 211, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 130, 211, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 180, 211, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 80, 111, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 180, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 130, 111, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 390, 150, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(270, 280, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 280, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 330, 111, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 330, 211, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self)
        self.lineEdit_6.setGeometry(QtCore.QRect(470, 130, 211, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 330, 211, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.pushButton_8 = QtWidgets.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(700, 130, 111, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(570, 390, 150, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_8 = QtWidgets.QLineEdit(self)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 280, 211, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_10 = QtWidgets.QPushButton(self)
        self.pushButton_10.setGeometry(QtCore.QRect(700, 80, 111, 28))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_12 = QtWidgets.QPushButton(self)
        self.pushButton_12.setGeometry(QtCore.QRect(700, 280, 111, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self)
        self.pushButton_13.setGeometry(QtCore.QRect(700, 180, 111, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(self)
        self.lineEdit_9.setGeometry(QtCore.QRect(470, 80, 211, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self)
        self.lineEdit_10.setGeometry(QtCore.QRect(470, 180, 211, 31))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.pushButton_14 = QtWidgets.QPushButton(self)
        self.pushButton_14.setGeometry(QtCore.QRect(700, 330, 111, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.lineEdit_11 = QtWidgets.QLineEdit(self)
        self.lineEdit_11.setGeometry(QtCore.QRect(40, 230, 211, 31))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_15 = QtWidgets.QPushButton(self)
        self.pushButton_15.setGeometry(QtCore.QRect(270, 230, 111, 31))
        self.pushButton_15.setObjectName("pushButton_15")
        self.lineEdit_12 = QtWidgets.QLineEdit(self)
        self.lineEdit_12.setGeometry(QtCore.QRect(470, 230, 211, 31))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton_16 = QtWidgets.QPushButton(self)
        self.pushButton_16.setGeometry(QtCore.QRect(700, 230, 111, 31))
        self.pushButton_16.setObjectName("pushButton_16")
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 421, 431))
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self)
        self.groupBox_2.setGeometry(QtCore.QRect(450, 20, 421, 431))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_13 = QtWidgets.QLineEdit(self)
        self.lineEdit_13.setGeometry(QtCore.QRect(40, 550, 211, 31))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_17 = QtWidgets.QPushButton(self)
        self.pushButton_17.setGeometry(QtCore.QRect(270, 550, 121, 28))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self)
        self.pushButton_18.setGeometry(QtCore.QRect(270, 500, 121, 28))
        self.pushButton_18.setObjectName("pushButton_18")
        self.lineEdit_14 = QtWidgets.QLineEdit(self)
        self.lineEdit_14.setGeometry(QtCore.QRect(40, 500, 211, 31))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_15 = QtWidgets.QLineEdit(self)
        self.lineEdit_15.setGeometry(QtCore.QRect(40, 600, 211, 31))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_19 = QtWidgets.QPushButton(self)
        self.pushButton_19.setGeometry(QtCore.QRect(270, 600, 121, 28))
        self.pushButton_19.setObjectName("pushButton_19")
        self.groupBox_3 = QtWidgets.QGroupBox(self)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 470, 671, 181))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_20.setGeometry(QtCore.QRect(450, 70, 201, 51))
        self.pushButton_20.setObjectName("pushButton_20")
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.groupBox.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.lineEdit_4.raise_()
        self.pushButton_7.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.lineEdit_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.lineEdit_8.raise_()
        self.pushButton_10.raise_()
        self.pushButton_12.raise_()
        self.pushButton_13.raise_()
        self.lineEdit_9.raise_()
        self.lineEdit_10.raise_()
        self.pushButton_14.raise_()
        self.lineEdit_11.raise_()
        self.pushButton_15.raise_()
        self.lineEdit_12.raise_()
        self.pushButton_16.raise_()
        self.lineEdit_13.raise_()
        self.pushButton_17.raise_()
        self.pushButton_18.raise_()
        self.lineEdit_14.raise_()
        self.lineEdit_15.raise_()
        self.pushButton_19.raise_()

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Band 3"))
        self.pushButton.clicked.connect(self.addBand3)
        self.pushButton_2.setText(_translate("Dialog", "Band 6"))
        self.pushButton_2.clicked.connect(self.addBand6)
        self.pushButton_3.setText(_translate("Dialog", "Band 4"))
        self.pushButton_3.clicked.connect(self.addBand4)
        self.pushButton_4.setText(_translate("Dialog", "NDVI və LST hesabla"))
        self.pushButton_4.clicked.connect(self.calculate_NDVI_LST_L5)
        self.pushButton_6.setText(_translate("Dialog", "NDVI output"))
        self.pushButton_6.clicked.connect(self.ndvi_output)
        self.pushButton_7.setText(_translate("Dialog", "Tempratur output"))
        self.pushButton_7.clicked.connect(self.lst_output)
        self.pushButton_8.setText(_translate("Dialog", "Band 5"))
        self.pushButton_8.clicked.connect(self.addBand5)
        self.pushButton_9.setText(_translate("Dialog", "NDVI və LST hesabla"))
        self.pushButton_9.clicked.connect(self.calculate_NDVI_LST_L8)
        self.pushButton_10.setText(_translate("Dialog", "Band 4"))
        self.pushButton_10.clicked.connect(self.addBand4_l8)
        self.pushButton_12.setText(_translate("Dialog", "NDVI output"))
        self.pushButton_12.clicked.connect(self.ndvi_output_l8)
        self.pushButton_13.setText(_translate("Dialog", "Band 10"))
        self.pushButton_13.clicked.connect(self.addBand10)
        self.pushButton_14.setText(_translate("Dialog", "Tempratur output"))
        self.pushButton_14.clicked.connect(self.lst_output_l8)
        self.pushButton_15.setText(_translate("Dialog", "Clip shape"))
        self.pushButton_15.clicked.connect(self.l5_clip)
        self.pushButton_16.setText(_translate("Dialog", "Clip shape"))
        self.pushButton_16.clicked.connect(self.l8_clip)
        self.groupBox.setTitle(_translate("Dialog", "Landsat 4/5 NDVI  və Temperatur hesablama"))
        self.groupBox_2.setTitle(_translate("Dialog", "Landsat 8/9 NDVI  və Temperatur hesablama"))
        self.pushButton_17.setText(_translate("Dialog", "LTS fayılları"))
        self.pushButton_17.clicked.connect(self.LST_Folder)
        self.pushButton_18.setText(_translate("Dialog", "NDVI fayilları"))
        self.pushButton_18.clicked.connect(self.NDVI_folder)
        self.pushButton_19.setText(_translate("Dialog", "Regressiya neticesi"))
        self.pushButton_19.clicked.connect(self.end_reg)
        self.groupBox_3.setTitle(_translate("Dialog", "Reqessiya hesablaması"))
        self.pushButton_20.setText(_translate("Dialog", "Reqresiyya hesablamasini başlat"))
        self.pushButton_20.clicked.connect(self.start_regression)
        
        
    def addBand3(self):
        B3_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select TIF File', '', 'TIF Files (*.tif)')
        self.lineEdit.setText(B3_path)


    def addBand6(self):
        
        B6_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select TIF File', '', 'TIF Files (*.tif)')
        self.lineEdit_3.setText(B6_path)
        
        
    def addBand4(self):
        
        B4_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select TIF File', '', 'TIF Files (*.tif)')
        self.lineEdit_2.setText(B4_path)
        
        
    def addBand5(self):
        B5_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select TIF File', '', 'TIF Files (*.tif)')
        self.lineEdit_6.setText(B5_path)
        
    def addBand4_l8(self):
        
        B4_path_l8, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select TIF File', '', 'TIF Files (*.tif)')
        self.lineEdit_9.setText(B4_path_l8)
        
        
    def addBand10(self):
        
        B10_path, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select TIF File', '', 'TIF Files (*.tif)')
        self.lineEdit_10.setText(B10_path)
        
        
        
    def NDVI_folder(self):
        ndvi_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        
        self.lineEdit_14.setText(ndvi_path)
        
    
    def LST_Folder(self):
        
        lst_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')
        
        self.lineEdit_13.setText(lst_path)
        
    def end_reg(self):
        
        reg_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select File', '', 'Regression File (*.tif);;All Files (*)')
        if reg_path:
            self.lineEdit_15.setText(reg_path)
        
        
        
    
        
        
    def l5_clip(self):
        shp_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select SHP File', '', 'Shapefiles (*.shp)')
        self.lineEdit_11.setText(shp_path)
        
    def l8_clip(self):
        
        shp_path_l8, _ = QtWidgets.QFileDialog.getOpenFileName(None, 'Select SHP File', '', 'Shapefiles (*.shp)')
        self.lineEdit_12.setText(shp_path_l8)
        
        
    def ndvi_output(self):
        
        ndvi_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select File', '', 'GeoTIFF files (*.tif);;All Files (*)')
        if ndvi_path:
            self.lineEdit_4.setText(ndvi_path)
        
    def ndvi_output_l8(self):
        
        ndvi_path_l8, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select File', '', 'GeoTIFF files (*.tif);;All Files (*)')
        if ndvi_path_l8:
            self.lineEdit_8.setText(ndvi_path_l8)
        
        
    def lst_output(self):
        
        lst_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select File', '', 'GeoTIFF files (*.tif);;All Files (*)')
        if lst_path:
            self.lineEdit_5.setText(lst_path)
        
    def lst_output_l8(self):
        
        lst_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Select File', '', 'GeoTIFF files (*.tif);;All Files (*)')
        if lst_path:
            self.lineEdit_7.setText(lst_path)
        
        
        
        
    def calculate_NDVI_LST_L5(self):
        
        band3 = self.lineEdit.text()
        band4 = self.lineEdit_2.text()
        band6 = self.lineEdit_3.text()
        shape = self.lineEdit_11.text()
        ndvi = self.lineEdit_4.text()
        lst = self.lineEdit_5.text()
        
        
        
        
        
        object1(band3,band4,band6,shape,ndvi,lst)
        
        
        
    
    def calculate_NDVI_LST_L8(self):
        
        band4_l8 = self.lineEdit_9.text()
        band5_l8 = self.lineEdit_6.text()
        band10_l8 = self.lineEdit_10.text()
        shape_l8 = self.lineEdit_12.text()
        ndvi_l8 = self.lineEdit_8.text()
        lst_l8 = self.lineEdit_7.text()
        
        object2(band4_l8,band5_l8,band10_l8,shape_l8,ndvi_l8,lst_l8)
        
        
    def start_regression(self):
        
        NDVI_files = self.lineEdit_14.text()
        LST_files = self.lineEdit_13.text()
        end_regression = self.lineEdit_15.text()
        
        object3(NDVI_files,LST_files,end_regression)
        
        
        
        
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    ui = Ui_Dialog()
   
    sys.exit(app.exec_())
