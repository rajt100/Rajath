from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msg
import cx_Oracle

form = Tk()
form.geometry("800x600")
form.title("NSR Registration")

title_label = Label(form, text="NSR Registration from", font=('bold',20),fg='blue')
title_label.place(x=230, y=10)

# Cancel button Validation
def cancel_registration():
    txt_name.delete(0,END)
    txt_mobile.delete(0,END)
    txt_email.delete(0,END)
    txt_city.delete(0,END)
    cmb_courses.set("Select your course")
    radio_male.select()
    txt_name.focus()

# Submit button functionality
def register_data():
    name = txt_name.get()
    mobile = txt_mobile.get()
    email = txt_email.get()
    city = txt_city.get()
    courses = cmb_courses.get()
    gender = selected_gender.get()
    
# Mobile number functionality
    if mobile == "":
        msg.showinfo("NSR","Please Enter Mobile Number!")
        txt_mobile.focus()
    elif mobile.isdigit() and len(mobile) < 10:
        msg.showinfo("NSR","Mobile number should be 10 digits!")
    elif not mobile.isdigit():
        msg.showerror("NSR","Mobile number must be in numbers")
    elif courses == "Select your courses":
        msg.showinfo("NSR","Please select the course!")
        cmb_courses.focus()
    else:
        #nsr_conn = cx_Oracle.connect(user="c##source",Password='source',port=1522,host='localhost',dsn='xe')
        nsr_conn = cx_Oracle.connect("c##source/source@localhost:1522/xe")
        nsr_cursor = nsr_conn.cursor()
        sql = "insert into nsr_registration1(name,mobile,email,city,courses,gender) values(:name, :mobile, :email, :city, :course, :gender)"
        nsr_cursor.execute(sql,{'name':name,'mobile':mobile,'email':email,'city':city,'course':courses,'gender':gender})
        nsr_conn.commit()

        msg.showinfo("message",'Registeration successfull!')

        txt_name.delete(0,END)
        txt_mobile.delete(0,END)
        txt_email.delete(0,END)
        txt_city.delete(0,END)
        cmb_courses.set("Select your course")
        radio_male.select()
        txt_name.focus()
        


    

# Creating the labels name and text boxes
##1) Name and textbox
lbl_name = Label(form,text='NAME :',font=('bold',15))
lbl_name.place(x=150, y=80)

txt_name = Entry(form,font=('bold',12),width=30)
txt_name.place(x=280,y=80,height=30)
txt_name.focus()

##2) Mobile,asterisk and checkbox
lbl_mobile = Label(form,text='MOBILE :',font=('bold',15))
lbl_mobile.place(x=150, y=134)

lbl_asterisk_label = Label(form, text="*", font=('bold',10),fg='red')
lbl_asterisk_label.place(x=240, y=140)

txt_mobile = Entry(form,font=('bold',12),width=30)
txt_mobile.place(x=280,y=135,height=30)

##3) email and checkbox
lbl_email = Label(form,text='EMAIL :',font=('bold',15))
lbl_email.place(x=150, y=200)

txt_email = Entry(form,font=('bold',12),width=30)
txt_email.place(x=280,y=198,height=30)

##4) city and checkbox
lbl_city = Label(form,text='CITY :',font=('bold',15))
lbl_city.place(x=150, y=260)

txt_city = Entry(form,font=('bold',12),width=30)
txt_city.place(x=280,y=250,height=30)

##5) courses and combobox
lbl_courses = Label(form,text='COURSES :',font=('bold',15))
lbl_courses.place(x=150, y=320)

lbl_asterisk = Label(form, text="*", font=('bold',10),fg='red')
lbl_asterisk.place(x=260, y=320)

courses = ["Hadoop Testing","ETL Testig","Manual Testing","Python Testing"]
selected_course = StringVar()

cmb_courses = ttk.Combobox(form, textvariable=selected_course, values=courses)
cmb_courses.set("Select you course")
cmb_courses.place(x=280, y=320,width=275,height=30)

##6) gender and radio button
lbl_gender = Label(form,text='GENDER :',font=('bold',15))
lbl_gender.place(x=150, y=380)

selected_gender = StringVar()

radio_male = Radiobutton(form,text="MALE", variable = selected_gender,value='M')
radio_male.place(x=280,y=380)
radio_male.select()

radio_female = Radiobutton(form,text="FEMALE", variable = selected_gender,value='F')
radio_female.place(x=380,y=380)

##7) gender and radio button
but_submit = Button(form, text="SUBMIT",command=register_data)
but_submit.place(x=280,y=450,width=80,height=30)

but_cancel = Button(form, text="CANCEL",command=cancel_registration)
but_cancel.place(x=390,y=450,width=80,height=30)










