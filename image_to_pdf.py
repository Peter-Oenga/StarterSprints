import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from PIL import Image
import os

class ImageToPDFConverter:
    def __init__(self, root):
        self.root = root
        self.image_paths = []
        self.output_pdf_name = tk.StringVar()
        self.selected_images_listbox = tk.Listbox(root, selectmode="MULTIPLE")


        self.initialize_ui()
    def initialize_ui(self):
        title_label = tk.Label(self.root, text="Image to PDF Converter", font=("Helvetica", 16 , "bold"))
        title_label.pack(pady=10)

        select_images_button = tk.Button(self.root, text="Select Images", command=self.select_images)
        select_images_button.pack(pady=(0, 10))

        self.selected_images_listbox.pack(padx=(0, 10), fill=tk.BOTH, expand=True)

        label = tk.Label(self.root, text="Enter output PDF")
        label.pack()

        pdf_entry_name = tk.Entry(self.root, textvariable=self.output_pdf_name, width=40, justify='center')
        pdf_entry_name.pack()

        convert_button = tk.Button(self.root, text="Convert to PDF", command=self.convert_images_to_pdf)
        convert_button.pack(pady=(20, 10))

    def select_images(self):
        self.image_paths = filedialog.askopenfilenames(title="Select images", filetypes=
        [("Image types", "*.png;*.jpg;*.jpeg;")])

        self.update_selected_images_listbox()

    def update_selected_images_listbox(self):
        self.selected_images_listbox.delete(0, tk.END)

        for image_path in self.image_paths:
            _, image_path = os.path.split(image_path)
            self.selected_images_listbox.insert(tk.END, image_path)

    def convert_images_to_pdf(self):
        if not self.image_paths:
            return
        output_path_pdf = self.output_pdf_name.get() + ".pdf" if self.output_pdf_name.get() else "output.pdf"

        pdf = canvas.Canvas(output_path_pdf, pagesize=(612, 792))

        for image_path in self.image_paths:
            img = Image.open(image_path)
            available_width = 540
            available_height = 720
            scale_factor = min(available_width/img.width, available_height/img.height)
            new_width = img.width * scale_factor
            new_height = img.height * scale_factor
            x_centered = (612 - new_width)/2
            y_centered = (792 - new_height)/2

            pdf.setFillColor(255, 255)
            pdf.rect(0, 0, 612, 792, fill=True)
            pdf.drawInlineImage(img, x_centered, y_centered, width=new_width, height=new_height)
            pdf.showPage()
        pdf.save()

def main():
    root = tk.Tk()
    root.title("Image to pdf")
    converter = ImageToPDFConverter(root)
    root.geometry = (400 * 600)
    root.mainloop()

if __name__ == "__main__":
    main()