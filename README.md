# PortHound - Network Port Scanner

![PortHound](https://user-images.githubusercontent.com/example/porthound-banner.png)

**PortHound** is a simple yet powerful network port scanner designed to scan open or closed ports on a target machine. It is developed to work efficiently on Termux and other Linux environments. This tool is primarily built for ethical hackers, security researchers, and network administrators who need to quickly check the status of network ports.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contribution](#contribution)
- [License](#license)

---

## Features

- **Fast Network Scanning:** Quickly scan a range of ports on a target machine to identify which ports are open or closed.
- **Cross-Platform Compatibility:** Works on both Termux (Android) and Linux-based systems.
- **Professional UI:** Includes a clean and colorful banner with clear terminal output for an intuitive user experience.
- **Customizable:** You can easily modify the code for personal needs, adding new functionalities or changing the appearance.
- **Error Handling:** Proper error handling for incorrect target input or connection issues.

---

## Prerequisites

Before installing and running **PortHound**, ensure you have the following dependencies installed:

- Python 3.x
- Termcolor (`pip install termcolor`)
- A working internet connection (for scanning remote hosts)

---

## Installation

To install and run **PortHound** on Termux or any Linux-based system, follow these steps:

### 1. Clone the repository:

```bash
git clone https://github.com/WizSafe/porthound.git
```
### 2. Change into the directory
```bash
cd porthound
```
### 3. Run the tool
```bash
python3 porthound.py
```

PortHound is an open-source project maintained by WizSafe Organization. Please use it responsibly and ethically.

