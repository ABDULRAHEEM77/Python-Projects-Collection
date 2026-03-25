import tkinter as tk

# Function to respond
def respond(event=None):   # event added for Enter key
    txt = entry.get()
    
    if txt.strip() == "":
        return
    
    chat.insert(tk.END, "You: " + txt + "\n", "user")

    # Simple smart replies
    if txt.lower() in ["hi", "hello"]:
        reply = "Hello! 😊"
    elif "how's it going" in txt.lower():
        reply = "I'm just code, but I'm doing great! 😄"
    elif "bye" in txt.lower():
        reply = "Goodbye! 👋"
    else:
        reply = "I don't understand that yet 🤔"

    chat.insert(tk.END, "Bot: " + reply + "\n\n", "bot")
    
    entry.delete(0, tk.END)   # clear input


# Main window
root = tk.Tk()
root.title("Simple Chatbot")

# Chat area
chat = tk.Text(root, width=50, height=20, bg="black", fg="white")
chat.pack(padx=10, pady=10)

# Styling tags
chat.tag_config("user", foreground="cyan")
chat.tag_config("bot", foreground="lightgreen")

# Input field
entry = tk.Entry(root, width=40)
entry.pack(side=tk.LEFT, padx=10, pady=10)

# Send button
btn = tk.Button(root, text="Send", command=respond)
btn.pack(side=tk.LEFT)

# Bind Enter key
root.bind("<Return>", respond)

# Run app
root.mainloop()