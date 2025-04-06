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

