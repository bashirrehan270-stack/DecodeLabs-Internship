# 🔐 Advanced Password Generator & Tracker

A terminal-based Python application that uses Object-Oriented Programming (OOP) to generate highly secure, customizable passwords and tracks them during the session.

## 🚀 Features

- **Multi-Password Generation**: Generate 1, 5, or as many passwords as you need at once using loops.
- **Custom Length & Complexity**: Define the exact length and toggle numbers/symbols (`y/n`) based on your security needs.
- **In-Memory Session Tracker**: View all previously generated passwords during the current run.
- **Interactive CLI Menu**: Simple, user-friendly command-line interface.

## 🛠️ Built With

- **Python 3.x**
- `random` (Python Built-in Module)
- `string` (Python Built-in Module)

## 🏗️ Code Architecture & Logic

### 1. Core Logic (`class password_generator`)
- **State Management**: Uses an internal list (`self.record`) to store password history dynamically during runtime.
- **Algorithm**: Uses Python's `random.choice()` and `string` constants to mix letters, digits, and symbols.

### 2. Control Flow (`main.py`)
- **tracker = password_generator()**: Creates the object to access functions and track data safely.
- **while True**: Runs the main menu for user choices (Generate, View, Exit).
- **for loop**: Runs multiple times to generate the exact number of passwords requested by the user.

## 💻 How To Run

1. Open your terminal or command prompt in the folder containing `main.py`.
2. Run the following command:
   ```bash
   python main.py
   ```

## 🎮 Sample Preview

```text
1: aB3@xE9!mK2q
2: pL8\$vR1#zW5t
3: nX4*fQ7&jY2m
```

## 📜 License
This project is open-source and free to use.




[screen-capture (1).webm](https://github.com/user-attachments/assets/6ff060e9-1c05-496b-8e26-8f8af486eed7)





