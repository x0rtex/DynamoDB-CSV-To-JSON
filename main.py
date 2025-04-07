import csv
import json
import os
import logging
from datetime import datetime

from colorama import Fore, init
from tqdm import tqdm

# Initialize colorama
init(autoreset=True)

# Constants for folder names and log messages
DEFAULT_INPUT_FOLDER = 'input'
DEFAULT_OUTPUT_FOLDER = 'output'
LOG_FILE = 'conversion_log.txt'

# Initialize logging
logging.basicConfig(filename="conversion_log.txt", level=logging.INFO, format='%(asctime)s - %(message)s')


def process_csv(input_folder: str, output_folder: str,
                csv_filename: str, object_type_folder: str) -> None:
    input_path: str = os.path.join(input_folder, csv_filename)

    if not os.path.exists(input_path):
        print(Fore.YELLOW + f"⚠️ File {csv_filename} does not exist in {input_folder}. Skipping...")
        return

    # Creating the output folder path
    object_output_folder: str = os.path.join(output_folder, object_type_folder)
    os.makedirs(object_output_folder, exist_ok=True)
    logging.info(f"✅ Created folder: {object_output_folder}")

    with open(input_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        try:
            headers = next(reader)
            if not headers:
                raise StopIteration
        except StopIteration:
            print(Fore.RED + f"❌ File {csv_filename} is empty. Skipping...")
            return
        except Exception as e:
            print(Fore.RED + f"❌ Error reading file {csv_filename}: {str(e)}")
            return

        # Process each row in the CSV with a progress bar
        rows = list(reader)  # Convert reader to a list to count rows
        if not rows:
            print(Fore.RED + f"❌ No data rows found in {csv_filename}. Skipping...")
            return

        csvfile.seek(0)  # Rewind the file to start processing again
        next(reader)  # Skip the header row

        for row in tqdm(rows, desc=f"🔄 Processing {csv_filename}", ncols=100, unit="row",
                        bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt}", total=len(rows)):
            data: dict = {}
            for index, value in enumerate(row):
                key: str = headers[index].strip()
                # If the column is numeric, assume it's a number, otherwise it's a string
                if value.isdigit():
                    data[key] = {"N": value}
                else:
                    data[key] = {"S": value.strip('"')}

            # Use the first column (or a unique identifier) for the file name
            unique_id: str = row[0]
            output_filename: str = f"{object_type_folder}_{unique_id}.json"
            output_path: str = os.path.join(output_folder, object_type_folder, output_filename)

            # Write the data into a JSON file
            try:
                with open(output_path, 'w') as json_file:
                    json.dump(data, json_file, indent=2)
                logging.info(f"✅ Successfully processed {output_filename}")
            except Exception as e:
                logging.error(f"❌ Error processing {output_filename}: {str(e)}")
                print(Fore.RED + f"⚠️ Error processing {output_filename}. See log for details.")


def main(input_folder: str, output_folder: str) -> None:
    # Get the current date and time to create a unique root folder
    current_time: str = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    root_output_folder: str = os.path.join(output_folder, current_time)
    os.makedirs(root_output_folder, exist_ok=True)
    logging.info(f"✅ Created root output folder: {root_output_folder}")

    print(Fore.CYAN + "🔍 Scanning for CSV files in the input folder...")

    csv_files: list[str] = [f for f in os.listdir(input_folder) if f.endswith('.csv')]

    if not csv_files:
        print(Fore.RED + "❌ No CSV files found in the input folder.")
        return

    for csv_filename in csv_files:
        object_type: str = csv_filename.split('.')[0].lower()
        process_csv(input_folder, root_output_folder, csv_filename, object_type)

    print(Fore.GREEN + "🎉 Conversion completed successfully!")


if __name__ == '__main__':
    print(Fore.MAGENTA + "👋 Welcome to the CSV to JSON Converter!")

    input_folder_path: str = (input(
        Fore.YELLOW + "📂 Enter the input folder path (or press Enter to use default 'input'): ")
                              .strip() or DEFAULT_INPUT_FOLDER)

    output_folder_path: str = (input(
        Fore.YELLOW + "📂 Enter the output folder path (or press Enter to use default 'output'): ")
                               .strip() or DEFAULT_OUTPUT_FOLDER)

    input_folder_path = os.path.abspath(input_folder_path)
    output_folder_path = os.path.abspath(output_folder_path)

    os.makedirs(input_folder_path, exist_ok=True)
    os.makedirs(output_folder_path, exist_ok=True)

    main(input_folder_path, output_folder_path)
