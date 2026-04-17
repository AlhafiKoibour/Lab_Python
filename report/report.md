# CYBE 6223 — Lab 0 Report

**Group Identification (NAME):** Group-07-merkle-roots

**Group Members (Names):**
* **Sime Delonney Njeba** (UBa25EP122) *Project Lead*
* **Alhafi Koïbour** (UBa25EP125)
* **Tchoffouo Djimyr Hassan** (UBa25EP132)
* **Mugob Irine Tawe** (UBa25EP141)
* **EKENU STEVE MBAH** (UBa25EP113)

**Date of Submission:** Friday

**GitHub Repository URL:**
https://github.com/cybe6223-2026/lab-0-tcp-socket-communication-the-merkle-rootsgroup.git

---

## 1. Implementation Summary
<!-- Briefly describe what your server and client do. 2–3 sentences. -->

Our TCP server listens for incoming connections on a specific port, receives a text message from the client, and echoes that same message back. The client initiates the connection, sends an identification string, displays the server's response, and terminates the session.
## 2. Socket Primitives — What Each Step Does
<!-- For each of the following primitives used in your code, explain
     in one sentence what it does and why it is called at that point:
     socket(), bind(), listen(), accept(), connect(), send/sendall(), recv(), close() -->

| Primitive | Purpose in your code |
|-----------|---------------------|
| socket()  | Creates the communication endpoint using the IPv4 address family and the TCP protocol.|
| bind()    |Assigns the server's socket to a specific IP address and port number to receive data.|
| listen()  |Places the server in a passive mode, allowing it to wait for connection attempts from clients.|
| accept()  |Blocks execution until a client connects, then creates a new socket dedicated to that specific exchange.|
| connect() |Used by the client to initiate a TCP handshake with the server at the specified address and port.|
| sendall() |Transmits the entire message through the socket, ensuring all data is sent before continuing.|
| recv()    |Reads incoming data sent by the other party (limited by the specified buffer size).
| close()   |Releases system resources and properly terminates the communication session.|

## 3. Failure Analysis
<!-- What happens if the client runs before the server is ready?
     What error do you observe? What does this tell you about
     assumptions in distributed systems? (~100 words) -->

If the client runs before the server is ready, the program crashes with a ConnectionRefusedError. This highlights a fundamental truth in distributed systems: one cannot assume component availability. In real-world environments, systems must be designed to handle connection failures using retry mechanisms or explicit error messages, as network nodes rarely start in perfect synchrony. This demonstrates that distributed components are inherently loosely coupled.

## 4. Security Observation
<!-- This TCP exchange has no authentication, no encryption, and
     no message integrity check. Identify one concrete attack that
     is possible against your implementation as written, and explain
     why it works. (~100 words) -->

A primary vulnerability is Eavesdropping via a Man-in-the-Middle (MitM) attack. Since this TCP exchange uses plaintext with no encryption (like **TLS/SSL**), an attacker using a tool like Wireshark on the same network can easily capture and read the message content. Furthermore, the lack of authentication means an attacker could perform a Denial of Service (DoS) by flooding the server or send fraudulent data by impersonating a legitimate client.

## 5. Reflection
<!-- What was the most important thing you learned from implementing
     this? Connect it to one concept from Week 1 lectures. (~75 words) -->

The most important lesson was understanding the client-server model beyond theoretical definitions. By manipulating these primitives, we observed how the **Transport Layer** abstraction manages data reliability. This connects directly to the concept of Location Transparency from Week 1: once the connection is established, the code handles data exchange almost like a local file operation, hiding the underlying network complexity.

## References
Tanenbaum, A. & Van Steen, M. (2017). *Distributed Systems: Principles and Paradigms* (3rd ed.). Chapter 4.
