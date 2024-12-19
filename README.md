# Password Manager

A simple, user-friendly password manager built with Python and Tkinter. This application helps generate secure passwords and store them for various websites securely in a local file.

---

## Features

### 1. Password Generator
- Generates a strong, random password with a mix of letters, numbers, and symbols.
- Automatically copies the generated password to the clipboard for easy use.

### 2. Save Passwords
- Saves credentials (website, email/username, password) to a local file (`password.txt`).
- Ensures that no fields are left empty before saving.
- Prompts the user for confirmation before saving credentials.

### 3. User-Friendly Interface
- Clean and intuitive GUI built using Tkinter.
- Default email/username pre-filled for convenience.
- Focuses automatically on the "Website" input field for faster data entry.

---

## Requirements

### Dependencies
- **Python 3.x**
- **tkinter**: Comes pre-installed with Python.
- **pyperclip**: To enable clipboard functionality.
  ```bash
  pip install pyperclip
  ```

### Additional Files
- `logo.png`: A logo image to be displayed in the application.

---

## Installation

1. Clone or download the repository:
   ```bash
   git clone https://github.com/your-username/password-manager.git
   cd password-manager
   ```

2. Ensure Python is installed on your system.

3. Install dependencies:
   ```bash
   pip install pyperclip
   ```

4. Place the `logo.png` file in the same directory as the script.

5. Run the application:
   ```bash
   python password_manager.py
   ```

---

## How to Use

1. **Generate a Password**:
   - Click the "Generate Password" button.
   - A secure password will appear in the password field and be copied to the clipboard.

2. **Save Credentials**:
   - Fill in the "Website" and "Email/Username" fields.
   - Click "Add" to save the credentials to `password.txt`.

3. **View Saved Passwords**:
   - Open the `password.txt` file to view saved credentials.

---

## File Structure

- **`password_manager.py`**: Main script for the application.
- **`password.txt`**: Stores saved credentials (created automatically after saving passwords).
- **`logo.png`**: Logo for the application.

---

## Improvements and Future Features

1. **Encryption**:
   - Encrypt saved passwords for better security.
   - Use a master password to access the stored data.

2. **Search Functionality**:
   - Add a search bar to retrieve specific credentials quickly.

3. **Database Integration**:
   - Replace `password.txt` with a database like SQLite for better scalability.

4. **Export and Import**:
   - Allow users to export and import saved credentials.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Pyperclip Documentation](https://pyperclip.readthedocs.io/)

