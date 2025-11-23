# Student Gradebook CLI

## Overview
Student Gradebook CLI is a Python-based Command-Line Interface (CLI) application for managing a student gradebook.  
It allows users to **add, update, delete courses**, view all courses in a structured format, and **calculate both overall and semester-based GPA**.  
All data is persisted in a JSON file (`gradebook.json`) between sessions, simulating a real-world student grade management system.

---

## Requirements
- Python 3.x
- Terminal / Command Prompt / VS Code (optional)

---

## Installation
1. Download or clone this project folder.
2. Ensure `gradebook.json` exists in the folder. For first use, create it with an empty list:
```json
[]
