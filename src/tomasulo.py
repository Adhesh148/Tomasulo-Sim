# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tomasulo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import parser
import re

cycles = 0
filename = "instr.txt"

# Define global variables
registers = [[None,0] for i in range(32)] 
instructions = []
current_instrs = []

RS_ADD = [["", "", "", "", "", "", 0] for i in range(4)]
RS_MUL = [["", "", "", "", "", "", 0] for i in range(2)]
RS_FADD = [["", "", "", "", "", "", 0] for i in range(2)]
RS_FMUL = [["", "", "", "", "", "", 0] for i in range(2)]
RS_LU = [["", "", "", "", "", "", 0] for i in range(4)]
RS_LOAD = [["", "", "", "", "", "", 0] for i in range(2)]

RS = {"ADD":RS_ADD, "MUL":RS_MUL, "FADD":RS_FADD, "FMUL":RS_FMUL, "LU": RS_LU, "LOAD":RS_LOAD}
operations = {"ADD":["ADD","ADDC","SUB","SUBB"], "MUL":["MUL"], "FADD":["FADD","FSUB"], "FMUL":["FMUL"], "LU":["AND","OR","NAND","NOR","XOR","NOT", "NEG"], "LOAD":["LDR","STR"]}

exec_cycles = {"ADD":3, "MUL":8, "FADD":8, "FMUL": 12, "LOAD":1, "LU":2}
exec_list = []
exec_entries = []

writeBack_list = []

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1643, 942)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(310, 20, 271, 281))
        self.groupBox.setObjectName("groupBox")
        self.registerTable = QtWidgets.QTableWidget(self.groupBox)
        self.registerTable.setGeometry(QtCore.QRect(10, 32, 251, 241))
        self.registerTable.setRowCount(32)
        self.registerTable.setColumnCount(2)
        self.registerTable.setObjectName("registerTable")
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(27, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(28, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(29, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(30, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setVerticalHeaderItem(31, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.registerTable.setHorizontalHeaderItem(1, item)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(70, 60, 211, 221))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(10, 30, 191, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 310, 1561, 561))
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 30, 741, 191))
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.groupBox_4)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 30, 721, 151))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(7)
        self.tableWidget_2.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_5.setGeometry(QtCore.QRect(800, 40, 741, 131))
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_3.setGeometry(QtCore.QRect(10, 30, 721, 91))
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(7)
        self.tableWidget_3.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 220, 741, 191))
        self.groupBox_6.setObjectName("groupBox_6")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.groupBox_6)
        self.tableWidget_4.setGeometry(QtCore.QRect(10, 30, 721, 151))
        self.tableWidget_4.setObjectName("tableWidget_4")
        self.tableWidget_4.setColumnCount(7)
        self.tableWidget_4.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_7.setGeometry(QtCore.QRect(800, 180, 741, 131))
        self.groupBox_7.setObjectName("groupBox_7")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_7)
        self.tableWidget_5.setGeometry(QtCore.QRect(10, 30, 721, 91))
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(7)
        self.tableWidget_5.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        self.groupBox_8 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 420, 741, 131))
        self.groupBox_8.setObjectName("groupBox_8")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.groupBox_8)
        self.tableWidget_6.setGeometry(QtCore.QRect(10, 30, 721, 91))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(7)
        self.tableWidget_6.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        self.groupBox_9 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_9.setGeometry(QtCore.QRect(800, 320, 741, 131))
        self.groupBox_9.setObjectName("groupBox_9")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.groupBox_9)
        self.tableWidget_7.setGeometry(QtCore.QRect(10, 30, 721, 91))
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(7)
        self.tableWidget_7.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, item)
        self.groupBox_10 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_10.setGeometry(QtCore.QRect(880, 30, 591, 281))
        self.groupBox_10.setObjectName("groupBox_10")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.groupBox_10)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 561, 241))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.groupBox_11 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_11.setGeometry(QtCore.QRect(630, 40, 181, 221))
        self.groupBox_11.setObjectName("groupBox_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 40, 121, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_11)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 160, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1643, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Add user-defined events

        # On clicking "Next Clock Cycle" button - trigger all necessary events that must happen on the next cc
        self.pushButton.clicked.connect(lambda: self.nextCycle(self.pushButton))

        # On clicking "Load File" btn - load the button from the filename provided 
        self.pushButton_3.clicked.connect(lambda: self.loadFile(self.pushButton_3))

        # On clicking "Reset" btn - reset everything : all tables and functions
        self.pushButton_2.clicked.connect(lambda: self.onReset(self.pushButton_2))

    def nextCycle(self, nextBtn):
        global cycles
        global current_instrs

        cycles += 1
        self.writeBack()
        self.executeInstrs()
        if len(current_instrs) > 0:
            self.issueNextInstr()
        
    def loadFile(self, loadBtn):
        global filename
        global instructions
        global current_instrs

        # Call reset first
        self.onReset(self.pushButton_2)

        # Create a file object of the parser class
        fo = parser.myParser(filename)
        instructions = fo.extractAll()
        print("[File] File has been loaded successfuly ...")
        print("[Register] Registers have been reset ...")

        # Load the first 5 instructions into the instruction queue
        if len(instructions) > 5:
            current_instrs = instructions[:5].copy()
            instructions = instructions[5:]
        else:
            current_instrs = instructions.copy()
            instructions = []

        print(instructions)
        self.updateInstrTable()
        print("[Update] Instruction Table has been updated ...")

    def onReset(self, resetBtn):
        """
        Reset function - to clear all registers, RS and status terminals
        """
        global instructions
        global current_instrs
        global cycles
        global RS_ADD, RS_MUL, RS_FADD, RS_FMUL, RS_LU, RS_LOAD, RS
        global exec_entries, exec_list, writeBack_list

        cycles = 0

        print("[Reset] Reset activated ...")
        self.resetRegisters()

        instructions = []
        current_instrs = []
        self.updateInstrTable(reset = 1)

        RS_ADD = [["", "", "", "", "", "", 0] for i in range(4)]
        RS_MUL = [["", "", "", "", "", "", 0] for i in range(2)]
        RS_FADD = [["", "", "", "", "", "", 0] for i in range(2)]
        RS_FMUL = [["", "", "", "", "", "", 0] for i in range(2)]
        RS_LU = [["", "", "", "", "", "", 0] for i in range(4)]
        RS_LOAD = [["", "", "", "", "", "", 0] for i in range(2)]

        RS = {"ADD":RS_ADD, "MUL":RS_MUL, "FADD":RS_FADD, "FMUL":RS_FMUL, "LU": RS_LU, "LOAD":RS_LOAD}
        self.updateRSTables(reset = 1)

        exec_entries = []
        exec_list = []
        writeBack_list = []

        print("[Reset] Sucessful ...")

    def resetRegisters(self,):
        global registers
        
        registers = [[None,0] for i in range(32)] 
        self.updateRegisterTable()

    def issueNextInstr(self,):
        global current_instrs
        global instructions
        global operations
        global registers

        isIssued = 0

        nextInstr = current_instrs[0]
        op = nextInstr[0].upper()
        val1 = 0            # flag, 0 => opnd is sourced from a RS, 1 => val is given in the opnd
        val2 = 0
        rs1 = None
        rs2 = None
        opnd1 = None
        opnd2 = None
        dst = None

        # Check if any reservation station is free for the given operation
        freeRSIndx,rsName = self.isRSFree(op = op)
        #print(op)
        #print(freeRSIndx,rsName)

        if freeRSIndx == -1:
            print("RS Full")
            return
        
        # Extract Destination
        if op == "STR":
            dst = int("".join(map(str,re.findall(r'\d+',nextInstr[2]))))
        else:
            dst = int("".join(map(str,re.findall(r'\d+',nextInstr[1]))))
        
        # Check if the destination register is free
        if registers[dst][0] != None:
            print("Destination clash")
            return

        isIssued = 1

        # Extract Opnds
        if op == "STR":
            opnd1 = float(re.findall(r'\d+[.]?\d*',nextInstr[1])[0])
            if '#' in nextInstr[1]:
                rs1 = None
                val1 = opnd1
            else:
                if registers[int(opnd1)][0] == None:
                    val1 = float(registers[int(opnd1)][1])
                else:
                    rs1 = registers[int(opnd1)][0]
                    val1 = None
        elif op == "LDR":
            opnd1 = float(re.findall(r'\d+[.]?\d*',str(nextInstr[2]))[0])
            #print(nextInstr[2],opnd1)
            if '#' in nextInstr[2]:
                rs1 = None
                val1 = opnd1
            else:
                if registers[int(opnd1)][0] == None:
                    val1 = float(registers[int(opnd1)][1])
                else:
                    rs1 = registers[int(opnd1)][0]
                    val1 = None
        else:
            opnd1 = float(re.findall(r'\d+[.]?\d*',nextInstr[2])[0])
            if '#' in nextInstr[2]:
                rs1 = None
                val1 = opnd1
            else:
                if registers[int(opnd1)][0] == None:
                    val1 = float(registers[int(opnd1)][1])
                else:
                    rs1 = registers[int(opnd1)][0]
                    val1 = None

            opnd2 = float(re.findall(r'\d+[.]?\d*',nextInstr[3])[0])
            if '#' in nextInstr[3]:
                rs2 = None
                val2 = opnd2
            else:
                if registers[int(opnd2)][0] == None:
                    val2 = float(registers[int(opnd2)][1])
                else:
                    rs2 = registers[int(opnd2)][0]
                    val2 = None

            if op not in ["FADD","FMUL","FSUB"]:
                if val1 != None:
                    val1 = int(val1)
                if val2 != None:
                    val2 = int(val2)

        # Update destination register
        registers[dst][0] = str("RS_"+rsName+"_"+str(freeRSIndx))

        # update instr table
        current_instrs.pop(0)
        if len(instructions) != 0:
            current_instrs.append(instructions[0])
            instructions.pop(0)

        # Update the particular entry of the RS Table
        entry = [op,rs1,rs2,val1,val2,None,1]
        #print(entry)

        # If issued
        if isIssued == 1:
            self.updateRegisterTable()
            self.updateInstrTable()
            self.updateRSTables(op = op,indx = freeRSIndx, entry = entry, rsName= rsName)

    def isRSFree(self, op):
        global RS
        global operations

        localRS = []
        rsName = ""
        if op in operations["ADD"]:
            localRS = RS["ADD"]
            rsName = "ADD"
        elif op in operations["MUL"]:
            localRS = RS["MUL"]
            rsName = "MUL"
        elif op in operations["FADD"]:
            localRS = RS["FADD"]
            rsName = "FADD"
        elif op in operations["FMUL"]:
            localRS = RS["FMUL"]
            rsName = "FMUL"
        elif op in operations["LU"]:
            localRS = RS["LU"]
            rsName = "LU"
        elif op in operations["LOAD"]:
            localRS = RS["LOAD"]
            rsName = "LOAD"

        for i in range(len(localRS)):
            # Check the busy flag of the all the RS of that op
            if localRS[i][-1] == 0:
                return [i,rsName]
        return [-1,""]

    def executeInstrs(self):
        global exec_cycles
        global exec_list
        global RS
        global exec_entries

        # Check all RS to see if any instr is ready to be executed
        
        # ADD RS
        localRS = RS["ADD"]
        for i in range(4):
            rsName = str("RS_ADD_"+str(i))
            if localRS[i][6] == 1 and rsName not in exec_list and localRS[i][1] == None and localRS[i][2] == None:
                exec_list.append(rsName)
                entry = [rsName,localRS[i][0],localRS[i][3],localRS[i][4],exec_cycles["ADD"]]
                exec_entries.append(entry)

        # MUL RS
        localRS = RS["MUL"]
        for i in range(2):
            rsName = str("RS_MUL_"+str(i))
            if localRS[i][6] == 1 and rsName not in exec_list and localRS[i][1] == None and localRS[i][2] == None:
                exec_list.append(rsName)
                entry = [rsName,localRS[i][0],localRS[i][3],localRS[i][4],exec_cycles["MUL"]]
                exec_entries.append(entry)

        # FADD RS
        localRS = RS["FADD"]
        for i in range(2):
            rsName = str("RS_FADD_"+str(i))
            if localRS[i][6] == 1 and rsName not in exec_list and localRS[i][1] == None and localRS[i][2] == None:
                exec_list.append(rsName)
                entry = [rsName,localRS[i][0],localRS[i][3],localRS[i][4],exec_cycles["FADD"]]
                exec_entries.append(entry)

        # FMUL RS
        localRS = RS["FMUL"]
        for i in range(2):
            rsName = str("RS_FMUL_"+str(i))
            if localRS[i][6] == 1 and rsName not in exec_list and localRS[i][1] == None and localRS[i][2] == None:
                exec_list.append(rsName)
                entry = [rsName,localRS[i][0],localRS[i][3],localRS[i][4],exec_cycles["FMUL"]]
                exec_entries.append(entry)

        # LU RS
        localRS = RS["LU"]
        for i in range(4):
            rsName = str("RS_LU_"+str(i))
            if localRS[i][6] == 1 and rsName not in exec_list and localRS[i][1] == None and localRS[i][2] == None:
                exec_list.append(rsName)
                entry = [rsName,localRS[i][0],localRS[i][3],localRS[i][4],exec_cycles["LU"]]
                exec_entries.append(entry)

        # LOAD RS
        localRS = RS["LOAD"]
        for i in range(2):
            rsName = str("RS_LOAD_"+str(i))
            if localRS[i][6] == 1 and rsName not in exec_list and localRS[i][1] == None:
                exec_list.append(rsName)
                entry = [rsName,localRS[i][0],localRS[i][3],localRS[i][4],exec_cycles["LOAD"]]
                exec_entries.append(entry)

        print(exec_entries)
  
        self.updateExistExec()
        pass

    def updateExistExec(self,):
        global exec_list
        global exec_entries
        global writeBack_list

        toDel = []
        for i in range(len(exec_entries)):
            exec_entries[i][4] -= 1
            if exec_entries[i][4] == 0:
                # Remove from both lists and append to writeBack list
                writeBack_list.append([exec_entries[i][0],self.solve(rsName = exec_entries[i][0],op = exec_entries[i][1],opnd1 = exec_entries[i][2], opnd2 = exec_entries[i][3])])
                toDel.insert(0,i)
        
        for i in toDel:
            exec_entries.pop(i)
            exec_list.pop(i)

        print("wb =",writeBack_list)

    def solve(self, rsName, op, opnd1, opnd2):
        op_category = rsName.split("_")[1]
        #print("Solve",op_category,op,opnd1,opnd2)

        if op_category == "ADD":
            if op == "ADDC":
                return opnd1 + opnd2 + 1
            elif op == "SUB":
                return opnd1 - opnd2
            elif op == "SUBB":
                return opnd1 - opnd2 + 1
            else:
                return opnd1 + opnd2
        elif op_category == "MUL":
            return opnd1 * opnd2
        elif op_category == "FADD":
            if op == "FSUB":
                return (opnd1 - opnd2)
            else:
                return (opnd1 + opnd2)
        elif op_category == "FMUL":
            return opnd1 * opnd2
        elif op_category == "LU":
            if op == "AND":
                return opnd1 & opnd2
            elif op == "OR":
                return opnd1 | opnd2
            elif op == "NAND":
                return ~(opnd1 & opnd2)
            elif op == "NOR":
                return ~(opnd1 | opnd2)
            elif op == "XOR":
                return opnd1 ^ opnd2
            elif op == "NOT":
                return ~opnd1
            else:
                return (~opnd1 + 1)
        else:
            return opnd1

    def writeBack(self):
        global writeBack_list
        global registers
        global RS

        for i in range(len(writeBack_list)):
            rsName = writeBack_list[i][0]

            # Update the register Buffer - destination
            for j in range(32):
                if registers[j][0] == rsName:
                    registers[j][0] = None
                    registers[j][1] = writeBack_list[i][1]
                    # Cant be more than one destination
                    break

            # Remove that entry from the RS Table
            _,op,indx = rsName.split("_")
            self.updateRSTables(op="",indx = int(indx), entry = ["", "", "", "", "", "", 0], rsName = op)

            #Update all RS - check for any dependecy and write in the value
            for key in RS.keys():
                opnd = writeBack_list[i][1]
                if key not in ["FADD","FSUB","FMUL"]:
                    opnd = int(opnd)
                for j in range(len(RS[key])):
                    if RS[key][j][1] == rsName:
                        entry = [RS[key][j][0],None , RS[key][j][2],opnd, RS[key][j][4], RS[key][j][5],RS[key][j][6]]
                        self.updateRSTables(op="",indx = j, entry = entry, rsName = key)
                    elif RS[key][j][1] == rsName:
                        entry = [RS[key][j][0],RS[key][j][1] ,None, RS[key][j][3], opnd, RS[key][j][5],RS[key][j][6]]
                        self.updateRSTables(op="",indx = j, entry = entry, rsName = key)

        writeBack_list = []
        self.updateRegisterTable()

        pass

        
    def updateRegisterTable(self,):
        global registers

        for i in range(len(registers)):
            entry = registers[i]
            self.registerTable.setItem(i,0,QtWidgets.QTableWidgetItem(str(entry[0])))
            self.registerTable.setItem(i,1,QtWidgets.QTableWidgetItem(str(entry[1])))

    def updateInstrTable(self, reset = 0):
        global current_instrs

        for i in range(5):
            entry = ""
            if i < len(current_instrs):
                entry = current_instrs[i][0] + " " + ", ".join(current_instrs[i][1:-1]) + ", "+ current_instrs[i][-1]+";"
            self.tableWidget.setItem(4-i, 0, QtWidgets.QTableWidgetItem(entry))

        if(reset == 1):
            for i in range(5):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(""))

    def updateRSTables(self, reset = 0, op = "", indx = -1, entry = [], rsName = ""):
        global RS

        if reset == 1:
            # Update RS ADD Table
            for i in range(4):
                for j in range(7):
                    self.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(RS["ADD"][i][j])))

            # Update RS MUL Table
            for i in range(2):
                for j in range(7):
                    self.tableWidget_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(RS["MUL"][i][j])))

            # Update RS FADD Table
            for i in range(2):
                for j in range(7):
                    self.tableWidget_5.setItem(i, j, QtWidgets.QTableWidgetItem(str(RS["FADD"][i][j])))

            # Update RS FMUL Table
            for i in range(2):
                for j in range(7):
                    self.tableWidget_7.setItem(i, j, QtWidgets.QTableWidgetItem(str(RS["FMUL"][i][j])))

            # Update RS LU Table
            for i in range(4):
                for j in range(7):
                    self.tableWidget_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(RS["LU"][i][j])))

            # Update RS LOAD Table
            for i in range(2):
                for j in range(7):
                    self.tableWidget_6.setItem(i, j, QtWidgets.QTableWidgetItem(str(RS["LOAD"][i][j])))

        else:
            RS[rsName][indx] = entry

            if rsName == "ADD":
                for j in range(7):
                    self.tableWidget_2.setItem(indx, j, QtWidgets.QTableWidgetItem(str(entry[j])))

            if rsName == "MUL":
                for j in range(7):
                    self.tableWidget_3.setItem(indx, j, QtWidgets.QTableWidgetItem(str(entry[j])))

            if rsName == "FADD":
                for j in range(7):
                    self.tableWidget_5.setItem(indx, j, QtWidgets.QTableWidgetItem(str(entry[j])))

            if rsName == "FMUL":
                for j in range(7):
                    self.tableWidget_7.setItem(indx, j, QtWidgets.QTableWidgetItem(str(entry[j])))

            if rsName == "LU":
                for j in range(7):
                    self.tableWidget_4.setItem(indx, j, QtWidgets.QTableWidgetItem(str(entry[j])))

            if rsName == "LOAD":
                for j in range(7):
                    self.tableWidget_6.setItem(indx, j, QtWidgets.QTableWidgetItem(str(entry[j])))


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Register View"))
        item = self.registerTable.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "R0"))
        item = self.registerTable.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "R1"))
        item = self.registerTable.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "R2"))
        item = self.registerTable.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "R3"))
        item = self.registerTable.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "R4"))
        item = self.registerTable.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "R5"))
        item = self.registerTable.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "R6"))
        item = self.registerTable.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "R7"))
        item = self.registerTable.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "R8"))
        item = self.registerTable.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "R9"))
        item = self.registerTable.verticalHeaderItem(10)
        item.setText(_translate("MainWindow", "R10"))
        item = self.registerTable.verticalHeaderItem(11)
        item.setText(_translate("MainWindow", "R11"))
        item = self.registerTable.verticalHeaderItem(12)
        item.setText(_translate("MainWindow", "R12"))
        item = self.registerTable.verticalHeaderItem(13)
        item.setText(_translate("MainWindow", "R13"))
        item = self.registerTable.verticalHeaderItem(14)
        item.setText(_translate("MainWindow", "R14"))
        item = self.registerTable.verticalHeaderItem(15)
        item.setText(_translate("MainWindow", "R15"))
        item = self.registerTable.verticalHeaderItem(16)
        item.setText(_translate("MainWindow", "R16"))
        item = self.registerTable.verticalHeaderItem(17)
        item.setText(_translate("MainWindow", "R17"))
        item = self.registerTable.verticalHeaderItem(18)
        item.setText(_translate("MainWindow", "R18"))
        item = self.registerTable.verticalHeaderItem(19)
        item.setText(_translate("MainWindow", "R19"))
        item = self.registerTable.verticalHeaderItem(20)
        item.setText(_translate("MainWindow", "R20"))
        item = self.registerTable.verticalHeaderItem(21)
        item.setText(_translate("MainWindow", "R21"))
        item = self.registerTable.verticalHeaderItem(22)
        item.setText(_translate("MainWindow", "R22"))
        item = self.registerTable.verticalHeaderItem(23)
        item.setText(_translate("MainWindow", "R23"))
        item = self.registerTable.verticalHeaderItem(24)
        item.setText(_translate("MainWindow", "R24"))
        item = self.registerTable.verticalHeaderItem(25)
        item.setText(_translate("MainWindow", "R25"))
        item = self.registerTable.verticalHeaderItem(26)
        item.setText(_translate("MainWindow", "R26"))
        item = self.registerTable.verticalHeaderItem(27)
        item.setText(_translate("MainWindow", "R27"))
        item = self.registerTable.verticalHeaderItem(28)
        item.setText(_translate("MainWindow", "R28"))
        item = self.registerTable.verticalHeaderItem(29)
        item.setText(_translate("MainWindow", "R29"))
        item = self.registerTable.verticalHeaderItem(30)
        item.setText(_translate("MainWindow", "R30"))
        item = self.registerTable.verticalHeaderItem(31)
        item.setText(_translate("MainWindow", "R31"))
        item = self.registerTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "RS"))
        item = self.registerTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Value"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Instruction Queue"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Instruction"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Reservation Stations"))
        self.groupBox_4.setTitle(_translate("MainWindow", "ADD"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RS1"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RS2"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val1"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Val2"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Imm Address"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Busy"))
        self.groupBox_5.setTitle(_translate("MainWindow", "MUL"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RS1"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RS2"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val1"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Val2"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Imm Address"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Busy"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Logical Unit"))
        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_4.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_4.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_4.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RS1"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RS2"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val1"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Val2"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Imm Address"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Busy"))
        self.groupBox_7.setTitle(_translate("MainWindow", "FADD"))
        item = self.tableWidget_5.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_5.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RS1"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RS2"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val1"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Val2"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Imm Address"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Busy"))
        self.groupBox_8.setTitle(_translate("MainWindow", "LOAD/STORE"))
        item = self.tableWidget_6.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_6.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RS1"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RS2"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val1"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Val2"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Imm Address"))
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Busy"))
        self.groupBox_9.setTitle(_translate("MainWindow", "FMUL"))
        item = self.tableWidget_7.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_7.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Operation"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "RS1"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "RS2"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Val1"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Val2"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Imm Address"))
        item = self.tableWidget_7.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Busy"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Status"))
        self.groupBox_11.setTitle(_translate("MainWindow", "Controls"))
        self.pushButton_3.setText(_translate("MainWindow", "Load File"))
        self.pushButton.setText(_translate("MainWindow", "Next Clock Cycle"))
        self.pushButton_2.setText(_translate("MainWindow", "Reset"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

