import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl


def enter_data():
    accepted = accept_var.get()
    if accepted == 'Accepted':
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()

        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = natinality_combobox.get()

            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemester = numsemester_spinbox.get()

            print('First name:', firstname, 'Last name:', lastname)
            print('Title:', title, 'Age:', age, 'Nationality:', nationality)
            print('# Courses:', numcourses, '# Semesters:', numsemester)
            print('Registration status', registration_status)
            print('*' * 30)

            filepath = r"D:\codefirst.io\Tkinter Data Entry\data.xlsx"
            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ['First name', 'Last name', 'Title', 'Age', 'Nationality',
                           '# Courses', '# Semesters', 'Registration Status']
                sheet.append(heading)
                workbook.save(filepath)

            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append([firstname, lastname, title, age, nationality, numcourses, numsemester, registration_status])
            workbook.save(filepath)
        else:
            tkinter.messagebox.showwarning(title='Error', message='Please enter both First name and Last name')
    else:
        tkinter.messagebox.showwarning(title='Error', message='You have not accepted the terms')

# Assuming the rest of the Tkinter GUI setup code follows...
