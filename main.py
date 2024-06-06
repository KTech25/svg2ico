import os
from tkinter import Tk, Label, Button, Entry, StringVar, filedialog, messagebox, OptionMenu, W, E
from PIL import Image

class ImageConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("img2img")
        master.configure(bg="#f0f0f0")  # Set background color

        self.label = Label(master, text="Select an image file:", font=("Arial", 12), bg="#f0f0f0")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.input_path = StringVar()
        self.input_entry = Entry(master, textvariable=self.input_path, width=50, font=("Arial", 10))
        self.input_entry.grid(row=1, column=0, padx=10, pady=10)

        self.browse_button = Button(master, text="Browse", command=self.browse_files, font=("Arial", 10), bg="#4CAF50", fg="white")
        self.browse_button.grid(row=1, column=1, padx=10, pady=10)

        self.format_label = Label(master, text="Select output format:", font=("Arial", 12), bg="#f0f0f0")
        self.format_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

        self.output_format = StringVar(master)
        self.output_format.set("PNG")  # default value
        self.format_menu = OptionMenu(master, self.output_format, "PNG", "JPEG", "BMP", "GIF", "TIFF", "ICO")
        self.format_menu.config(font=("Arial", 10), bg="#4CAF50", fg="white")
        self.format_menu.grid(row=3, column=0, padx=10, pady=10)

        self.convert_button = Button(master, text="Convert", command=self.convert_image, font=("Arial", 12), bg="#008CBA", fg="white")
        self.convert_button.grid(row=4, column=0, padx=10, pady=10, sticky=W)

        self.status_label = Label(master, text="", font=("Arial", 10), bg="#f0f0f0", fg="green")
        self.status_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)

    def browse_files(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.input_path.set(file_path)

    def convert_image(self):
        input_path = self.input_path.get()
        output_format = self.output_format.get().upper()

        if not input_path:
            messagebox.showerror("Error", "Please select an input file.")
            return

        output_path = self.get_output_path(input_path, output_format)

        try:
            with Image.open(input_path) as img:
                img.save(output_path, output_format)
            self.status_label.config(text=f"Converted to {output_path}", fg="green")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_label.config(text="")

    def get_output_path(self, input_path, output_format):
        base = os.path.splitext(input_path)[0]
        return f"{base}.{output_format.lower()}"

def main():
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
