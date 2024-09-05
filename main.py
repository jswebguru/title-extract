import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from Extraction import generate_response_new


class TextTransferApp:
    def __init__(self, root):
        self.output_text_widget = None
        self.transfer_button = None
        self.input_text_widget = None
        self.root = root
        self.root.title("Text Transfer App")

        # Load a database-related background image from a URL
        # Database server isometric icon from Freepik
        image_url = "https://img.freepik.com/free-vector/database-server-isometric-icon_1284-16327.jpg"

        response = requests.get(image_url)
        image_data = BytesIO(response.content)

        self.background_image = Image.open(image_data)
        self.background_image = self.background_image.resize((700, 600),
                                                             Image.Resampling.LANCZOS)  # Adjust size using new 
        # Resampling enum
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas and place the background image
        self.canvas = tk.Canvas(root, width=700, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Create and place widgets on top of the canvas
        self.create_widgets()

    def create_widgets(self):
        """Create and arrange the widgets in the application."""
        input_frame = tk.Frame(self.root, bg="#ffffff")
        self.canvas.create_window(100, 60, window=input_frame, anchor="nw")
        self.input_text_widget = tk.Text(input_frame, height=10, width=50)
        self.input_text_widget.pack(padx=10, pady=5)

        button_frame = tk.Frame(self.root, bg="#ffffff")
        self.canvas.create_window(250, 250, window=button_frame, anchor="nw")

        self.transfer_button = tk.Button(button_frame, text="Transfer Text", command=self.transfer_text, bg="#4CAF50",
                                         fg="#ffffff", padx=10, pady=5)
        self.transfer_button.pack()

        output_frame = tk.Frame(self.root, bg="#ffffff")
        self.canvas.create_window(100, 340, window=output_frame, anchor="nw")

        self.output_text_widget = tk.Text(output_frame, height=10, width=50)
        self.output_text_widget.pack(padx=10, pady=5)

    def transfer_text(self):
        """Transfer text from the input widget to the output widget."""
        input_text = self.input_text_widget.get("1.0", tk.END)
        self.output_text_widget.delete("1.0", tk.END)

        prompt = ('You have to only give me the fully analyzed answers not include any abbreviations. '
                  'From the following content, only give me the name of the product as well as the value of that. '
                  'Never include any other strings.'
                  'In this format, maybe: Grand Theft Auto V: $10' + input_text)

        content = generate_response_new(prompt)

        self.output_text_widget.insert(tk.END, content)


if __name__ == "__main__":
    root = tk.Tk()

    # Adjust window size to fit your background image
    root.geometry("700x600")

    # Instantiate and run the application
    app = TextTransferApp(root)
    root.mainloop()
