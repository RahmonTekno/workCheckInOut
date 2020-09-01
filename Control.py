from tkinter import *
from tkinter import ttk
import datetime
import  time
import DB_connector
from tkinter import messagebox

db =  DB_connector.db_connect()
ID=-1

root = Tk()
root.title("Pro_Timer")
root.geometry("930x240")
root.resizable(0,0)
style= ttk.Style()
style.configure("Treeview.Heading",font=(None,15))
style.configure("mystyle.Treeview",font=(None,12))

# fram1
frm1=ttk.Frame(root)
frm1.pack(padx=15,pady=15,side=RIGHT)
frm1.config(width=200,height=40,relief=RIDGE)
# fram2
frm2 =ttk.Frame(root)
frm2.pack(pady=15,side=BOTTOM)
frm2.config(width=200,height=50,relief=RIDGE)


But_in = ttk.Button(frm1, text="IN")
But_in.grid(row=1, column=0, pady=15, padx=15,sticky='snew')

But_out = ttk.Button(frm1, text="OUT")
But_out.grid(row=1, column=1, pady=15, padx=15,sticky='snew')
ttk.Label(frm1,text="Total hours:").grid(row=2,column=0,ipadx=10, ipady=20,pady=15, padx=10 ,sticky='snew')

tree1 = ttk.Treeview(frm2, style="mystyle.Treeview")
tree1.pack()
tree1.configure(columns=('Time_Out','Total'))
tree1.heading('#0', text="Time in",anchor=CENTER)
tree1.heading('Time_Out',text="Time Out")
tree1.heading('Total',text="Total")
tree1.column('#0',anchor=CENTER)
tree1.column('Time_Out',anchor=CENTER)
tree1.column('Total',width=150,anchor=CENTER)

cursor = db.View()
for row in cursor:
                tree1.insert('', 'end', '#{}'.format(row['ID']), text=row['Time_IN'])
                tree1.set('#{}'.format(row['ID']), 'Time_Out', row['Time_Out'])
                tree1.set('#{}'.format(row['ID']), 'Total', row['Total'])
                ID  = row['ID']
                print(ID)

def  check():
    global B
    global ID

    if tree1.exists('#{}'.format(ID)):

            for child in tree1.get_children():
                c=child

            if tree1.exists(c)==True:
                if len(tree1.item(c)["values"])==2:
                    print("len of child",len(tree1.item(c)["values"]))
                    print("child", tree1.item(c)["values"])
                    return True
                else:

                    print("len of child",len(tree1.item(c)["values"]) )
                    print("False")
                    return False
            else:
                    print ("True")
                    return True
    else:return True













def IN_Butt(event):
    global H1
    global M1
    global ID
        # a way to get time inbutt=datetime.datetime.time(datetime.datetime.now())
# if statement (row complete )


#inset db----------------------------

    if  check() is  True :
            Time = time.strftime("%Y-%m-%d    %H:%M")
            db.insert_in(Time)
            cursor = db.View()
            for row in cursor:
                r=row

            tree1.insert('', 'end', '#{}'.format(r['ID']), text=row['Time_IN'])
            ID = r['ID']
            print("ID len ",ID)

            messagebox.showinfo("Timer Insert", "The Tiem is requested ")
# sum up the time ------------------------
            H1 = time.strftime("%H")
            M1 = time.strftime("%M")

    else:
        messagebox.showinfo("Timer Insert", "Time is not OUT yet")

    But_out.configure(state=NORMAL)
    But_in.configure(state=DISABLED)




def OUT_Butt(event):
        global H1
        global M1

# extract from db ----------------------------
        if check() is True:
            messagebox.showinfo("Timer Insert", "Time OUT is not submitted yet")
        else:

# sum up the time ------------------------
            Time = time.strftime("%Y-%m-%d    %H:%M")
            But_in.configure(state=NORMAL)
            But_out.configure(state=DISABLED)
            H = time.strftime("%H")
            M = time.strftime("%M")
            s = str(int(H) - int(H1))
            s2 = str(int(M) - int(M1))
            Total = s, s2
            Total = ":".join(Total)
# insert to db ----------------------------



            print ("ID len ",ID)

            db.insert_Out(Time, Total,ID)
            cursor = db.View()
            for row in cursor:
                tree1.set('#{}'.format(ID), 'Time_Out',row['Time_Out'])
                tree1.set('#{}'.format(ID), 'Total', row['Total'])
            messagebox.showinfo("Timer Insert", "Time OUT is submitted ")

# TODO make the db to put the Time_Out and Total in same row of last Time_IN


But_out.bind('<ButtonPress>',OUT_Butt)
But_in.bind('<ButtonPress>', IN_Butt)
root.mainloop()