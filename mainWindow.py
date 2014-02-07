#!/usr/bin/python
# -*- coding: utf-8 -*-
#mainWindow.py
from PyQt4 import QtGui, QtCore, uic
import datetime

class QMainWindow(QtGui.QMainWindow):
	def __init__(self):
		super(QMainWindow,self).__init__()
		self.initUI()
		self.linkObjDict = {}
	#初始化窗口布局
	def initUI(self):
		uic.loadUi('ui/mainWindow.ui', self)
		self.setWindowTitle(u'统计套利信号客户端')
		self.statusBar().showMessage(u'已连接服务器')
	#显示信号
	def showMessage(self, meessage):
		meessage = unicode(meessage, 'gb2312')
		if meessage[0] == "0":
			self.showS(meessage)
		elif meessage[0] == "1":
			self.showTradeMessage(meessage)
		self.saveLog(meessage)
	#显示标准价差
	def showS(self, meessage):
		meessages = meessage.split('_')
		if meessages[1] == "600000":
			self.lcdNumber_1.display(meessages[2].replace("-",""))
		elif meessages[1] == "600648":
			self.lcdNumber_2.display(meessages[2].replace("-",""))
	#显示交易信号
	def showTradeMessage(self, meessage):
		meessages = meessage.split('_')
		if meessages[1] == "600000":
			self.listWidget_1.addItem(meessages[2])
			if self.listWidget_1.count() > 100:
				self.listWidget_1.takeItem(0)
		elif meessages[1] == "600648":
			self.listWidget_2.addItem(meessages[2])
			if self.listWidget_2.count() > 100:
				self.listWidget_2.takeItem(0)
	#保存日志
	def saveLog(self, logStr):
		logFile = open("log.log", "a")
		content = "%s %s\n"%(str(datetime.datetime.now()), logStr.encode('gb2312'))
		logFile.write(content)
		logFile.close()