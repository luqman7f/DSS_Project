# **DSS Web App Project** 🚀

## **Overview** 📜

This project is a web-based Digital Signature System (DSS) that allows users to sign and verify messages using RSA cryptography and SHA-256 hashing. It provides a simple graphical interface built with Flask and HTML/CSS for secure and easy-to-use digital signature functionality.
---

## 🎥 Project Demo Video

🔗 [Click to Watch Demo Video](https://drive.google.com/file/d/1GWTxuHizhojR_nnasx3zEQoNyQcLEDBx/view?usp=sharing)

---

✨ Features
🔐 RSA Digital Signature
Sign and verify messages using RSA public-private key cryptography.

🔎 SHA-256 Hashing
Ensures message integrity during signature verification.

🌐 Web Interface
Built with Flask for backend and HTML/CSS for the frontend.

🧾 Signature Preview
View base64-encoded digital signature and SHA-256 hash.

✅ Verification Feedback
Shows popup messages confirming whether the signature is valid or not.

---

🛠️ Technologies Used
Python 3.x

Flask (for backend and routing)

HTML/CSS (for frontend)

JavaScript (for interactive elements like popups)

PyCryptodome (for RSA and SHA-256 operations)

Base64 (for signature encoding/decoding)

---

## **How It Works** 🔍

1. **Sign a Message** ✍️:  
   - Users input a message on the frontend, which is then encrypted and signed using RSA.
   
2. **Verify a Signature** 🔏:  
   - The signed message can be verified against the public key using the verification process on the frontend.
   
3. **Encryption & Storage** 🔐:  
   - Messages are encrypted using AES-256 for secure storage and transmission.

4. **Password Security** 🔒:  
   - User credentials are hashed using bcrypt before storing them in the system for secure authentication.

5. **Signature Verification** ✅:  
   - Once a message is signed, its authenticity can be verified by comparing its SHA-256 hash with the signature.

---

## **Project Structure** 🗂️

Here's a quick overview of the project structure:
```
DSS_Project/
│
├── app.py                # Flask application and backend logic
├── requirements.txt      # Required dependencies for the project
├── templates/            # Frontend HTML files
│   └── index.html        # Main user interface for signing and verifying messages
│
├── static/               # Static files for styling (CSS, JavaScript)
│   ├── styles.css        # CSS styles for the frontend
│   └── script.js         # JavaScript for handling frontend logic
│
├── crypto/               # Cryptographic functions
│   ├── rsa.py            # RSA signing and verification functions
│   ├── aes.py            # AES-256 encryption/decryption functions
│   └── bcrypt_hash.py    # bcrypt hashing functions for password security
│
└── README.md             # Project documentation
```


---

## **Installation Instructions** ⚡

### **Prerequisites** 📋

- **Python 3.x**
- **Flask**
- **Cryptography libraries** (e.g., `pycryptodome`)

### **Steps to Set Up** 🔧

1. **Clone the repository**:

    ```bash
    git clone https://github.com/luqman7f/DSS_Project.git
    ```

2. **Navigate to the project folder**:

    ```bash
    cd DSS_Project
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application**:

    ```bash
    python app.py
    ```

5. **Open the application**:  
   - Go to **`http://127.0.0.1:5000/`** in your web browser.

---

## **Contributing** 🤝

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new **Pull Request**.

---

## **📄 License**

This project is for **educational** and **research purposes**. Use responsibly.

For more details, refer to the **LICENSE** file in the repository.

---

## **Contact** 📬

For any questions or feedback, feel free to reach out via:

- **Email**: [luqmanmohd009@gmail.com](mailto:luqmanmohd009@gmail.com)
- **GitHub**: [luqman7f](https://github.com/luqman7f)


