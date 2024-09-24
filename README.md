# Notepad GUI

## Project Overview

**Notepad GUI** is a simple text editor application built using **Python's Tkinter** library. It mimics the functionality of a basic notepad, allowing users to create, edit, and save text documents in a user-friendly graphical interface.

## Features

- **New File**: Create a new text file and start editing.
- **Open File**: Open and edit an existing text file.
- **Save File**: Save the current text document, either as a new file or overwrite an existing one.
- **User-friendly Interface**: Simple and intuitive GUI built using Tkinter.

## Technologies Used

- **Programming Language**: Python
- **GUI Library**: Tkinter
- **File Handling**: OS, tkinter's `askopenfilename`, `asksaveasfilename` for file dialog boxes.

## How to Use

1. **Install Python**:
   Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

2. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/notepad-gui.git
   cd notepad-gui
   ```

3. **Run the Program**:
   Run the Python script to launch the Notepad GUI:
   ```bash
   python notepad_gui.py
   ```

4. **Use the Application**:
   - To create a new file, select **File > New**.
   - To open an existing file, select **File > Open** and browse to your file.
   - To save a file, select **File > Save** or **Save As**.

## Code Structure

- **`newFile()`**: Clears the text area and resets the title to "Untitled-Notepad."
- **`openFile()`**: Opens an existing text file and loads its contents into the text area.
- **`saveFile()`**: Saves the current file. If it's a new file, the user is prompted to name it.
- **Text Area**: The main editable area where the user types.

## Example

```python
root = Tk()
root.title("Untitled-Notepad")
root.geometry("600x400")

# Text area for writing
TextArea = Text(root, font="lucida 13")
TextArea.pack(expand=True, fill=BOTH)
```

## Future Improvements

- **Find and Replace**: Add functionality for finding and replacing text in the document.
- **Cut, Copy, Paste**: Enhance the editing capabilities by adding clipboard features.
- **Word Count**: Display a word count for the document.
- **Themes**: Implement dark mode and other themes for a customizable user experience.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
