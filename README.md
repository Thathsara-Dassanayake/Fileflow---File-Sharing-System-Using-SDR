# Fileflow---File-Sharing-System-Using-SDR
Innovative system for robust file sharing between two computers using Software Defined Radio. 
![image](https://github.com/user-attachments/assets/122f4d4a-8c95-41ed-bff6-ff2315bbb47a)
## Introduction

The Fileflow project, part of our Semester 3 Communication Design module, aims to create a simple, robust file sharing system for audio, video, and text files between two computers. This system employs RTL-SDR (Software Defined Radio) and BladeRF devices, known for their flexibility and high performance in wireless communication. Utilizing GNU Radio software, we will implement the software components necessary for encoding, transmitting, receiving, and decoding files, ensuring a customizable and efficient communication pipeline. This project highlights the practical applications of these advanced technologies in modern file sharing solutions.

## Requirements

The Fileflow project entails the development of a point-to-point digital wireless communication system using software-defined radios (SDRs). The following are the key requirements for the project:

#### Communication System Implementation:
* Design and implement a digital wireless communication system that uses RTL-SDR and BladeRF devices to establish a secure and reliable connection between two computers.
#### Security and Reliability:
* Ensure that communications are both secure and reliable, incorporating measures to prevent eavesdropping and mitigate the effects of external jamming.
#### Transmitter Design:
* Encoding: Develop encoding mechanisms to prepare files for transmission.
* Security Implementation: Implement security protocols to protect data.
* Reliability Enhancement: Include features to enhance the reliability of data transmission.
* Jamming Protection: Integrate protection against potential jamming attacks.
* Modulation: Apply suitable modulation techniques for effective data transmission.
#### Receiver Design:
* Reliability Enhancement: Implement measures to enhance the reliability of received data.
* Demodulation: Develop demodulation techniques to accurately retrieve data from the signal.
* Decoding: Create decoding methods to reconstruct the original files from the received data.
#### Operational Parameters:
* Frequency Band: Operate the system within the 2.4 GHz ISM band, adhering to maximum power limitations to comply with regulations.
* User Interface: Design a user-friendly interface to facilitate easy operation and monitoring of the system.
#### Performance Evaluation:
* Assess the system's performance by evaluating communication effectiveness over varying distances and measuring end-to-end delay to ensure minimal latency.
#### Optional Features:
* Channel Estimation: Implement techniques to estimate channel conditions for optimizing communication parameters.
* Adaptive Transmission: Incorporate adaptive transmission methods to adjust to changing channel conditions dynamically.
* Closed-Loop System: Develop a closed-loop system to enhance communication efficiency and reliability through feedback mechanisms.

## The Main Block diagram of the communication system
![image](https://github.com/user-attachments/assets/9d823499-d250-4e8f-a46f-99fa5cbe86a0)

## GNU Radio Files
### Image Files Transfer
![image](https://github.com/user-attachments/assets/baf96a9e-23ba-436a-83c6-b6a841993529)
### TXT File Transfer
![image](https://github.com/user-attachments/assets/61bce768-0fac-48df-be1a-da2ed4085039)
### Audio File Transfer
![image](https://github.com/user-attachments/assets/10419b02-623f-4f2e-8571-105714975b0d)
### File Transfer (Also used final demonstration)
![image](https://github.com/user-attachments/assets/d079f4ce-0065-47b7-8994-6bc2c470eac2)
## Other
### Simple Fm radio
![image](https://github.com/user-attachments/assets/a63ba0ef-67f4-4d89-9e0a-b2b5252d3d6a)
### AM modulation
![image](https://github.com/user-attachments/assets/21ad81a9-f5a3-48af-b38d-af146af5d44d)

## Software Used

- **GNU Radio**: 
  - [GNU Radio](https://www.gnuradio.org/) is a free and open-source toolkit for building software-defined radios and signal-processing systems.
- **MATLAB**: 
  - [MATLAB](https://www.mathworks.com/products/matlab.html) is a programming platform designed specifically for engineers and scientists.

## Resources

- **GNU Radio Tutorials**: 
  - [GNU Radio Tutorials](https://wiki.gnuradio.org/index.php/Tutorials) offer comprehensive guides and examples to help users get started with GNU Radio.
