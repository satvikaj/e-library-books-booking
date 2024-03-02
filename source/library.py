from tkinter import Tk, Frame, Label, Entry, Button, messagebox,ttk,Scrollbar,VERTICAL, HORIZONTAL
from PIL import Image, ImageTk
import mysql.connector
import ctypes
import logging

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
window_width = int(screen_width * 0.8)
window_height = int(screen_height * 0.8)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satvika@777",
    database="libraray_database"
)
mycursor = mydb.cursor()



fonts = ('Courier New', 13, 'bold')
fonts1 = ('Courier New', 17, 'bold')
fonts2 = ('Times New Roman', 25)
fonts3 = ('Lucida Calligraphy', 35)

root = Tk()


class welcome_page:
    def __init__(self, root):
        self.root = root
        self.root.title("HOME")
        self.page = Frame(self.root, width=1550, height=800)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/cover.png')
        self.image = self.image.resize((1550, 800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        self.main_label_btn = Button(self.page, text='Let\'s Dive', font=fonts1, command=self.home_login,
                                     bg="aquamarine3", fg="white")
        self.main_label_btn.place(x=250, y=600)

    def home_login(self):
        self.page.destroy()
        home_obj = Login_page(root)


class Login_page:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN PAGE")
        self.right = Frame(self.root, width=1550, height=800, bg='darkseagreen1')
        self.right.place(x=0, y=0)

        self.image = Image.open('../assets/login1.png')
        self.image = self.image.resize((1550,800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)
        


        self.admin_logo = Image.open('../assets/ai.png')
        self.admin_logo = self.admin_logo.resize((150, 150))
        self.admin_logo = ImageTk.PhotoImage(self.admin_logo)
        self.admin_logo_lbl = Label(self.right, image=self.admin_logo)
        self.admin_logo_lbl.place(x=250, y=150)

        self.admin__login = Label(self.right, text="Admin login")
        self.admin__login.place(x=250, y=310)
        self.admin_name = Label(self.right, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_name.place(x=250, y=345)
        self.admin_name_entry = Entry(self.right, width=10, font=fonts)
        self.admin_name_entry.place(x=350, y=345)
        self.admin_pass = Label(self.right, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.admin_pass.place(x=250, y=380)
        self.admin_pass_entry = Entry(self.right, width=10, font=fonts)
        self.admin_pass_entry.place(x=350, y=380)

        self.admin_login_btn = Button(self.right, text='LOGIN', font=fonts, command=self.admin_login)
        self.admin_login_btn.place(x=250, y=445)

        self.left = Frame(self.root, width=1550, height=800)
        self.left.place(x=800, y=0)

        self.image = Image.open('../assets/login1.png')
        self.image = self.image.resize((1550,800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left,image=self.image)
        self.image_label.place(x=0,y=0)


        self.student_logo = Image.open('../assets/si.png')
        self.student_logo = self.student_logo.resize((150, 150))
        self.student_logo = ImageTk.PhotoImage(self.student_logo)
        self.student_logo_lbl = Label(self.left, image=self.student_logo)
        self.student_logo_lbl.place(x=250, y=150)

        self.student__login = Label(self.left, text="Student login")
        self.student__login.place(x=250, y=310)

        self.student_name = Label(self.left, text='USER ID', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_name.place(x=250, y=345)
        self.student_name_entry = Entry(self.left, width=10, font=fonts)
        self.student_name_entry.place(x=350, y=345)

        self.student_pass = Label(self.left, text='PASSWORD', bg='steel blue', fg='white', font=fonts, width=9)
        self.student_pass.place(x=250, y=380)
        self.student_pass_entry = Entry(self.left, width=10, font=fonts)
        self.student_pass_entry.place(x=350, y=380)

        self.student_login_btn = Button(self.left, text='LOGIN', font=fonts, command=self.student_login)
        self.student_login_btn.place(x=250, y=445)

    def admin_login(self):
        self.b_name = self.admin_name_entry.get()
        self.b_pass = self.admin_pass_entry.get()

        # Query to check if admin credentials exist in the database
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

        mycursor.execute("SELECT * FROM student WHERE userid= %s AND password = %s", (self.b_name, self.b_pass))
        student_data = mycursor.fetchone()

        if student_data:
            self.right.destroy()
            self.left.destroy()
            student_obj = Student_page(root)
        else:
            messagebox.showerror('INVALID', 'Invalid UserID or Password')


class Admin_page:
    def __init__(self, root, admin_id):
        self.root = root
        self.root.title("ADMIN DASHBOARD")
        self.right = Frame(self.root, width=1550, height=800)
        self.right.place(x=0, y=0)
        self.image = Image.open('../assets/admin home.png')
        self.image = self.image.resize((1550, 800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.right, image=self.image)
        self.image_label.place(x=0, y=0)

        self.profile_image = Image.open('../assets/profile1.png')
        self.profile_image = self.profile_image.resize((100, 100))
        self.profile_photo = ImageTk.PhotoImage(self.profile_image)
        self.profile_button = Button(self.right, image=self.profile_photo, bg='gray', bd=0,
                                     command=lambda: self.profile(admin_id))
        self.profile_button.place(x=1450, y=5)


        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.right, image=self.back_image, bg='gray', bd=0)
        self.back_button.image=self.back_image
        self.back_button.place(x=10, y=740)
        self.back_button.bind('<Button-1>',self.go_back)
                              


        self.add_book_btn = Button(self.right, text='STUDENT DETAILS', font=fonts, bg='firebrick', fg='white',
                                   width=25, command=self.student1)
        self.add_book_btn.place(x=200, y=300)
        self.add_book_btn = Button(self.right, text='ADD STUDENT DETAILS', font=fonts, bg='firebrick', fg='white', width=25,
                                   command=self.Student)
        self.add_book_btn.place(x=200, y=380)
        self.add_book_btn = Button(self.right, text='ADD BOOK OR DELETE BOOK', font=fonts, bg='firebrick', fg='white',
                                   width=25, command=self.add_book)
        self.add_book_btn.place(x=200, y=450)
    
        self.add_book_btn = Button(self.right, text='ISSUE/RETURN BOOK', font=fonts, bg='firebrick', fg='white',
                                   width=25, command=self.issue_return)
        self.add_book_btn.place(x=200, y=520)
        self.add_book_btn = Button(self.right, text='PRE-BOOKING REQUEST', font=fonts, bg='firebrick', fg='white',
                                   width=25, command=self.pre_request)
        self.add_book_btn.place(x=200, y=600)

    
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

    def Student(self):
        self.right.destroy()
        Admin_obj = Student_details(root)

    def issue_return(self):
        self.right.destroy()
        Admin_obj = Issue_page(root)

    def pre_request(self):
        self.right.destroy()
        Admin_obj = Request_page(root)


class profile_page(Login_page):
    def __init__(self, root, admin_id):
        self.root = root
        self.root.title("Profile page")
        self.page = Frame(self.root, width=1500, height=800)
        self.page.place(x=0, y=0)

        self.image = Image.open('../assets/profilebg.png')
        self.image = self.image.resize((1550,800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page,image=self.image)
        self.image_label.image=self.image
        self.image_label.place(x=0,y=0)


        mycursor.execute("SELECT * FROM Admin WHERE userid= %s", (admin_id,))
        admin_data = mycursor.fetchone()

        if admin_data:
            admin_user_label = Label(self.page, text=f"Userid: {admin_data[0]}", font=fonts2)
            admin_user_label.place(x=600, y=450)

            admin_name_label = Label(self.page, text=f"Name: {admin_data[2]}", font=fonts2)
            admin_name_label.place(x=600, y=525)

            admin_email_label = Label(self.page, text=f"Email: {admin_data[3]}", font=fonts2)
            admin_email_label.place(x=600, y=600)

            admin_phone_label = Label(self.page, text=f"Phone number: {admin_data[4]}", font=fonts2)
            admin_phone_label.place(x=600, y=675)



class Add_page:
     def __init__(self, root):
        self.root = root
        self.root.title("Book Details")
        self.page = Frame(self.root, width = 1550, height = 800)
        self.page.place(x = 0, y = 0)

        
        self.image = Image.open('../assets/book_add.png')
        self.image = self.image.resize((1550, 800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        self.book__details = Label(self.page,text="BOOK DETAILS",fg='black',font=fonts2)
        self.book__details.place(x=650,y=125)

        self.book_id = Label(self.page, text = 'Book Id:',fg ='black', font = fonts2,width=10)
        self.book_id.place(x = 500, y = 250)
        self.book_id_entry = Entry(self.page,width=20, font = fonts2)
        self.book_id_entry.place(x = 700, y = 250)

        self.book_title= Label(self.page, text = 'Book Name:',fg ='black', font = fonts2,width=10)
        self.book_title.place(x = 500, y = 325)
        self.book_title_entry = Entry(self.page,width=20, font = fonts2)
        self.book_title_entry.place(x = 700, y = 325)

        self.book_author= Label(self.page, text = 'Author:',fg ='black', font = fonts2,width=10)
        self.book_author.place(x = 500, y = 400)
        self.book_author_entry = Entry(self.page,width=20, font = fonts2)
        self.book_author_entry.place(x = 700, y = 400)

        self.book_edition= Label(self.page, text = 'Edition:',fg ='black', font = fonts2,width=10)
        self.book_edition.place(x = 500, y = 475)
        self.book_edition_entry = Entry(self.page,width=20, font = fonts2)
        self.book_edition_entry.place(x = 700, y = 475)

        self.book_status= Label(self.page, text = 'Status:',fg ='black', font = fonts2,width=10)
        self.book_status.place(x = 500, y = 550)
        self.book_status_entry = Entry(self.page,width=20, font = fonts2)
        self.book_status_entry.place(x = 700, y = 550)

        self.save_button = Button(self.page, text="ADD",width=12, font=fonts2,command=self.save_to_database)
        self.save_button.place(x=300, y=700)

        self.save_button = Button(self.page, text="DELETE",width=12, font=fonts2,command=self.delete_from_database)
        self.save_button.place(x=1000, y=700)


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

        try:
            mycursor.execute(query, values)
            mydb.commit()
            print("Deletion successful")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
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
        self.page = Frame(self.root, width=1550, height=800)
        self.page.place(x=0, y=0)

        

        self.tree = ttk.Treeview(self.page, columns=('ID', 'Name', 'Email', 'Branch', 'PhoneNumber'), show='headings', height=30)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Email', text='Email') 
        self.tree.heading('Branch', text='Branch') 
        self.tree.heading('PhoneNumber', text='Phone no')
        
        self.tree.column('ID', width=100, anchor='center')  
        self.tree.column('Name', width=250, anchor='center') 
        self.tree.column('Email', width=400, anchor='center')  
        self.tree.column('Branch', width=100, anchor='center')  
        self.tree.column('PhoneNumber', width=200, anchor='center')  
        self.tree.pack(pady=100)

        
        v_scrollbar = Scrollbar(self.page, orient=VERTICAL, command=self.tree.yview)
        v_scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=v_scrollbar.set)

     
        h_scrollbar = Scrollbar(self.page, orient=HORIZONTAL, command=self.tree.xview)
        h_scrollbar.pack(side="bottom", fill="x")
        self.tree.configure(xscrollcommand=h_scrollbar.set)

        
        mycursor.execute("SELECT * FROM student")
        student_data = mycursor.fetchall()

        
        for data in student_data:
            self.tree.insert('', 'end', values=data)



class Student_details:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Details")
        self.page = Frame(self.root, width=1550, height=800,bg='darksalmon')
        self.page.place(x=0, y=0)
        self.image = Image.open('../assets/Student_add.png')
        self.image = self.image.resize((1550, 800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.page, image=self.image)
        self.image_label.place(x=0, y=0)

        self.student__details = Label(self.page,text="STUDENT DETAILS",fg='black',font=fonts2)
        self.student__details.place(x=620,y=135)

        self.student_id = Label(self.page, text = 'Student ID:',fg ='black', font = fonts2,width=13)
        self.student_id.place(x = 450, y = 250)
        self.student_id_entry = Entry(self.page,width=20, font = fonts2)
        self.student_id_entry.place(x = 700, y = 250)

        self.student_name= Label(self.page, text = 'Student Name:',fg ='black', font = fonts2,width=13)
        self.student_name.place(x = 450, y = 325)
        self.student_name_entry = Entry(self.page,width=20, font = fonts2)
        self.student_name_entry.place(x = 700, y = 325)

        self.student_email= Label(self.page, text = 'Email:',fg ='black', font = fonts2,width=13)
        self.student_email.place(x = 450, y = 400)
        self.student_email_entry = Entry(self.page,width=20, font = fonts2)
        self.student_email_entry.place(x = 700, y = 400)

        self.student_branch= Label(self.page, text = 'Branch:',fg ='black', font = fonts2,width=13)
        self.student_branch.place(x = 450, y = 475)
        self.student_branch_entry = Entry(self.page,width=20, font = fonts2)
        self.student_branch_entry.place(x = 700, y = 475)

        self.student_phonenumber = Label(self.page, text='Phone Number:', fg='black', font=fonts2, width=13)
        self.student_phonenumber.place(x=450, y=550)
        self.student_phonenumber_entry = Entry(self.page, width=20, font=fonts2)
        self.student_phonenumber_entry.place(x=700, y=550)

        self.student_password = Label(self.page, text='Password:', fg='black', font=fonts2, width=13)
        self.student_password.place(x=450, y=625)
        self.student_password_entry = Entry(self.page, width=20, font=fonts2)
        self.student_password_entry.place(x=700, y=625)

        self.save_button = Button(self.page, text="ADD", width=12, font=fonts2, command=self.save_to_database,bg='azure3')
        self.save_button.place(x=300, y=700)

        self.save_button = Button(self.page, text="DELETE", width=12, font=fonts2, command=self.delete_from_database,bg='azure3')
        self.save_button.place(x=1000, y=700)


    def save_to_database(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_email= self.student_email_entry .get()
        student_branch =self.student_branch_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        student_password=self.student_password_entry.get()

        query = "INSERT INTO Student (userid,Name,Email,Branch,PhoneNumber,password) VALUES (%s, %s, %s, %s,%s,%s)"
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


        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Satvika@777",
            database="libraray_database"
        )
        mycursor = mydb.cursor()



        query = "DELETE FROM Student WHERE userid=%s AND Name = %s AND Email = %s AND Branch = %s AND PhoneNumber = %s AND password=%s"
        values = (student_id,student_name,student_email, student_branch,student_phonenumber,student_password)

        try:
            mycursor.execute(query, values)
            mydb.commit()
            print("Deletion successful")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            mycursor.close()
            mydb.close()

        self.student_id_entry.delete(0, 'end')
        self.student_name_entry.delete(0, 'end')
        self.student_email_entry.delete(0, 'end')
        self.student_branch_entry.delete(0, 'end')
        self.student_phonenumber_entry.delete(0, 'end')
        self.student_password_entry.delete(0,'end')

class Issue_page:
    def __init__(self, root):
        self.root = root
        self.root.title("ISSUE OR RETURN BOOK")
        self.page = Frame(self.root, width=1550, height=800)
        self.page.place(x=0, y=0)


class Request_page:
    def __init__(self, root):
        self.root = root
        self.root.title("PRE-BOOKING REQUEST")
        self.page = Frame(self.root, width=1550, height=800)
        self.page.place(x=0, y=0)


class Student_page:
    def __init__(self, root):
        self.root = root
        self.root.title('STUDENT DASHBOARD')
        self.left = Frame(self.root, width=1550, height=800)
        self.left.place(x=0, y=0)

        self.image = Image.open('../assets/login.png')
        self.image = self.image.resize((1550, 800))
        self.image = ImageTk.PhotoImage(self.image)
        self.image_label = Label(self.left, image=self.image)
        self.image_label.place(x=0, y=0)
        

        self.back_image = Image.open('../assets/backicon.png')
        self.back_image = self.back_image.resize((40, 40))
        self.back_image = ImageTk.PhotoImage(self.back_image)
        self.back_button = Label(self.left, image=self.back_image, bg='gray', bd=0)
        self.back_button.image=self.back_image
        self.back_button.place(x=10, y=750)
        self.back_button.bind('<Button-1>',self.go_back)
                              

        self.student__login = Label(self.left, text="HELLO ENTHUSIASTS!", fg='red', font=fonts3)
        self.student__login.place(x=250, y=40)

        self.history_btn = Button(self.left, text='Book Store', font=fonts2, command=self.book_store_next, width=20)
        self.history_btn.place(x=300, y=250)

        self.book_store_btn = Button(self.left, text='Request Status', font=fonts2, command=self.request_status_next,
                                      width=20)
        self.book_store_btn.place(x=300, y=350)

        self.book_store_btn = Button(self.left, text='Wishlist', font=fonts2, command=self.wishlist_next, width=20)
        self.book_store_btn.place(x=300, y=450)

       
    def wishlist_next(self):
        self.left.destroy()
        wishlist_obj = Wishlist_page(root)

    def request_status_next(self):
        self.left.destroy()
        request_status_obj = Request_status_page(root)

    def book_store_next(self):
        self.left.destroy()
        store_obj = book_store_page(root)

    def go_back(self,event):    
        self.left.destroy()
        std_obj=Login_page(root)


class Wishlist_page:
    def __init__(self, root):
        self.root = root
        self.root.title("WISHLIST")
        self.page = Frame(self.root, width=1550, height=800)
        self.page.place(x=0, y=0)


class Request_status_page:
    def _init_(self, root):
        self.root = root
        self.root.title("REQUEST STATUS")
        self.page = Frame(self.root, width=1550, height=800)
        self.page.place(x=0, y=0)


class book_store_page:
    def __init__(self, root):
        self.root = root
        self.root.title("BOOK STORE")
        self.left = Frame(self.root, width=1500, height=800)
        self.left.place(x=0, y=0)


root.geometry(f"{window_width}x{window_height}+{screen_width//2 - window_width//2}+{screen_height//2 - window_height//2}")
home = welcome_page(root)
root.mainloop()