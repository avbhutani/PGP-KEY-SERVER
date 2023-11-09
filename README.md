# PGP-KEY-SERVER
PGP Key Server
Overview
This PGP Key Server application provides a secure and centralized repository for storing, retrieving, and managing PGP public keys. It enables users to easily search for and access keys based on email addresses, ensuring secure and confidential communication.

Key Features
Secure Key Storage: The application employs robust encryption mechanisms to safeguard stored PGP public keys.

Efficient Key Retrieval: Keys can be quickly retrieved from a designated folder, facilitating efficient key management and usage.

Seamless Email-Based Search: Users can effortlessly search for keys associated with specific email addresses, streamlining the key discovery process.

Usage Instructions
Key Upload: Users can upload their PGP public keys to the server by providing the key file and the associated email address.

Key Retrieval: To retrieve a key, provide the corresponding email address. The server will locate and return the associated key file.

Key Search: Users can search for keys associated with specific email addresses. The search results will display a list of matching keys, along with their corresponding email addresses.

System Requirements
Operating System: Linux or Windows
Programming Language: Python
Dependencies: PyOpenPGP, Flask
Installation Instructions
Clone the Repository: Clone the project repository to your local machine.
Install Dependencies: Install the required Python dependencies using pip:


First run the command to install the dependencies.
**pip install pyopenpgp flask**

Run the program using the command listed below.
python app.py

Access the Application: Open a web browser and navigate to http://localhost:5000.
