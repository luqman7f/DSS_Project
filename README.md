DSS Web App Project
Overview
This project is a web-based implementation of a Digital Signature Scheme (DSS) for secure data handling. The project integrates cryptographic techniques to provide a secure interface for signing and verifying messages. The backend is built with Flask, while the frontend uses HTML, CSS, and JavaScript to provide a user-friendly interface. The project utilizes cryptographic algorithms such as RSA, AES-256, bcrypt, and SHA-256 for ensuring data security.

Features
Digital Signature Scheme: Users can sign messages and verify signatures using RSA encryption.

AES-256 Encryption: Data is securely stored and transmitted using AES-256 encryption.

Password Hashing: bcrypt is used for password hashing, ensuring secure storage of user credentials.

Message Verification: The system verifies the authenticity of the signed message using SHA-256 hashing.

Frontend Interface: A clean and intuitive frontend for message signing, signature preview, and verification.

Server Integration: The application communicates with the server to validate signatures and messages.

Technologies Used
Backend: Flask (Python)

Frontend: HTML, CSS, JavaScript

Cryptography:

RSA for digital signatures

AES-256 for encryption

bcrypt for password hashing

SHA-256 for message hashing

Email Transmission: SMTP for sending emails securely

Web Development: HTML5, CSS3, JavaScript for building the user interface

Installation Instructions
Prerequisites
Python 3.x

Flask

Cryptography libraries

Steps to Set Up
Clone the repository:

bash
Copy
Edit
