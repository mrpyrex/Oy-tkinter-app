from tkinter import *
from tkinter import ttk
import requests
import json


root = Tk()
root.geometry("700x350")
root.title("Cat Fun Fact API ")

text = Text(root, height=10, width=50, wrap="word")
text.config(font="Arial, 12")

# Create a label widget
label = Label(root, text="Cat Fun Facts")
label.config(font="Calibri, 14")

# Add the API URL
url = 'https://catfact.ninja/fact'

# Define a function to retrieve the response
# and text attribute from the JSON response
def get_zen():
   response = requests.get(url).text
   response_info = json.loads(response)
   Fact = response_info["fact"]
   text.delete('1.0', END)
   text.insert(END, Fact)

# Create Next and Exit Button
b1 = Button(root, text="Next", command=get_zen)
b2 = Button(root, text="Exit", command=root.destroy)

label.pack()
text.pack()
b1.pack()
b2.pack()

get_zen()

root.mainloop()

