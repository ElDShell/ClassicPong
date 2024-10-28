import tkinter as tk
# Function to handle the submit button click

# Main window

def get_names():
    player_names = []  # List to store player names

    def submit_names():
        # Retrieve player names from the entry fields
        player1_name = entry_player1.get()
        player2_name = entry_player2.get()
        player_names.extend([player1_name, player2_name])  # Store names in the list
        root.destroy()  # Close the window

    root = tk.Tk()
    root.title("Player Entry Screen")
    root.geometry("400x300")
    root.configure(bg="#f0f0f0")

    # Main frame
    frame = tk.Frame(root, bg="#e0e0e0", bd=5, relief="groove")
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Title label
    title_label = tk.Label(frame, text="Enter Players' Names", font=("Arial", 16, "bold"), bg="#e0e0e0")
    title_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Player 1 label and entry
    label_player1 = tk.Label(frame, text="Player 1 Name:", font=("Arial", 12), bg="#e0e0e0")
    label_player1.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_player1 = tk.Entry(frame, font=("Arial", 12), width=20)
    entry_player1.grid(row=1, column=1, padx=10, pady=10)

    # Player 2 label and entry
    label_player2 = tk.Label(frame, text="Player 2 Name:", font=("Arial", 12), bg="#e0e0e0")
    label_player2.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_player2 = tk.Entry(frame, font=("Arial", 12), width=20)
    entry_player2.grid(row=2, column=1, padx=10, pady=10)

    # Submit button
    submit_button = tk.Button(frame, text="Play", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=submit_names)
    submit_button.grid(row=3, column=0, columnspan=2, pady=20)

    # Start the main loop
    root.mainloop()

    return player_names


