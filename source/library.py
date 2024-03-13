from tkinter import Tk, Frame, Label, Entry, Button, messagebox,ttk,Scrollbar,VERTICAL, HORIZONTAL,Toplevel,Listbox,END
from PIL import Image, ImageTk
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satvika@777",
    database="libraray_database"
)
mycursor = mydb.cursor()



fonts = ('Courier New', 15, 'bold')
fonts1 = ('Courier New', 20, 'bold')


root = Tk()
root.resizable(0,0)


class welcome_page:
    def __init__(self, root):
        self.root = root
        self.root.title("HOME")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/cover.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        self.main_label_btn = Button(self.page, text='Let\'s Dive', font=fonts1, command=self.home_login,
                                     bg="aquamarine3", fg="white")
        self.main_label_btn.place(x=200, y=400)

    def home_login(self):
        self.page.destroy()
        home_obj = Login_page(root)


class Login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right = Frame(self.root, width=1000, height=600)
        self.right.place(x=0, y=0)

        self.image = Image.open('../assets/login_img.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right, image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0, y=0)

        self.admin_logo = Image.open('../assets/ai.png')
        self.admin_logo = self.admin_logo.resize((100, 100))
        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)
        self.admin_logo_lbl = Label(self.right, image=self.admin_logo)
        self.admin_logo_lbl.place(x=150, y=100)



        self.admin__login = Label(self.right, text="Admin login")
        self.admin__login.place(x=150, y=220)
        self.admin_name = Label(self.right, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_name.place(x=100, y=280)
        self.admin_name_entry = Entry(self.right, width=10, font=fonts)
        self.admin_name_entry.place(x=230, y=280)
        self.admin_pass = Label(self.right, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_pass.place(x=100, y=320)
        self.admin_pass_entry = Entry(self.right, width=10, font=fonts)
        self.admin_pass_entry.place(x=230, y=320)

        self.admin_login_btn = Button(self.right, text='LOGIN', font=fonts, command=self.admin_login)
        self.admin_login_btn.place(x=150, y=400)

        self.left = Frame(self.root, width=1000, height=600)
        self.left.place(x=500, y=0)

        self.image = Image.open('../assets/login_img.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left, image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0, y=0)

        self.student_logo = Image.open('../assets/si.png')
        self.student_logo = self.student_logo.resize((100, 100))
        self.student_logo = ImageTk.PhotoImage(self.student_logo)
        self.student_logo_lbl = Label(self.left, image=self.student_logo)
        self.student_logo_lbl.place(x=150, y=100)

        self.student__login = Label(self.left, text="Student login")
        self.student__login.place(x=150, y=220)

        self.student_name = Label(self.left, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_name.place(x=100, y=280)
        self.student_name_entry = Entry(self.left, width=10, font=fonts)
        self.student_name_entry.place(x=230, y=280)

        self.student_pass = Label(self.left, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_pass.place(x=100, y=320)
        self.student_pass_entry = Entry(self.left, width=10, font=fonts)
        self.student_pass_entry.place(x=230, y=320)

        self.student_login_btn = Button(self.left, text='LOGIN', font=fonts, command=self.student_login)
        self.student_login_btn.place(x=150, y=400)

    def admin_login(self):
        self.b_name = self.admin_name_entry.get()
        self.b_pass = self.admin_pass_entry.get()

        mycursor.execute("SELECT * FROM admin WHERE userid= %s AND password = %s", (self.b_name, self.b_pass))
        admin_data = mycursor.fetchone()

        if admin_data:
            self.right.destroy()
            self.left.destroy()
            admin_obj = Admin_page(root, self.b_name)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')

    def student_login(self):
        self.b_name = self.student_name_entry.get()
        self.b_pass = self.student_pass_entry.get()

        mycursor.execute("SELECT * FROM Student WHERE userid= %s AND password = %s", (self.b_name, self.b_pass))
        student_data = mycursor.fetchone()

        if student_data:
            self.right.destroy()
            self.left.destroy()
            student_obj = Student_page(root,self.b_name)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')


class Admin_page:
    def __init__(self, root, admin_id):
        self.root = root
        self.root.title("ADMIN DASHBOARD")
        self.right = Frame(self.root, width=1000, height=600)
        self.right.place(x=0, y=0)


        
        self.image = Image.open('../assets/admin_space_home.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right, image=self.image)
        self.image_label.place(x=0, y=0)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.right, image=self.back_image, bg='gray')
        self.back_button.image=self.back_image
        self.back_button.place(x=10, y=520)
        self.back_button.bind('<Button-1>',self.go_back)
        

        self.profile_image = Image.open('../assets/profile1.png')
        self.profile_image = self.profile_image.resize((50, 50))
        self.profile_photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = Button(self.right, image=self.profile_photo, bg='gray', bd=0,
                                     command=lambda: self.profile(admin_id))
        self.profile_button.place(x=948, y=2)
                              


        self.add_book_btn = Button(self.right, text='STUDENT DETAILS', font=fonts, bg='firebrick', fg='white',width=22, command=self.student1)
        self.add_book_btn.place(x=150, y=200)
        self.add_book_btn = Button(self.right, text='ADD OR DELETE STUDENT', font=fonts, bg='firebrick', fg='white',width=22, command=self.add_student)
        self.add_book_btn.place(x=150, y=250)
        self.add_book_btn = Button(self.right, text='ADD OR DELETE BOOK', font=fonts, bg='firebrick', fg='white', width=22,command=self.add_book)
        self.add_book_btn.place(x=150, y=300)
        self.add_book_btn = Button(self.right, text='BOOKING INFO', font=fonts, bg='firebrick', fg='white',width=22, command=self.booking)
        self.add_book_btn.place(x=150, y=350)
        self.add_book_btn = Button(self.right, text='REQUEST INFO', font=fonts, bg='firebrick', fg='white',width=22, command=self.request)
        self.add_book_btn.place(x=150, y=400)
        self.add_book_btn = Button(self.right, text='RETURN', font=fonts, bg='firebrick', fg='white',width=22, command=self.return_next)
        self.add_book_btn.place(x=150, y=450)


    def go_back(self,event):    
        self.right.destroy()
        Admin_obj=Login_page(root)

    

    def profile(self, admin_id):
        self.right.destroy()
        Admin_obj = profile_page(root, admin_id)

    def student1(self):
        self.right.destroy()
        Admin_obj = Std_page(root)

    def add_book(self):
        self.right.destroy()
        Admin_obj = Add_page(root)

    def add_student(self):
        self.right.destroy()
        Admin_obj = Student_det_page(root)

    def booking(self):
        self.right.destroy()
        Admin_obj = Booking_info(root)

    def request(self):
        self.right.destroy()
        Admin_obj = Request_info(root)
    
    def return_next(self):
        self.right.destroy()
        Admin_obj = return_next_page(root)


class profile_page(Login_page):
    def __init__(self, root, admin_id):
        self.root = root
        self.admin_id=admin_id
        self.root.title("Profile page")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/profilebg.png')
        self.image = self.image.resize((1000,600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root, '')


        mycursor.execute("SELECT * FROM admin WHERE userid= %s", (self.admin_id,))
        admin_data = mycursor.fetchone()

        if admin_data:
            admin_user_label = Label(self.page, text=f"Userid: {admin_data[0]}", font=fonts)
            admin_user_label.place(x=400, y=310)

            admin_name_label = Label(self.page, text=f"Name: {admin_data[2]}", font=fonts)
            admin_name_label.place(x=400, y=340)

            admin_email_label = Label(self.page, text=f"Email: {admin_data[3]}", font=fonts)
            admin_email_label.place(x=400, y=370)

            admin_phone_label = Label(self.page, text=f"Phone number: {admin_data[4]}", font=fonts)
            admin_phone_label.place(x=400, y=400)



class Add_page:
     def __init__(self, root):
        self.root = root
        self.root.title("Book Details")
        self.page = Frame(self.root, width = 1000, height = 600)
        self.page.place(x = 0, y = 0)

        self.image = Image.open('../assets/book_add.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)


        self.book__details = Label(self.page,text="BOOK DETAILS",fg='red',font=fonts1)
        self.book__details.place(x=400,y=60)

        self.book_id = Label(self.page, text = 'BOOK ID:',fg ='black', font = fonts,width=11)
        self.book_id.place(x = 300, y = 200)
        self.book_id_entry = Entry(self.page,width=20, font = fonts)
        self.book_id_entry.place(x = 450, y = 200)

        self.book_title= Label(self.page, text = 'BOOK NAME:',fg ='black', font = fonts,width=11)
        self.book_title.place(x = 300, y = 240)
        self.book_title_entry = Entry(self.page,width=20, font = fonts)
        self.book_title_entry.place(x = 450, y = 240)

        self.book_author= Label(self.page, text = 'AUTHOR:',fg ='black', font = fonts,width=11)
        self.book_author.place(x = 300, y = 280)
        self.book_author_entry = Entry(self.page,width=20, font = fonts)
        self.book_author_entry.place(x = 450, y = 280)

        self.book_edition= Label(self.page, text = 'EDITION:',fg ='black', font = fonts,width=11)
        self.book_edition.place(x = 300, y = 320)
        self.book_edition_entry = Entry(self.page,width=20, font = fonts)
        self.book_edition_entry.place(x = 450, y = 320)

        self.book_status= Label(self.page, text = 'STATUS:',fg ='black', font = fonts,width=11)
        self.book_status.place(x = 300, y = 360)
        self.book_status_entry = Entry(self.page,width=20, font = fonts)
        self.book_status_entry.place(x = 450, y = 360)

        self.save_button = Button(self.page, text="ADD",width=12, font=fonts,command=self.save_to_database)
        self.save_button.place(x=350, y=430)

        self.save_button = Button(self.page, text="DELETE",width=12, font=fonts,command=self.delete_from_database)
        self.save_button.place(x=550, y=430)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

     def go_back(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root, '')


     def save_to_database(self):
        book_id = self.book_id_entry.get()
        book_title = self.book_title_entry.get()
        book_author = self.book_author_entry.get()
        book_edition = self.book_edition_entry.get()
        book_status = self.book_status_entry.get()


        query = "INSERT INTO books (bid, book_title,author,edition,status) VALUES (%s, %s, %s, %s,%s)"
        values = (book_id, book_title, book_author,book_edition, book_status)
        mycursor.execute(query, values)


        mydb.commit()
        mydb.close()

        self.book_id_entry.delete(0, 'end')
        self.book_title_entry.delete(0, 'end')
        self.book_author_entry.delete(0, 'end')
        self.book_edition_entry.delete(0, 'end')
        self.book_status_entry.delete(0, 'end')
     
     
     def delete_from_database(self):
        book_id = self.book_id_entry.get()
        book_title = self.book_title_entry.get()
        book_author = self.book_author_entry.get()
        book_edition = self.book_edition_entry.get()
        book_status = self.book_status_entry.get()

        mydb = mysql.connector.connect(
             host="localhost",
             user="root",
             password="Satvika@777",
             database="libraray_database"
        )
        mycursor = mydb.cursor()


        query = "DELETE FROM books WHERE bid=%s AND book_title = %s AND author = %s AND edition = %s AND status = %s"
        values = (book_id, book_title, book_author, book_edition, book_status)

        mycursor.execute(query,values)
        mydb.commit()
        mycursor.close()
        mydb.close()

        self.book_id_entry.delete(0, 'end')
        self.book_title_entry.delete(0, 'end')
        self.book_author_entry.delete(0, 'end')
        self.book_edition_entry.delete(0, 'end')
        self.book_status_entry.delete(0, 'end')





class Std_page:
    def __init__(self, root):
        self.root = root
        self.root.title("STUDENT DETAILS")
        self.page = Frame(self.root, width=1000, height=600,bg='gray86')
        self.page.place(x=0, y=0)

        heading_label = Label(self.page, text="STUDENT DETAILS", font=('bold',25 ), bg='gray86')
        heading_label.pack(pady=5)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

     



        self.tree = ttk.Treeview(self.page, columns=('ID', 'Name', 'Email', 'Branch Name', 'Phone Number'), show='headings', height=20)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email') 
        self.tree.heading('Branch Name', text='Branch') 
        self.tree.heading('Phone Number', text='Phone no')
        
        self.tree.column('ID', width=100, anchor='center')  
        self.tree.column('Name', width=300, anchor='center') 
        self.tree.column('Email', width=300, anchor='center')  
        self.tree.column('Branch Name', width=100, anchor='center')  
        self.tree.column('Phone Number', width=200, anchor='center')  
        self.tree.pack(pady=80)

        
        v_scrollbar = Scrollbar(self.page, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scrollbar.set)

     
        h_scrollbar = Scrollbar(self.page, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=h_scrollbar.set)

        
        mycursor.execute("SELECT * FROM student")
        student_data = mycursor.fetchall()

        
        for data in student_data:
            self.tree.insert('', 'end', values=data)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root, '')




class Student_det_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/Student_add.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        self.student__details = Label(self.page,text="STUDENT DETAILS",fg='black',font=fonts)
        self.student__details.place(x=400,y=60)

        self.student_id = Label(self.page, text = 'Student ID:',fg ='black', font = fonts,width=13)
        self.student_id.place(x = 300, y = 200)
        self.student_id_entry = Entry(self.page,width=20, font = fonts)
        self.student_id_entry.place(x = 470, y = 200)

        self.student_name= Label(self.page, text = 'Student Name:',fg ='black', font = fonts,width=13)
        self.student_name.place(x = 300, y = 240)
        self.student_name_entry = Entry(self.page,width=20, font = fonts)
        self.student_name_entry.place(x = 470, y = 240)

        self.student_email= Label(self.page, text = 'Email:',fg ='black', font = fonts,width=13)
        self.student_email.place(x = 300, y = 280)
        self.student_email_entry = Entry(self.page,width=20, font = fonts)
        self.student_email_entry.place(x = 470, y = 280)

        self.student_branch= Label(self.page, text = 'Branch:',fg ='black', font = fonts,width=13)
        self.student_branch.place(x = 300, y = 320)
        self.student_branch_entry = Entry(self.page,width=20, font = fonts)
        self.student_branch_entry.place(x = 470, y = 320)

        self.student_phonenumber = Label(self.page, text='Phone Number:', fg='black', font=fonts, width=13)
        self.student_phonenumber.place(x=300, y=360)
        self.student_phonenumber_entry = Entry(self.page, width=20, font=fonts)
        self.student_phonenumber_entry.place(x=470, y=360)

        self.student_password = Label(self.page, text='Password:', fg='black', font=fonts, width=13)
        self.student_password.place(x=300, y=400)
        self.student_password_entry = Entry(self.page, width=20, font=fonts)
        self.student_password_entry.place(x=470, y=400)

        self.save_button = Button(self.page, text="ADD", width=12, font=fonts, command=self.save_to_database,bg='azure3')
        self.save_button.place(x=330, y=470)

        self.save_button = Button(self.page, text="DELETE", width=12, font=fonts, command=self.delete_from_database,bg='azure3')
        self.save_button.place(x=530, y=470)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root, '')


    def save_to_database(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_email= self.student_email_entry .get()
        student_branch =self.student_branch_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        student_password=self.student_password_entry.get()
    
        query = "INSERT INTO student (Userid,Name,Email,Branch,PhoneNumber,Password) VALUES (%s, %s, %s, %s,%s,%s)"
        values = (student_id,student_name,student_email, student_branch,student_phonenumber,student_password)
        mycursor.execute(query, values)


        mydb.commit()
        mydb.close()

        self.student_id_entry.delete(0, 'end')
        self.student_name_entry.delete(0, 'end')
        self.student_email_entry.delete(0, 'end')
        self.student_branch_entry.delete(0, 'end')
        self.student_phonenumber_entry.delete(0, 'end')
        self.student_password_entry.delete(0,'end')
     
     
    def delete_from_database(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_email= self.student_email_entry .get()
        student_branch =self.student_branch_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        student_password=self.student_password_entry.get()



        query = "DELETE FROM Student WHERE Userid=%s AND Name = %s AND Email = %s AND Branch = %s AND PhoneNumber = %s AND Password=%s"
        values = (student_id,student_name,student_email, student_branch,student_phonenumber,student_password)

        mycursor.execute(query,values)
        mydb.commit()
        mycursor.execute(query, values)
        mydb.commit()

        self.student_id_entry.delete(0, 'end')
        self.student_name_entry.delete(0, 'end')
        self.student_email_entry.delete(0, 'end')
        self.student_branch_entry.delete(0, 'end')
        self.student_phonenumber_entry.delete(0, 'end')
        self.student_password_entry.delete(0,'end')
     

class Booking_info:
    def __init__(self, root):
        self.root = root
        self.root.title("BOOKING_INFO")
        self.page = Frame(self.root, width=1000, height=600,bg='gray86')
        self.page.place(x=0, y=0)

        heading_label = Label(self.page, text="BOOKING INFORMATION", font=('bold', 25), bg='gray86')
        heading_label.pack(pady=10)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

     

        self.tree = ttk.Treeview(self.page, columns=( 'Name', 'Email', 'Book_Title',"BID"), show='headings', height=15)
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email') 
        self.tree.heading('Book_Title', text='Book_Title')
        self.tree.heading('BID', text='BID') 
        
        self.tree.column('Name', width=300, anchor='center') 
        self.tree.column('Email', width=250, anchor='center')  
        self.tree.column('Book_Title', width=350, anchor='center')  
        self.tree.column('BID', width=100, anchor='center')  
        self.tree.pack(pady=100)

        
        v_scrollbar = Scrollbar(self.page, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scrollbar.set)

     
        h_scrollbar = Scrollbar(self.page, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=h_scrollbar.set)

        mycursor.execute("SELECT * FROM booking_info")
        student_data = mycursor.fetchall()

        
        for data in student_data:
            self.tree.insert('', 'end', values=data)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root, '')





class Request_info:
    def __init__(self,root):
        self.root = root
        self.root.title("Request_info")
        self.page = Frame(self.root, width=1000, height=600,bg='gray86')
        self.page.place(x=0, y=0)

    
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Satvika@777",
        database="libraray_database"
        )

        self.cursor = self.db.cursor()

        self.request_listbox = Listbox(self.page, width=80, height=18,font=fonts)
        self.request_listbox.grid(row=0, column=0, padx=10, pady=10)

        self.refresh_requests()

        accept_button = Button(self.page, text="Accept", command=self.accept_request, width=15, bg='azure3', font=fonts)
        accept_button.grid(row=1, column=0, padx=10, pady=5, sticky="w")


        deny_button = Button(self.page, text="Deny", command=self.deny_request,width=15,bg='azure3',font=fonts)
        deny_button.grid(row=1, column=0, padx=10, pady=5, sticky="e")


        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=40, y=560)
        self.back_button.bind('<Button-1>', self.go_back)


    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root, '')



    def refresh_requests(self):
        self.request_listbox.delete(0, END)
        self.cursor.execute("SELECT * FROM request_info WHERE status='pending'")
        requests = self.cursor.fetchall()
        for request in requests:
           self.request_listbox.insert(END, f"{request[0]} - {request[1]} - {request[2]} - {request[4]}")


    def accept_request(self):
            selected_index = self.request_listbox.curselection()[0]
            selected_request = self.request_listbox.get(selected_index)
            request_parts = selected_request.split(" - ")
        
            if len(request_parts) != 4:
                messagebox.showerror("Error", f"Invalid request selection: {selected_request}")
                return

            request_id = (request_parts[2])

            self.cursor.execute("UPDATE  request_info SET status='Accepted' WHERE email=%s",(request_id,))
            self.db.commit()
            messagebox.showinfo("Success", "Request Accepted")
            self.refresh_requests()

    def deny_request(self):
        selected_request = self.request_listbox.get(self.request_listbox.curselection())
        request_id =(selected_request.split(" - ")[2])

        self.cursor.execute("UPDATE request_info SET status='Denied' WHERE email=%s", (request_id,))
        self.db.commit()
        messagebox.showinfo("Success", "Request Denied")
        self.refresh_requests()



class return_next_page:
    def __init__(self, root):
        self.root = root
        self.root.title('RETURNED BOOKS')
        self.left = Frame(self.root, width=1550, height=800,bg='gray86')
        self.left.place(x=0, y=0)

        self.image = Image.open('../assets/request_next_page.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left, image=self.image)
        self.image_label.place(x=0, y=0)


        self.book_id_label = Label(self.left, text="Enter Book ID:",font=fonts)
        self.book_id_label.place(x=250,y=250)
        self.book_id_entry = Entry(self.left,width=40)
        self.book_id_entry.place(x=450,y=250)

        self.update_button = Button(self.left, text="Update Status", command=self.update_status,font=fonts)
        self.update_button.place(x=400,y=300)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.left, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

    def go_back(self, event):
        self.left.destroy()
        Admin_obj = Admin_page(root, '')


    def update_status(self):
        book_id = self.book_id_entry.get()
        if not book_id:
            messagebox.showerror("Error", "Please enter a book ID.")
            return

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Satvika@777",
                database="libraray_database"
            )
            cursor = connection.cursor()

            cursor.execute("UPDATE books SET status = 'yes' WHERE bid = %s", (book_id,))

        
            cursor.execute("UPDATE request_info SET status = 'book' WHERE id = %s AND status = 'accepted'", (book_id,))

            connection.commit()

         
            messagebox.showinfo("Success", "Book status updated successfully.")

            cursor.close()
            connection.close()

            self.book_id_entry.delete(0, END)

        except mysql.connector.Error as error:
            messagebox.showerror("Error", f"An error occurred: {error}")


class Student_page:
    def __init__(self, root,sid):
        self.root = root
        self.sid=sid
        self.root.title('STUDENT DASHBOARD')
        self.left = Frame(self.root, width=1000, height=600)
        self.left.place(x=0, y=0)

        self.image = Image.open('../assets/student_home_page_img.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left, image=self.image)
        self.image_label.place(x=0, y=0)
        

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.left, image=self.back_image, bg='gray', bd=0)
        self.back_button.image=self.back_image
        self.back_button.place(x=10, y=540)
        self.back_button.bind('<Button-1>',self.go_back)

        self.profile_image = Image.open('../assets/profile1.png')
        self.profile_image = self.profile_image.resize((50, 50))
        self.profile_photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = Button(self.left, image=self.profile_photo, bg='gray', bd=0,
                                     command=lambda: self.profile(self.sid))
        self.profile_button.place(x=948, y=2)
                              

        self.student__login = Label(self.left, text="HELLO ENTHUSIASTS!", fg='red', font=fonts1)
        self.student__login.place(x=350, y=40)

        self.history_btn = Button(self.left, text='Book Store', font=fonts, command=self.book_store_next, width=20)
        self.history_btn.place(x=360, y=200)

        self.book_store_btn = Button(self.left, text='Request Status', font=fonts, command=self.request_status_next,
                                      width=20)
        self.book_store_btn.place(x=360, y=250)

        self.book_store_btn = Button(self.left, text='Book Now', font=fonts, command=self.book_now_next, width=20)
        self.book_store_btn.place(x=360, y=300)


    def go_back(self,event):    
        self.left.destroy()
        Admin_obj=Login_page(root)



    def book_now_next(self):
        self.left.destroy()
        book_now_obj = book_now_page(root)


    def profile(self, admin_id):
        self.left.destroy()
        profile_obj = student_profile_page(root, self.sid)


    def request_status_next(self):
        self.left.destroy()
        request_status_obj = Request_status_page(root,self.sid)

    def book_store_next(self):
        self.left.destroy()
        store_obj = book_store_page(root)



class student_profile_page(Login_page):
    def __init__(self, root, sid):
        self.root = root
        self.root.title("Profile page")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/profilebg.png')
        self.image = self.image.resize((1000,600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)




        mycursor.execute("SELECT * FROM student WHERE userid= %s", (sid,))
        student_data = mycursor.fetchone()

        if student_data:
            student_user_label = Label(self.page, text=f"Userid: {student_data[0]}", font=fonts)
            student_user_label.place(x=400, y=310)

            student_name_label = Label(self.page, text=f"Name: {student_data[1]}", font=fonts)
            student_name_label.place(x=400, y=340)

            student_email_label = Label(self.page, text=f"Email: {student_data[2]}", font=fonts)
            student_email_label.place(x=400, y=370)

            student_phone_label = Label(self.page, text=f"Phone number: {student_data[4]}", font=fonts)
            student_phone_label.place(x=400, y=400)

            student_phone_label = Label(self.page, text=f"Branch: {student_data[3]}", font=fonts)
            student_phone_label.place(x=400, y=430)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Student_page(root, '')




class book_now_page:
    def __init__(self, root):
        self.root = root
        self.root.title("Book Now")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)


        self.image = Image.open('../assets/book_now.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)


        self.book_id = Label(self.page, text='BOOK ID:', fg='black', font=fonts, width=13)
        self.book_id.place(x=200, y=200)
        self.book_id_entry = Entry(self.page, width=30, font=fonts)
        self.book_id_entry.place(x=400, y=200)

        self.book_name = Label(self.page, text='BOOK NAME:', fg='black', font=fonts, width=13)
        self.book_name.place(x=200, y=250)
        self.book_name_entry = Entry(self.page, width=30, font=fonts)
        self.book_name_entry.place(x=400, y=250)

        self.student_login_btn = Button(self.page, text='Enter', font=fonts, command=self.book_now_entry,width=20,bg='azure3')
        self.student_login_btn.place(x=300, y=300)


        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Student_page(root, '')



    def book_now_entry(self):
        self.b_name = self.book_name_entry.get()
        self.bi_name = self.book_id_entry.get()

        mycursor.execute("SELECT * FROM Books WHERE bid = %s AND book_title=%s", (self.bi_name,self.b_name,))
        book_data = mycursor.fetchone()

        if book_data:
            self.page.destroy()
            book_now_obj = Booking_page(self.root, self.bi_name,self.b_name)
        else:
            messagebox.showerror('INVALID', ' Invalid Book Name')


class Request_status_page:
    def __init__(self, root, userid):
        self.root = root
        self.userid = userid
        self.root.title("REQUEST STATUS")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)


        heading_label = Label(self.page, text="REQUEST STATUS", font=('bold', 25))
        heading_label.pack(pady=5)


        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Satvika@777",
            database="libraray_database"
        )
        self.cursor = self.connection.cursor()


      
        self.cursor.execute("SELECT email FROM student WHERE Userid = %s", (userid,))
        student_email = self.cursor.fetchone()[0]

        self.tree = ttk.Treeview(self.page, columns=("Student Name", "Student Email", "book_title", "Status"),show='headings')
       

        self.tree.heading("Student Name", text="Student Name")
        self.tree.heading("Student Email", text="Student Email")
        self.tree.heading("book_title", text="book_title")
        self.tree.heading("Status", text="Status")

        self.tree.column('Student Name', width=240, anchor='center') 
        self.tree.column('Student Email', width=250, anchor='center')  
        self.tree.column('book_title', width=400, anchor='center') 
        self.tree.column('Status', width=100, anchor='center')    
        self.tree.pack(pady=100)

      
        self.cursor.execute("SELECT name, email, book_title, status FROM request_info WHERE email = %s", (student_email,))
        requests = self.cursor.fetchall()

        for i, request in enumerate(requests):
            self.tree.insert("", "end", text=str(i), values=request)

       
        self.connection.close()

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Student_page(root,'')

        

class book_store_page:
    def __init__(self, root):
        self.root = root
        self.root.title("BOOK STORE")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)


        heading_label = Label(self.page, text="BOOKS DETAILS", font=('bold', 25))
        heading_label.pack(pady=5)


        self.tree = ttk.Treeview(self.root, columns=('bid', 'Name', 'author', 'edition'), show='headings', height=20)
        self.tree.heading('bid', text='BID')
        self.tree.heading('Name', text='Book Name')
        self.tree.heading('author', text='Author') 
        self.tree.heading('edition', text='Edition') 
        
        self.tree.column('bid', width=90, anchor='center')  
        self.tree.column('Name', width=500, anchor='center') 
        self.tree.column('author', width=300, anchor='center')  
        self.tree.column('edition', width=100, anchor='center')    
        self.tree.pack(pady=150)

        
        v_scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=v_scrollbar.set)

     
        h_scrollbar = Scrollbar(self.root, orient=HORIZONTAL, command=self.tree.xview)
        self.tree.configure(xscrollcommand=h_scrollbar.set)

        
        mycursor.execute("SELECT * FROM books")
        books_data = mycursor.fetchall()

        
        for data in books_data:
            self.tree.insert('', 'end', values=data)




class Booking_page:
    def __init__(self, root,book_id,book_name):
        self.root = root
        self.book_id = book_id
        self.book_name=book_name
        self.root.title("Booking")
        self.page = Frame(self.root, width=1000, height=600)
        self.page.place(x=0, y=0)
        

        self.image = Image.open('../assets/book_now_next.png')
        self.image = self.image.resize((1000, 600))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Satvika@777",
        database="libraray_database"
        )
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM Books WHERE bid=%s and book_title= %s", (self.book_id,self.book_name))
        book_data = mycursor.fetchone()

        if book_data:
            status = book_data[4] 
            bid_label = Label(self.page, text=f"bid: {book_data[0]}", font=fonts)
            bid_label.place(x=350, y=150)

            book_title_label =Label(self.page, text=f"Title: {book_data[1]}", font=fonts)
            book_title_label.place(x=350, y=200)

            author_label =Label(self.page, text=f"Author: {book_data[2]}", font=fonts)
            author_label.place(x=350, y=250)

            edition_label =Label(self.page, text=f"Edition: {book_data[3]}", font=fonts)
            edition_label.place(x=350, y=300)

            if status == "yes":
                self.booking_button = Button(self.page, text="Book Now", command=self.book_now)
                self.booking_button.place(x=400, y=350)
            else:
                self.request_button = Button(self.page, text="Make a Request", command=self.make_request)
                self.request_button.place(x=400, y=350)


        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.page, image=self.back_image, bg='gray', bd=0)
        self.back_button.image = self.back_image
        self.back_button.place(x=20, y=20)
        self.back_button.bind('<Button-1>', self.go_back)

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Student_page(root, '')


    def book_now(self):
        self.booking_window =Toplevel(self.root)
        self.booking_window.title("Book Now")
        self.booking_window.geometry("300x200")


        Label(self.booking_window, text="Name:").grid(row=0, column=2,padx=10,pady=10,sticky="e")
        Label(self.booking_window, text="Email:").grid(row=1, column=2,padx=10,pady=10,sticky="e")

        self.name_entry =Entry(self.booking_window)
        self.name_entry.grid(row=0, column=4,padx=10,pady=10)
        self.email_entry = Entry(self.booking_window)
        self.email_entry.grid(row=1, column=4,padx=10,pady=10)

        Button(self.booking_window, text="Confirm Booking", command=self.confirm_booking).grid(row=2, column=3,columnspan=2,pady=10)

    def confirm_booking(self):
        mycursor.execute("UPDATE books SET status = 'booked' WHERE bid=%s AND book_title = %s", (self.book_id, self.book_name,))
        mydb.commit()

        name = self.name_entry.get()
        email = self.email_entry.get()
        book_details = (name, email, self.book_name,self.book_id)
        mycursor.execute("INSERT INTO booking_info (name, email, book_title,bid) VALUES (%s, %s, %s,%s)", book_details)
        mydb.commit()

        messagebox.showinfo("Booking Status", "Your book has been booked successfully.")
        self.booking_window.destroy()

    def make_request(self):
        self.request_window = Toplevel(self.root)
        self.request_window.title("Make a Request")
        self.request_window.geometry("300x200")

        Label(self.request_window, text="Name:").grid(row=0, column=2,padx=10,pady=10,sticky="e")
        Label(self.request_window, text="Email:").grid(row=1, column=2,padx=10,pady=10,sticky="e")
       
        self.name_entry = Entry(self.request_window)
        self.name_entry.grid(row=0, column=4,padx=10,pady=10)
        self.email_entry =Entry(self.request_window)
        self.email_entry.grid(row=1, column=4,padx=10,pady=10)

        Button(self.request_window, text="Submit Request", command=self.submit_request).grid(row=2, column=3,columnspan=2,pady=10)

    def submit_request(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        status="pending"
        request_details = (self.book_id,name, email, self.book_name,status)
        mycursor.execute("INSERT INTO Request_info (id, name, email, book_title, status) VALUES (%s, %s, %s, %s, %s)", request_details)
        mydb.commit()

        messagebox.showinfo("Request Status", "Your request has been submitted successfully.")
        self.request_window.destroy()
   



root.geometry('1000x600+100+50')
home = welcome_page(root)
root.mainloop()