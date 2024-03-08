# Python Download Organizer

This Python script automatically organizes your downloads into folders by date, helping you keep your Downloads directory clean and sorted.

## Features

- **Automatic Organization**: Moves downloaded files into date-stamped folders.
- **Runs in Background**: Once set up as a scheduled task, the script operates quietly in the background.
- **Customizable**: Easy to modify for different paths or organization schemes.

## Getting Started

### Prerequisites

- Python 3.6 or newer installed on your machine.
- The `watchdog` Python package. Install it using `pip install watchdog`.

### Installation

1. Clone the repository or download the script to your preferred location:

https://github.com/breimato/DownloadOrganizer.git


2. Ensure Python and pip are correctly installed on your system by running `python --version` and `pip --version`.

3. Install the required Python package:

pip install watchdog



## Usage

1. Modify the `downloads_path` variable in the script to match your Downloads directory path.
2. To run the script manually, navigate to the script's directory and run:

python download_organizer.py



### Setting Up as a Scheduled Task in Windows

To have the script run automatically in the background, set it up as a scheduled task:

1. Open **Task Scheduler** in Windows.
2. Select **Create Task** in the right pane.
3. **General tab**: Enter a name for the task.
4. **Triggers tab**: Click **New** and set the trigger to **At log on** or **At startup**.
5. **Actions tab**: Click **New**.
 - **Program/script**: Enter the path to your `python.exe` (usually found in your Python installation directory).
 - **Add arguments (optional)**: Enter the path to the script.
 - **Start in (optional)**: Enter the script directory path.
6. **Conditions tab**: Adjust conditions as needed.
7. **Settings tab**: Adjust settings as needed.
8. Click **OK** to save the task.

## Contributions

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

## License

Distributed under the MIT License. See `LICENSE` for more information.
