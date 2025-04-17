from tkinter.ttk import Label
import pandas as pd
import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()

root.title("Bookshop Management System")  # create taskbar

root.geometry('300x200')  # declare dimensions of window

lbl = Label(root, text="Welcome to the Bookshop!",
            justify='center')  # add text to window
lbl.pack(pady=10, padx=50)  # align

# add dataframe to store book information with sample book entry
book_info = {
    "Title": ["The huge Story", "Unexpected visit", "Reign of emperor"],
    "Author": ["JK Rowling", "Alexander Asimov", "George Tolkein"],
    "ISBN": ["3457", "1271", "9845"],
    "Price": ["70$", "40$", "80$"]
}

df = pd.DataFrame(book_info)

# print(df)


def book_price_chart():

    # check price field contain any non numeric value
    has_number = df["Price"].str.contains(r"\d+", regex=True)
    if has_number.all():  # check all values in "Price" is numeric

        prices = df["Price"].str.replace(
            r"[^0-9.]", "", regex=True).astype(float)
        # prices = df["Price"].astype(float)  # data cleaning string->float

        plt.bar(df['Title'],
                prices,
                width=0.5, color="orange")

        plt.title('Prices of the books')
        plt.xlabel('Title')
        plt.ylabel("Price")

        plt.grid(True)
        plt.show()
    else:
        print("Enter Numeric Value Into 'Price' field")


# create button for chart function caling
chart_btn = tk.Button(root, text="Click Me", command=book_price_chart)
chart_btn.pack(pady=10)

root.mainloop()
