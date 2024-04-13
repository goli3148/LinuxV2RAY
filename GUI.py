import tkinter as tk
from tkinter import ttk
import subprocess

import threading

from editConfigJson import editConfigFile
from path import paths
import os


def runV2RAY():
    v2ray = paths()['v2ray']
    config = paths()['config']

    # output = subprocess.check_output(f'{v2ray} -config={config}', shell=True)

    os.system(f'{v2ray} -config={config} &')
    # output_text.config(state=tk.NORMAL)
    # output_text.insert(tk.END, output.decode())
    # output_text.config(state=tk.DISABLED)

RUNNING = False
RunningThread = threading.Thread(target=runV2RAY)


def save_info():
    if RUNNING:
        stop_process()
    protocol = protocol_entry.get()
    address = address_entry.get()
    port = int(port_entry.get())
    uid = uid_entry.get()
    host = host_entry.get()
    header_type = header_type_entry.get()
    network_type = network_type_entry.get()
    editConfigFile(protocol=protocol, address=address, port=port, uid=uid, host=host, headerType=header_type, networkType=network_type)

def run_process():
    global RUNNING
    global RunningThread
    if RUNNING:
        stop_process()
    RunningThread = threading.Thread(target=runV2RAY)
    RunningThread.start()
    RUNNING = True

def stop_process():
    # Add code to stop your process here
    global RUNNING
    global RunningThread
    PID = os.popen('pgrep v2ray').read().strip()
    os.system(f'kill {PID}')
    RunningThread.join()
    print('thread stpped')
    RUNNING = False

def get_default_values():
    return {
        "protocol": "vless",
        "address": "fr.v2landsshop.top",
        "port": 36887,
        "uid": "95975b55-40e9-4338-90ba-7c244e63bd7d",
        "host": "speedtest.net",
        "header_type": "http",
        "network_type": "tcp"
    }

root = tk.Tk()
root.title("V2Linux")

style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#007bff", foreground="white")

input_frame = ttk.Frame(root)
input_frame.pack(padx=20, pady=10)

default_values = get_default_values()

protocol_label = ttk.Label(input_frame, text="Protocol:")
protocol_label.grid(row=0, column=0, padx=5, pady=5)
protocol_entry = ttk.Entry(input_frame)
protocol_entry.grid(row=0, column=1, padx=5, pady=5)
protocol_entry.insert(0, default_values["protocol"])

address_label = ttk.Label(input_frame, text="Address:")
address_label.grid(row=1, column=0, padx=5, pady=5)
address_entry = ttk.Entry(input_frame)
address_entry.grid(row=1, column=1, padx=5, pady=5)
address_entry.insert(0, default_values["address"])

port_label = ttk.Label(input_frame, text="Port:")
port_label.grid(row=2, column=0, padx=5, pady=5)
port_entry = ttk.Entry(input_frame)
port_entry.grid(row=2, column=1, padx=5, pady=5)
port_entry.insert(0, default_values["port"])

uid_label = ttk.Label(input_frame, text="UID:")
uid_label.grid(row=3, column=0, padx=5, pady=5)
uid_entry = ttk.Entry(input_frame)
uid_entry.grid(row=3, column=1, padx=5, pady=5)
uid_entry.insert(0, default_values["uid"])

host_label = ttk.Label(input_frame, text="Host:")
host_label.grid(row=4, column=0, padx=5, pady=5)
host_entry = ttk.Entry(input_frame)
host_entry.grid(row=4, column=1, padx=5, pady=5)
host_entry.insert(0, default_values["host"])

header_type_label = ttk.Label(input_frame, text="Header Type:")
header_type_label.grid(row=5, column=0, padx=5, pady=5)
header_type_entry = ttk.Entry(input_frame)
header_type_entry.grid(row=5, column=1, padx=5, pady=5)
header_type_entry.insert(0, default_values["header_type"])

network_type_label = ttk.Label(input_frame, text="Network Type:")
network_type_label.grid(row=6, column=0, padx=5, pady=5)
network_type_entry = ttk.Entry(input_frame)
network_type_entry.grid(row=6, column=1, padx=5, pady=5)
network_type_entry.insert(0, default_values["network_type"])

button_frame = ttk.Frame(root)
button_frame.pack(pady=10)

save_button = ttk.Button(button_frame, text="Save", command=save_info)
save_button.grid(row=0, column=0, padx=5, pady=5)

run_button = ttk.Button(button_frame, text="Run", command=run_process)
run_button.grid(row=0, column=1, padx=5, pady=5)

stop_button = ttk.Button(button_frame, text="Stop", command=stop_process)
stop_button.grid(row=0, column=2, padx=5, pady=5)

output_text = tk.Text(root, height=10, width=50)
output_text.pack(pady=10)
output_text.config(state=tk.DISABLED)

root.mainloop()
