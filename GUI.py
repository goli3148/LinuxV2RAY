import tkinter as tk
from tkinter import ttk

def save_info():
    protocol = protocol_entry.get()
    address = address_entry.get()
    port = port_entry.get()
    uid = uid_entry.get()
    host = host_entry.get()
    header_type = header_type_entry.get()
    network_type = network_type_entry.get()
    # You can save the information wherever you want
    
def run_process():
    # Add code to run your process here
    pass

def stop_process():
    # Add code to stop your process here
    pass

def get_default_values():
    # Function to get default values
    return {
        "protocol": "HTTP",
        "address": "example.com",
        "port": "80",
        "uid": "user123",
        "host": "localhost",
        "header_type": "application/json",
        "network_type": "IPv4"
    }

# Create main window
root = tk.Tk()
root.title("GUI")

# Create a style
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#007bff", foreground="white")

# Frame to contain input fields
input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=10)

# Default values
default_values = get_default_values()

# Protocol
protocol_label = ttk.Label(input_frame, text="Protocol:")
protocol_label.grid(row=0, column=0, padx=5, pady=5)
protocol_entry = ttk.Entry(input_frame)
protocol_entry.grid(row=0, column=1, padx=5, pady=5)
protocol_entry.insert(0, default_values["protocol"])

# Address
address_label = ttk.Label(input_frame, text="Address:")
address_label.grid(row=1, column=0, padx=5, pady=5)
address_entry = ttk.Entry(input_frame)
address_entry.grid(row=1, column=1, padx=5, pady=5)
address_entry.insert(0, default_values["address"])

# Port
port_label = ttk.Label(input_frame, text="Port:")
port_label.grid(row=2, column=0, padx=5, pady=5)
port_entry = ttk.Entry(input_frame)
port_entry.grid(row=2, column=1, padx=5, pady=5)
port_entry.insert(0, default_values["port"])

# UID
uid_label = ttk.Label(input_frame, text="UID:")
uid_label.grid(row=3, column=0, padx=5, pady=5)
uid_entry = ttk.Entry(input_frame)
uid_entry.grid(row=3, column=1, padx=5, pady=5)
uid_entry.insert(0, default_values["uid"])

# Host
host_label = ttk.Label(input_frame, text="Host:")
host_label.grid(row=4, column=0, padx=5, pady=5)
host_entry = ttk.Entry(input_frame)
host_entry.grid(row=4, column=1, padx=5, pady=5)
host_entry.insert(0, default_values["host"])

# Header Type
header_type_label = ttk.Label(input_frame, text="Header Type:")
header_type_label.grid(row=5, column=0, padx=5, pady=5)
header_type_entry = ttk.Entry(input_frame)
header_type_entry.grid(row=5, column=1, padx=5, pady=5)
header_type_entry.insert(0, default_values["header_type"])

# Network Type
network_type_label = ttk.Label(input_frame, text="Network Type:")
network_type_label.grid(row=6, column=0, padx=5, pady=5)
network_type_entry = ttk.Entry(input_frame)
network_type_entry.grid(row=6, column=1, padx=5, pady=5)
network_type_entry.insert(0, default_values["network_type"])

# Button frame
button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

# Save button
save_button = ttk.Button(button_frame, text="Save", command=save_info)
save_button.grid(row=0, column=0, padx=5, pady=5)

# Run button
run_button = ttk.Button(button_frame, text="Run", command=run_process)
run_button.grid(row=0, column=1, padx=5, pady=5)

# Stop button
stop_button = ttk.Button(button_frame, text="Stop", command=stop_process)
stop_button.grid(row=0, column=2, padx=5, pady=5)

# Run the main event loop
root.mainloop()
