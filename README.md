# CSV to JSON Converter 📝➡️📦

A simple Python script to convert CSV files into JSON format for use with AWS DynamoDB. This script reads CSV files containing structured data, processes each row, and generates individual JSON files that can be imported as new items into a DynamoDB table.

## Features 🌟

- ✅ Converts CSV files to JSON format for DynamoDB import.
- 🗂️ Prompts to choose input and output folder paths.
- 🗓️ Automatically organizes JSON files into folders based on CSV object types.
- 📋 Logs processing details to a log file for tracking purposes.

## Prerequisites 🛠️

- 🐍 Python 3.6 or higher (Tested on Python 3.12)
- 📦 `tqdm` library for progress bars
- 🌈 `colorama` library for colored output

## Installation 🔧

1. Clone the repository:

   ```
   git clone https://github.com/x0rtex/dynamodb-csv-to-json.git
   ```
   
2. Navigate to the project directory:

   ```
   cd dynamodb-csv-to-json
   ```
   
3. Install required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage 🚀

1. Place your CSV files (e.g., `songs.csv`, `albums.csv`, `artists.csv`) in the input folder.

2. Run the script:

   ```
   python csv_to_json_converter.py
   ```

3. Follow the prompts to specify input and output folder paths.

4. The script will create a folder named with the current date and time and store the JSON files within corresponding subfolders based on the object type (e.g., `songs`, `albums`, `artists`).

## Example 📁

Here's an example of what the input and output will look like:

```
input/ 
   ├── songs.csv
   ├── albums.csv
   ├── artists.csv
   └── ...
```

```
output/ 
└── 2025-04-07_14-30-00/ 
   ├── songs/ 
   │ ├── song_1.json 
   │ ├── song_2.json 
   │ └── ... 
   ├── albums/ 
   │ ├── album_1.json 
   │ ├── album_2.json 
   │ └── ... 
   ├── artists/ 
   │ ├──  artist_1.json 
   │ ├──  artist_2.json 
   │ └──  ...
   ...
```
