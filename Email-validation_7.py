# Program to make a simple
# login screen


import tkinter as tk
import re

root=tk.Tk()
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
name_var=tk.StringVar()
email_var=tk.StringVar()



# Define a function for
# for validating an Email
def check(email):

    # pass the regular expression
    # and the string in search() method
    if(re.search(regex,email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if name == 'main' :

    # Enter the email
    email = email_var.get()

    # calling run function
    check(email)



# creating a label for
# name using widget Label
name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))

# creating an entry for input
# name using widget Entry
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))

# creating a label for password
email_label = tk.Label(root, text = 'Email', font = ('calibre',10,'bold'))

# creating an entry for password
email_entry=tk.Entry(root, textvariable = email_var, font = ('calibre',10,'normal') )

# creating a button using the widget
# Button that will call the submit function
sub_btn=tk.Button(root,text = 'Submit', command = "submit")

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0,column=0)
name_entry.grid(row=0,column=1)
email_label.grid(row=1,column=0)
email_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)

# performing an infinite loop
# for the window to display
root.mainloop()
