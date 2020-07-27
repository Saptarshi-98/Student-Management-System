# ----------------Button functions -------------------
# -------------------Add function -----------------
def add():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions',
                                            'Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,
                                                                                                                  name),
                                            parent=addroot)
            if (res == True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','Id already exists try another Id...',parent=addroot)
        strr = "select * from studentdata1"
        mycursor.execute(strr)
        # our values were displayed in tuples format
        datas = mycursor.fetchall()
        # now we need to take this data and show them in the tabular format
        # we will clean the data first then add the new data or same data will show multiple times:
        # it will access everything with the star and gets all children that means all the datas
        studenttable.delete(* studenttable.get_children())
        for i in datas:
            # we will use a list to store all the values inside the treeview
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            # now we will store them in the table on show data frame
            studenttable.insert("",END,values=vv)



    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.config(bg="black")
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False, False)
    addroot.title("Add Student Details")
    # --------------------- Add Student Details Labels ----------------

    # --------------------- 1. ID -------------------------------------
    idlabel = Label(addroot, text="Enter ID", bg="grey", font=("Times",20,"bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    idlabel.place(x=10, y=10)

    # ----------------------- 2. Name ----------------------------------
    namelabel = Label(addroot, text="Full Name", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    namelabel.place(x=10, y=70)

    # ----------------------- 3. Mobile -------------------------------
    mobilelabel = Label(addroot, text="Mobile Number ", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(addroot, text="Email ID", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    emaillabel.place(x=10, y=190)

    addresslabel = Label(addroot, text="Address", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    addresslabel.place(x=10, y=250)

    genderlabel = Label(addroot, text="Gender", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    genderlabel.place(x=10, y=310)

    doblabel = Label(addroot, text="D.O.B", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    doblabel.place(x=10, y=370)


    # --------------------------------Add Student Entry-----------------------------------------

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(addroot, font=("roman", 15, "bold"), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    # -------------------------------- Submit BUTTON -------------------------
    sbtbtn = Button(addroot, text="Submit", font=("Roman", 15, "bold"), anchor="n",
                      activeforeground="white", activebackground="blue", width=20, bd=5, command=submitadd)
    sbtbtn.place(x=150, y=420)

    addroot.mainloop()

# ----------------Button functions -------------------
# ------------------- Search function -----------------
def searchstudent():
    def search():
        id = idval.get()
        # name = nameval.get()
        # mobile = mobileval.get()
        # email = emailval.get()
        # address = addressval.get()
        # gender = genderval.get()
        # dob = dobval.get()
        # addeddate = time.strftime("%d/%m/%Y")

        if (id != " "):
            strr = "select * from studentdata1 where id=%s"
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            # we need to delete the previously searched data or else it will show multiple data that are searched.
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                # we will use a list to store all the values inside the treeview or table
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                # now we will store them in the table on show data frame
                studenttable.insert("", END, values=vv)
        # elif name != " ":
        #     strr = "select * from studentdata1 where name=%s"
        #     mycursor.execute(strr, (name))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)
        # elif mobile != " ":
        #     strr = "select * from studentdata1 where monile=%s"
        #     mycursor.execute(strr, (mobile))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)
        # elif email != " ":
        #     strr = "select * from studentdata1 where email=%s"
        #     mycursor.execute(strr, (email))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)
        # elif address != " ":
        #     strr = "select * from studentdata1 where address=%s"
        #     mycursor.execute(strr, (address))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)
        # elif gender != " ":
        #     strr = "select * from studentdata1 where gender=%s"
        #     mycursor.execute(strr, (gender))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)
        # elif dob != " ":
        #     strr = "select * from studentdata1 where dob=%s"
        #     mycursor.execute(strr, (dob))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)
        # elif addeddate != " ":
        #     strr = "select * from studentdata1 where date=%s"
        #     mycursor.execute(strr, (addeddate))
        #     datas = mycursor.fetchall()
        #     # we need to delete the previously searched data or else it will show multiple data that are searched.
        #     studenttable.delete(*studenttable.get_children())
        #     for i in datas:
        #         # we will use a list to store all the values inside the treeview or table
        #         vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        #         # now we will store them in the table on show data frame
        #         studenttable.insert("", END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x160+220+160')
    searchroot.config(bg="firebrick1")
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False, False)
    searchroot.title("Search for Student Record")
    # --------------------- Add Student Details Labels ----------------

    # --------------------- 1. ID -------------------------------------
    idlabel = Label(searchroot, text="Enter ID", bg="grey", font=("Times",20,"bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    idlabel.place(x=10, y=10)

    # ----------------------- 2. Name ----------------------------------
    # namelabel = Label(searchroot, text="Full Name", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # namelabel.place(x=10, y=70)
    #
    # # ----------------------- 3. Mobile -------------------------------
    # mobilelabel = Label(searchroot, text="Mobile Number ", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # mobilelabel.place(x=10, y=130)
    #
    # emaillabel = Label(searchroot, text="Email ID", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # emaillabel.place(x=10, y=190)
    #
    # addresslabel = Label(searchroot, text="Address", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # addresslabel.place(x=10, y=250)
    #
    # genderlabel = Label(searchroot, text="Gender", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # genderlabel.place(x=10, y=310)
    #
    # doblabel = Label(searchroot, text="D.O.B", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # doblabel.place(x=10, y=370)
    #
    # datelabel = Label(searchroot, text="Date", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
    #                 width=12, anchor="w")
    # datelabel.place(x=10, y=430)

    # --------------------------------Add Student Entry-----------------------------------------

    idval = StringVar()
    # nameval = StringVar()
    # mobileval = StringVar()
    # emailval = StringVar()
    # addressval = StringVar()
    # genderval = StringVar()
    # dobval = StringVar()
    # dateval = StringVar()

    identry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=idval)
    identry.place(x=250, y=10)
    #
    # nameentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=nameval)
    # nameentry.place(x=250, y=70)
    #
    # mobileentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=mobileval)
    # mobileentry.place(x=250, y=130)
    #
    # emailentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=emailval)
    # emailentry.place(x=250, y=190)
    #
    # addressentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=addressval)
    # addressentry.place(x=250, y=250)
    #
    # genderentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=genderval)
    # genderentry.place(x=250, y=310)
    #
    # dobentry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=dobval)
    # dobentry.place(x=250, y=370)
    #
    # date_entry = Entry(searchroot, font=("roman", 15, "bold"), bd=5, textvariable=dateval)
    # date_entry.place(x=250, y=430)

    # -------------------------------- Submit BUTTON -------------------------
    searchbtn = Button(searchroot, text="Submit", font=("Roman", 15, "bold"), anchor="n",
                      activeforeground="white", activebackground="blue", width=20, bd=5, command=search)
    searchbtn.place(x=150, y=80)

    searchroot.mainloop()
def delete():
    # we have a foucs function in treeview which helps us to find where we have clicked in the show data frame
    cc = studenttable.focus()               # it will give the place into cc
    content = studenttable.item(cc)         # it will give all the contents of that place into content
    # now we will use id to delete the data of that row as id is the primary key
    # so we need to store the id inside a variable
    pp = content["values"][0]               # this stores the key and on zeroe th index we have ID
    strr = "delete from studentdata1 where id=%s"
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo("Notification", "Id {} deleted successfully....".format(pp))

    # now we need to update the tree view and then show it else it will not reflect it directly after deleting any record
    # after deleting we will fetch all the data again, which won't have the data that has been deleted
    strr = "select * from studentdata1"
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    # we need to delete the previously searched data or else it will show multiple data that are searched.
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        # we will use a list to store all the values inside the treeview or table
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        # now we will store them in the table on show data frame
        studenttable.insert("", END, values=vv)

def update():
    def updating():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = "update studentdata1 set name=%s, monile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s"
        mycursor.execute(strr, (name, mobile, email, address, gender, dob, date, time, id))
        con.commit()
        messagebox.showinfo("Notification", "Id {} updated successfully".format(id),parent=updateroot)
        # now we need to update the tree view and then show it else it will not reflect it directly after deleting any record
        # after deleting we will fetch all the data again, which won't have the data that has been deleted
        strr = "select * from studentdata1"
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        # we need to delete the previously searched data or else it will show multiple data that are searched.
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            # we will use a list to store all the values inside the treeview or table
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            # now we will store them in the table on show data frame
            studenttable.insert("", END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+200')
    updateroot.config(bg="firebrick4")
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False, False)
    updateroot.title("Update Student Details")
    # --------------------- Add Student Details Labels ----------------

    # --------------------- 1. ID -------------------------------------
    idlabel = Label(updateroot, text="Enter ID", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                    width=12, anchor="w")
    idlabel.place(x=10, y=10)

    # ----------------------- 2. Name ----------------------------------
    namelabel = Label(updateroot, text="Full Name", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                      width=12, anchor="w")
    namelabel.place(x=10, y=70)

    # ----------------------- 3. Mobile -------------------------------
    mobilelabel = Label(updateroot, text="Mobile Number ", bg="grey", font=("Times", 20, "bold"), borderwidth=3,
                        relief=GROOVE,
                        width=12, anchor="w")
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text="Email ID", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                       width=12, anchor="w")
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text="Address", bg="grey", font=("Times", 20, "bold"), borderwidth=3,
                         relief=GROOVE,
                         width=12, anchor="w")
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text="Gender", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                        width=12, anchor="w")
    genderlabel.place(x=10, y=310)

    doblabel = Label(updateroot, text="D.O.B", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                     width=12, anchor="w")
    doblabel.place(x=10, y=370)

    datelabel = Label(updateroot, text="Date", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                      width=12, anchor="w")
    datelabel.place(x=10, y=430)

    timelabel = Label(updateroot, text="Time", bg="grey", font=("Times", 20, "bold"), borderwidth=3, relief=GROOVE,
                      width=12, anchor="w")
    timelabel.place(x=10, y=430)

    # --------------------------------Add Student Entry-----------------------------------------

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=idval)
    identry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    dobentry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=dobval)
    dobentry.place(x=250, y=370)

    date_entry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=dateval)
    date_entry.place(x=250, y=430)

    time_entry = Entry(updateroot, font=("roman", 15, "bold"), bd=5, textvariable=timeval)
    time_entry.place(x=250, y=430)

    # -------------------------------- Submit BUTTON -------------------------
    updatebtn = Button(updateroot, text="Submit", font=("Roman", 15, "bold"), anchor="n",
                       activeforeground="black", activebackground="pink", width=20, bd=5, command=updating)
    updatebtn.place(x=150, y=520)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content["values"]
    if (len(pp) != 0):

        # this will just place all the values in the respective entry field of the record which we have accessed
        # or clicked on.
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])



    updateroot.mainloop()
def show():
   # to show all the data
    strr = "select * from studentdata1"
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    # we need to delete the previously searched data or else it will show multiple data that are searched.
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        # we will use a list to store all the values inside the treeview or table
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        # now we will store them in the table on show data frame
        studenttable.insert("", END, values=vv)
def export():
    ff = filedialog.asksaveasfilename()             # this will give us the path where we are saving the file
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addedate,addedtime = [],[],[],[],[],[],[],[],[]

    # we have all the data in gg from studentdatable
    # this data will be in list form
    for i in gg:
        content = studenttable.item(i)              # we will access all the data from i
        pp = content["values"]
        id.append(pp[0]), name.append(pp[1]), mobile.append(pp[2]), email.append(pp[3]), address.append(pp[4]), gender.append(pp[5]),
        dob.append(pp[6]), addedate.append(pp[7]), addedtime.append(pp[8])
    # to show the field in any file: for heading
    dd = ["ID", "Name", "Mobile no.", "Email ID", "Address", "Gender", "D.O.B", "Added Date", "Added Time"]

    # we are taking all the values together from the list and appending them inside the data frame
    df = pandas.DataFrame(list(zip( id,name,mobile,email,address,gender,dob,addedate,addedtime)), columns=dd)
    # csv = comma seperated values
    paths = r"{}.csv".format(ff)
    # now we have to save it
    df.to_csv(paths, index=False)
    messagebox.showinfo("Notification", "Student Data is saved {}".format(paths))



def exit():
    result = messagebox.askyesnocancel("Notification", "Do you want to exit")
    if result == True:
        root.destroy()



# --------------------connect to database-------------------------------------------------------------
def Connect_db():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        # host = "localhost"
        # user = "root"
        # password = "Saptarshi@98"

        # ---------- this try and except block is used to check, ----------------------------
        # if the credentials entered by the user is right or wrong----------------------------
        try:
            con = pymysql.connect(host=host, user=user, password=password)
           # we need a cursor, this is a handler it is required by default
           # we will now use this cursor to do the whole work
            mycursor = con.cursor()
        except:
            messagebox.showerror("Notification", "Invalid Credentials Entered please try again!!", parent=dbroot)
            return

        # ---- when it will be ready to be installed in other persons' system, the creation of database will occur
        # automatic and there will no need to create a database by writing SQL commands for that particular user
        try:
            # ---------------------- firing queries -----------------------------------
            strr = "create database studentmanagementsystem1"
            mycursor.execute(strr)           # this will execute str and our database will be created
            strr = "use studentmanagementsystem1"
            mycursor.execute(strr)          # this will allow the user to use the database
            # ------------- now we need to create fields inside the table ----------------------------------------------
            strr = "create table studentdata1(id int, name varchar(30), mobile varchar(20), email varchar(30), address varchar(100),gender varchar(5), dob varchar(20), date varchar(20), time varchar(20))"
            mycursor.execute(strr)
            # now we will make the id field a primary key and also it cannot be null
            strr = "alter table studentdata1 modify column id int not null"
            mycursor.execute(strr)
            strr = "alter table studentdata1 modify column id int primary key"
            mycursor.execute(strr)
            messagebox.showinfo("Notification", "Database created successfully and you are connected to the Database", parent=dbroot)


        # if the databasse is already created tables are already prepared we need not have to do it once again
        # so we will come to the except block and use the database directly
        except:
            strr = "use studentmanagementsystem1"
            mycursor.execute(strr)
            messagebox.showinfo("Notification", "Now you are connected to Database", parent=dbroot)
        # if none of the try except works we will destroy the database
        dbroot.destroy()


    # database root (window created)
    dbroot = Toplevel()
    # this function does not allow to perform action second time, and also if we don't use this function, we could
    # face problems like, suppose we click on any other place on the window the previously opened window will go to
    # background or gets minimized if we are doing it without closing the previous window
    # that has already been opened earlier
    dbroot.grab_set()
    # now we need to add label, button, etc...
    # width * height of the GUI, we also need to add some extra arguments,
    # so that it always opens up at the same position on the screen and here, height = 250 pixel and width = 470 pixel
    # and axis x = 800 and y = 230
    dbroot.geometry('470x250+800+230')
    # for inserting icon
    dbroot.iconbitmap("mana.ico")
    # we also need to make sure that no one should be able to change the height and width of the window by themselves
    # if we pass the parameters as true to any of them it becomes changeable
    dbroot.resizable(False, False)
    dbroot.config(bg="sky blue")

    # ----------------------- Connect to DB Labels---------------------------------------------------------------
    idlabel= Label(dbroot, text= "Enter Host: ", font=("Times", 20, 'bold'), relief=GROOVE, borderwidth=3, width=13,
                   bg='Black', fg='White', anchor="w")
    idlabel.place(x=10, y=10)

    userlabel = Label(dbroot, text="Enter User: ", font=("Times", 20, 'bold'), relief=GROOVE, borderwidth=3,
                      width=13, bg='Black', fg='White', anchor="w")
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text="Enter Password: ", font=("Times", 20, 'bold'), relief=GROOVE, borderwidth=3,
                          width=13, bg='Black', fg='White', anchor="w")
    passwordlabel.place(x=10, y=130)

    # --------------------------Connect to DB Entry-----------------------------------------------------
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

    # ------------------------connectDB submit button---------------------------------------------
    submitbutton = Button(dbroot, text="Submit", font=("Roman", 15, "bold"), width=20, activebackground="blue",
                          activeforeground="white", command=submitdb)
    submitbutton.place(x=150, y=190)

    # to make the screen stay forever otherwise the screen will just appear and vanish
    dbroot.mainloop()
# this function is for the clock
def tick():
    time_string = time.strftime("%H:%M:%S")     # this strftime() function is used to place the current time
    date_string = time.strftime("%d-%m-%y")
    clock.config(text='Date:' + date_string + "\n" + "Time:" + time_string)
    clock.after(200, tick)
# this function is used to insert the letters to the label one by one
def intro_label_tick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ""
        SliderLabel.config(text=text)
    else:
        text = text + ss[count]                 # stores letter in the text variable one after another simultaneously
        SliderLabel.config(text=text)
        count = count+1
    SliderLabel.after(170,intro_label_tick)     # after() function is used to automatically call the function after
                                                # a given period of time (in this case it's 100 microsecond)
# we need to import tkinter to make the frames or GUI
from tkinter import *
# to get a top level window
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
# we need to build a time module
import time

# Root catches the screen and we need to initialise Tk()
root = Tk()
# To display the title
root.title("Student Database Management System")
# to give the background colour
root.config(bg='Grey')
# width * height of the GUI wc also need to add some extra arguments,
# so that it always opens up at the same position on the screen and here, height = 700 pixel and width = 1174 pixel
# and axis x = 200 and y = 50
root.geometry('1174x700+200+50')
# to insert a icon for your database
root.iconbitmap('mana.ico')
# we also need to make sure that no one should be able to change the height and width of the window by themselves
# if we pass the parameters as true to any of them it becomes changeable
root.resizable(False, False)

# -----------------------------------FRAMES-----------------------------------------------------------------------
# now we need to design 5 frames inside the root
# -----------1st frame for adding entering data---------
DataEntryFrame = Frame(root, bg='pink', relief=GROOVE, borderwidth=5)
# now we need to place this inside the root
DataEntryFrame.place(x=10, y=80, width=510, height=600)

# --------------------Data entry frame intro-----------------------------------
# we will show options at the top for this we will use pack() function which eventually move it to the top
# as we go on adding buttons in the data enrty frame
frontlabel = Label(DataEntryFrame, text="MENU", bg='green', width=30, font=("Arial", 22, "bold"),fg="black")
frontlabel.pack(side=TOP, expand=True)
# -----------------------------buttons-----------------------------------------------------------------------

# -------------------------------1. ADD -----------------------
addbtn = Button(DataEntryFrame, text="1. Add Student", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w",command=add)
addbtn.pack(side=TOP, expand=True)

# -------------------------------2. SEARCH-----------------------
searchbtn = Button(DataEntryFrame, text="2. Search Student", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w",
                command=searchstudent)
searchbtn.pack(side=TOP, expand=True)

# --------------------------------3. Delete ----------------------
deletebtn = Button(DataEntryFrame, text="3. Delete Student", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w", command= delete)
deletebtn.pack(side=TOP, expand=True)

# ---------------------------------4. Update ------------------------
updatebtn = Button(DataEntryFrame, text="4. Update Student", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w", command= update)
updatebtn.pack(side=TOP, expand=True)

# --------------------------------5. Show all ------------------------
showbtn = Button(DataEntryFrame, text="5. Show All", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w", command=show)
showbtn.pack(side=TOP, expand=True)

# --------------------------------6. Export Data ---------------------
exportbtn = Button(DataEntryFrame, text="6. Export Data", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w", command= export)
exportbtn.pack(side=TOP, expand=True)

# -----------------------------------7. Exit button ---------------------
exitbtn = Button(DataEntryFrame, text="7. Exit", width=18, font=("Arial", 19, "bold"), bd=6,relief=RIDGE,
              fg="Blue", bg="sky blue", activebackground="White", activeforeground="Blue", anchor="w", command= exit)
exitbtn.pack(side=TOP, expand=True)

# ----------------2nd Frame for showing data------------------------------------
ShowDataFrame = Frame(root, bg='Sky blue', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=550, y=80, width=615, height=600)

# ----------------- Show Data Frame --------------------------------------

# -------------------Style ------------
style = ttk.Style()                 # here Style() is an attribute of ttk and ttk is a module of tkinter
style.configure("Treeview.Heading", font=("Helvetica", 18, "bold"), fg="Black", bg="Grey")
style.configure("Treeview", font=("Times", 15, "bold"), fg="Black", bg="sky blue")
# --------------- scroll ------------------------
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)

studenttable = Treeview(ShowDataFrame,column=("ID", "Name", "Mobile No.", "Email ID", "Address", "Gender",
                                              "D.O.B", "Added Date", "Added Time"),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading("ID", text="ID")
studenttable.heading("Name", text="Name")
studenttable.heading("Mobile No.", text="Mobile No.")
studenttable.heading("Email ID", text="Email ID")
studenttable.heading("Address", text="Address")
studenttable.heading("Gender", text="Gender")
studenttable.heading("D.O.B", text="D.O.B")
studenttable.heading("Added Date", text="Added Date")
studenttable.heading("Added Time", text="Added Time")

# ------------------- to show the heading listed above only ---------------
studenttable["show"]= "headings"

# ---------------- SIZE of each column -------------
studenttable.column("ID", width=100)
studenttable.column("Name", width=200)
studenttable.column("Mobile No.", width=200)
studenttable.column("Email ID", width=300)
studenttable.column("Address", width=200)
studenttable.column("Gender", width=100)
studenttable.column("D.O.B", width=150)
studenttable.column("Added Date", width=150)
studenttable.column("Added Time", width=150)

studenttable.pack(fill=BOTH, expand=1)

# -------------------------------------SLIDER---------------------------------------------------------------------
ss = "Welcome to Student Management System"
count = 0
text = ""
# First we need to make the label
SliderLabel = Label(root, text=ss, font=("Arial", 20, 'bold'), relief=RIDGE, borderwidth=4, width=33, bg='Brown',
                    fg="Sky Blue")
SliderLabel.place(x=260, y=0)
intro_label_tick()

# -------------------------------------CLOCK----------------------------------------------------------------------
clock = Label(root, font=("Times", 15, 'bold'), relief=RIDGE, borderwidth=4, bg='cyan')
clock.place(x=10, y=0)
tick()

# ---------------------------------------CONNECT TO DATABASE BUTTON------------------------------------------------
ConnectButton = Button(root, text="Connect to Database", width=20, fg="white", bg="black", font=("Arial", 15, "bold"),
                       borderwidth=3, relief=RIDGE, activebackground='white', activeforeground='black',
                       command=Connect_db)
ConnectButton.place(x=910, y=0)
# to make the screen stay forever otherwise the screen will just appear and vanish
root.mainloop()