import tkinter as tk
import mysql.connector as mysql
from tkinter import ttk
from random import *
from tkinter import messagebox
import pickle
from PIL import ImageTk, Image  

def login():
    
    def sb1():
        name=passentry1.get()
        age2=age1.get()
        fa=fentry1.get()
        ma=mentry1.get()
        ea=eentry1.get()
        cr=centry1.get()
        yr=yentry1.get()
        oc=oentry1.get()
        ad=adentry1.get()
        disa=disentry1.get()
        mar=dobentry1.get()
        try:
            myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
            mycur=myconn.cursor()
            mycur.execute('select * from prisoner')
            rs=mycur.fetchall()
            if rs==[]:
                pid='P001'
            
            elif int(rs[-1][0][1:])<9:
                pid='P00'+str(int(rs[-1][0][1:])+1)
            else:
                pid='P0'+str(int(rs[-1][0][1:])+1)

            for i in rs:
                if i[1]==name:
                    break
            else:
                
                cellno=randint(1,100)
                mycur.execute('insert into prisoner values ("{}","{}",{},"{}","{}",{},"{}","{}","{}","{}","{}","{}","{}","{}",{})'.format(pid,name,int(age2),ad,cr,float(yr),oc,fa,ma,ea,gen,disa,mar,cellno,float(yr)*365))
                myconn.commit()
                messagebox.showinfo('ALERT!!','The assigned cell no is '+str(cellno))
        except EOFError as e:
            print(e)
    
    def sel1():
        global gen
        gen='M'
    def sel2():
        global gen
        gen='F'
    def sel3():
        global gen
        gen='O'
    '''global root1
    root1=tk.Tk()
    var1=tk.IntVar()
    root1.geometry('830x740')
    root1.title('Prisoner REGISTRATION')
    label = tk.Label(root1,text='PRISONER\'S REGISTRATION',fg='black',width=40,height=0,font=('Times New Roman',24))
    label.place(x=-140,y=0)
    labeluser=tk.Label(root1,text='Name',fg='black',width=10,height=0,font=('Times New Roman',14))
    labeluser.place(x=0,y=100)
    global passentry1
    passentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    passentry1.place(x=350,y=100)
    submitpg2=tk.Button(root1,text='Submit',width=10,height=2,command=sb1)
    submitpg2.place(x=700,y=580)
    backbtn=tk.Button(root1,text='Go to Home Page',width=20,height=2)
    backbtn.place(x=460,y=580)

    gender=tk.Label(root1,text='Gender:',fg='black',width=10,height=0,font=('Times New Roman',14))
    gender.place(x=10,y=140)
    global genderm
    genderm = tk.Radiobutton(root1,text='Male',variable=var1,value=1,font=("Times New Roman", 14),command=sel1)
    genderm.pack()
    genderm.place(x=230,y=140,width=100)
    global genderf
    genderf=tk.Radiobutton(root1,text='Female',variable=var1,value=2,font=('Times New Roman',14),command=sel2)
    genderf.pack()
    genderf.place(x=410,y=140,width=120)
    global age1
    age=tk.Label(root1,text='Age:',fg='black',width=50,height=0,font=('Times New Roman',14))
    age.place(x=-274,y=180)
    age1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    age1.place(x=350,y=180)
    global fentry1
    Father=tk.Label(root1,text="Father's Name:",fg='black',width=50,height=0,font=('Times New Roman',14))
    Father.place(x=-254,y=220)
    fentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    fentry1.place(x=350,y=220)
    global mentry1
    Mother=tk.Label(root1,text="Mother's Name:",fg='black',width=50,height=0,font=('Times New Roman',14))
    Mother.place(x=-244,y=260)
    mentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    mentry1.place(x=350,y=260)
    global eentry1
    ede=tk.Label(root1,text="Educational bg",fg='black',width=50,height=0,font=('Times New Roman',14))
    ede.place(x=-294,y=300)
    eentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    eentry1.place(x=350,y=300)
    global centry1
    crime=tk.Label(root1,text="Crime",fg='black',width=50,height=0,font=('Times New Roman',14))
    crime.place(x=-254,y=340)
    centry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    centry1.place(x=350,y=340)
    global yentry1
    year=tk.Label(root1,text="Year",fg='black',width=50,height=0,font=('Times New Roman',14))
    year.place(x=-264,y=380)
    yentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    yentry1.place(x=350,y=380)
    cate=tk.Label(root1,text="Occupation",fg='black',width=50,height=0,font=('Times New Roman',14))
    cate.place(x=-284,y=420)
    global oentry1
    oentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    oentry1.place(x=350,y=420)
    city=tk.Label(root1,text="Address",fg='black',width=50,height=0,font=('Times New Roman',14))
    city.place(x=-304,y=480)
    global adentry1
    adentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    adentry1.place(x=350,y=480)
    global disentry1
    dis=tk.Label(root1,text="Disabilities:",fg='black',width=50,height=0,font=('Times New Roman',14))
    dis.place(x=-304,y=520)
    disentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    disentry1.place(x=350,y=520)
    global dobentry1
    dob=tk.Label(root1,text="Marital status:",fg='black',width=50,height=0,font=('Times New Roman',14))
    dob.place(x=-264,y=560)
    dobentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    dobentry1.place(x=350,y=560)'''
    
    global root1
    root1=tk.Tk()
    var1=tk.IntVar()
    root1.geometry('1180x740')
    root1.title('Prisoner REGISTRATION')
    label = tk.Label(root1,text='PRISONER\'S REGISTRATION',fg='white',width=40,height=0,bg="brown",font=('Times New Roman',24,'bold underline'))
    label.pack()
    labeluser=tk.Label(root1,text='Name',fg='white',width=15,height=0,bg="red",font=('Times New Roman',14))
    labeluser.place(x=150,y=100)
    global passentry1
    passentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    passentry1.place(x=550,y=100)
    submitpg2=tk.Button(root1,text='Submit',width=10,height=2,command=sb1)
    submitpg2.place(x=1000,y=650)


    gender=tk.Label(root1,text='Gender:',fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    gender.place(x=150,y=140)
    global genderm
    genderm = tk.Radiobutton(root1,text='Male',variable=var1,value=1,font=("Times New Roman", 14),command=sel1)
    genderm.pack()
    genderm.place(x=430,y=140,width=100)
    global genderf
    genderf=tk.Radiobutton(root1,text='Female',variable=var1,value=2,font=('Times New Roman',14),command=sel2)
    genderf.pack()
    genderf.place(x=690,y=140,width=120)
    global gendero
    gendero=tk.Radiobutton(root1,text='Others',variable=var1,value=2,font=('Times New Roman',14),command=sel3)
    gendero.pack()
    gendero.place(x=920,y=140,width=120)
    global age1
    age=tk.Label(root1,text='Age:',fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    age.place(x=150,y=180)
    age1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    age1.place(x=550,y=180)
    global fentry1
    Father=tk.Label(root1,text="Father's Name:",fg="white",width=15,bg="red",height=0,font=('Times New Roman',14))
    Father.place(x=150,y=220)
    fentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    fentry1.place(x=550,y=220)
    global mentry1
    Mother=tk.Label(root1,text="Mother's Name:",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    Mother.place(x=150,y=260)
    mentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    mentry1.place(x=550,y=260)
    global eentry1
    ede=tk.Label(root1,text="Educatoinal bg",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    ede.place(x=150,y=300)
    eentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    eentry1.place(x=550,y=300)
    global centry1
    crime=tk.Label(root1,text="Crime",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    crime.place(x=150,y=340)
    centry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    centry1.place(x=550,y=340)
    global yentry1
    year=tk.Label(root1,text="Year",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    year.place(x=150,y=380)
    yentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    yentry1.place(x=550,y=380)
    cate=tk.Label(root1,text="Occupation",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    cate.place(x=150,y=420)
    global oentry1
    oentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    oentry1.place(x=550,y=420)
    city=tk.Label(root1,text="Address",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    city.place(x=150,y=480)
    global adentry1
    adentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    adentry1.place(x=550,y=480)
    global disentry1
    dis=tk.Label(root1,text="Disabilities:",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    dis.place(x=150,y=520)
    disentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    disentry1.place(x=550,y=520)
    global dobentry1
    dob=tk.Label(root1,text="Marital status:",fg="white",width=15,height=0,bg="red",font=('Times New Roman',14))
    dob.place(x=150,y=560)
    dobentry1= tk.Entry(root1,fg="black", width=10,font=("Times New Roman Bold", 10))
    dobentry1.place(x=550,y=560)
    root1.configure(bg="brown")
       


def lo(tkwin):
    tkwin.quit()

def submit():
    opt=tk.Tk()
    opt.geometry('2000x2000')
    pri=tk.Label(opt,text='Prisoner ID:',font=(25))
    pri.place(x=100,y=100)
    pid=tk.Entry(opt,width=8)
    pid.place(x=230,y=107)
    lab1=tk.Label(opt,text='OR',font=(35))
    lab1.place(x=100,y=170)
    cellno=tk.Label(opt,text='Cell Number:',font=(25))
    cellno.place(x=100,y=250)
    cent=tk.Entry(opt,width=3)
    cent.place(x=230,y=255)
    enter=tk.Button(opt,text='Submit',height=1,width=5,command=prison)
    enter.place(x=100,y=400)


def view(n):
    
    def daily():
        #bs=[]
        global sum1
        sum1=0

        def Add():
            global s
            s=sum1+s
            #global bs
            #bs.append(s)
            root7.destroy()

        def exception():
            global root8
            root8=tk.Tk()
            root8.geometry('1000x1000')
            root8.title('Exceptions')
            global sum1
            
            def add():
                global sum1
                sum1= int((e12.get()).strip() or 0)+int((e22.get()).strip() or 0)+int((e32.get()).strip() or 0)+int((e42.get()).strip() or 0)+int((e52.get()).strip() or 0) 

            def subm():
                root8.destroy()
            
            e11 = tk.Entry(root8,fg="black", width=20,font=("Times New Roman Bold", 10)).place(x=50, y=30)
            e12 = tk.Entry(root8)
            e12.place(x=200, y=30)
                
            e21 = tk.Entry(root8,fg="black", width=20,font=("Times New Roman Bold", 10)).place(x=50, y=90)
            e22 = tk.Entry(root8)
            e22.place(x=200, y=90)
            
            e31 = tk.Entry(root8,fg="black", width=20,font=("Times New Roman Bold", 10)).place(x=50, y=150)
            e32 = tk.Entry(root8)
            e32.place(x=200, y=150)
            
            e41 = tk.Entry(root8,fg="black", width=20,font=("Times New Roman Bold", 10)).place(x=50, y=210)
            e42 = tk.Entry(root8)
            e42.place(x=200, y=210)
            
            e51 =tk.Entry(root8,fg="black", width=20,font=("Times New Roman Bold", 10)).place(x=50, y=270)
            e52 =tk.Entry(root8)
            e52.place(x=200, y=270)
            subt=tk.Button(root8,text='Add',width=10,font=('Times New Roman',18), command=add)
            subt.place(x=400,y=500)
            
            sub=tk.Button(root8,text='Close',width=10,font=('Times New Roman',18), command=subm)
            sub.place(x=400,y=600)
        global root7
        root7=tk.Tk()
        var1=tk.IntVar()
        var2=tk.IntVar()
        var3=tk.IntVar()
        var4=tk.IntVar()
        var5=tk.IntVar()

        root7.geometry('1000x1000')
        root7.title('Everyday Entry')
        global s
        s=0
        def fin():
            global s
            s+=1
        label = tk.Label(root7,text='1. Prison-hold Chores',fg='black',width=40,height=0,font=('Times New Roman',10))
        label.place(x=0,y=30)

        b1=tk.Radiobutton(root7,variable=var1,value=1,font=('Times New Roman',10),command=fin)
        b1.place(x=350,y=30)
        label1 = tk.Label(root7,text='2. Kitchen Chores',fg='black',width=40,height=0,font=('Times New Roman',10))
        label1.place(x=0,y=90)

        b3=tk.Radiobutton(root7,variable=var2,value=1,font=('Times New Roman',10),command=fin)
        b3.place(x=350,y=90)
        label3 = tk.Label(root7,text='3. Library/ Reading',fg='black',width=40,height=0,font=('Times New Roman',10))
        label3.place(x=0,y=150)
        b5=tk.Radiobutton(root7,variable=var3,value=1,font=('Times New Roman',10),command=fin)
        b5.place(x=350,y=150)
        label4 = tk.Label(root7,text='4. Family Visits',fg='black',width=40,height=0,font=('Times New Roman',10))
        label4.place(x=0,y=210)
        b7=tk.Radiobutton(root7,variable=var4,value=1,font=('Times New Roman',10),command=fin)
        b7.place(x=350,y=210)
        label5=tk.Label(root7,text='5. Psychiatrist Visit in the week',fg='black',width=40,height=0,font=('Times New Roman',10))
        label5.place(x=0,y=270)
        b9=tk.Radiobutton(root7,variable=var5,value=1,font=('Times New Roman',10),command=fin)
        b9.place(x=350,y=270)
        exe=tk.Button(root7,text='Exceptions',width=10,font=('Times New Roman',15), command=exception)
        exe.place(x=100,y=360)
        sub=tk.Button(root7,text='Add',width=10,font=('Times New Roman',18), command=Add)
        sub.place(x=500,y=500)
        
    
    def graph():
        import matplotlib.pyplot as plt
        
        #from binary file
        global xt
#         xt=0
        # corresponding y axis values
         #list frm binary file
        global yt
#         
#         yt=0
        y1=s
        
        import pickle
        f=open(n+'.dat','wb')
        global x
        global y
        try:
            pickle.dump([x,y],f)
            
        except UnboundLocalError as e:
            
            x=[]
            y=[]
            xt=0
            yt=0
        except NameError as e:
            
            x=[]
            y=[]
            xt=0
            yt=0
        except EOFError as e:
            print(e)
                
        f.close()
        f=open(n+'.dat','rb')

        try:
            l=pickle.load(f)
            x=l[0]
            y=l[1]
            if x==[] and y==[]:

                x.append(0)
                y.append(0)
        except EOFError as e:
            print()

        f.close()

        if x!=[] and y!=[]:
            if y1==5:
                xt+=1
                yt+=1
                x.append(xt)
                y.append(yt)
                plt.plot(x, y,color='red',marker='o',markersize=4,linewidth=1)

            if y1>5:
                xt+=1
                yt+=1+(y1-5)
                x.append(xt)
                y.append(yt)
                plt.plot(x,y,color='red',marker='o',markersize=4,linewidth=1)

            if y1<5:
                xt+=1
                yt-=(5-y1)
                x.append(xt)
                y.append(yt)
                plt.plot(x,y,color='red',marker='o',markersize=4,linewidth=1) 

        
        # naming the x axis
        plt.xlabel('Days')
        # naming the y axis
        plt.ylabel('Points')
          
        # giving a title to my graph
        plt.title('Behavioral Graph')
          
        # function to show the plot
        plt.show()
    
    def routine():
        lst=['sweeping','reading','outdoor','miscellane','cooking','family','psychiatri']
        lst1=list(range(1,10))
        try:
            myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
            mycur=myconn.cursor()
            mycur.execute('select pid from prisoner')
            rs=mycur.fetchall()
            mycur.execute('show tables')
            rs1=mycur.fetchall()
            for i in rs:
                for j in rs1:
                    c=i[0][0].lower()+i[0][1:]
                    if c == j[0]:
                        mycur.execute('select * from '+c)
                        rs2=mycur.fetchall()

                        if rs2==[]:
                            for k in range(7):
                                mycur.execute('insert into '+i[0]+' values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)],lst[randint(0,6)]))
                                myconn.commit()

                        break

                else:
                    mycur.execute('create table '+i[0]+' (7_8 char(10),8_9 char(10),9_10 char(10),10_11 char(10),12_1 char(10),1_2 char(10),2_3 char(10),5_6 char(10),6_7 char(10),7_8pm char(10))')
                    
                                          
        except EOFError as e:
                print(e)
        root = tk.Tk()
        root.geometry('2000x2000')
        root.title('ROUTINE OF PRISONER')
        label=tk.Label(root,text='Routine of Prisoner',fg='black',bg='SteelBlue1',font=('Algerian',25,'bold underline'))
        label.grid(row=0,column=5)


        class Table:
             
            def __init__(self,root):
                 
                # code for creating table
                for i in range(total_rows):
                    for j in range(total_columns):
                         
                        self.e = tk.Entry(root, width=10, fg='black', bg='#BAE5E2',
                                       font=('Courier ',12,'bold'))
                         
                        self.e.grid(row=i+150, column=j)
                        self.e.insert(tk.END, lst[i][j])
        root.configure(bg='SteelBlue1')
        # take the data
        mycur.execute('select * from '+n)
        rs2=mycur.fetchall()
        lst = [('     ',' 7-8AM',' 8-9AM ',' 9-10AM ',' 10-11AM ',' 12-1pm ',' 1.15-2PM ',' 2-3PM ',' 5-6PM ',' 6-7PM ',' 7-8PM '),
               ('Mon',rs2[0][0].capitalize(),rs2[0][1].capitalize(),rs2[0][2].capitalize(),rs2[0][3].capitalize(),rs2[0][4].capitalize(),rs2[0][5].capitalize(),rs2[0][6].capitalize(),rs2[0][7].capitalize(),rs2[0][8].capitalize(),rs2[0][9].capitalize()),
               ('Tues',rs2[1][0].capitalize(),rs2[1][1].capitalize(),rs2[1][2].capitalize(),rs2[1][3].capitalize(),rs2[1][4].capitalize(),rs2[1][5].capitalize(),rs2[1][6].capitalize(),rs2[1][7].capitalize(),rs2[1][8].capitalize(),rs2[1][9].capitalize()),
               ('Wed',rs2[2][0].capitalize(),rs2[2][1].capitalize(),rs2[2][2].capitalize(),rs2[2][3].capitalize(),rs2[2][4].capitalize(),rs2[2][5].capitalize(),rs2[2][6].capitalize(),rs2[2][7].capitalize(),rs2[2][8].capitalize(),rs2[2][9].capitalize()),
               ('Thurs',rs2[3][0].capitalize(),rs2[3][1].capitalize(),rs2[3][2].capitalize(),rs2[3][3].capitalize(),rs2[3][4].capitalize(),rs2[3][5].capitalize(),rs2[3][6].capitalize(),rs2[3][7].capitalize(),rs2[3][8].capitalize(),rs2[3][9].capitalize()),
               ('Fri',rs2[4][0].capitalize(),rs2[4][1].capitalize(),rs2[4][2].capitalize(),rs2[4][3].capitalize(),rs2[4][4].capitalize(),rs2[4][5].capitalize(),rs2[4][6].capitalize(),rs2[4][7].capitalize(),rs2[4][8].capitalize(),rs2[4][9].capitalize()),
               ('Sat',rs2[5][0].capitalize(),rs2[5][1].capitalize(),rs2[5][2].capitalize(),rs2[5][3].capitalize(),rs2[5][4].capitalize(),rs2[5][5].capitalize(),rs2[5][6].capitalize(),rs2[5][7].capitalize(),rs2[5][8].capitalize(),rs2[5][9].capitalize()),
               ('Sun',rs2[6][0].capitalize(),rs2[6][1].capitalize(),rs2[6][2].capitalize(),rs2[6][3].capitalize(),rs2[6][4].capitalize(),rs2[6][5].capitalize(),rs2[6][6].capitalize(),rs2[6][7].capitalize(),rs2[6][8].capitalize(),rs2[6][9].capitalize())]
        total_rows = len(lst)
        total_columns = len(lst[0])
          
        # create root window

        t = Table(root)
    
    views=tk.Tk()
    views.configure(bg="black")
    don=tk.Label(views,text="PRISONERS RECORD",font=('Times New Roman Bold',30),bg="white").pack()
    views.geometry('970x750')
    enter0=tk.Button(views,text='Behavioral Graph',height=5,width=20,font=('Times',12,'bold italic'),command=graph)
    enter0.place(x=80,y=250)
    enter1=tk.Button(views,text='Daily Routine',height=5,width=20,font=('Times',12,'bold italic'),command=routine)
    enter1.place(x=680,y=250)
    enter2=tk.Button(views,text='Daily Entry',height=5,width=20,font=('Times',12,'bold italic'),command=daily)
    enter2.place(x=385,y=450)
    global s
    global sum1
    global bs
    s=0
    sum1=0
    bs=[]

def prison(n):
    global sub
    sub=tk.Toplevel()
    sub.geometry('2000x2000')
    sub.configure(bg="#CCD2CC")
    scrollbar = tk.Scrollbar(sub)
    scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
    try:
        myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
        mycur=myconn.cursor()
        mycur.execute('select * from prisoner')
        rs=mycur.fetchall()
        label1=tk.Label(sub,text='Welcome: '+name1,fg='black',font=('Arial',20))
        label1.place(x=50,y=50)
        
        label=tk.Label(sub,text=' PRISONER DETAILS',fg='black',font=('Arial',17,'bold underline'))
        label.place(x=100,y=130)
        
        for rs1 in rs:
            if rs1[0]==n:
                lb1=tk.Label(sub,text='Prisoner ID:'+rs1[0],fg='black',font=('Arial',12))
                lb1.place(x=200,y=200)
                lb2=tk.Label(sub,text='Name: '+rs1[1],font=('Arial',12))
                lb2.place(x=200,y=250)
                lb3=tk.Label(sub,text='Cell Number: '+str(rs1[-2]),font=('Arial',12))
                lb3.place(x=200,y=300)
                lb4=tk.Label(sub,text='Crime: '+rs1[4],font=('Arial',12))
                lb4.place(x=200,y=350)
                lb5=tk.Label(sub,text='Address:'+rs1[3],fg='black',font=('Arial',12))
                lb5.place(x=200,y=400)
                lb6=tk.Label(sub,text='Disabilities: '+rs1[-4],font=('Arial',12))
                lb6.place(x=200,y=450)
                lb7=tk.Label(sub,text='Marital Status: '+rs1[-3],font=('Arial',12))
                lb7.place(x=200,y=500)
                lb8=tk.Label(sub,text='Sentence: '+str(rs1[5])+' Years',font=('Arial',12))
                lb8.place(x=200,y=550)
                lb9=tk.Label(sub,text='Remaining: '+str(round(rs1[-1]/365,2))+' Years',font=('Arial',12))
                lb9.place(x=200,y=600)
                import py_avataaars as pa
                import random as r
                def e(n):
                    a=r.choice(list(n))
                    return(a)
                
                import os
                def view3():
                    
                    view(n)
                def plac():
                    global img
                    img = ImageTk.PhotoImage(Image.open('avatar'+rs1[0]+'.png'))
                    label = tk.Button(sub, image = img,command=view3)
                    label.place(x=1100,y=200)
                for x in os.listdir():
                    if x.endswith('avatar'+rs1[0]+'.png'):
                        plac()
                        break
                else:
                    avatar = pa.PyAvataaar(
                    style=pa.AvatarStyle.CIRCLE,
                    skin_color=e(pa.SkinColor),
                    hair_color=e(pa.HairColor),
                    facial_hair_type=e(pa.FacialHairType),
                    facial_hair_color=e(pa.HairColor),
                    top_type=e(pa.TopType),
                    hat_color=e(pa.Color),
                    mouth_type=e(pa.MouthType),
                    eye_type=e(pa.EyesType),
                    eyebrow_type=e(pa.EyebrowType),
                    nose_type=e(pa.NoseType),
                    accessories_type=e(pa.AccessoriesType),
                    clothe_type=e(pa.ClotheType),
                    clothe_color=e(pa.Color),
                    clothe_graphic_type=e(pa.ClotheGraphicType),
                    )
                    avatar.render_png_file('avatar'+rs1[0]+'.png')
                    plac()
                
        logout=tk.Button(sub,text='Logout',width=9,height=1,font=(17),command=lo1)
        logout.place(x=1700,y=0)
    except EOFError as e:
        print(e)
    label1=tk.Label(sub,text='Welcome: '+name1,fg='black',font=('Arial',20))
    label1.place(x=50,y=50)
    


def prison1(n):
    global sub1
    sub1=tk.Toplevel()
    sub1.geometry('1700x1000')
    sub1.configure(bg="#CCD2CC")
    scrollbar = tk.Scrollbar(sub1)
    scrollbar.pack( side = tk.RIGHT, fill = tk.Y )
    try:
        myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
        mycur=myconn.cursor()
        mycur.execute('select * from prisoner')
        rs=mycur.fetchall()
        label1=tk.Label(sub1,text='Welcome: '+name1,fg='black',font=(20))
        label1.place(x=50,y=50)
        
        label=tk.Label(sub1,text=' PRISONER DETAILS',fg='black',font=(20))
        label.place(x=100,y=100)
        y1=270
        a=150
        imgs=[]
        def view1():
            view(imgs[0][6:-4])
        def view2():
            view(imgs[1][6:-4])
        for rs1 in rs:
            if rs1[-2]==int(n):
                lb1=tk.Label(sub1,text='Prisoner ID:'+rs1[0],fg='black',font=(19))
                
                lb1.place(x=200,y=a)
                lb2=tk.Label(sub1,text='Name: '+rs1[1],font=(19))
                lb2.place(x=200,y=a+50)
                lb3=tk.Label(sub1,text='Cell Number: '+str(rs1[-2]),font=(19))
                lb3.place(x=200,y=a+100)
                lb4=tk.Label(sub1,text='Crime: '+rs1[4],font=(19))
                lb4.place(x=200,y=a+150)
                
                '''view1=tk.Button(sub1,text='View',width=5,height=1,font=(17),command=view)
                view1.place(x=200,y=a+200)'''
                a+=y1

                import py_avataaars as pa
                import random as r
                def e(n):
                    a=r.choice(list(n))
                    return(a)
                import os
                
                for x in os.listdir():
                    if x.endswith('avatar'+rs1[0]+'.png'):
                        
                        imgs.append('avatar'+rs1[0]+'.png')
                        break
                else:
                    avatar = pa.PyAvataaar(
                    style=pa.AvatarStyle.CIRCLE,
                    skin_color=e(pa.SkinColor),
                    hair_color=e(pa.HairColor),
                    facial_hair_type=e(pa.FacialHairType),
                    facial_hair_color=e(pa.HairColor),
                    top_type=e(pa.TopType),
                    hat_color=e(pa.Color),
                    mouth_type=e(pa.MouthType),
                    eye_type=e(pa.EyesType),
                    eyebrow_type=e(pa.EyebrowType),
                    nose_type=e(pa.NoseType),
                    accessories_type=e(pa.AccessoriesType),
                    clothe_type=e(pa.ClotheType),
                    clothe_color=e(pa.Color),
                    clothe_graphic_type=e(pa.ClotheGraphicType),
                    )
                    avatar.render_png_file('avatar'+rs1[0]+'.png')
                    imgs.append('avatar'+rs1[0]+'.png')
        def plac(n):
                global img
                img = ImageTk.PhotoImage(Image.open(imgs[0]))
                label = tk.Button(sub1, image = img,command=view1)
                label.place(x=1100,y=100)
                global img1
                img1 = ImageTk.PhotoImage(Image.open(imgs[1]))
                label1 = tk.Button(sub1, image = img1,command=view2)
                label1.place(x=1100,y=470)
                
        plac(imgs)
        logout=tk.Button(sub1,text='Logout',width=9,height=1,font=(17),command=lo1 )
        logout.place(x=1100,y=0)
    except EOFError as e:
        print(e)

    
def lo():
    tkwin.quit()
def lo1():
    sub.destroy()
    
    
def passive():
    
    
    try:
        myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
        mycur=myconn.cursor()
        query='select * from passive'
        mycur.execute(query)
        rs=mycur.fetchall()
        entries=[]
        count=190
        if rs==[]:
            messagebox.showinfo('ALERT','No Records found')
        else:
            tkwin=tk.Tk()
            tkwin.geometry('1200x600')
            tkwin.configure(bg='#E2D1F9')
            label4=tk.Label(tkwin,text='PRISONER LOG', fg='black',bg='#E2D1F9',font=('Times New Roman',25,'bold underline')).place(x=400,y=0)
            header_label1 = tk.Label(tkwin,text='NAME',fg='white',bg='#317773',width=15,height=0,font=('Times New Roman',11))
            header_label1.place(x=0,y=150)
            header_label2 = tk.Label(tkwin,text='AGE',fg='white',bg='#317773',width=15,height=0,font=('Times New Roman',11))
            header_label2.place(x=235,y=150)
            header_label3 = tk.Label(tkwin,text='Address',fg='white',bg='#317773',width=15,height=0,font=('Times New Roman',11))
            header_label3.place(x=470,y=150)
            header_label4 = tk.Label(tkwin,text='Crime',fg='white',bg='#317773',width=15,height=0,font=('Times New Roman',11))
            header_label4.place(x=705,y=150)
            header_label5 = tk.Label(tkwin,text='Occupation',fg='white',bg='#317773',width=15,height=0,font=('Times New Roman',11))
            header_label5.place(x=940,y=150)
            for record in rs:
                lst=[str(record[1]),str(record[2]),str(record[3]),str(record[4]),str(record[6])]
                entries += [lst]
            for i in range(len(entries)):
                count+=40
                for j in range(len(entries[i])):
                    query_label1 = tk.Label(tkwin,text=entries[i][0],fg='black',bg='#BAE5E2',width=15,height=0,font=('Times New Roman',11))
                    query_label1.place(x=0,y=count)
                    query_label2 = tk.Label(tkwin,text=entries[i][1],fg='black',bg='#BAE5E2',width=15,height=0,font=('Times New Roman',11))
                    query_label2.place(x=235,y=count)
                    query_label3 = tk.Label(tkwin,text=entries[i][2],fg='black',bg='#BAE5E2',width=15,height=0,font=('Times New Roman',11))
                    query_label3.place(x=470,y=count)
                    query_label4 = tk.Label(tkwin,text=entries[i][3],fg='black',bg='#BAE5E2',width=15,height=0,font=('Times New Roman',11))
                    query_label4.place(x=705,y=count)
                    query_label5 = tk.Label(tkwin,text=entries[i][4],fg='black',bg='#BAE5E2',width=15,height=0,font=('Times New Roman',11))
                    query_label5.place(x=940,y=count)
    except EOFError as e:
        print(e)
def admin():
    
    def sub2():
        
        p=pid.get()
        c=cent.get()
        try:
            myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
            mycur=myconn.cursor()
            mycur.execute('select * from prisoner')
            rs=mycur.fetchall()
            for j in rs:
                if p=='':
                    if j[-2]==int(c):
                        prison1(c)
                        break
                elif c=='':
                    if j[0]==p:
                        prison(p)
                else:
                    messagebox.showinfo('ALERT','Both columns are filled')
                    break
        except EOFError as e:
                print(e)
            
    def submit1():
        '''opt=tk.Tk()
        opt.geometry('2000x2000')
        pri=tk.Label(opt,text='Prisoner ID:',font=(25))
        pri.place(x=100,y=100)
        global pid
        pid=tk.Entry(opt,width=8)
        pid.place(x=230,y=107)
        lab1=tk.Label(opt,text='OR',font=(35))
        lab1.place(x=100,y=170)
        cellno=tk.Label(opt,text='Cell Number:',font=(25))
        cellno.place(x=100,y=250)
        global cent
        cent=tk.Entry(opt,width=3)
        cent.place(x=230,y=255)
        enter=tk.Button(opt,text='Submit',height=1,width=5,command=sub2)
        enter.place(x=100,y=400)'''
        
        opt=tk.Tk()
        opt.geometry('1400x900')
        opt.configure(bg="brown")
        pri=tk.Label(opt,text='Prisoner ID',bg="brown",fg='white',font=('Times New Roman',20,'bold underline'))
        pri.place(x=240,y=150)

        global pid
        pid=tk.Entry(opt,width=20)
        pid.place(x=240,y=225)
        lab1=tk.Label(opt,text='OR',font=(35))
        lab1.place(x=650,y=170)
        cellno=tk.Label(opt,text='Cell Number',bg="brown",fg='white',font=('Times New Roman',20,'bold underline'))
        cellno.place(x=990,y=155)
        global cent
        cent=tk.Entry(opt,width=20)
        cent.place(x=990,y=225)
        enter=tk.Button(opt,text='Submit',height=2,width=10,bg="white",command=sub2)
        enter.place(x=620,y=300)
        enter1=tk.Button(opt,text='Records',height=2,width=10,bg="white",command=passive)
        enter1.place(x=1250,y=0)
        dev=tk.Label(opt,text="Jail Management System",bg="ivory",font=('Times New Roman',30,'bold underline'))
        dev.place(x=400,y=3)
        
    def sub():
        u=unEntry.get()
        p = pwEntry.get()
        global d
        d={'W001':['1111','Atul Vikram'],'W002':['2222','Darren C Veigas'],'W003':['3333','Dhruv Chaudhary'],'W004':['4444','Dhevesh Arun']}
        
        
        for i in d:
            if u==i and p==d[i][0]:
                global name1
                name1=d[i][1]
                messagebox.showinfo('ALERT',' Login Successful')
                try:
                    myconn=mysql.connect(host='localhost',user='root',passwd='adis',database='firstyr')
                    mycur=myconn.cursor()
                    mycur.execute('select * from prisoner')
                    rs=mycur.fetchall()
                    for j in rs:
                        if j[-1]==None:
                            mycur.execute('update prisoner set days={} where pid="{}"'.format(j[5]*365,j[0]))
                            myconn.commit()
                        elif j[-1]>0:
                            mycur.execute('update prisoner set days={} where pid="{}"'.format(j[-1]-1,j[0]))
                            myconn.commit()
                        elif j[-1]==0:
                            
                            mycur.execute('insert into passive values("{}","{}",{},"{}","{}",{},"{}","{}","{}","{}","{}","{}","{}",{})'.format(j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7],j[8],j[9],j[10],j[11],j[12],j[13]))
                            myconn.commit()
                        mycur.execute('delete from prisoner where days=0')
                except EOFError as e:
                        print(e)
                            
    
                submit1()
                break
        else:
            messagebox.showinfo('ALERT',' INCORRRECT  USERNAME/ PASSWORD')
    '''
    root=tk.Tk()
    root.geometry('1000x1000')
    
    root.geometry('600x600')  
    root.title('Login Form')
    global unEntry
    unLabel = tk.Label(root, text="User Name:").grid(row=0, column=0)
    unEntry = tk.Entry(root)
    unEntry.grid(row=0, column=1)  
    global pwEntry
    pwLabel = tk.Label(root,text="pw:").grid(row=1, column=0)  
    pwEntry = tk.Entry(root, show='*')
    pwEntry.grid(row=1, column=1)
    submit=tk.Button(root,text="SUBMIT",width=10,height=2,font=('Times New Roman',17),command=sub)
    submit.place(x=240,y=400)'''
    
    root=tk.Tk()
    root.geometry('750x600')

    root.title('Login Form')
    root.configure(bg="brown")
    global text
    topic=tk.Label(root,text="LOGIN PAGE ",bg="red",font=('Calibri',20,'bold underline'))
    topic.place(x=260,y=4)
    global unEntry
    unLabel = tk.Label(root, text="User Name",font=20).place(x=110,y=180)
    unEntry = tk.Entry(root)
    unEntry.place(x=110,y=230)
    global pwEntry
    pwLabel = tk.Label(root,text="Password",font="20").place(x=450,y=175)
    pwEntry = tk.Entry(root, show='*')
    pwEntry.place(x=450,y=230)
    submit=tk.Button(root,text="SUBMIT",width=10,height=2,font=('Times New Roman bold',17),command=sub)
    submit.place(x=240,y=400)
    
import turtle
dist=1
flag=1200
spiral=turtle.Turtle()
spiral.speed(999999999999999999)
while flag:
    spiral.forward(dist)
    spiral.left(120)
    spiral.left(1)
    dist+=1
    flag-=1
turtle.hideturtle()
turtle.exitonclick()
tkwin=tk.Tk()
tkwin.geometry('850x650')


img=tk.PhotoImage(file='1.png')
lab = tk.Label(tkwin, text="WELCOME!!!",fg='white',font=('Times New Roman Bold',60))
lab.grid()
lab["compound"] = tk.CENTER
lab["image"] = img
buttonuser= tk.Button(tkwin,text="REGISTER",width=15,height=2,font=('Times New Roman',17),command=login)
buttonadmin=tk.Button(tkwin,text="ADMIN",width=15,height=2,font=('Times New Roman',17),command=admin)
buttonuser.place(x=40,y=510)
buttonadmin.place(x=510,y=510)