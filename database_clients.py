import tkinter as tk
from client.gui_db import mainframe, menu_tools

def main():
    root = tk.Tk()
    root.title('Droomi Store DataBase - Clientes')
    root.iconbitmap('droomi-store-profile-02.ico')
    root.resizable(0,0)
    menu_tools(root)
    app = mainframe(root = root)
    
    app.mainloop()

if __name__ == '__main__':
    main()