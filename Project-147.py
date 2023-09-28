from tkinter import *
root = Tk()
root.title("Ascii")
root.geometry("400x400")
root.configure(background="snow")
enter_word = Entry(root)
enter_word.place(relx=0.5, rely=0.4, anchor=CENTER)
label = Label(root, text="Name is ASCII: ", bg="light yellow", fg="black")
enc_label=Label(root, text="Encrypted Name: ")
def asciiConverter():
    input_word = enter_word.get()
    for letter in input_word:
        ascii=int(ord(letter))
        label["text"]+=str(ord(letter))+" "
        enc=str(ascii-1)
        enc_label["text"]+=str(chr(enc))
btn=Button(root, text="Show name in ASCII", command=asciiConverter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.6, anchor=CENTER)
enc_label.place(relx=0.5, rely=0.7, anchor=CENTER)
root.mainloop()