import tkinter as tk
from tkinter import messagebox
import subprocess
from datetime import datetime

class WindowsUtilityApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PyChumpa")
        self.geometry("640x480")

        self.init_ui()

    def init_ui(self):
        # Меню
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Experimental mode", command=self.show_experimental_mode_warning)
        file_menu.add_command(label="Open Command Prompt", command=self.open_cmd_prompt)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_application)
        menubar.add_cascade(label="File", menu=file_menu)

        utilities_menu = tk.Menu(menubar, tearoff=0)
        utilities_menu.add_command(label="Check Ping", command=self.check_ping)
        utilities_menu.add_command(label="Get External IP", command=self.get_external_ip)
        utilities_menu.add_command(label="Get Hostname", command=self.get_hostname)
        utilities_menu.add_command(label="Get Local IP", command=self.get_local_ip)
        menubar.add_cascade(label="Utilities", menu=utilities_menu)

        system_menu = tk.Menu(menubar, tearoff=0)
        system_menu.add_command(label="Windows Version", command=self.open_windows_version)
        system_menu.add_command(label="Time and Date", command=self.open_time_and_date)
        system_menu.add_command(label="Task Manager", command=self.open_task_manager)
        system_menu.add_command(label="Programs and Features", command=self.open_programs_and_features)
        system_menu.add_command(label="Network Connections", command=self.open_network_connections)
        system_menu.add_command(label="Power Options", command=self.open_power_options)
        system_menu.add_command(label="Windows Firewall", command=self.open_windows_firewall)
        system_menu.add_command(label="Device Manager", command=self.open_device_manager)
        system_menu.add_command(label="Computer Management", command=self.open_computer_management)
        system_menu.add_command(label="System Properties", command=self.open_system_properties)
        system_menu.add_command(label="Check Disk", command=self.check_disk)
        system_menu.add_command(label="Registry Editor", command=self.open_registry_editor)
        system_menu.add_command(label="DirectX Diagnostic Tool", command=self.open_dxdiag)
        system_menu.add_command(label="Disk Cleanup", command=self.open_disk_cleanup)
        system_menu.add_command(label="Disk Management", command=self.open_disk_management)
        system_menu.add_command(label="Disk Defragmentation", command=self.open_disk_defragmentation)
        system_menu.add_command(label="Diskpart", command=self.open_diskpart)
        system_menu.add_command(label="Event Viewer", command=self.open_event_viewer)
        system_menu.add_command(label="Folders Properties", command=self.open_folders_properties)
        system_menu.add_command(label="Remote Desktop Connection", command=self.open_remote_desktop)
        system_menu.add_command(label="IP Configuration", command=self.show_ip_config)
        menubar.add_cascade(label="System", menu=system_menu)

        about_menu = tk.Menu(menubar, tearoff=0)
        about_menu.add_command(label="About", command=self.show_about_info)
        menubar.add_cascade(label="About", menu=about_menu)

        # Виджеты
        self.label = tk.Label(self, text="Right-click to open context menu", pady=10)
        self.label.pack(fill=tk.X)

        self.text_entry = tk.Entry(self, width=50)
        self.text_entry.pack(pady=10)

        self.ping_button = tk.Button(self, text="Check Ping", command=self.check_ping)
        self.ping_button.pack()

        # Костыль для отключения кнопок
        self.disable_buttons()

    def show_experimental_mode_warning(self):
        messagebox.showinfo("Experimental Mode", "Experimental mode unlocks few locked and unfinished functions, be careful!")

    def open_cmd_prompt(self):
        subprocess.run("cmd.exe", cwd="C:\\")

    def check_ping(self):
        url = self.text_entry.get()
        ping_cmd = " -n 8"
        subprocess.run(["ping", url + ping_cmd])

    def get_external_ip(self):
        ip_external = subprocess.run(["curl", "ifconfig.me"], capture_output=True, text=True)
        messagebox.showinfo("External IP", ip_external.stdout.strip())

    def get_hostname(self):
        host = subprocess.run(["hostname"], capture_output=True, text=True)
        self.label.config(text=host.stdout.strip())
        self.disable_buttons()

    def get_local_ip(self):
        local_ip = subprocess.run(["ipconfig"], capture_output=True, text=True)
        for line in local_ip.stdout.splitlines():
            if "IPv4 Address" in line:
                ip = line.split(":")[1].strip()
                self.label.config(text=ip)
                self.disable_buttons()
                break

    def disable_buttons(self):
        self.ping_button.config(state=tk.DISABLED)

    def open_windows_version(self):
        subprocess.run("winver")

    def open_time_and_date(self):
        subprocess.run("timedate.cpl")

    def open_task_manager(self):
        subprocess.run("taskmgr")

    def open_programs_and_features(self):
        subprocess.run("appwiz.cpl")

    def open_network_connections(self):
        subprocess.run("ncpa.cpl")

    def open_power_options(self):
        subprocess.run("powercfg.cpl")

    def open_windows_firewall(self):
        subprocess.run("Firewall.cpl")

    def open_device_manager(self):
        subprocess.run("hdwwiz.cpl")

    def open_computer_management(self):
        subprocess.run("compmgmt.msc")

    def open_system_properties(self):
        subprocess.run("sysdm.cpl")

    def check_disk(self):
        subprocess.run("chkdsk")

    def open_registry_editor(self):
        subprocess.run("regedit")

    def open_dxdiag(self):
        subprocess.run("dxdiag")

    def open_disk_cleanup(self):
        subprocess.run("cleanmgr")

    def open_disk_management(self):
        subprocess.run("diskmgmt.msc")

    def open_disk_defragmentation(self):
        subprocess.run("dfrgui.exe")

    def open_diskpart(self):
        subprocess.run("diskpart")

    def open_event_viewer(self):
        subprocess.run("eventvwr.msc")

    def open_folders_properties(self):
        subprocess.run(["control", "/name Microsoft.Folders"])

    def open_remote_desktop(self):
        subprocess.run("mstsc")

    def show_ip_config(self):
        subprocess.run(["ipconfig", "/all"])

    def show_about_info(self):
        messagebox.showinfo("PyChumpa", "This is a recoded version of my first shell program for system and service utilities from C# to Python, designed for the Windows operating system. \nAuthor: Aydar Gainullin aka 4yd4r \nt.me/yaaydar")

    def exit_application(self):
        self.destroy()

if __name__ == "__main__":
    app = WindowsUtilityApp()
    app.mainloop()
