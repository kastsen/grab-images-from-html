import requests
import re
import os

def download_images_from_html(html_file_path, output_dir):
    """
    Download images from an HTML file.

    Args:
        html_file_path (str): Path to the HTML file.
        output_dir (str): Directory to save the downloaded images.
    """
    # Check if the specified directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read the content of the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Find all image URLs in the HTML content
    image_urls = re.findall(r'(https?://\S+?\.(?:jpg|png|gif|mp4|webp))', html_content)

    # Download images
    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            # Create a file name based on the image URL
            file_name = os.path.join(output_dir, url.split('/')[-1])
            # Write the image content to the file
            with open(file_name, 'wb') as f:
                f.write(response.content)
            print(f"Image {file_name} successfully downloaded")
        else:
            print(f"Failed to download image from URL: {url}")

if __name__ == "__main__":
    # Example HTML file path
    html_file_path = "example.html"

    # Specify the directory to save images
    output_directory = 'assets'

    # Call the function to download images from the HTML file
    download_images_from_html(html_file_path, output_directory)
