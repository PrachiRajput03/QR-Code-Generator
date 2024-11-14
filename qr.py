import qrcode
from tkinter import *
from tkinter import messagebox

#Creating the window

wn = Tk()
wn.title("QR Code Generator")
wn.geometry("700x700")
wn.config(bg="SteelBlue3")

#Function to generate the QR Code and save it.

def generateCode():
    #Check if all fields are filled out
    if not text.get() or not loc.get() or not name.get() or not size.get():
        messagebox.showwarning("Input Error", "Please fill out all fields.")
        return
    try:
        qr_size = int(size.get())
        if qr_size < 1 or qr_size > 40:
            messagebox.showwarning("Input Error", "Size must be an integer between 1 and 40.")
            return
    except ValueError:
        messagebox.showwarning("Input Error", "Size must be an integer.")
        return


    try:
    #Creating a QRCode Object of the size specified by the user
        qr = qrcode.QRCode(version = int(size.get()),
                       box_size=10,
                       border=5
                       )
        qr.add_data(text.get())
        #Adding the data to be encoded to the QRCode object
        qr.make(fit=True) #Making the entire QR Code space utilized
        img = qr.make_image()
        #Generating the QRCode

        fileDirec = loc.get() + '\\' + name.get()  #Getting the directory where the file has to be save

        img.save(f"{fileDirec}.png")   #Saving the QRCode

    #Showing the pop up message on saving the file
    messagebox.showinfo("QR Code Generator","QRCode is saved successfully!")

    #Label for window
    headingFrame = Frame(wn, bg="azure", bd=5)
    headingFrame.place(relx=0.15, rely=0.05, relwidth=0.7, relheight=0.1)
    headingLabel = Label(headingFrame, text="Generate QRCode", bg="azure", font=("Times", 20, "bold"))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    #Taking the input of the text or URL to get the QRCode
    Frame1 = Frame(wn, bg="SteelBlue3")
    Frame1.place(relx=0.1, rely=0.15, relwidth=0.7, relheight=0.3)
    label1 = Label(Frame1, text="Enter the text/URL:", bg="Steelblue3", fg="azure", font=("Courier", 13, "bold"))
    label1.place(relx=0.05, rely=0.2, relheight=0.08)
    text = Entry(Frame1, font=("Century", 12))
    text.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

    #Getting input of the location to save QR Code
    Frame2 = Frame(wn, bg="SteelBlue3")
    Frame2.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.3)
    label2 = Label(Frame2, text="Enter the location to save the QR Code:", bg="SteelBlue3", fg="azure", font=("Courier", 13, "bold"))
    label2.place(relx=0.05, rely=0.2, relheight=0.08)
    loc = Entry(Frame2, font=("Century", 12))
    loc.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

    #Getting input of the QRCode image name
    Frame3 = Frame(wn, bg="SteelBlue3")
    Frame3.place(relx=0.1, rely=0.35, relwidth=0.7, relheight=0.1)
    label3 = Label(Frame3, text="Enter the name of the QRCode:", bg="SteelBlue3,", fg="azure", font=("Courier", 13, "bold"))
    label3.place(relx=0.05, rely=0.2, relheight=0.08)

    name = Entry(Frame3, font=("Century", 12))
    name.place(relx=0.05, rely=0.4, relwidth=1, relheight=0.2)

    #Getting the input of the size of the QRCode
    Frame4 = Frame(wn, bg="SteelBlue3")
    Frame4.place(relx=0.1, rely=0.45, relwidth=0.7, relheight=0.1)
    label4 = Label(Frame4, text="Enter the size from 1 to 40 with 1 being 21x21: ", bg="SteelBlue3", fg="azure", font=("Courier",13, "bold"))
    label4.place(relx=0.05, rely=0.2, relheight=0.08)
    size = Entry(Frame4, font=("Century", 12))
    size.place(relx=0.05, rely=0.4, relwidth=0.5, relheight=0.2)

    #Button to generate and save the QRCode
    button = Button(wn, text="Generate Code", font=("Courier", 15, "normal"), command=generateCode)
    button.place(relx=0.35, rely=0.6, relwidth=0.25, relheight=0.05)

    #Runs the window till it is closed manually
    wn.mainloop()

