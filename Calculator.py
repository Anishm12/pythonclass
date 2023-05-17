import customtkinter as ctk

currentText = '0'
num = 0
op = ''

def calculate():
    global currentText
    global num
    global op

    currentNum = float(currentText)
    result = 0
    if op == '+':
        result = num + currentNum
    if op == '-':
        result = num - currentNum
    if op == '*':
        result = num * currentNum
    if op == '/':
        result = num / currentNum



    num = result
    currentText = str(result)
    updateText()

def operation(str):
    global currentText
    global num
    global op
    if op == '':
        num = float(currentText)
        currentText = '0'
    else:
        calculate()

    if str == '=':
        op = ''
    else:
        op = str
        currentText = '0'

def plus_minus():
    global  currentText
    if '-' in currentText:
        currentText = currentText[1:]
    else:
        currentText = '-' + currentText
    updateText()

def Back():
    global currentText
    currentText = currentText[0:len(currentText)-1]
    if len(currentText) == 0:
        currentText = '0'
    updateText()

def CE():
    global currentText
    global num
    global op
    currentText = '0'
    num = 0
    op = ''
    updateText()

def updateText():
    global currentText
    if len(currentText) > 12:
        currentText = currentText[:12]


    ctkLabel.configure(text=currentText)

def addText(str):
    global currentText
    if float(currentText) == 0 and str != '.' and '.' not in currentText:
        currentText = ''
    if '.' in currentText and str == '.':
        return

    updateText()

    currentText = currentText + str
    ctkLabel.configure(text=currentText)

app = ctk.CTk()
app.geometry('350x500')
app.title('calculator')
app.configure(bg_color='white', fg_color='white')

calcFrame = ctk.CTkFrame(app, width= 340, height=100, bg_color='white')
calcFrame.grid(row=0, column=0, padx = 5, pady = 5)

ctkLabel = ctk.CTkLabel(calcFrame, width=340, height=100, anchor='e', text='0', font=ctk.CTkFont(size=45), padx = 5, bg_color='white')
ctkLabel.grid(row=0, column=0)


btnFrame = ctk.CTkFrame(app, width=340, height=390, bg_color='white')
btnFrame.grid(row=1, column=0, padx=5, pady=5)

btnCE = ctk.CTkButton(btnFrame, width=85, height=70, text='CE', font=ctk.CTkFont(size=40), fg_color='gray', command=CE)
btnCE.grid(row=0, column=0, padx=2, pady=2)

btnSquared = ctk.CTkButton(btnFrame, width=85, height=70, text = '%', font=ctk.CTkFont(size=40), fg_color='gray', command=lambda : operation('%'))
btnSquared.grid(row=0, column=1, padx=2, pady=2)

btnBack = ctk.CTkButton(btnFrame, width=85, height=70, text = '<--', font=ctk.CTkFont(size=40), fg_color='gray', command=Back)
btnBack.grid(row=0, column=2, padx=2, pady=2)

btnDivide = ctk.CTkButton(btnFrame, width=75, height=70, text = '/', font=ctk.CTkFont(size=40), fg_color='gray', command=lambda : operation('/'))
btnDivide.grid(row=0, column=3, padx=2, pady=2)

btnSeven = ctk.CTkButton(btnFrame, width=85, height=70, text = '7', font=ctk.CTkFont(size=40), command=lambda: addText('7'))
btnSeven.grid(row=1, column=0, padx=2, pady=2)

btnEight = ctk.CTkButton(btnFrame, width=85, height=70, text = '8', font=ctk.CTkFont(size=40), command=lambda: addText('8'))
btnEight.grid(row=1, column=1, padx=2, pady=2)

btnNine = ctk.CTkButton(btnFrame, width=85, height=70, text = '9', font=ctk.CTkFont(size=40), command=lambda: addText('9'))
btnNine.grid(row=1, column=2, padx=2, pady=2)

btnMulti = ctk.CTkButton(btnFrame, width=75, height=70, text = 'X', font=ctk.CTkFont(size=40), fg_color='gray', command=lambda : operation('*'))
btnMulti.grid(row=1, column=3, padx=2, pady=2)

btnFour = ctk.CTkButton(btnFrame, width=85, height=70, text = '4', font=ctk.CTkFont(size=40), command=lambda: addText('4'))
btnFour.grid(row=2, column=0, padx=2, pady=2)

btnFive = ctk.CTkButton(btnFrame, width=85, height=70, text = '5', font=ctk.CTkFont(size=40), command=lambda: addText('5'))
btnFive.grid(row=2, column=1, padx=2, pady=2)

btnSix = ctk.CTkButton(btnFrame, width=85, height=70, text = '6', font=ctk.CTkFont(size=40), command=lambda: addText('6'))
btnSix.grid(row=2, column=2, padx=2, pady=2)

btnMinus = ctk.CTkButton(btnFrame, width=75, height=70, text = '-', font=ctk.CTkFont(size=40), fg_color='gray', command=lambda : operation('-'))
btnMinus.grid(row=2, column=3, padx=2, pady=2)

btnOne = ctk.CTkButton(btnFrame, width=85, height=70, text = '1', font=ctk.CTkFont(size=40), command=lambda: addText('1'))
btnOne.grid(row=3, column=0, padx=2, pady=2)

btnTwo = ctk.CTkButton(btnFrame, width=85, height=70, text='2', font=ctk.CTkFont(size=40), command=lambda: addText('2'))
btnTwo.grid(row=3, column=1, padx=2, pady=2)

btnThree = ctk.CTkButton(btnFrame, width=85, height=70, text = '3', font=ctk.CTkFont(size=40), command=lambda: addText('3'))
btnThree.grid(row=3, column=2, padx=2, pady=2)

btnPlus = ctk.CTkButton(btnFrame, width=75, height=70, text = '+', font=ctk.CTkFont(size=40), fg_color='gray', command=lambda : operation('+'))
btnPlus.grid(row=3, column=3, padx=2, pady=2)

btnPM = ctk.CTkButton(btnFrame, width=85, height=70, text = '+/-', font=ctk.CTkFont(size=40), command=plus_minus)
btnPM.grid(row=4, column=0, padx=2, pady=2)

btnZero = ctk.CTkButton(btnFrame, width=85, height=70, text = '0', font=ctk.CTkFont(size=40), command=lambda: addText('0'))
btnZero.grid(row=4, column=1, padx=2, pady=2)

btnDot = ctk.CTkButton(btnFrame, width=85, height=70, text = '.', font=ctk.CTkFont(size=40), command=lambda : addText('.'))
btnDot.grid(row=4, column=2, padx=2, pady=2)

btnEqual = ctk.CTkButton(btnFrame, width=75, height=70, text = '=', font=ctk.CTkFont(size=40), fg_color='gray', command=lambda : operation('='))
btnEqual.grid(row=4, column=3, padx=2, pady=2)



app.mainloop()
