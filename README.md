# HTML Image Downloader

This Python script allows you to download images from an HTML file by extracting image URLs and saving the images to a specified directory. It can be useful when you need to scrape images from a web page or process HTML content containing image links.

## Features

- Downloads images from an HTML file.
- Supports various image formats such as JPG, PNG, GIF, MP4, and WebP.
- Provides flexibility to specify the output directory for downloaded images.

## How to Use

1. Install Python if you haven't already (https://www.python.org/).
2. Clone this repository or download the script `assets_loader.py`.
3. Prepare your HTML file containing image links.
4. Open a terminal or command prompt and navigate to the directory containing the script.
5. Run the script by executing the command: 

python assets_loader.py file_name.html


Replace `file_name.html` with the path to your HTML file.

6. Specify the directory where you want to save the downloaded images when prompted.

## Example

Suppose you have an HTML file named `example.html` with image links. You can use this script to download the images by running:

python assets_loader.py example.html


## Dependencies

- requests: For making HTTP requests to download images.
- re: For regular expression-based pattern matching.
- os: For interacting with the file system.


Feel free to contribute or report issues [here](https://github.com/kastsen/grab-images-from-html).


