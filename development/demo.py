from sys import platform


from tkfontawesome_mizraith import icon_to_image
import tkinter as tk

from sys import platform
if platform == 'win32':
    # NOTE: My testing indicated that this wasn't even needed.
    from ctypes import windll
    windll.user32.SetProcessDPIAware()
elif platform == 'darwin':
    pass
elif platform in ['linux', 'linux2']:
    pass


icons = [
    (
        "band-aid",
        "basketball-ball",
        "box",
        "child",
        "church",
        "feather-alt",
        "save",
        "drafting-compass",
    ),
    (
        "vial",
        "fish",
        "user-ninja",
        "concierge-bell",
        "tooth",
        "sign",
        "caravan",
        "file-prescription",
    ),
    (
        "wine-glass-alt",
        "mitten",
        "couch",
        "mortar-pestle",
        "dna",
        "bus-alt",
        "car",
        "stethoscope",
    ),
]

root = tk.Tk()
images = []     # NOTE that you need to retain your icons (as a global or class variable) to keep it in scope.

for i, row in enumerate(icons):
    root.rowconfigure(i, weight=1)
    for j, icon in enumerate(row):
        root.columnconfigure(j, weight=1)
        images.append(icon_to_image(icon, scale_to_width=64))
        tk.Label(root, image=images[-1]).grid(row=i, column=j, padx=5, pady=5)

root.mainloop()
