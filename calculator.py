from tkinter import *

def btnClick(numbers):
    global operator, text_Input
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClearDisplay():
    global operator, text_Input
    operator = ""
    text_Input.set("")

def btnEqualsInput():
    global operator, text_Input
    try:
        sumup=str(eval(operator))
        text_Input.set(sumup)
        operator = ""
    except (ValueError, ZeroDivisionError,SyntaxError):
        text_Input.set("Error")
        operator = ""

def set_up_first_row():
    global cal
    btn7= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange",  font=("arial", 15, 'bold'),
                 text="7", command=lambda:btnClick(7)).grid(row=1, column=0)
    btn8= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="8", command=lambda:btnClick(8)).grid(row=1, column=1)
    btn9= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="9", command=lambda:btnClick(9)).grid(row=1, column=2)
    addition= Button(cal, padx=22, pady=6, bd=8, fg="white",bg="black", font=("arial", 15, 'bold'),
                 text="+",command=lambda:btnClick("+")).grid(row=1, column=3)

def set_up_second_row():
    global cal
    btn4= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="4", command=lambda:btnClick(4)).grid(row=2, column=0)
    btn5= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange",  font=("arial", 15, 'bold'),
                 text="5", command=lambda:btnClick(5)).grid(row=2, column=1)
    btn6= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="6", command=lambda:btnClick(6)).grid(row=2, column=2)
    subtraction= Button(cal, padx=22, pady=6, bd=8, fg="white",bg="black", font=("arial", 15, 'bold'),
                 text="-",command=lambda:btnClick("-")).grid(row=2, column=3)

def set_up_third_row():
    global cal
    btn1= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="1",command=lambda:btnClick(1)).grid(row=3, column=0)
    btn2= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange",  font=("arial", 15, 'bold'),
                 text="2", command=lambda:btnClick(2)).grid(row=3, column=1)
    btn3= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="3",command=lambda:btnClick(3)).grid(row=3, column=2)
    multiple= Button(cal, padx=22, pady=6, bd=8, fg="white", bg="black", font=("arial", 15, 'bold'),
                 text="*",command=lambda:btnClick("*")).grid(row=3, column=3)

def set_up_fourth_row():
    global cal
    btn0= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="0",command=lambda:btnClick(0)).grid(row=4, column=1)
    btnClear= Button(cal, padx=22, pady=6, bd=8, fg="black",bg="red",  font=("arial", 15, 'bold'),
                 text="C",command=btnClearDisplay).grid(row=4, column=0)
    btnEquals= Button(cal, padx=22, pady=6, bd=8, fg="black", bg="orange", font=("arial", 15, 'bold'),
                 text="=",command = btnEqualsInput).grid(row=4, column=2)
    Division= Button(cal, padx=22, pady=6, bd=8, fg="white",bg="black", font=("arial", 15, 'bold'),
                 text="/",command=lambda:btnClick("/")).grid(row=4, column=3)
    
    
def set_up_display():
    global operator, text_Input, cal
    cal= Tk()
    cal.title("Calculator")
    
    operator=""
    text_Input=StringVar()

    textDisplay= Entry(cal, font=("arial", 20, 'bold'), textvariable=text_Input, bd=10, insertwidth=4,
                       bg="white", justify="right").grid(columnspan = 4)
    set_up_first_row()
    set_up_second_row()
    set_up_third_row()
    set_up_fourth_row()
    cal.mainloop()
    

if __name__ == "__main__":
    set_up_display()

    
          
