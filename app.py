import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
root = tk.Tk()

canvas = tk.Canvas(root, height=600, width=600, bg="#242324")
canvas.grid(columnspan=3, rowspan=3)

# *Logo
logo = Image.open("logo.png")  # *Open the image
logo = ImageTk.PhotoImage(logo)  # *Loading the image as a tkinter image
logo_label = tk.Label(image=logo)  # *Placing the image in a label widget
logo_label.image = logo
logo_label.grid(column=1, row=0)  # * Load the image in the window element

# *Instructions
instructions = tk.Label(root, text="Select a file",
                        font="JetBrains", bg="#7503ad", fg="#bf9406")  # * Creating a label
# * Placing the label in our window
instructions.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("Loading...")  # * Changing the button text
    file = askopenfile(parent=root, mode="rb",
                       title="Choose a file", filetypes=[("PDF file", "*.pdf")])  # * Open a file select dialog box
    if(file):
        pdf_content = PyPDF2.PdfFileReader(file)
        page = pdf_content.getPage(0)
        page_content = page.extractText()

        # * Text box
        text_box = tk.Text(root, height=50, width=50, padx=15, pady=15)
        text_box.insert(1.0, page_content)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


# * Browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text,
                       font="JetBrains", bg="#7503ad", fg="#bf9406", command=open_file)  # * Creating a button
browse_text.set("Browse")  # *Naming the button
browse_btn.grid(column=1, row=2)  # * Placing the button


root.mainloop()
