from tkinter import *
root = Tk()

sizex = 1000
sizey = 800
root.wm_geometry("%dx%d" % (sizex, sizey))

def getNewProblem(number): # Store these arrays in database? Pick a random one?
    newProblem = [["4","2","",""],["","1","",""],["","","4",""],["","","3","1"]]
    answersForProblem = [["1","3"],["3","2","4"],["1","3","2"],["2","4"]]
    if number == 1:
        return(newProblem)
    else:
        return(answersForProblem)

def createGame(problemArray,answerArray):
    global numbersFrame,font,contentFrame
    row = 0
    column = 0
    entryBoxValues = []
    for i in range (0,len(problemArray)):
        for j in range (0,len(problemArray[i])):
            if problemArray[i][j] == "":
                entryBoxValues.append(StringVar())
                
                Entry(numbersFrame,font=font,textvariable=entryBoxValues[int(len(entryBoxValues)-1)],justify='center',width=3).grid(row=row,column=column)          
                
            elif problemArray[i][j] != "":
                #Label(numbersFrame,text = str(problemArray[i][j]),font=font).grid(row=row,column=column)
                e = Entry(numbersFrame,font=font,justify='center',width=3)
                e.insert(END, str(problemArray[i][j]))
                e.config(state='disabled')
                e.grid(row=row,column=column)
            column = column + 1

            if column == 4:
                row = row + 1
                column = 0

    Button(contentFrame,font=font,text="Check",command= lambda: checkAnswer(entryBoxValues,answerArray)).grid(row = 2,column = 0)

def checkAnswer(entryBoxValues,answerArray):
    global numbersFrame
    plainAnswers = []
    for i in range (0,len(entryBoxValues)):
        plainAnswers.append(entryBoxValues[i].get())

    stringOfPlainAnswers = ''.join(plainAnswers)

    stringOfAnswers = ""
    for i in range (0,len(answerArray)):
        for j in range (0,len(answerArray[i])):
            stringOfAnswers = str(stringOfAnswers) + str(answerArray[i][j])

    if stringOfPlainAnswers == stringOfAnswers:
        print("You Win")
        numbersFrame.destroy()
        main()
    else:
        print("Wrong - Try Again")


def main():
    global numbersFrame,font,contentFrame


    contentFrame = Frame(root)
    contentFrame.grid(row=0,column=0)

    font = ("Helvetica", 20)

    titleFrame = Frame(contentFrame)
    titleFrame.grid(row = 0,column=0)

    title = Label(contentFrame,text = "Welcome To Soduku",font=font)
    title.grid(row=0,column=0)

    numbersFrame = Frame(contentFrame)
    numbersFrame.grid(row=1,column=0)
    
    createGame(getNewProblem(1),getNewProblem(2))
    
    root.title("Suduku 2.0")
    root.mainloop()

main()


            
    
