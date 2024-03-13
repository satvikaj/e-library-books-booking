from tkinter import Tk, Frame, Label, Entry, Button, messagebox,ttk,Scrollbar,VERTICAL, HORIZONTAL,Toplevel,Listbox,END,LEFT
from PIL import Image, ImageTk
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Satvika@777",
    database="attendence"
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
        self.admin_pass_entry = Entry(self.right, width=10, font=fonts,show="*")
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
        self.admin_id=admin_id
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
        self.add_book_btn = Button(self.right, text='REQUEST INFO', font=fonts, bg='firebrick', fg='white',width=22, command=self.request)
        self.add_book_btn.place(x=150, y=400)
       


    def go_back(self,event):    
        self.right.destroy()
        Admin_obj=Login_page(root)

    

    def profile(self, admin_id):
        self.right.destroy()
        Admin_obj = profile_page(root,admin_id)

    def student1(self):
        self.right.destroy()
    # Pass the branch of the logged-in HOD to Std_page
        Admin_obj = Std_page(root, self.admin_id)
        


    def add_student(self):
        self.right.destroy()
        Admin_obj = Student_det_page(root)

    def request(self):
        # Pass the admin_id to the Request_info class
        self.right.destroy()
        Admin_obj = Request_info(root, self.admin_id)

    


class profile_page(Login_page):
    def __init__(self, root,admin_id):
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
        self.back_button.bind('<Button-1>', self.go_back1)

    


        mycursor.execute("SELECT * FROM admin WHERE userid= %s", (self.admin_id,))
        admin_data = mycursor.fetchone()

        if admin_data:
            admin_user_label = Label(self.page, text=f"Userid: {admin_data[0]}", font=fonts)
            admin_user_label.place(x=400, y=310)

            admin_name_label = Label(self.page, text=f"Name: {admin_data[1]}", font=fonts)
            admin_name_label.place(x=400, y=340)

            admin_email_label = Label(self.page, text=f"branch: {admin_data[2]}", font=fonts)
            admin_email_label.place(x=400, y=370)

            admin_phone_label = Label(self.page, text=f"Phone number: {admin_data[3]}", font=fonts)
            admin_phone_label.place(x=400, y=400)

    def go_back1(self, event):
        self.page.destroy()
        Admin_obj = Admin_page(root,'')

class Std_page:
    def __init__(self, root, admin_id):
        self.root = root
        self.admin_id=admin_id
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


        self.refresh_requests()

    def refresh_requests(self):
        mycursor.execute("SELECT branch FROM admin WHERE userid=%s", (self.admin_id,))
        hod_branch = mycursor.fetchone()[0]
        mycursor.execute("SELECT * FROM student WHERE branch=%s", (hod_branch,))
        students = mycursor.fetchall()
        if students:
            self.tree = ttk.Treeview(self.page, columns=('ID', 'Name', 'Branch Name', 'Phone Number'), show='headings', height=20)
            self.tree.heading('ID', text='ID')
            self.tree.heading('Name', text='Name')
            self.tree.heading('Branch Name', text='Branch') 
            self.tree.heading('Phone Number', text='Phone no')
    
            self.tree.column('ID', width=250, anchor='center')  
            self.tree.column('Name', width=300, anchor='center')   
            self.tree.column('Branch Name', width=250, anchor='center')  
            self.tree.column('Phone Number', width=250, anchor='center')

            self.tree.pack(fill='both', expand=True, pady=80)
        
            # Configure column weights
            self.tree.columnconfigure(0, weight=1)  

            for student in students:
                self.tree.insert('', 'end', values=student)

            self.tree.pack(pady=80)
            v_scrollbar = Scrollbar(self.page, orient=VERTICAL, command=self.tree.yview)
            self.tree.configure(yscrollcommand=v_scrollbar.set)
 
            h_scrollbar = Scrollbar(self.page, orient=HORIZONTAL, command=self.tree.xview)
            self.tree.configure(xscrollcommand=h_scrollbar.set)
        else:
            messagebox.showinfo("No results found.")

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
        student_branch =self.student_branch_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        student_password=self.student_password_entry.get()
    
        query = "INSERT INTO student (Userid,Name,Branch,PhoneNumber,Password) VALUES (%s, %s, %s,%s,%s)"
        values = (student_id,student_name,student_branch,student_phonenumber,student_password)
        mycursor.execute(query, values)


        mydb.commit()
       

        self.student_id_entry.delete(0, 'end')
        self.student_name_entry.delete(0, 'end')
        self.student_branch_entry.delete(0, 'end')
        self.student_phonenumber_entry.delete(0, 'end')
        self.student_password_entry.delete(0,'end')
     
     
    def delete_from_database(self):
        student_id = self.student_id_entry.get()
        student_name = self.student_name_entry.get()
        student_branch =self.student_branch_entry.get()
        student_phonenumber = self.student_phonenumber_entry.get()
        student_password=self.student_password_entry.get()



        query = "DELETE FROM Student WHERE Userid=%s AND Name = %s  AND Branch = %s AND PhoneNumber = %s AND Password=%s"
        values = (student_id,student_name,student_branch,student_phonenumber,student_password)

        mycursor.execute(query,values)
        mydb.commit()
        mycursor.execute(query, values)
        mydb.commit()

        self.student_id_entry.delete(0, 'end')
        self.student_name_entry.delete(0, 'end')
        self.student_branch_entry.delete(0, 'end')
        self.student_phonenumber_entry.delete(0, 'end')
        self.student_password_entry.delete(0,'end')
     

class Request_info:
    def __init__(self, root, admin_id):
        self.root = root
        self.admin_id = admin_id
        self.root.title("Request_info")
        self.page = Frame(self.root, width=1000, height=600, bg='gray86')
        self.page.place(x=0, y=0)

        self.request_listbox = Listbox(self.page, width=100)
        self.request_listbox.pack(pady=10)

        self.accept_button = Button(self.page, text="Accept", command=self.accept_request)
        self.accept_button.pack(side=LEFT, padx=10)
        self.deny_button = Button(self.page, text="Deny", command=self.deny_request)
        self.deny_button.pack(side=LEFT)

        self.refresh_requests()

    def refresh_requests(self):
        self.request_listbox.delete(0, END)
        mycursor.execute("SELECT branch FROM admin WHERE userid=%s", (self.admin_id,))
        hod_branch = mycursor.fetchone()[0]
        mycursor.execute("SELECT * FROM requests WHERE branch=%s", (hod_branch,))
        requests = mycursor.fetchall()
        if requests:
            for request in requests:
                self.request_listbox.insert(END, f"ID: {request[0]}, Name: {request[1]}, Branch: {request[2]}, Start Date: {request[3]}, End Date: {request[4]}, periods: {request[6]}, reason: {request[5]},status: {request[7]}")
        else:
            self.request_listbox.insert(END, "No requests found.")

    def accept_request(self):
        selected_index = self.request_listbox.curselection()
        if selected_index:
            selected_request = self.request_listbox.get(selected_index)
            request_id = selected_request.split(',')[0].split(':')[1].strip()
            # Update status in database
            mycursor.execute("UPDATE requests SET status = 'Accepted' WHERE id = %s", (request_id,))
            mydb.commit()
            messagebox.showinfo("Success", "Request accepted successfully.")
            self.refresh_requests()
        else:
            messagebox.showerror("Error", "Please select a request to accept.")

    def deny_request(self):
        selected_index = self.request_listbox.curselection()
        if selected_index:
            selected_request = self.request_listbox.get(selected_index)
            request_id = selected_request.split(',')[0].split(':')[1].strip()
            # Update status in database
            mycursor.execute("UPDATE requests SET status = 'Denied' WHERE id = %s", (request_id,))
            mydb.commit()
            messagebox.showinfo("Success", "Request denied successfully.")
            self.refresh_requests()
        else:
            messagebox.showerror("Error", "Please select a request to deny.")


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

        self.history_btn = Button(self.left, text='Make request', font=fonts, command=self.make_request, width=20)
        self.history_btn.place(x=360, y=200)

        self.book_store_btn = Button(self.left, text='Request Status', font=fonts, command=self.request_status_next,
                                      width=20)
        self.book_store_btn.place(x=360, y=250)



    def go_back(self,event):    
        self.left.destroy()
        Admin_obj=Login_page(root)



    def profile(self, admin_id):
        self.left.destroy()
        profile_obj = student_profile_page(root, self.sid)


    def request_status_next(self):
        self.left.destroy()
        request_status_obj = Request_status_page(root,self.sid)

    def make_request(self):
        self.left.destroy()
        store_obj = make_req_page(root)



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

            student_phone_label = Label(self.page, text=f"Phone number: {student_data[3]}", font=fonts)
            student_phone_label.place(x=400, y=370)

            student_phone_label = Label(self.page, text=f"Branch: {student_data[2]}", font=fonts)
            student_phone_label.place(x=400, y=400)

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




class make_req_page:
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

        self.std_id = Label(self.page, text='ID:', fg='black', font=fonts, width=13)
        self.std_id.place(x=200, y=150)
        self.std_id_entry = Entry(self.page, width=30, font=fonts)
        self.std_id_entry.place(x=400, y=150)
        self.std_name = Label(self.page, text='name;', fg='black', font=fonts, width=13)
        self.std_name.place(x=200, y=200)
        self.std_name_entry = Entry(self.page, width=30, font=fonts)
        self.std_name_entry.place(x=400, y=200)

        self.std_br = Label(self.page, text='branch:', fg='black', font=fonts, width=13)
        self.std_br.place(x=200, y=250)
        self.std_br_entry = Entry(self.page, width=30, font=fonts)
        self.std_br_entry.place(x=400, y=250)
        self.f_date = Label(self.page, text='from date:', fg='black', font=fonts, width=13)
        self.f_date.place(x=200, y=300)
        self.f_date_entry = Entry(self.page, width=30, font=fonts)
        self.f_date_entry.place(x=400, y=300)
        self.t_date = Label(self.page, text='to date', fg='black', font=fonts, width=13)
        self.t_date.place(x=200, y=350)
        self.t_date_entry = Entry(self.page, width=30, font=fonts)
        self.t_date_entry.place(x=400, y=350)
        self.periods_label = Label(self.page, text='Periods:', fg='black', font=fonts, width=13)
        self.periods_label.place(x=200, y=400)
        self.periods_entry = Entry(self.page, width=30, font=fonts)
        self.periods_entry.place(x=400, y=400)
        

        self.reason = Label(self.page, text='reason', fg='black', font=fonts, width=13)
        self.reason.place(x=200, y=450)
        self.reason_entry = Entry(self.page, width=30, font=fonts)
        self.reason_entry.place(x=400, y=450)

        self.student_login_btn = Button(self.page, text='Enter', font=fonts, command=self.req_confirm,width=20,bg='azure3')
        self.student_login_btn.place(x=500, y=500)


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

    def req_confirm(self):
        id = self.std_id_entry.get()
        name = self.std_name_entry.get()
        branch = self.std_br_entry.get()
        from_date = self.f_date_entry.get()
        to_date = self.t_date_entry.get()
        reason = self.reason_entry.get()
        periods=self.periods_entry.get()

        query = "INSERT INTO requests (id, name, branch, fdate, tdate,periods, reason) VALUES (%s, %s, %s, %s, %s,%s, %s)"
        values = (id, name, branch, from_date, to_date,periods, reason)

        try:
            mycursor.execute(query, values)
            mydb.commit()
            messagebox.showinfo("Success", "Request submitted successfully.")
        except mysql.connector.Error as error:
            print("Failed to insert record into requests table:", error)
            messagebox.showerror("Error", "Failed to submit request.")

        self.std_id_entry.delete(0, 'end')
        self.std_name_entry.delete(0, 'end')
        self.std_br_entry.delete(0, 'end')
        self.f_date_entry.delete(0, 'end')
        self.t_date_entry.delete(0, 'end')
        self.reason_entry.delete(0, 'end')
        self.periods_entry.delete(0,'end')
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

        self.request_listbox = Listbox(self.page, width=100)
        self.request_listbox.pack(pady=10)

        self.refresh_requests()

    def refresh_requests(self):
        self.request_listbox.delete(0, END)
        mycursor.execute("SELECT * FROM requests WHERE id=%s", (self.userid,))
        requests = mycursor.fetchall()
        if requests:
            for request in requests:
                self.request_listbox.insert(END, f"ID: {request[0]}, Name: {request[1]}, Branch: {request[2]}, Start Date: {request[3]}, End Date: {request[4]},Period: {request[6]}, Reason: {request[5]}, Status: {request[7]}")
        else:
            self.request_listbox.insert(END, "No requests found.")


    

    def go_back(self, event):
        self.page.destroy()
        Admin_obj = Student_page(root,'')

        


root.geometry('1000x600+250+100')
home = welcome_page(root)
root.mainloop()