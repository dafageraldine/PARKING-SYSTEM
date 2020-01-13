import sys
from PyQt5 import QtWidgets, uic, QtGui, QtCore, QtNetwork
from PyQt5.QtWidgets import (QLineEdit,QWidget,QApplication,QMessageBox,QLabel,QComboBox)
from Module.sql import *
from Module.topup_new import *
from Module.login import *
from Module.ui_main_window import *
from datetime import datetime
from barcode.writer import ImageWriter

class Pelanggan():
	def __init__(self,widget):
		self.pelanggan = widget.mysql
		font = QtGui.QFont()
		font.setPointSize(12)

		self.parent = widget
		self.w = QtWidgets.QWidget(widget)
		self.w.setGeometry(250,50,1366,768)

		self.ui_main_window = Ui_Form(widget)
		self.topup_new = Topup(widget)
		self.data = QtWidgets.QLabel(self.w)
		self.data.setGeometry(QtCore.QRect(210, 15, 115, 17))
		self.data.setText("Data pelanggan")
		self.data.setFont(font)

		self.comboBox = QtWidgets.QComboBox(self.w)
		self.comboBox.setGeometry(QtCore.QRect(10, 15, 131, 31))
		self.comboBox.addItem("Regular")
		self.comboBox.addItem("Khusus")
		self.comboBox.currentTextChanged.connect(self.change)
		
		self.line_2 = QtWidgets.QFrame(self.w)
		self.line_2.setGeometry(QtCore.QRect(200, 35, 131, 16))
		self.line_2.setStyleSheet("border-top:3px solid black")
		self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)

		self.img = QtWidgets.QLabel(self.w)
		self.pixmap = QtGui.QPixmap("placeholder.png")
		self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
		self.img.setGeometry(QtCore.QRect(185, 48, 161, 191))

		self.labelrfid = QtWidgets.QLabel(self.w)
		self.labelrfid.setText("RFID")
		self.labelrfid.setGeometry(QtCore.QRect(590, 40, 67, 17))
		self.labelrfid.setFont(font)

		self.labelid = QtWidgets.QLabel(self.w)
		self.labelid.setText("ID")
		self.labelid.setGeometry(QtCore.QRect(590, 0, 365, 17))
		self.labelid.setFont(font)
		self.labelid.hide()

		self.labelnama = QtWidgets.QLabel(self.w)
		self.labelnama.setFont(font)
		self.labelnama.setText("Nama")
		self.labelnama.setGeometry(QtCore.QRect(590, 80, 67, 17))

		self.labelgender = QtWidgets.QLabel(self.w)
		self.labelgender.setText("Gender")
		self.labelgender.setGeometry(QtCore.QRect(590, 120, 61, 17))

		self.labelAlamat = QtWidgets.QLabel(self.w)
		self.labelAlamat.setText("Alamat")
		self.labelAlamat.setGeometry(QtCore.QRect(590, 160, 67, 17))
		self.labelAlamat.setFont(font)

		self.labelhp = QtWidgets.QLabel(self.w)
		self.labelhp.setText("No HP")
		self.labelhp.setGeometry(QtCore.QRect(590, 200, 61, 17))
		self.labelhp.setFont(font)

		self.ID = QLineEdit(self.w)
		self.ID.setGeometry(QtCore.QRect(670, 0, 431, 21))
		self.ID.hide()

		self.rfid = QLineEdit(self.w)
		self.rfid.setGeometry(QtCore.QRect(670, 40, 431, 21))
		self.rfid.setPlaceholderText("Tempelkan kartu pada scanner")
		self.rfid.setMaxLength(10)

		self.nama = QLineEdit(self.w)
		self.nama.setGeometry(QtCore.QRect(670, 80, 431, 21))

		self.radioButton = QtWidgets.QRadioButton(self.w)
		self.radioButton.setGeometry(QtCore.QRect(670, 120, 112, 23))
		self.radioButton.setText("Laki-laki")
		self.radioButton.setFont(font)

		self.radioButton_2 = QtWidgets.QRadioButton(self.w)
		self.radioButton_2.setGeometry(QtCore.QRect(780, 120, 112, 23))
		self.radioButton_2.setFont(font)
		self.radioButton_2.setText("Perempuan")

		self.alamat = QLineEdit(self.w)
		self.alamat.setGeometry(QtCore.QRect(670, 160, 431, 21))

		self.hp = QLineEdit(self.w)
		self.hp.setGeometry(QtCore.QRect(670, 200, 431, 21))

		self.foto = QtWidgets.QPushButton(self.w)
		self.foto.setText("Capture")
		self.foto.setGeometry(QtCore.QRect(190, 250, 151, 41))
		self.foto.setFont(font)
		self.foto.setStyleSheet("QPushButton {\n"
				"    background-color: #555;\n"
				"    border:none;\n"
				"    color:white;\n"
				"    border-radius: 6px;\n"
				"}\n"
				"QPushButton:pressed {\n"
				"    background-color: white;\n"
				"    border: 2px solid #555;\n"
				"    color: #555;\n"
				"}")
		self.foto.clicked.connect(self.takephoto)

		self.line_3 = QtWidgets.QFrame(self.w)
		self.line_3.setGeometry(QtCore.QRect(20, 340, 1091, 20))
		self.line_3.setStyleSheet("")
		self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
		self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)

		self.labelpoint = QtWidgets.QLabel(self.w)
		self.labelpoint.setText("Point")
		self.labelpoint.setStyleSheet("color : #ff8f00")
		self.labelpoint.setGeometry(QtCore.QRect(680, 230, 67, 17))
		self.labelpoint.setFont(font)

		self.point = QLineEdit(self.w)
		self.point.setFont(font)
		self.point.setGeometry(QtCore.QRect(610, 250, 171, 51))
		self.point.setStyleSheet("background :#ff8f00;\n"
			"color : white")
		self.point.setPlaceholderText("0")
		self.point.setEnabled(False)

		self.point2 = QLineEdit(self.w)
		self.point2.setFont(font)
		self.point2.setGeometry(QtCore.QRect(610, 250, 171, 51))
		self.point2.setStyleSheet("background :#ff8f00;\n"
			"color : white")
		self.point2.hide()

		self.labelsaldo = QtWidgets.QLabel(self.w)
		self.labelsaldo.setFont(font)
		self.labelsaldo.setText("Saldo")
		self.labelsaldo.setGeometry(QtCore.QRect(940, 230, 67, 17))
		self.labelsaldo.setStyleSheet("color : #00c853")

		self.saldo = QLineEdit(self.w)
		self.saldo.setFont(font)
		self.saldo.setGeometry(QtCore.QRect(850, 250, 241, 51))
		self.saldo.setStyleSheet("background :#00c853;\n"
			"position : center;\n"
			"color : white")
		self.saldo.setPlaceholderText("Rp 0")
		self.saldo.setEnabled(False)

		self.cari = QtWidgets.QLineEdit(self.w)
		self.cari.setGeometry(QtCore.QRect(20, 310, 981, 29))
		self.cari.setStyleSheet("border-radius: 10px;\n"
			"padding-left: 10px;\n"
			"position : center")
		self.cari.setAlignment(QtCore.Qt.AlignCenter)
		self.cari.setPlaceholderText("Masukan idPelanggan/scan kartu")

		self.cariBtn_2 = QtWidgets.QPushButton(self.w)
		self.cariBtn_2.setGeometry(QtCore.QRect(1020, 310, 80, 29))
		self.cariBtn_2.setStyleSheet("QPushButton {\n"
					"    background: #555;\n"
					"    border-radius: 6px;\n"
					"    border: none;\n"
					"    color: white;\n"
					"    outline: none;\n"
					"}\n"
					"\n"
					"QPushButton:pressed {\n"
					"    border: 2px solid #555;\n"
					"    background: white;\n"
					"    color: #555;\n"
					"}")
		self.cariBtn_2.setText("Cari")
		self.cariBtn_2.clicked.connect(self.findProduct)

		self.tabelPelanggan = QtWidgets.QTableWidget(self.w)
		self.tabelPelanggan.setGeometry(QtCore.QRect(30, 370, 1000, 260))
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.tabelPelanggan.sizePolicy().hasHeightForWidth())
		self.tabelPelanggan.setSizePolicy(sizePolicy)
		self.tabelPelanggan.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.tabelPelanggan.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
		self.tabelPelanggan.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.tabelPelanggan.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
		self.tabelPelanggan.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
		self.tabelPelanggan.setColumnCount(11)
		self.tabelPelanggan.setRowCount(0)
		item = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(0, item)
		item.setText("id")
		item2 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(1, item2)
		item2.setText("idPelanggan")
		item3 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(2, item3)
		item3.setText("nama")
		item4 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(3, item4)
		item4.setText("gender")
		item5 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(4, item5)
		item5.setText("member")
		item6 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(5, item6)
		item6.setText("alamat")
		item7 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(6, item7)
		item7.setText("kontak")
		item8 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(7, item8)
		item8.setText("foto")
		item9 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(8, item9)
		item9.setText("saldo")
		item10 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(9, item10)
		item10.setText("point")
		item11 = QtWidgets.QTableWidgetItem()
		self.tabelPelanggan.setHorizontalHeaderItem(10, item11)
		item11.setText("rfid")
		self.tabelPelanggan.horizontalHeader().setCascadingSectionResizes(True)
		self.tabelPelanggan.itemClicked.connect(self.selectProduct)
		self.getProduct()

		self.simpan = QtWidgets.QPushButton(self.w)
		self.simpan.setFont(font)
		self.simpan.setGeometry(QtCore.QRect(20, 650, 151, 41))
		self.simpan.setStyleSheet("QPushButton {\n"
			"    background-color: #2962ff;\n"
			"    border:none;\n"
			"    color:white;\n"
			"    border-radius: 6px;\n"
			"}\n"
			"QPushButton:pressed {\n"
			"    background-color: white;\n"
			"    border: 2px solid #2962ff;\n"
			"    color: #2962ff;\n"
			"}")
		self.simpan.setText("simpan")
		self.simpan.clicked.connect(self.flag)

		self.hapus = QtWidgets.QPushButton(self.w)
		self.hapus.setGeometry(QtCore.QRect(180, 650, 151, 41))
		self.hapus.setFont(font)
		self.hapus.setStyleSheet("QPushButton {\n"
				"    background-color: #ff3d00;\n"
				"    border:none;\n"
				"    color:white;\n"
				"    border-radius: 6px;\n"
				"}\n"
				"QPushButton:pressed {\n"
				"    background-color: white;\n"
				"    border: 2px solid #ff3d00;\n"
				"    color: #ff3d00;\n"
				"}")
		self.hapus.setText("hapus")
		self.hapus.clicked.connect(self.deleteProduct)

		self.Topup = QtWidgets.QPushButton(self.w)
		self.Topup.setGeometry(QtCore.QRect(900, 650, 151, 41))
		self.Topup.setStyleSheet("QPushButton {\n"
			"    background-color: #00c853;\n"
			"    border:none;\n"
			"    color:white;\n"
			"    border-radius: 6px;\n"
			"}\n"
			"QPushButton:pressed {\n"
			"    background-color: white;\n"
			"    border: 2px solid #00c853;\n"
			"    color: #00c853;\n"
			"}")
		self.Topup.setText("Top up")
		self.Topup.setFont(font)
		self.Topup.clicked.connect(self.Topupedit)

		self.Khusus = QtWidgets.QLabel(self.w)
		self.Khusus.setGeometry(QtCore.QRect(670, 0, 365, 17))
		self.Khusus.setText("ANDA MEMASUKKAN DATA PELANGGAN KHUSUS")
		self.Khusus.setStyleSheet("color : red")
		self.Khusus.setFont(font)
		self.Khusus.hide()

		self.gender = QtWidgets.QLineEdit(self.w)
		self.gender.setGeometry(QtCore.QRect(670, 120, 431, 21))
		self.gender.hide()

		self.w.close()

	def Topupedit(self):
		i = 0
		tt = self.tabelPelanggan.selectedItems()
		if len(tt) < 1:
			self.parent.showDialog("information", "Informasi","Tolong pilih pelanggan yang hendak Topup")
			return
		else:
			self.hapus.setEnabled(False)
			self.login = Login(self.parent)
			self.login.show()
			if self.login.isLogin:
				self.topup_new.show()
	
	def change(self):
		if (self.comboBox.currentText() == "Khusus"):
			
			self.tabelPelanggan.clearSelection()
			self.Khusus.show()
			self.nama.clear()
			self.alamat.clear()
			self.hp.clear()
			self.saldo.clear()
			self.ID.clear()
			self.ID.hide()
			self.rfid.clear()
			self.labelid.hide()
			self.gender.clear()
			self.gender.hide()
			self.radioButton.show()
			self.radioButton_2.show()
			self.point2.show()
			self.point.clear()
			self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
			self.hapus.setEnabled(True)
			self.tabelPelanggan.clearSelection()

		elif(self.comboBox.currentText() == "Regular"):
			
			self.Khusus.hide()
			self.tabelPelanggan.clearSelection()
			self.nama.clear()
			self.rfid.clear()
			self.alamat.clear()
			self.hp.clear()
			self.saldo.clear()
			self.ID.clear()
			self.point.clear()
			self.ID.hide()
			self.labelid.hide()
			self.gender.clear()
			self.gender.hide()
			self.point2.hide()
			self.radioButton.show()
			self.radioButton_2.show()
			self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
			self.hapus.setEnabled(True)
			self.tabelPelanggan.clearSelection()

	def flag(self):
		if(self.nama.text() and self.alamat.text() and self.hp.text() and self.gender.text() and self.rfid.text() != ""):
			self.register2()
		else:
			if (self.comboBox.currentText() == "Regular"):
				if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
					if(self.nama.text() and self.alamat.text() and self.hp.text() and self.rfid.text() != ""):
						if(self.ui_main_window.n >= 1):
							self.ui_main_window.n = 0
							self.register()
						else:
							self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
							return
					else:
						self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
						return
				else:
						self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
						return
	
			if (self.comboBox.currentText() == "Khusus"):
				if (self.radioButton.isChecked() or self.radioButton_2.isChecked()):
					if(self.nama.text() and self.alamat.text() and self.hp.text() and self.point2.text() and self.rfid.text() != ""):
						if(self.ui_main_window.n >= 1):
							self.ui_main_window.n = 0
							self.register()
						else:
							self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
							return
					else:
						self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
						return
				else:
					self.parent.showDialog("warning", "Gagal","data tidak boleh kosong")
					return

	def register2(self):
		filename = self.ID.text() + str(".jpg")
		idp = filename[:-4]
		key = "idPelanggan = \"{}\",rfid = \"{}\", nama = \"{}\",gender = \"{}\",alamat= \"{}\",kontak= \"{}\",foto= \"{}\""
		key = key.format(idp,self.rfid.text(),self.nama.text(),self.gender.text(),self.alamat.text(),self.hp.text(),filename)
		ids = "idPelanggan = \"{}\""
		ids = ids.format(idp)
		self.pelanggan.update("pelanggan",key,ids)
				
		self.parent.showDialog("information","success","data berhasil di input")
		self.getProduct()
		self.nama.clear()
		self.alamat.clear()
		self.hp.clear()
		self.saldo.clear()
		self.gender.clear()
		self.gender.hide()
		self.rfid.clear()
		self.radioButton.show()
		self.radioButton_2.show()
		self.point.clear()
		self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
		self.point2.clear()
		self.ID.clear()
		self.ID.hide()
		self.labelid.hide()
		self.point2.hide()
		self.tabelPelanggan.clearSelection()
		self.hapus.setEnabled(True)

	def register(self):
		idp = self.ui_main_window.filename[:-4]
		self.code = self.ui_main_window.filename[:-4]
		setpoint = self.pelanggan.find("batasbawah,batastengah,batasatas","setting","idSettings","set-1","False")
		# print(setpoint)
		if (self.comboBox.currentText() == "Regular"):
			if (self.radioButton.isChecked()):
				point = 0
				if (point < setpoint[0][0]):
					member = "Bronze"
				if (point >= setpoint[0][0] and point < setpoint[0][1]):
					member = "Silver"
				if (point > setpoint[0][1] and point < setpoint[0][2]):
					member = "Gold"
				if (point > setpoint[0][2]):
					member = "Platinum" 

				val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
				val = val.format(idp,self.rfid.text(),self.nama.text(),"Laki-laki",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,0)
				err = self.pelanggan.insertTo(
                		"pelanggan", "idPelanggan,rfid,nama,gender,member,alamat,kontak,foto,saldo,point", val)
				self.parent.showDialog("information","success","data berhasil di input")
				self.getProduct()
				self.nama.clear()
				self.alamat.clear()
				self.hp.clear()
				self.ID.clear()
				self.rfid.clear()
				self.ID.hide()
				self.labelid.hide()
				self.saldo.clear()
				self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
				self.tabelPelanggan.clearSelection()
				self.hapus.setEnabled(True)

			if (self.radioButton_2.isChecked()):
				point = 0
				if (point < setpoint[0][0]):
					member = "Bronze"
				if (point >= setpoint[0][0] and point < setpoint[0][1]):
					member = "Silver"
				if (point > setpoint[0][1] and point < setpoint[0][2]):
					member = "Gold"
				if (point > setpoint[0][2]):
					member = "Platinum"

				val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
				val = val.format(idp,self.rfid.text(),self.nama.text(),"Perempuan",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,0)
				err = self.pelanggan.insertTo(
					"pelanggan", "idPelanggan,rfid,nama,gender,member,alamat,kontak,foto,saldo,point", val)
				self.parent.showDialog("information","success","data berhasil di input")
				self.getProduct()
				self.nama.clear()
				self.alamat.clear()
				self.hp.clear()
				self.rfid.clear()
				self.ID.clear()
				self.ID.hide()
				self.labelid.hide()
				self.saldo.clear()
				self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
				self.tabelPelanggan.clearSelection()
				self.hapus.setEnabled(True)

		if (self.comboBox.currentText() == "Khusus"):
			if (self.radioButton.isChecked()):
				points = int(self.point2.text())
				if (points < setpoint[0][0]):
					member = "Bronze"
				if (points >= setpoint[0][0] and points < setpoint[0][1]):
					member = "Silver"
				if (points > setpoint[0][1] and points < setpoint[0][2]):
					member = "Gold"
				if (points > setpoint[0][2]):
					member = "Platinum"

				val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
				val = val.format(idp,self.rfid.text(),self.nama.text(),"Laki-laki",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,self.point2.text())
				err = self.pelanggan.insertTo(
                		"pelanggan", "idPelanggan,rfid,nama,gender,member,alamat,kontak,foto,saldo,point", val)
				self.parent.showDialog("information","success","data berhasil di input")
				self.getProduct()
				self.nama.clear()
				self.alamat.clear()
				self.hp.clear()
				self.point.clear()
				self.point2.clear()
				self.point2.hide()
				self.rfid.clear()
				self.ID.clear()
				self.ID.hide()
				self.labelid.hide()
				self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
				self.tabelPelanggan.clearSelection()
				self.hapus.setEnabled(True)

			if (self.radioButton_2.isChecked()):
				points = int(self.point2.text())
				if (points < setpoint[0][0]):
					member = "Bronze"
				if (points >= setpoint[0][0] and points < setpoint[0][1]):
					member = "Silver"
				if (points > setpoint[0][1] and points < setpoint[0][2]):
					member = "Gold"
				if (points > setpoint[0][2]):
					member = "Platinum"

				val = "\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",{},{}"
				val = val.format(idp,self.rfid.text(),self.nama.text(),"Perempuan",member, self.alamat.text(),self.hp.text(),self.ui_main_window.filename,0,self.point2.text())
				err = self.pelanggan.insertTo(
					"pelanggan", "idPelanggan,rfid,nama,gender,member,alamat,kontak,foto,saldo,point", val)
				self.parent.showDialog("information","success","data berhasil di input")
				self.getProduct()
				self.nama.clear()
				self.alamat.clear()
				self.hp.clear()
				self.point.clear()
				self.point2.clear()
				self.point2.hide()
				self.ID.clear()
				self.ID.hide()
				self.rfid.clear()
				self.labelid.hide()
				self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
				self.tabelPelanggan.clearSelection()
				self.hapus.setEnabled(True)

	def takephoto(self):
		self.ui_main_window.show()
		self.ui_main_window.timer.stop()
		self.ui_main_window.cap.release()
		self.ui_main_window.image_label.setText("\t\t\t\tArahkan Wajah Anda\n \t\t\t\tKe Dalam Box Hijau")
		self.ui_main_window.close()

	def getProduct(self):
		listPelanggan = self.pelanggan.select(
            "id,idPelanggan,nama,gender,member,alamat,kontak,foto,saldo,point,rfid", "pelanggan", True)
		# print(listPelanggan)
		self.tabelPelanggan.setRowCount(len(listPelanggan))
		row = 0
		for data in listPelanggan:
			col = 0
			for val in data:
				if col is 0:
					val = str(val)
				if col is 8:
					val = "Rp " + str(val)
				if col is 9:
					val = str(val)
				self.tabelPelanggan.setItem(
					row, col, QtWidgets.QTableWidgetItem(val))
				col = col + 1
			row = row + 1

	def deleteProduct(self):
		i = 0
		tt = self.tabelPelanggan.selectedItems()
		if len(tt) < 1:
			self.parent.showDialog("information", "Informasi","Tolong pilih pelanggan yang hendak dihapus")
			return
		prompt = self.parent.showDialog("question", "Hapus Pelanggan", "Apakah anda ingin menghapus data pelanggan?")
		if prompt == QtWidgets.QMessageBox.Yes:
			for col in tt:
				if i is 0 or i % 10 is 0:
					key = "id = \"{}\""
					self.pelanggan.delete("pelanggan", key.format(col.text()))

				i = i+1
			self.img.setPixmap(self.pixmap.scaled(200, 170, QtCore.Qt.KeepAspectRatio))
			self.nama.clear()
			self.alamat.clear()
			self.hp.clear()
			self.saldo.clear()
			self.point.clear()
			self.point2.hide()
			self.ID.clear()
			self.rfid.clear()
			self.gender.clear()
			self.radioButton.show()
			self.radioButton_2.show()
			self.gender.hide()
			self.getProduct()
			self.tabelPelanggan.clearSelection()
			self.ID.hide()
			self.labelid.hide()

	def showDialog(self, msgType: str, title: str, message: str):
		msgBox = QtWidgets.QMessageBox()
		if msgType is "critical":
			msgBox.critical(self, title, message)
		elif msgType is "warning":
			msgBox.warning(self, title, message)
		elif msgType is "information":
			msgBox.information(self, title, message)
		elif msgType is "question":
			return msgBox.question(self, title, message)

	def findProduct(self):
		listPelanggan = self.pelanggan.find(
            "id,idPelanggan,nama,gender,member,alamat,kontak,foto,saldo,point,rfid", "pelanggan",
            "idPelanggan", self.cari.text(), True,
            "idPelanggan ASC")
		if len(listPelanggan) < 1:
			listPelanggan = self.pelanggan.find(
                "id,idPelanggan,nama,gender,member,alamat,kontak,foto,saldo,point,rfid", "pelanggan",
                "RFID", self.cari.text(), True,
                "idPelanggan ASC")
		# print(listPelanggan)
		self.tabelPelanggan.setRowCount(len(listPelanggan))
		row = 0
		for data in listPelanggan:
			col = 0
			for val in data:
				if col is 0:
					val = str(val)
					# print(val)
				if col is 8:
					val = "Rp " + str(val)
				if col is 9:
					val = str(val)
				self.tabelPelanggan.setItem(
					row, col, QtWidgets.QTableWidgetItem(val))
				col = col + 1
			row = row + 1
		self.tabelPelanggan.clearSelection()

	def selectProduct(self):
		row = self.tabelPelanggan.currentRow()
		self.labelid.show()
		self.ID.show()
		self.ID.setEnabled(False)
		self.radioButton.hide()
		self.radioButton_2.hide()
		self.gender.show()
		self.Khusus.hide()
		self.rfid.setText(self.tabelPelanggan.item(row, 10).text())
		self.ID.setText(self.tabelPelanggan.item(row, 1).text())
		self.nama.setText(self.tabelPelanggan.item(row, 2).text())
		self.gender.setText(self.tabelPelanggan.item(row, 3).text())
		self.alamat.setText(self.tabelPelanggan.item(row, 5).text())
		self.hp.setText(self.tabelPelanggan.item(row, 6).text())
		self.saldo.setText(self.tabelPelanggan.item(row, 8).text())
		self.point.setText(self.tabelPelanggan.item(row, 9).text())
		path = QtCore.QDir.currentPath()
		path = path + '/Module/static'
		imagepath = path + '/' + self.tabelPelanggan.item(row,7).text()
		imagess = QtGui.QPixmap(imagepath)	
		self.img.setPixmap(imagess.scaled(200,250,QtCore.Qt.KeepAspectRatio))

	def show(self):
		self.w.show()
	def close(self):
		self.w.close()
n = 0