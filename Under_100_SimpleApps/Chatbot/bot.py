import tkinter as tk
from transformers import pipeline

# Load the pre-trained model
chatbot = pipeline("text-generation", model="gpt2")

def send_message(event=None):
    """Function to send the user's message and get a response from the chatbot."""
    message = entry.get()
    if message.strip() != "":
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n")
        chat_box.see(tk.END)
        chat_box.config(state=tk.DISABLED)
        entry.delete(0, tk.END)
        respond_to_message(message)

def respond_to_message(message):
    """Function to get a response from the chatbot and display it."""
    response = "Bot: " + chatbot(message, max_length=50, num_return_sequences=1)[0]['generated_text']
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, response + "\n")
    chat_box.see(tk.END)
    chat_box.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Chat Box")

# Create chat history box
chat_box = tk.Text(root, bg="white", fg="black", height=20, width=50)
chat_box.config(state=tk.DISABLED)
chat_box.pack(pady=10)

# Create message entry box
entry = tk.Entry(root, width=50)
entry.bind("<Return>", send_message)
entry.pack(side=tk.LEFT, padx=10)

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=5)

# Run the application
root.mainloop()
