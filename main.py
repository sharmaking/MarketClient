#!/usr/bin/python
# -*- coding: utf-8 -*-
import controller
import mainWindow
import sys
from PyQt4 import QtGui

def main():
	app = QtGui.QApplication(sys.argv)
	QMain = mainWindow.QMainWindow()
	#创建信号监视进程
	Controller = controller.QWindowsController(QMain)
	Controller.start()
	#显示主窗口
	QMain.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()