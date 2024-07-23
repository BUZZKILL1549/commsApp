from tkinter import *
from tkinter import ttk
from connect.connector import Connection

if __name__ == '__main__':
    connection = Connection()
    def update():
        commsRetriever = connection.retrieveComms()
        trv.delete(*trv.get_children())

        for retrievedComms in commsRetriever:
            trv.insert("", END, values = retrievedComms)
        root.after(1000, update)

    root = Tk()
    root.title("Comms")

    mainFrame = ttk.Frame(root)
    mainFrame.pack(padx = 20, pady = 20)

    trv = ttk.Treeview(mainFrame, selectmode = BROWSE)
    trv.pack(side = RIGHT)

    scrlbar = ttk.Scrollbar(mainFrame, orient = VERTICAL, command = trv.yview)
    scrlbar.pack(side = RIGHT, fill = Y)

    trv.configure(yscrollcommand = scrlbar.set)

    trv["columns"] = ("1", "2")
    trv['show'] = 'headings'

    trv.column("1", width = 200, anchor = 'c')
    trv.column("2", width = 400, anchor = 'w')
    
    trv.heading("1", text = "User")
    trv.heading("2", text = "Message")

    ttk.Label(mainFrame, text = "Enter username: ").pack(anchor = 'w')
    userBox = ttk.Entry(mainFrame)
    userBox.pack(pady = 10)
    ttk.Label(mainFrame, text = "Enter message: ").pack(anchor = 'w')
    msgBox = ttk.Entry(mainFrame)
    msgBox.pack(pady = 10)  
    ttk.Button(mainFrame, text = "Send", command = lambda: connection.sendComms(userBox.get(), msgBox.get())).pack()

    update()

    root.mainloop()