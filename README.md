# **DSS Web App Project** 🚀

## **Overview** 📜

This project is a **web-based implementation of a Digital Signature Scheme (DSS)** for secure data handling. It integrates **cryptographic techniques** to provide a secure interface for **signing** and **verifying messages**. The **backend** is built with **Flask**, while the **frontend** uses **HTML**, **CSS**, and **JavaScript** to create a user-friendly interface. The project utilizes several cryptographic algorithms such as **RSA**, **AES-256**, **bcrypt**, and **SHA-256** to ensure high-level **data security**.

---

## **Features** ⚙️

- **Digital Signature Scheme** 🖊️:  
  - Users can **sign messages** and **verify signatures** using **RSA encryption**.

- **AES-256 Encryption** 🔒:  
  - Data is securely **stored** and **transmitted** using **AES-256 encryption**.

- **Password Hashing** 🔑:  
  - **bcrypt** is used for **password hashing**, ensuring **secure storage** of user credentials.

- **Message Verification** 🧐:  
  - The system **verifies** the authenticity of the signed message using **SHA-256 hashing**.

- **Frontend Interface** 🎨:  
  - A clean and intuitive **frontend** for message signing, signature preview, and verification.

- **Server Integration** 🌐:  
  - The application communicates with the server to validate signatures and messages.

---

## **Technologies Used** 💻

- **Backend**:  
  - **Flask** (Python)

- **Frontend**:  
  - **HTML5**, **CSS3**, **JavaScript**

- **Cryptography**:  
  - **RSA** for digital signatures  
  - **AES-256** for encryption  
  - **bcrypt** for password hashing  
  - **SHA-256** for message hashing

- **Email Transmission** 📧:  
  - **SMTP** for sending emails securely

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

## **License** 📜

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## **Contact** 📬

For any questions or feedback, feel free to reach out via:

- **Email**: [luqmanmohd009@gmail.com](mailto:luqmanmohd009@gmail.com)
- **GitHub**: [luqman7f](https://github.com/luqman7f)

