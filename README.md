# LAN-VoIP-Web-App

A real-time Voice over IP (VoIP) web application designed for Local Area Networks (LAN) using WebRTC technology.

## Overview

This project implements a WebRTC signaling server using Flask and Socket.IO to enable peer-to-peer voice/video communication within a local network. It's specifically designed for LAN environments, making it suitable for internal communication systems.

## Features

- Real-time voice/video communication
- WebRTC-based peer-to-peer connections
- Local network optimization
- Simple and intuitive web interface
- Signaling server using Flask-SocketIO

## Tech Stack

- **Backend**: Python with Flask
- **Signaling**: Flask-SocketIO
- **Frontend**: HTML, CSS, JavaScript
- **Communication Protocol**: WebRTC

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AbuKhuzaima/LAN-VoIP-Web-App.git
```

2. Install required packages:
```bash
pip install flask flask-socketio
```

3. Run the application:
```bash
python app.py
```

4. Access the application at:
```
http://localhost:3000
```

## Usage

1. Open the application in a web browser
2. Allow microphone/camera permissions when prompted
3. Connect with other users on the same network
4. Start communicating!

## Contributing

Feel free to fork this project and submit pull requests for any improvements.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

- AbuKhuzaima

---
**Note**: This application is designed for LAN environments and may require additional configuration for internet-facing deployments.
