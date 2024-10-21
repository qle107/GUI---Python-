# Excel File Viewer and Data Analyst using PySimpleGUI, pandas, and lxml

## Overview

This application allows users to read data from an Excel file and display it in a graphical interface using `PySimpleGUI`. The data is imported using `pandas`, and various data analysis functions can be performed on the Excel data. The application leverages the `lxml` library for Excel file parsing, `pandas` for data manipulation, and `PySimpleGUI` for the graphical user interface.

## Features

- **Load Excel Files**: Read and import Excel files (`.xlsx`) using `pandas`.
- **Graphical User Interface**: Display the contents of the Excel file in a user-friendly table format using `PySimpleGUI`.
- **Data Analysis**: Perform data analysis and manipulation using `pandas`, such as filtering, grouping, and summarizing the data.
  
## Technologies Used

- **pandas**: For data manipulation and analysis.
- **lxml**: For Excel file parsing.
- **PySimpleGUI**: For building the graphical user interface (GUI).

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.6+
- pip (Python package manager)

### Install Required Python Libraries

To install the necessary Python libraries, run the following command:

```bash
pip install -r requirement.txt
```

### Note:
- `pandas` is used for reading, analyzing, and manipulating Excel data.
- `lxml` is required for parsing XML data (used internally by Excel files).
- `PySimpleGUI` is used to create the GUI.

## Usage

### 1. Running the Application

1. Clone or download the repository to your local machine.
2. Ensure you have installed the necessary dependencies (see [Installation](#installation)).
3. Run the Python script that contains the GUI and data processing logic:

```bash
python app.py
```

### 2. Loading an Excel File

1. When the application starts, a GUI window will appear with an option to **Browse** for an Excel file (`.xlsx`).
2. Click the **Browse** button to select the file you want to load.

### 3. Viewing and Analyzing Data

- Once the file is loaded, the data will be displayed in a table within the GUI.
- You can interact with the data, view different sheets, and perform data analysis (filtering, grouping, etc.) using the built-in options provided in the application.
  

### Example GUI Workflow

- The app opens a PySimpleGUI window with a file selection dialog.
- Upon selecting an Excel file, the data is loaded into a `pandas` DataFrame.
- The data is displayed in a table on the GUI.
- Users can perform basic data manipulation like sorting, filtering, or grouping using `pandas` functionalities.

