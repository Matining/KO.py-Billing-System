import os, tempfile
import time, math
from tkinter import *
from tkinter import messagebox

def products():
    global receipt_text

    root1 = Toplevel()
    root1.grab_set()
    root1.title('PRODUCTS')
    root1.config(bg='burlywood3')
    root1.resizable(False, False)
    root1.geometry("1300x700")

    root1.rowconfigure(1, weight=1)
    root1.columnconfigure(1, weight=1)

    root1.grab_set()
    root1.title('PRODUCTS')

    ProductsFrame = LabelFrame(root1, font=('arial', 16, 'bold'), bd=6, bg='burlywood3', relief=GROOVE, fg='black',
                               width=900, height=500)
    ProductsFrame.grid(row=0, column=0, padx=40, pady=20)

    ReceiptFrame = LabelFrame(root1, font=('arial', 16, 'bold'), bg='burlywood3', relief=GROOVE, fg='black',
                              width=400, height=700)
    ReceiptFrame.grid(row=0, column=1, padx=5, pady=20, sticky="n")

    canvas = Canvas(ProductsFrame, bg='burlywood3', bd=0, relief='flat', height=600, width=800)
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(ProductsFrame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    frame_buttons = Frame(canvas, bg='burlywood3')
    canvas.create_window((0, 0), window=frame_buttons, anchor='nw')

    img1 = PhotoImage(file=r"./pics/belgian2.png")
    img2 = PhotoImage(file=r"./pics/Dolce Latte.png")
    img3 = PhotoImage(file=r"./pics/original.png")
    img4 = PhotoImage(file=r"./pics/white mocha .png")
    img5 = PhotoImage(file=r"./pics/chocolate.png")
    img6 = PhotoImage(file=r"./pics/fraffe.png")
    img7 = PhotoImage(file=r"./pics/Hot Espresso.png")
    img8 = PhotoImage(file=r"./pics/Hot Americano.png")
    img9 = PhotoImage(file=r"./pics/Hot flatwhite.png")
    img10 = PhotoImage(file=r"./pics/Hot Vienna.png")
    img11 = PhotoImage(file=r"./pics/Hot Mocha.png")
    img12 = PhotoImage(file=r"./pics/Hot Cappuccino.png")
    img13 = PhotoImage(file=r"./pics/waffles.png")
    img14 = PhotoImage(file=r"./pics/Burgerfries.png")
    img15 = PhotoImage(file=r"./pics/Fries.png")
    img16 = PhotoImage(file=r"./pics/Bowl Nachos.png")
    img17 = PhotoImage(file=r"./pics/Hungarian.png")
    img18 = PhotoImage(file=r"./pics/pizza.png")

    receipt_text = Text(ReceiptFrame, height=25, width=100, wrap=WORD)
    receipt_text.pack(side=TOP)

    receipt_text.insert(END, "Product\t\tQuantity\t\tPrice\n", )
    receipt_text.pack(pady=10, padx=10)

    total_price_var = DoubleVar(value=0.0)


    def add_to_receipt(item_name, item_price_str):
        item_price = float(item_price_str)
        current_text = receipt_text.get("1.0", "end-1c")
        lines = current_text.split("\n")

        total_price = total_price_var.get()

        for i, line in enumerate(lines):
            if item_name in line:
                # Product already in the receipt, update the quantity and price
                parts = line.split("\t\t")
                quantity = int(parts[1].strip())
                new_quantity = quantity + 1
                new_price = new_quantity * item_price
                new_line = f"{item_name}\t\t{new_quantity}\t\t₱{new_price:.2f}"
                lines[i] = new_line
                total_price += item_price
                break
        else:
            # Product not in the receipt, add a new entry
            new_line = f"{item_name}\t\t1\t\t₱{item_price:.2f}"
            lines.append(new_line)
            total_price += item_price

        updated_text = "\n".join(lines)
        receipt_text.delete("1.0", "end")
        receipt_text.insert("1.0", updated_text)

        total_price_var.set(total_price)


    def create_menu_button(image, item_name, item_price, row, column):
        button = Button(frame_buttons, image=image, text=f"{item_name}\nPrice: ₱{item_price}", compound=TOP,
                        bg="#090b17", font=('arial', 5, 'bold'), relief=FLAT, width=270, height=200,
                        command=lambda name=item_name, price=item_price: add_to_receipt(name, price))
        button.grid(row=row, column=column, padx=0, pady=0)
        return button

    Cold_Label = Label(frame_buttons, text='COLD COFFEE', font=('times new roman', 28, 'bold'), bg='burlywood3',
                       fg='black')
    Cold_Label.grid(row=0, column=0, columnspan=3)

    # First Row
    img1_button_cold = create_menu_button(img1, "Belgian Choco", 130, 1, 0)
    img2_button_cold = create_menu_button(img2, "Dolce Latte", 160, 1, 1)
    img3_button_cold = create_menu_button(img3, "Original", 130, 1, 2)

    # Second Row
    img4_button_cold = create_menu_button(img4, "White Mocha", 160, 2, 0)
    img5_button_cold = create_menu_button(img5, "Chocolate", 130, 2, 1)
    img6_button_cold = create_menu_button(img6, "Choco Frappe", 160, 2, 2)

    # Hot Coffee Label
    Hot_Label = Label(frame_buttons, text='HOT COFFEE', font=('times new roman', 28, 'bold'), bg='burlywood3',
                      fg='black')
    Hot_Label.grid(row=3, column=0, columnspan=3)

    # First Row (Hot Coffee)
    img7_button_hot = create_menu_button(img7, "Espresso", 99, 4, 0)
    img8_button_hot = create_menu_button(img8, "Americano", 99, 4, 1)
    img9_button_hot = create_menu_button(img9, "Flat White", 99, 4, 2)

    # Second Row (Hot Coffee)
    img10_button_hot = create_menu_button(img10, "Cafe Vienna", 120, 5, 0)
    img11_button_hot = create_menu_button(img11, "Cafe Mocha", 120, 5, 1)
    img12_button_hot = create_menu_button(img12, "Cappucino", 120, 5, 2)

    # Foods
    Foods_Label = Label(frame_buttons, text='FOODS', font=('times new roman', 28, 'bold'), bg='burlywood3', fg='black')
    Foods_Label.grid(row=6, column=0, columnspan=3)

    # First Row (Foods)
    img13_button_foods = create_menu_button(img13, "Waffles", 100, 7, 0)
    img14_button_foods = create_menu_button(img14, "Hungarian Sandwich", 150, 7, 1)
    img15_button_foods = create_menu_button(img15, "Overload fries", 130, 7, 2)

    # Second Row (Foods)
    img16_button_foods = create_menu_button(img16, "Nachos", 130, 8, 0)
    img17_button_foods = create_menu_button(img17, "Burger with Fries", 150, 8, 1)
    img18_button_foods = create_menu_button(img18, "Pizza", 250, 8, 2)

    frame_buttons.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    total_label = Label(ReceiptFrame, textvariable=total_price_var, font=('arial', 14, 'bold'), bg='burlywood3', fg='black')
    total_label.pack(side=TOP, pady=10)

    totalbutton = Button(ReceiptFrame, text='PLACE ORDER', font=('arial', 15, 'bold'), bg='gray20', fg='white', bd=5,
                         width=15, pady=10, command=print_user)
    totalbutton.pack(fill=X)

    root1.mainloop()


def print_user():
    if receipt_text.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        content =receipt_text.get(1.0, END)
        file = tempfile.mktemp('.txt')
        with open(file, 'w', encoding="utf-8") as f:
            f.write(content)
            os.startfile(file, 'print')
def real_time():
    global time_string
    time_string = time.strftime('%A, %B %d, %Y \n%H:%M:%S %p')
    DateLabel.config(text=time_string)
    DateLabel.after(1000, real_time)


def clear():
    for entry in entries:
        entry.delete(0, END)
        entry.insert(0, '0')

    textarea.configure(state='normal')
    TOTAL_entry.delete(0, END)
    coffee_taxentry.delete(0, END)
    TotalPrice_entry.delete(0, END)
    textarea.delete(1.0, END)
    nameEntry.delete(0, END)
    receiptnameEntry.delete(0, END)
    TenderedCashentry.delete(0, END)

    dir_path = r'bills/'
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1


def printbill():
    if textarea.get(1.0, END) == '\n':
        messagebox.showerror('Error', 'Bill is Empty')
    else:
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0, END))
        os.startfile(file, 'print')


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == receiptnameEntry.get():
            f = open(f'bills/{i}', 'r')
            textarea.delete(1.0, END)
            for data in f:
                textarea.insert(END, data)
            f.close()
            textarea.configure(state='disabled')
            break
    else:
        messagebox.showerror('Error', 'Invalid Bill Number')


if not os.path.exists('bills'):
    os.mkdir('bills')


def save_bill():
    billcontent = textarea.get(1.0, END)
    file = open(f'bills/{receipt}.txt', 'w')
    file.write(billcontent)
    file.close()
    messagebox.showinfo('Success', f'Bill number {receipt} is saved  successfully!')


def billarea():
    global product, y, receipt

    dir_path = r'bills/'
    count = 0
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1

    count += 1
    receipt = f'{count:04}'

    if nameEntry.get() == '':
        messagebox.showerror('Error', 'Customer Details are Required')
    elif TOTAL_entry.get() == '':
        messagebox.showerror('Error', 'No Products are Selected')
    elif TOTAL_entry.get() == '0 pesos':
        messagebox.showerror('Error', 'No Products are Selected')
    else:
        textarea.delete(1.0, END)
        textarea.insert(END, '\t******WELCOME CUSTOMER******\n\n')
        textarea.insert(END, f'{time_string}\n\n')
        textarea.insert(END, f'Receipt Number: {receipt}\n')
        textarea.insert(END, f'Customer Name: {nameEntry.get()}\n')
        textarea.insert(END, '\n============================================\n')
        textarea.insert(END, f'Product\t\t  Quantity\t\t  Price')
        textarea.insert(END, '\n============================================\n')
        Cash = TenderedCashentry.get()
        Change = int(Cash) - totalbill
        index = 0
        str(selected)
        while index < len(entries):
            for entry in entries:
                product = entry.get()
                if product != '0':
                    textarea.insert(END, f'\n{ProductList[index]}\t\t\t{product}\t  {selected[index]}.00')
                index += 1
        textarea.insert(END, '\n\n-------------------------------------------\n')
        textarea.insert(END, f'  TOTAL\t\t\t\t  {totalbill}.00\n')
        textarea.insert(END, f'\n  CASH\t\t\t\t  {TenderedCashentry.get()}.00\n') # Cash received
        textarea.insert(END, f'  CHANGE\t\t\t\t  {Change}.00')
        textarea.insert(END, '\n-------------------------------------------')

        textarea.insert(END, f'\nVATable Sales\t\t\t\t  {price}.00') #no tax yet
        if coffee_taxentry.get():
            textarea.insert(END, f'\nVAT AMOUNT\t\t\t\t  {coffee_taxentry.get()}')
        textarea.insert(END, '\n-------------------------------------------')
        textarea.insert(END, '\n\t\t THANK YOU!')
        textarea.configure(state='disabled')
        save_bill()


def total():
    global entries, selected, price, totalbill

    selected = []
    index = 0
    while index < len(entries):
        for entry in entries:
            product = entry.get()
            if index == 0 :
                Original = int(product) * 130
                selected.append(Original)
            elif index == 1:
                Belgian = int(product) * 130
                selected.append(Belgian)
            elif index == 2:
                Chocolate = int(product) * 130
                selected.append(Chocolate)
            elif index == 3:
                IcedMocha = int(product) * 160
                selected.append(IcedMocha)
            elif index == 4:
                Dolce = int(product) * 160
                selected.append(Dolce)
            elif index == 5:
                C_Cappuccino = int(product) * 160
                selected.append(C_Cappuccino)
            elif index == 6:  # HOT COFFEE
                Espresso = int(product) * 99
                selected.append(Espresso)
            elif index == 7:
                Americano = int(product) * 99
                selected.append(Americano)
            elif index == 8:
                FlatWhite = int(product) * 99
                selected.append(FlatWhite)
            elif index == 9:
                Vienna = int(product) * 120
                selected.append(Vienna)
            elif index == 10:
                CafeMoch = int(product) * 120
                selected.append(CafeMoch)
            elif index == 11:
                H_Cappuccino = int(product) * 120
                selected.append(H_Cappuccino)
            elif index == 12:  # FOOD
                Waffles = int(product) * 100
                selected.append(Waffles)
            elif index == 13:
                Hungarian = int(product) * 150
                selected.append(Hungarian)
            elif index == 14:
                Over_Fries = int(product) * 130
                selected.append(Over_Fries)
            elif index == 15:
                Nachos = int(product) * 130
                selected.append(Nachos)
            elif index == 16:
                BFries = int(product) * 150
                selected.append(BFries)
            elif index == 17:
                Pizza = int(product) * 250
                selected.append(Pizza)
            index += 1
    tuple(selected)
    price = sum(selected)

    TOTAL_entry.delete(0, END)
    TOTAL_entry.insert(0, f'{price}.00 pesos')

    coffeetax = price * 0.2
    coffee_taxentry.delete(0, END)
    coffee_taxentry.insert(0, "%.2f" % coffeetax)

    totalbill = price + coffeetax
    totalbill = int(math.ceil(totalbill))
    TotalPrice_entry.delete(0, END)
    TotalPrice_entry.insert(0, f'{totalbill}.00 pesos')


root = Tk()
root.title("Koffee.py Billing System")
root.geometry('1570x858')
headingLabel = Label(root, text='KO.PY BILLING SYSTEM', font=('times new roman', 50, 'bold'), bg='burlywood3', bd=12,
                     relief=GROOVE, pady=20)

headingLabel.pack(fill=X)

customer_details = LabelFrame(root, text='Customer details', font=('times new roman', 15, 'bold'), bg='burlywood3',
                              bd=8, relief=RIDGE)
customer_details.pack(fill=X)

nameLabel = Label(customer_details, text='Name', font=('times new roman', 15, 'bold'), bg='burlywood3', fg='black')
nameLabel.grid(row=0, column=0, padx=20)

nameEntry = Entry(customer_details, font=('arial', 15), bd=7, width=18)
nameEntry.grid(row=0, column=1, padx=(8, 30))

ProductsButton = Button(customer_details, text='ORDER HERE', font=('arial', 12, 'bold'), bd=7, width=20,
                        command=products)
ProductsButton.grid(row=0, column=2, padx=(30, 20), pady=8)

ReceiptLabel = Label(customer_details, text='Receipt No.', font=('times new roman', 15, 'bold'), bg='burlywood3',
                     fg='black')
ReceiptLabel.grid(row=0, column=3, padx=20, pady=2)

receiptnameEntry = Entry(customer_details, font=('arial', 15), bd=7, width=18)
receiptnameEntry.grid(row=0, column=4, padx=8)

searchButton = Button(customer_details, text='SEARCH', font=('arial', 12, 'bold'), bd=7, width=10, command=search_bill)
searchButton.grid(row=0, column=5, padx=10, pady=8)

DateLabel = Label(customer_details, font=('times new roman', 14, 'bold'), bg='burlywood3', fg='black')
DateLabel.grid(row=0, column=6, padx=(80, 0))

real_time()

productsFrame = Frame(root)
productsFrame.pack(fill=X)

entries = []
ProductList = ["Original", "Belgian Chocolate", "Chocolate", "Iced Mocha", "Dolce Latte", "Cappuccino",
                  "Espresso", "Americano", "Flat White", "Cafe Vienna", "Cafe Mocha", "Cappuccino",
                  "Waffles", "Hungarian Sandwich", "Overload Fries", "Nachos", "Burger with Fries", "Pizza"]

ColdCoffeeFrame = LabelFrame(productsFrame, text='COLD COFFEE', font=('times new roman', 15, 'bold'), bg='peachpuff3',
                             bd=7,relief=RIDGE)
ColdCoffeeFrame.grid(row=0, column=0)

i = 0
j = 0
while i < 6:
    Label(ColdCoffeeFrame, text=ProductList[i], font=('times new roman', 15, 'bold'), bg='peachpuff3',
          fg='black').grid(
        padx=(10, 10), pady=13)
    i += 1

while j < 6:
    en = Entry(ColdCoffeeFrame, font=('arial', 15), bd=5, width=15)
    en.grid(row=j, column=1, padx=5)
    en.insert(0, '0')
    entries.append(en)
    j += 1

HotFrame = LabelFrame(productsFrame, text='HOT COFFEE', font=('times new roman', 15, 'bold'), bg='peachpuff3', bd=8,
                      relief=RIDGE)
HotFrame.grid(row=0, column=1)

i = 0
j = 0
ind = 6

while i < 6:
    Label(HotFrame, text=ProductList[ind], font=('times new roman', 15, 'bold'), bg='peachpuff3', fg='black').grid(
        padx=(15, 15), pady=13)
    ind += 1
    i += 1

while j < 6:
    en = Entry(HotFrame, font=('arial', 15), bd=5, width=15)
    en.grid(row=j, column=1, padx=7)
    en.insert(0, '0')
    entries.append(en)
    j += 1

FoodFrame = LabelFrame(productsFrame, text='FOOD', font=('times new roman', 15, 'bold'), bg='peachpuff3', bd=8,
                       relief=RIDGE)
FoodFrame.grid(row=0, column=2)

i = 0
j = 0
indx = 12

while i < 6:
    Label(FoodFrame, text=ProductList[indx], font=('times new roman', 15, 'bold'), bg='peachpuff3', fg='black').grid(
        padx=(12, 12), pady=13)
    indx += 1
    i += 1

while j < 6:
    en = Entry(FoodFrame, font=('arial', 15), bd=5, width=15)
    en.grid(row=j, column=1, padx=7)
    en.insert(0, '0')
    entries.append(en)
    j += 1

bill_frame = Frame(productsFrame, bd=8, relief=GROOVE)
bill_frame.grid(row=0, column=3)

bill_areaLabel = Label(bill_frame, text='Bill Area', font=('times new roman', 16, 'bold'), bd=7, relief=GROOVE)
bill_areaLabel.pack(fill=X)

scrollbar = Scrollbar(bill_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

textarea = Text(bill_frame, height=19, width=44, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

bill_menuFrame = LabelFrame(root, text='BILL MENU', font=('times new roman', 13, 'bold'), bg='burlywood3', bd=8,
                            relief=RIDGE)
bill_menuFrame.pack(fill=X)

Total = Label(bill_menuFrame, text='Price', font=('times new roman', 15, 'bold'), bg='burlywood3', fg='black')
Total.grid(row=0, column=0, padx=(50, 4), pady=6, sticky='W')
TOTAL_entry = Entry(bill_menuFrame, font=('arial', 15), bd=5, width=18)
TOTAL_entry.grid(row=0, column=1, padx=(4, 0), pady=6, sticky='W')

coffee_tax = Label(bill_menuFrame, text='Additional tax', font=('times new roman', 15, 'bold'), bg='burlywood3',
                   fg='black')
coffee_tax.grid(row=1, column=0, padx=(30, 0), pady=6, sticky='W')
coffee_taxentry = Entry(bill_menuFrame, font=('arial', 15), bd=5, width=18)
coffee_taxentry.grid(row=1, column=1, padx=(4, 50), pady=6, sticky='W')

TotalPrice = Label(bill_menuFrame, text='TOTAL', font=('times new roman', 15, 'bold'), bg='burlywood3', fg='black')
TotalPrice.grid(row=0, column=3, padx=(30, 0), pady=6, sticky='W')
TotalPrice_entry = Entry(bill_menuFrame, font=('arial', 15), fg='red', bd=5, width=18)
TotalPrice_entry.grid(row=0, column=4, padx=(4, 100), pady=6, sticky='W')

TenderedCash = Label(bill_menuFrame, text='CASH', font=('times new roman', 15, 'bold'), bg='burlywood3', fg='black')
TenderedCash.grid(row=1, column=3, padx=(30, 0), pady=6, sticky='W')
TenderedCashentry = Entry(bill_menuFrame, font=('arial', 15), fg='red', bd=5, width=18)
TenderedCashentry.grid(row=1, column=4, padx=(4, 100), pady=6, sticky='W')

button_frame = Button(bill_menuFrame, bd=8, relief=GROOVE)
button_frame.grid(row=0, column=5, rowspan=3, pady=20, padx=(100, 0))

total_button = Button(button_frame, text='TOTAL', font=('arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                      pady=10, command=total)
total_button.grid(row=0, column=0, pady=20, padx=5)

bill_button = Button(button_frame, text='BILL', font=('arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                     pady=10, command=billarea)
bill_button.grid(row=0, column=1, pady=20, padx=5)

print_button = Button(button_frame, text='PRINT', font=('arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                      pady=10, command=printbill)
print_button.grid(row=0, column=2, pady=20, padx=5)

clear_button = Button(button_frame, text='CLEAR', font=('arial', 15, 'bold'), bg='gray20', fg='white', bd=5, width=8,
                      pady=10, command=clear)
clear_button.grid(row=0, column=3, pady=20, padx=5)

root.mainloop()