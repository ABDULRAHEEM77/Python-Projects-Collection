import tkinter as tk
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# Function to respond using AI
def respond(event=None):
    user_input = entry.get()
    
    if user_input.strip() == "":
        return
    
    chat.insert(tk.END, "You: " + user_input + "\n", "user")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        
        bot_reply = response.choices[0].message.content

    except Exception as e:
        bot_reply = "Error: " + str(e)

    chat.insert(tk.END, "Bot: " + bot_reply + "\n\n", "bot")
    
    entry.delete(0, tk.END)


# GUI Setup
root = tk.Tk()
root.title("AI Chatbot")

chat = tk.Text(root, width=60, height=20, bg="black", fg="white")
chat.pack(padx=10, pady=10)

chat.tag_config("user", foreground="cyan")
chat.tag_config("bot", foreground="lightgreen")

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10, pady=10)

tk.Button(root, text="Send", command=respond).pack(side=tk.LEFT)

root.bind("<Return>", respond)

root.mainloop()