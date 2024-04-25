# Writeup for Cryptography/Port Decoder Challenge

Authors: Swati Agrawal

## Description

This challenge is designed to test participants' understanding of network communication, encoding schemes, and basic web interaction. Players will start with a simple web page that prompts them to decode a port number, connect to this port, and then decode a message to retrieve a flag.

## Challenge

### Inspiration
The primary motivation for creating this challenge was to introduce participants to common encoding schemes used in cybersecurity such as hexadecimal and Base64, and to provide a real-world scenario of interacting with network services using these encodings.

### Types of Challenges
- **Encoding/Decoding**: Participants will decode a Base64 encoded string to discover a port number and decode a hexadecimal string to retrieve the final flag.
- **Network Interaction**: Participants will use network client tools like `netcat` to interact with a server running on a decoded port, simulating an interaction with a live server.
- **Web Interaction**: The challenge begins with a web interface where users must input their findings to progress, mimicking the need to interact with web-based systems in many real-world cybersecurity tasks.

## Steps to Solve

1. **Base64 Decoding**: Start at the index.html page, which includes a Base64 encoded string that represents a port number. Decode this string to find the correct port to interact with the server.
2. **Connect to the Server**: Use `netcat` or a similar tool to connect to the server on the decoded port. This connection will provide a hexadecimal encoded flag.
3. **Hexadecimal Decoding**: Decode the hexadecimal string to reveal the flag.
4. **Submit the Flag**: Return to the CTF2.html page to submit your flag and complete the challenge.

## Lessons Learned

Participants will gain practical experience with:
- Decoding common encoding schemes used in data transmission.
- Basic client-server interaction over a network.
- Critical thinking about how to extract necessary information from encoded messages.

This challenge is designed to be beginner-friendly but also to provide a foundational understanding of essential concepts used in cybersecurity and network communication.
