from tkinter import *
from PIL import Image, ImageTk
import random
#pls use the images in the folder for the
#window
root =Tk()
root.title("Rock Paper Scissors")
root.configure(background="light blue")

#Image
rock_img=ImageTk.PhotoImage(Image.open("rock_user.png"))
scissor_img=ImageTk.PhotoImage(Image.open("scissor_user.png"))
paper_img=ImageTk.PhotoImage(Image.open("paper_user.png"))
rock_img_comp=ImageTk.PhotoImage(Image.open("rock.png"))
scissor_img_comp=ImageTk.PhotoImage(Image.open("scissor.png"))
paper_img_comp=ImageTk.PhotoImage(Image.open("paper.png"))

#insert_img
user_label=Label(root,image=scissor_img,bg="light blue")
comp_label=Label(root,image=scissor_img_comp,bg="light blue")
comp_label.grid(row=1,column=4)
user_label.grid(row=1,column=0)

# Reset function
def reset_game():
    playerscore['text'] = 0
    computerscore['text'] = 0
    msg['text'] = ""
    user_label.configure(image=None)
    comp_label.configure(image=None)

# Reset button
reset_button = Button(root, text="Reset", fg="black", bg="orange", command=reset_game)
reset_button.grid(row=4, column=1, columnspan=3)


#score
playerscore=Label(root,text=0,font=100,bg="light blue",fg="Black")
computerscore=Label(root,text=0,font=100,bg="light blue",fg="black")
computerscore.grid(row=1,column=3)
playerscore.grid(row=1,column=1)

#updatescore
def updateuserscore():
    score=int(playerscore['text'])
    score+=1
    playerscore['text']=str(score)
def updatecompscore():
    score_com=int(computerscore['text'])
    score_com+=1
    computerscore['text']=str(score_com)

#indicators
user_indicator=Label(root,font=50,text="Computer",bg="light blue",fg="black")
user_indicator.grid(row=0,column=3)
comp_indicator=Label(root,font=50,text="User",bg="light blue",fg="black")
comp_indicator.grid(row=0,column=1)

#message
msg=Label(root,font=(50),bg="light blue",fg="black")
msg.grid(row=3,column=2)

#updatedmsg
def updatedmsg(x):
    msg['text']=x

#choice
choice=['rock','paper','scissor']
def updatechocie(x):
    #comp choice
    compchoice=random.choice(choice)
    if compchoice=="rock":
        comp_label.configure(image=rock_img_comp)
    elif compchoice=="paper":
        comp_label.configure(image=paper_img_comp)
    else:
        comp_label.configure(image=scissor_img_comp)

    #user choice
    if x=="rock":
        user_label.configure(image=rock_img)
    elif x=="paper":
        user_label.configure(image=paper_img)
    else:
        user_label.configure(image=scissor_img)
    win(x,compchoice)

#button
rock=Button(root,text="Rock",height=3,width=20,fg="Black",bg="#FF3E4D",command=lambda:updatechocie("rock"))
rock.grid(row=2,column=1)
paper=Button(root,text="Paper",fg="black",height=3,width=20,bg="Green",command=lambda:updatechocie("paper"))
paper.grid(row=2,column=2)
scissor=Button(root,text="Scissor",fg="black",height=3,width=20,bg="Yellow",command=lambda:updatechocie("scissor"))
scissor.grid(row=2,column=3)

#checkwinner
def win(player,computer):
    if player==computer:
        updatedmsg("Its a Tie")
    elif player=="rock":
        if computer=="paper":
            updatedmsg("Computer Wins!!")
            updatecompscore()
        else:
            updatedmsg("User Wins!!")
            updateuserscore()
    elif player=="paper":
        if computer=="scissor":
            updatedmsg("Computer Wins!!")
            updatecompscore()
        else:
            updatedmsg("User Wins!!")
            updateuserscore()
    elif player=="scissor":
        if computer=="rock":
            updatedmsg("Computer Wins!!")
            updatecompscore()
        else:
            updatedmsg("User Wins!!")
            updateuserscore()
    else:
        pass


root.mainloop()




