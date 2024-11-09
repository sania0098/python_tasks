############# TO UNDERSTAND GUI  HERE IS SIMPLE PROJECT


# import tkinter as tk
# from tkinter import messagebox
#
# # Create the main application window
# root = tk.Tk()
# root.title("Simple Tkinter App")
#
# # Set the window size
# root.geometry("500x300")
#
# # Function to be called when the button is clicked
# def on_button_click():
#     messagebox.showinfo("Hello", "Hello, Tkinter!")
#
# # Create a label widget
# label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 19))
# label.pack(pady=30)
#
# # Create a button widget
# button = tk.Button(root, text="Click Me", command=on_button_click, font=("Arial", 12))
# button.pack(pady=10)
#
# # Start the Tkinter event loop
# root.mainloop()



##################STUDENT REGISTRATION FORM
import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x400")

# Function to handle form submission
def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    course = course_var.get()

    if name and age and gender and course:
        messagebox.showinfo("Form Submission", f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}")
    else:
        messagebox.showwarning("Form Incomplete", "Please fill in all fields")

# Labels and Entry widgets for the form
label_title = tk.Label(root, text="Student Registration Form", font=("Arial", 16))
label_title.pack(pady=20)

label_name = tk.Label(root, text="Name:", font=("Arial", 12))
label_name.pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 12))
entry_name.pack(pady=5)

label_age = tk.Label(root, text="Age:", font=("Arial", 12))
label_age.pack(pady=5)
entry_age = tk.Entry(root, font=("Arial", 12))
entry_age.pack(pady=5)

label_gender = tk.Label(root, text="Gender:", font=("Arial", 12))
label_gender.pack(pady=5)

# Gender Radio Buttons
gender_var = tk.StringVar(value="Male")
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", font=("Arial", 12))
radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", font=("Arial", 12))
radio_male.pack(pady=5)
radio_female.pack(pady=5)

label_course = tk.Label(root, text="Course:", font=("Arial", 12))
label_course.pack(pady=5)

# Course Dropdown (OptionMenu)
course_var = tk.StringVar(value="Select Course")
course_menu = tk.OptionMenu(root, course_var, "Computer Science", "Mathematics", "Physics", "Chemistry", "Biology")
course_menu.config(font=("Arial", 12))
course_menu.pack(pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_form, font=("Arial", 12))
submit_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
