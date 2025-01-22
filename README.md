# PDF Unlocker Web App

[![Deployed App](https://img.shields.io/badge/Live%20App-Link-green)](https://password-recovery-for-pdf-file.onrender.com)

A **Flask-based web application** that allows users to upload password-protected PDF files and unlock them using a brute-force method. The application provides an intuitive interface for uploading files, specifying password parameters, and downloading the unlocked PDF.

## Features

- **User-Friendly Interface**: Modern and simple design for ease of use.
- **Brute-Force Password Recovery**: Efficiently attempts all possible password combinations.
- **Dynamic Password Options**:
  - Supports letters (A-Z), digits (0-9), or both.
  - Users can specify the password length.
- **Real-Time Feedback**: Displays the correct password once found.
- **Secure File Handling**: Temporarily stores files for processing and deletes them after unlocking.
- **Free Deployment**: Deployed on Render and accessible online.

## Live Demo

Access the application here: [PDF Unlocker Web App](https://password-recovery-for-pdf-file.onrender.com)

## How to Use

1. **Upload PDF**: Select the password-protected PDF file to unlock.
2. **Set Password Parameters**:
   - Specify the expected password length.
   - Choose the type of password (letters, digits, or both).
3. **Unlock PDF**: Click the "Unlock PDF" button and wait for the app to find the password.
4. **Download Unlocked File**: Once unlocked, the app displays the password and provides a link to download the file.

## Requirements

To run the app locally, you need the following:

- Python 3.7 or later
- The dependencies listed in `requirements.txt`:
  ```plaintext
  Flask==2.3.2
  PyPDF2==3.0.1
  gunicorn==21.0.0
  ```

## Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/pdf-unlocker.git
   cd pdf-unlocker
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   flask run
   ```
5. Access the app locally at:
   ```
   http://127.0.0.1:5000/
   ```

## Deployment

The app is deployed on Render. To deploy your own version:

1. Push your code to a GitHub repository.
2. Create a free Render account and link your repository.
3. Set the build and start commands:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
4. Deploy and enjoy your live app!

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

- [Flask Documentation](https://flask.palletsprojects.com/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [Render Deployment](https://render.com)

---

Feel free to contribute or raise issues to improve this project!

