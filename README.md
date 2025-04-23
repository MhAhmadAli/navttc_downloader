# NAVTTC Course Material Downloader

This project provides a simple tool to download course materials from the National Vocational and Technical Training Commission (NAVTTC) website. It automates the process of downloading multiple course materials listed in a text file.

## Features

- Downloads course materials from NAVTTC website
- Processes a list of URLs from a text file
- Creates a downloads directory to store the files
- Handles URL-encoded filenames
- Provides progress feedback during downloads
- Generates a summary of successful and failed downloads

## Requirements

- Python 3.6+
- Required Python packages:
  - requests

## Installation

1. Clone this repository or download the source code
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Create a file named `links.txt` in the same directory as the script
2. Add the URLs of the course materials you want to download to `links.txt`, one URL per line
3. Run the main script:
   ```
   python main.py
   ```
4. The script will create a `downloads` directory and download all files there
5. After downloading, you can run the rename script to handle URL-encoded filenames:
   ```
   python rename.py
   ```

## Files

- `main.py` - The main script that downloads files from the URLs in links.txt
- `rename.py` - A utility script that renames downloaded files to handle URL-encoded characters
- `links.txt` - A text file containing the URLs of course materials to download

## Example

The `links.txt` file should contain URLs like:
```
https://navttc.gov.pk/CrashCoursesOverseas/BuildingElectrician.rar
https://navttc.gov.pk/LessonPlans/6Months/3DAnimation.pdf
```

## Notes

- The script will create a `downloads` directory if it doesn't exist
- Files are downloaded with their original filenames
- The rename script can be used to handle URL-encoded characters in filenames
- The script provides feedback on the download progress and a summary at the end 