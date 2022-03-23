import tkinter


def miles_to_km():
    miles = float(mile_input.get())
    km = miles * 1.689
    result_in_km.config(text=f"{km}")


window = tkinter.Tk()
window.title("Oscar's Window")
window.config(padx=20, pady=20)

mile_input = tkinter.Entry(width=7)
mile_input.grid(column=2, row=1)

mile_label = tkinter.Label(text="Miles", font=("Arial", 12, "bold"))
mile_label.grid(column=3, row=1)

is_equal_to = tkinter.Label(text="is equal to", font=("Arial", 12, "bold"))
is_equal_to.grid(column=1, row=2)

result_in_km = tkinter.Label(text="0", font=("Arial", 12, "bold"))
result_in_km.grid(column=2, row=2)

km_label = tkinter.Label(text="Km", font=("Arial", 12, "bold"))
km_label.grid(column=3, row=2)

calculate_button = tkinter.Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=2, row=3)

# # label
# my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
# my_label.place(x=250, y=30)
# my_label.grid(column=1, row=1)
#
#
# # button
#
#
# def button_click():
#     new_text = inputs.get()
#     my_label.config(text=new_text)
#
#
# button = tkinter.Button(text="Click me", command=button_click)
# button.grid(column=2, row=2)
#
# # entry
#
# inputs = tkinter.Entry()
# inputs.grid(column=5, row=5)

window.mainloop()
