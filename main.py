from tkinter import *

back_ground = "#2c2c2c"
content_color = "#0d121a"
title_window = "goof"
x_axis = None
y_axis = None

root = Tk()

root.overrideredirect(True)
root.geometry('600x300')
root.resizable(width=False, height=False)

title_bar = Frame(root, bg=back_ground, relief='raised', bd=1, highlightcolor=back_ground,highlightthickness=0)

close_button = Button(title_bar, text='x',  command=root.destroy,bg=back_ground, padx=10, pady=4, activebackground="red", bd=0,font="bold", fg='white',activeforeground="white", highlightthickness=0)
title_name = Label(title_bar, text=title_window, bg=back_ground, fg="white")
window = Canvas(root, bg="#0d121a", highlightthickness=0)

title_bar.pack(expand=1, fill=X)
title_name.pack(side=LEFT)
close_button.pack(side=RIGHT)
window.pack(expand=1, fill=BOTH)

def move_window(event):
    root.geometry('+{0}+{1}'.format(event.x_root, event.y_root))


def change_on_hovering(event):
    global close_button
    close_button['bg'] = 'red'


def return_to_normal_state(event):
   global close_button
   close_button['bg'] = back_ground


title_bar.bind('<B1-Motion>', move_window)
close_button.bind('<Enter>', change_on_hovering)
close_button.bind('<Leave>', return_to_normal_state)

root.mainloop()
