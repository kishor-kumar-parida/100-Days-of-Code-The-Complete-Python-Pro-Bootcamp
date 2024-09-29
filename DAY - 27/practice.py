import tkinter

window = tkinter.Tk()
window.title("GUI")
window.minsize(width=500, height=300)


# padding for window
window.config(padx=20, pady=20)


# Label
my_label = tkinter.Label(text="Hello world", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
# my_label.pack()

# my_label.place(x=0, y=0)

my_label.grid(column=0, row=0)

# my_label["text"] = "Hello world"  # edit parameter
# my_label.config(text="new text")  # edit parameters


# Button
def click():
    # print("clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="click", command=click)
# button.pack()
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=10)
# input.pack()
input.grid(column=2, row=2)
print(input.get())


window.mainloop()


# ******************************** #


# # Arguments (*)
# def add(*args):
#     sum = 0
#     for arg in args:
#         sum += arg
#     return sum


# print(add(1, 2, 3))


# ******************************** #


# # kwargs (**)
# def cal(n, **kwargs):
#     # print(kwargs)
#     # for key,value in kwargs.items():
#     #     print(key)
#     #     print(value)

#     # print(kwargs["add"])

#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)


# cal(2, add=3, multiply=5)


# ******************************** #


# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")


# my_car = Car(make="Nisaan")
# print(my_car.make)
# print(my_car.model)


# ******************************** #
