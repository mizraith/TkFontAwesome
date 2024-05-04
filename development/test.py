from sys import platform
if platform == 'win32':
    # NOTE: My testing indicated that this wasn't even needed.
    from ctypes import windll
    windll.user32.SetProcessDPIAware()
elif platform == 'darwin':
    pass
elif platform in ['linux', 'linux2']:
    pass


import tkinter as tk
from tkfontawesome_mizraith import icon_to_image

root = tk.Tk()
fb = icon_to_image("facebook", fill="#4267B2", scale_to_width=64)
send = icon_to_image("paper-plane", fill="#1D9F75", scale_to_width=64)

tk.Label(root, image=fb).pack(padx=10, pady=10)
tk.Button(root, image=send).pack(padx=10, pady=10)

root.mainloop()
