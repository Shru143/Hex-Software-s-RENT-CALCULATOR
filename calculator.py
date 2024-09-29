import tkinter as tk
from tkinter import messagebox

def calculate_rent():
    """
    Function to calculate total rent and additional charges based on user input
    """
    try:
        # Get input values
        persons = int(persons_input.get())
        rent = float(rent_input.get())
        food_charges = float(food_input.get())
        water_charges = float(water_input.get())
        electricity_charges = float(electricity_input.get())
        other_expenses = float(other_expenses_input.get())
        months = int(months_input.get())

        if persons <= 0 or rent < 0 or food_charges < 0 or water_charges < 0 or electricity_charges < 0 or other_expenses < 0 or months <= 0:
            raise ValueError("Values cannot be negative or zero")

        total_monthly_cost = rent + food_charges + water_charges + electricity_charges + other_expenses

        total_cost = total_monthly_cost * months

        per_person_monthly_cost = total_monthly_cost / persons
        per_person_total_cost = total_cost / persons

        result_label.config(
            text=f"Total Monthly Cost: ₹{total_monthly_cost:.2f}\n"
                 f"Total for {months} months: ₹{total_cost:.2f}\n"
                 f"Each Person Pays Monthly: ₹{per_person_monthly_cost:.2f}\n"
                 f"Each Person Pays Total for {months} months: ₹{per_person_total_cost:.2f}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
        result_label.config(text="")

def clear_inputs():
    """
    Function to clear all input fields
    """
    persons_input.set("")
    rent_input.set("")
    food_input.set("")
    water_input.set("")
    electricity_input.set("")
    other_expenses_input.set("")
    months_input.set("")
    result_label.config(text="")

window = tk.Tk()
window.title("Rent Calculator")
window.geometry("400x500")
window.configure(bg="light blue")

persons_input = tk.StringVar()
rent_input = tk.StringVar()
food_input = tk.StringVar()
water_input = tk.StringVar()
electricity_input = tk.StringVar()
other_expenses_input = tk.StringVar()
months_input = tk.StringVar()

title_label = tk.Label(window, text="Rent Calculator", font=('Arial', 18, 'bold'), bg="light blue")
title_label.pack(pady=10)

tk.Label(window, text="Number of Persons:", font=('Arial', 12), bg="light blue").pack(pady=5)
persons_entry = tk.Entry(window, textvariable=persons_input, font=('Arial', 12))
persons_entry.pack(pady=5)

tk.Label(window, text="Monthly Rent (₹):", font=('Arial', 12), bg="light blue").pack(pady=5)
rent_entry = tk.Entry(window, textvariable=rent_input, font=('Arial', 12))
rent_entry.pack(pady=5)

tk.Label(window, text="Food Charges (₹):", font=('Arial', 12), bg="light blue").pack(pady=5)
food_entry = tk.Entry(window, textvariable=food_input, font=('Arial', 12))
food_entry.pack(pady=5)

tk.Label(window, text="Water Charges (₹):", font=('Arial', 12), bg="light blue").pack(pady=5)
water_entry = tk.Entry(window, textvariable=water_input, font=('Arial', 12))
water_entry.pack(pady=5)

tk.Label(window, text="Electricity Charges (₹):", font=('Arial', 12), bg="light blue").pack(pady=5)     
electricity_entry = tk.Entry(window, textvariable=electricity_input, font=('Arial', 12))
electricity_entry.pack(pady=5)

tk.Label(window, text="Other Expenses (₹):", font=('Arial', 12), bg="light blue").pack(pady=5)
other_expenses_entry = tk.Entry(window, textvariable=other_expenses_input, font=('Arial', 12))
other_expenses_entry.pack(pady=5)

tk.Label(window, text="Number of Months:", font=('Arial', 12), bg="light blue").pack(pady=5)
months_entry = tk.Entry(window, textvariable=months_input, font=('Arial', 12))
months_entry.pack(pady=5)

calculate_button = tk.Button(window, text="Calculate Rent", font=('Arial', 12, 'bold'), bg="light green", command=calculate_rent)
calculate_button.pack(pady=10)

clear_button = tk.Button(window, text="Clear", font=('Arial', 12, 'bold'), bg="orange", command=clear_inputs)
clear_button.pack(pady=5)

result_label = tk.Label(window, text="", font=('Arial', 12), bg="light blue")
result_label.pack(pady=10)

window.mainloop()
