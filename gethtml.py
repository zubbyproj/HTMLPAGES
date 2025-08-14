import json
import os
from bs4 import BeautifulSoup

def get_unique_filename(directory, base_name):
    """
    Generate a unique filename by appending a number if needed.
    """
    name, ext = os.path.splitext(base_name)
    counter = 1
    new_name = base_name

    while os.path.exists(os.path.join(directory, new_name)):
        new_name = f"{name}_{counter}{ext}"
        counter += 1

    return new_name

def extract_and_format_html(json_path, output_dir):
    # Load JSON data
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for filename, html_content in data.items():
        # Format HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')
        pretty_html = soup.prettify()

        # Ensure filename ends with .html
        if not filename.endswith('.html'):
            filename += '.html'

        # Get a unique filename to avoid overwriting
        unique_filename = get_unique_filename(output_dir, filename)

        # Save formatted HTML to file
        file_path = os.path.join(output_dir, unique_filename)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(pretty_html)

        print(f"Saved: {file_path}")

# Example usage
if __name__ == "__main__":
    json_file = 'C://Users//zubai//OneDrive//WORK//HTMLPAGES//embrista_landing_pages.json'         # Replace with your JSON file path
    output_folder = 'C://Users//zubai//OneDrive//WORK//HTMLPAGES//WebPages'    # Folder to save HTML files
    extract_and_format_html(json_file, output_folder)