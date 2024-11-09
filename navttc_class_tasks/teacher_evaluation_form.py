import tkinter as tk
from tkinter import messagebox, ttk
import os


# Function to submit the form data and save to a file
def submit_form():
    teacher_name = teacher_name_var.get()
    subject = subject_var.get()

    if not teacher_name or not subject:
        messagebox.showwarning("Input Error", "Please fill out the Teacher's Name and Subject.")
        return

    # Gather selected options
    responses = {
        "Punctuality": punctuality_var.get(),
        "Knowledge": knowledge_var.get(),
        "Communication": communication_var.get(),
        "Engagement": engagement_var.get(),
        "Feedback": feedback_var.get(),
    }

    # Create a summary of the evaluation
    summary = f"Teacher Evaluation Summary\n----------------------------\n"
    summary += f"Teacher Name: {teacher_name}\n"
    summary += f"Subject: {subject}\n\n"
    for question, response in responses.items():
        summary += f"{question}: {response}\n"

    # Save the summary to a file on the user's desktop
    desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    save_path = os.path.join(desktop_path, "teacher_evaluation.txt")
    with open(save_path, "a") as file:
        file.write(summary + "\n\n")

    # Show a confirmation message
    messagebox.showinfo("Evaluation Submitted", f"Evaluation saved to {save_path}")


# Initialize the main window
root = tk.Tk()
root.title("Teacher Evaluation Form")
root.geometry("500x600")

# Create a canvas and a scrollbar
canvas = tk.Canvas(root, bg="lightblue")
scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = ttk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

# Set the background color for the scrollable frame
scrollable_frame.config(style="Custom.TFrame")

# Define a style for labels and radio buttons
style = ttk.Style()
style.configure("Custom.TLabel", background="lightblue", font=("Helvetica", 12, "bold"), foreground="navy")
style.configure("Custom.TRadiobutton", background="lightblue", font=("Helvetica", 10), foreground="black")
style.configure("Custom.TFrame", background="lightblue")

# Title labels
title_font = ("Helvetica", 18, "bold")
college_font = ("Helvetica", 14, "italic")

ttk.Label(scrollable_frame, text="Frontier College and University", font=college_font, background="lightblue",
          foreground="darkred").pack(anchor='n', pady=(20, 5))
ttk.Label(scrollable_frame, text="Teacher Evaluation", font=title_font, background="lightblue", foreground="navy").pack(
    anchor='n', pady=(0, 20))

# Variables to hold form data
teacher_name_var = tk.StringVar()
subject_var = tk.StringVar()

# Initialize variables for radio button selections
punctuality_var = tk.StringVar(value="Agree")
knowledge_var = tk.StringVar(value="Agree")
communication_var = tk.StringVar(value="Agree")
engagement_var = tk.StringVar(value="Agree")
feedback_var = tk.StringVar(value="Agree")

# Options for radio buttons
options = ["Strongly Agree", "Agree", "Disagree", "Strongly Disagree"]

# Teacher's Name
ttk.Label(scrollable_frame, text="Teacher's Name:", style="Custom.TLabel").pack(anchor='w', padx=10, pady=5)
ttk.Entry(scrollable_frame, textvariable=teacher_name_var, width=40).pack(anchor='w', padx=10, pady=5)

# Subject
ttk.Label(scrollable_frame, text="Subject:", style="Custom.TLabel").pack(anchor='w', padx=10, pady=5)
ttk.Entry(scrollable_frame, textvariable=subject_var, width=40).pack(anchor='w', padx=10, pady=5)

# Punctuality
ttk.Label(scrollable_frame, text="The teacher is punctual:", style="Custom.TLabel").pack(anchor='w', padx=10, pady=5)
for option in options:
    ttk.Radiobutton(scrollable_frame, text=option, variable=punctuality_var, value=option,
                    style="Custom.TRadiobutton").pack(anchor='w', padx=20)

# Knowledge
ttk.Label(scrollable_frame, text="The teacher has a strong knowledge of the subject:", style="Custom.TLabel").pack(
    anchor='w', padx=10, pady=5)
for option in options:
    ttk.Radiobutton(scrollable_frame, text=option, variable=knowledge_var, value=option,
                    style="Custom.TRadiobutton").pack(anchor='w', padx=20)

# Communication
ttk.Label(scrollable_frame, text="The teacher communicates effectively:", style="Custom.TLabel").pack(anchor='w',
                                                                                                      padx=10, pady=5)
for option in options:
    ttk.Radiobutton(scrollable_frame, text=option, variable=communication_var, value=option,
                    style="Custom.TRadiobutton").pack(anchor='w', padx=20)

# Engagement
ttk.Label(scrollable_frame, text="The teacher engages students in learning:", style="Custom.TLabel").pack(anchor='w',
                                                                                                          padx=10,
                                                                                                          pady=5)
for option in options:
    ttk.Radiobutton(scrollable_frame, text=option, variable=engagement_var, value=option,
                    style="Custom.TRadiobutton").pack(anchor='w', padx=20)

# Feedback
ttk.Label(scrollable_frame, text="The teacher provides constructive feedback:", style="Custom.TLabel").pack(anchor='w',
                                                                                                            padx=10,
                                                                                                            pady=5)
for option in options:
    ttk.Radiobutton(scrollable_frame, text=option, variable=feedback_var, value=option,
                    style="Custom.TRadiobutton").pack(anchor='w', padx=20)

# Submit Button at the bottom of the form
ttk.Button(scrollable_frame, text="Submit Evaluation", command=submit_form, style="Custom.TLabel").pack(pady=20)

# Pack the canvas and scrollbar
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Start the Tkinter event loop

root.mainloop()
