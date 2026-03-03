# AI X-Ray Report Generator
Automatically generates accurate medical reports from chest X-ray images using a pretrained medical AI model.

## Features

- **Purpose:** Use a pretrained medical AI model to generate accurate medical reports from chest X-ray images.

### 👤 Role-Based Access Control

The system supports three user roles:

- **Regular User**
  - Upload chest X-ray images.
  - Automatically generate AI-based medical reports.
  - Save generated reports to the personal "My Reports" database.
  - Submit reports for professional review.

- **Doctor**
  - Access "Pending Reports for Review".
  - Evaluate and edit AI-generated reports.
  - Approve or modify reports submitted by users.

- **Admin**
  - View all reports from all users.
  - Access pending review reports.
  - Manage user accounts (create, delete, and modify roles).
    
## Installation

### Option 1: Using Python 3.10 / 3.11 (Recommended)

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
pip install -r requirements.txt
```
### Option 2: Using Conda (for other Python version users)

```bash
conda create -n py311 python=3.11
conda activate py311
pip install -r requirements.txt
```
## Usage

```bash
python app.py
```
Open your browser at http://127.0.0.1:5001

### Note on Full Functionality
The current version runs on CPU for demonstration purposes.  
Full functionality, including integration with large language models (LLMs) for enhanced report generation, can be enabled on a GPU.

## Third‑Party Code / Attribution

The folder `backend/CXR‑RePaiR` contains code from the open‑source project:

**CXR‑RePaiR**  
https://github.com/rajpurkarlab/CXR‑RePaiR

This code is included here and used as part of our X‑ray report system.

⚠️ This project is for research and educational purposes only.  
It should not be used for clinical diagnosis or treatment.
