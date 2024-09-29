import tkinter


def calculate_km():
    miles = float(miles_input.get())
    km = miles * 1.60934  # Conversion factor from miles to kilometers
    km_result_label.config(text=f"{km:.2f}")  # Update the result label


window = tkinter.Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

# Entry for miles input
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0, padx=20, pady=20)

# Label for miles
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0, padx=20, pady=20)

# Label for "is equal to"
is_equal_label = tkinter.Label(text="is equal to")
is_equal_label.grid(column=0, row=1, padx=20, pady=20)

# Label to show the result in kilometers
km_result_label = tkinter.Label(text="0")
km_result_label.grid(column=1, row=1, padx=20, pady=20)

# Label for kilometers
km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1, padx=20, pady=20)

# Button to calculate kilometers
calculate_button = tkinter.Button(text="Calculate", command=calculate_km)
calculate_button.grid(column=1, row=2, padx=20, pady=20)

window.mainloop()
