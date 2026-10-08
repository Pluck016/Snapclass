# Snapclass

An automated AI-powered attendance system that uses voice recognition and image processing to quickly capture and verify student attendance.

---

## Table of Contents
- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## About the Project

**Snapclass** is designed to streamline classroom management by automating attendance tracking. Instead of manually taking roll calls, teachers can capture attendance through audio recordings (voice roll call recognition) or group classroom photos (facial identification).

### Key Features
* 🎙️ **Voice Attendance:** Record voice roll calls and automatically match student responses to the class roster.
* 📸 **Visual Verification:** Upload classroom/group pictures to identify present students via image processing.
* 📊 **Automated Logs:** Generate instant attendance reports and export daily attendance logs.
* 🔍 **Roster Management:** Easily map audio profiles and photos to specific student IDs.

---

## Built With

* [Python](https://python.org)
* [Flask](https://palletsprojects.com)
* [OpenCV](https://opencv.org) / [Pillow](https://python-pillow.org/)
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) / [HTML5 Speech API](https://developer.mozilla.org/en-US/docs/Web/API/SpeechRecognition)

---

## Getting Started

Follow these instructions to set up the project locally on your machine.

### Prerequisites

* Python 3.8 or higher
* `pip` package manager
* `git`
* System microphone access (for voice recording)

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/Pluck016/Snapclass.git](https://github.com/Pluck016/Snapclass.git)

2. Navigate to the project directory:
   bash
   cd Snapclass
   
   
3. Create and activate a virtual environment:
   bash
   python -m venv venv
   venv\Scripts\activate

4. Install depedencies:
   bash
   pip install -r requirements.txt

## Usage
1. Start the local server:
   bash
   python app.py

2. Open web browser and navigate to:
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

3. Choose either Voice Attendance mode(record roll call) or Photo Mode
   (upload a picture of the class)  to mark attendence.

## Roadmap

[x] Basic project structure and user interface

[ ] Implement audio processing & speech-to-text roll call parsing

[ ] Implement image detection for classroom photos

[ ] Add attendance log export (CSV/Excel support)

[ ] Add student database and roster management UI

## Contributing
Contributions make the open-source community an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

1. Fork the Project

2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

3. Commit your Changes (git commit -m 'Add some AmazingFeature')

4. Push to the Branch (git origin push feature/AmazingFeature)

5. Open a Pull Request

## Contact
Pluck016 - GitHub Profile
Project Link: https://github.com/Pluck016/Snapclass




    

