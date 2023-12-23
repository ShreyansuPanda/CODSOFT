#please downloaded all the images in the folder for perfect result
from tkinter import *

root = Tk()
root.title("To-Do-List")
root.geometry("400x650+400+100")
root.resizable(False, False)

task_lists = []


def addTask():
    task = task_entry.get()
    if task:
        with open("tasklist.txt", 'a') as taskfile:
            taskfile.write(f"{task}\n")
        task_lists.append(task)
        listbox.insert(END, task)
        task_entry.delete(0, END)


def deleteTask():
    task = str(listbox.get(ANCHOR))
    if task in task_lists:
        task_lists.remove(task)
        with open('tasklist.txt', 'w') as taskfile:
            for t in task_lists:
                taskfile.write(t + "\n")
        listbox.delete(ANCHOR)


def openTaskFile():
    try:
        global task_lists
        with open("tasklist.txt", "r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task.strip():
                task_lists.append(task.strip())
                listbox.insert(END, task.strip())
    except FileNotFoundError:
        file = open('tasklist.txt', 'w')
        file.close()


# icons
Img_icon = PhotoImage(file="Images/task.png")
root.iconphoto(False, Img_icon)

# topbar
TopImage = PhotoImage(file="Images/topbar.png")
Label(root, image=TopImage).pack()

dockImage = PhotoImage(file="Images/dock.png")
Label(root, image=dockImage, bg='#32405b').place(x=30, y=25)

noteImage = PhotoImage(file="Images/task.png")
Label(root, image=noteImage, bg='#32405b').place(x=340, y=25)

heading = Label(root, text=" Tasks", font='arial 20 bold', bg='#32405b', fg='white')
heading.place(x=130, y=20)

frame = Frame(root, width=400, height=50, bg='white')
frame.place(x=0, y=180)

task = StringVar()
task_entry = Entry(frame, width=20, font='arial 20', bd=0, textvariable=task)
task_entry.place(x=10, y=7)
task_entry.focus()

button = Button(frame, text='Add', font='arial 20 bold', fg='#fff', bd=0, bg='#5a95ff', command=addTask)
button.place(x=325, y=0)

frame1 = Frame(root, bd=3, width=700, height=280, bg="#32405b")
frame1.pack(pady=(160, 0))
listbox = Listbox(frame1, font=("arial", 12), width=40, height=16, bg="#32405b", fg="white", cursor="hand2",
                  selectbackground='#5a95ff')
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

Delete_icon = PhotoImage(file="Images/delete.png")
Button(root, image=Delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)

openTaskFile()

root.mainloop()
