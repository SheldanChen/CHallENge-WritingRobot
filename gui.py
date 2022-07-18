import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import pandaPaint_coord
import sys
import random
import ast
import re

#A4
# paper_position_y_zheng = 0.1
# paper_position_y_fu = -0.19
#A3
paper_position_y_zheng = 0.16
paper_position_y_fu = -0.235

frameScale = [0.00026, 0.00021, 0.00016, 0.00013, 0.00009, 0.00006]

file = open("dict_word_ENCH.txt")
word_ENCH = file.read()
dict_word_ENCH = ast.literal_eval(word_ENCH)
file.close()

file = open("dict_zh2name.txt")
contents = file.read()
dictionary_CH = ast.literal_eval(contents)
file.close()

def getInput():
  EN_word = (var_text.get()).lower()
  # if(tick==0):
  listbox_update('')

  if(EN_word in contents):
    
    CH_words = dict_word_ENCH[EN_word]
    num_word = len(CH_words)
    messagebox.showinfo('Translation Done!', 'Translation done!\n'+ str(num_word) +' characters will be written.\n\nClick on "OK" and Robot will start writing.')
    
    for i in range(num_word):
      result = paper_position_y_zheng - ((paper_position_y_zheng-paper_position_y_fu)*(1+2*i))/(2*num_word)
      pandaPaint_coord.paint(CH_words[i], result, frameScale[num_word-1])
    answer = messagebox.askquestion('Success', 'Done!  \n \nWould you like to try another word?')
    if answer=="no":
      sys.exit()
    var_text.set('')
  else:
    messagebox.showerror("Word Not Found!", "Robot is not smart enough to translate this word now.")
      

def on_change(*args):
    #print(args)
          
    value = var_text.get()
    value = value.strip().lower()

    # get data from test_list
    if value == '':
        data = contents
    else:
        data = []
        for item in contents:
            if value in item.lower():
                data.append(item)  

    # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data 
    data = sorted(filter((lambda x: re.search(r'^'+var_text.get(), x, re.IGNORECASE)), data))

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):

    var_text.set(event.widget.get(event.widget.curselection()) )




rootwindow = tk.Tk()
rootwindow.title("Writing Robot")
rootwindow.configure(bg='#fef8d4')

# font setting
fontExample = ("Lucida Sans", 40, "bold")
fontExample2 = ("Lucida Sans", 30, "bold")

# put image in window
photo = tk.PhotoImage(file = "./RobotWriter.png")
photo_zoom = photo.subsample(5,5)
w = tk.Label(rootwindow, image=photo_zoom,borderwidth=0,compound="center",highlightthickness = 0,padx=0,pady=0)
w.pack()

#put the window at the center of the screen
window_width = 1640
# window_width = photo.width()
window_height = 1000
# window_height = photo.height()

# get the screen dimension
screen_width = rootwindow.winfo_screenwidth()
screen_height = rootwindow.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
rootwindow.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


#obtain list
file = open("support_words.txt")
contents = file.read().splitlines()
file.close()
random.shuffle(contents)

# add box and list
var_text = tk.StringVar()
var_text.trace('w', on_change)

entry = tk.Entry(rootwindow, textvariable=var_text, width=25, font=fontExample, background='#fef8d4')
entry.pack()

listbox = tk.Listbox(rootwindow, font=fontExample, height=3, width=25, cursor='pencil', highlightthickness=0,
                      activestyle='underline', background='#fef8d4', borderwidth=0)
listbox.pack()
listbox.bind('<<ListboxSelect>>', on_select)
listbox_update('')


#button
button = tk.Button(rootwindow, text="Translate and Write", height = 1, width = 18, 
                  bg='#8db8c1', fg='black', font=fontExample2, command=getInput,  highlightbackground= '#fef8d4')
button.pack()


#logo
photo2 = tk.PhotoImage(file = "./logo.png")
photo_zoom2 = photo2.subsample(7,7)
w2 = tk.Label(rootwindow, image=photo_zoom2, borderwidth=0,compound="center",highlightthickness = 0,padx=0,pady=0)
w2.pack()

rootwindow.mainloop()