# Super Bowl Boxes Generator

This project automates the management of a Super Bowl Squares (Boxes) pool hosted on a Google Spreadsheet. It handles the randomization of score axes and helps fill the board by distributing available squares among existing participants.

## Features

*   **Smart Filling:** specific logic to calculate and distribute remaining squares evenly among participants who have already selected a box.
*   **Randomized Axes:** Generates and shuffles digits (0-9) for the horizontal and vertical score headers.
*   **Visual Feedback:** Highlights auto-generated square assignments in yellow to distinguish them from manual entries.
*   **Google Sheets Integration:** Uses `gspread` to read and write directly to a live Google Sheet.

## Prerequisites

1.  **Python 3.x**
2.  **Google Cloud Service Account:** You need a JSON key file for a service account with the **Google Sheets API** and **Google Drive API** enabled.

## Installation

1.  Install the required Python packages:
    ```bash
    pip install gspread oauth2client
    ```

2.  **Credentials:**
    *   Place your service account JSON key file in a secure location.
    *   Ensure the `secret_key_path` in `sbb_generator.py` points to this file.
    *   **Share the Spreadsheet:** Open your Google Sheet and share it (Editor access) with the `client_email` address found inside your JSON key file.

## Configuration

Modify `sbb_generator.py` to match your environment:

*   `spreadsheet_name`: The name of your Google Sheet (e.g., "Super Bowl LX").
*   `secret_key_path`: The absolute path to your `secret_key.json`.

## Usage

1.  Open the Google Sheet.
2.  Enter the names of the participants into the main grid area (C3:L12).
3.  Run the script:
    ```bash
    python sbb_generator.py
    ```
4.  The script will:
    *   Calculate the fill factor based on the number of existing names.
    *   Randomly assign empty cells to the existing participants.
    *   Highlight the newly assigned cells.
    *   Randomize the row and column headers (digits 0-9).

## Grid Layout Assumptions

*   **Main Grid:** Cells `C3:L12` (10x10 grid).
*   **Header Rows/Cols:** Row 2 (columns 3-12) and Column 2 (rows 3-12) are reserved for the score digits.
