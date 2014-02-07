#!/usr/bin/python
# -*- coding: utf-8 -*-
#controller.py
from PyQt4 import QtCore
import socket
import struct
import uuid

class QWindowsController(QtCore.QThread):
	def __init__(self, QMain):
		QtCore.QThread.__init__(self)
		execfile("config.ini")
		self.tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.tcpClient.connect((self.HOST, self.PORT))
		self.QMain = QMain
		self.subscibeMacAddress()

	def __del__(self):
		self.wait()

	def run(self):
		while 1:
			data = self.tcpClient.recv(1024)
			if data.strip():
				self.QMain.showMessage(data)
		self.terminate()

	def subscibeMacAddress(self):
		macAddress = uuid.UUID(int = uuid.getnode()).hex[-12:]
		registerPara = {
			"macAddress"	: macAddress,
			"subStocks"		: ["600000", "601169", "600648", "600663"],
			"subSignals"	: ["baseSignal"],
			"subMultiples"	: ["statisticalArbitrageMultiple"]
		}
		registerPara = str(registerPara)

		fmt = "ii%ds" %len(registerPara)
		sn = 0
		length = len(registerPara)
		bytes = struct.pack(fmt, sn, length, registerPara)
		self.tcpClient.send(bytes)
