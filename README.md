# Python-Image-downloader

Dowload all the images from a webpage.

## Requirements

Firstly install bs4 and requests for python3 using

```bash
pip3 install -r requirements.txt
```

## Usage

There are two ways to use this script:
  1. Assign the value of "url" to the link of the webpage and run downloader.py
  2. Import ImageDownloader class from downloader.py and create its object by passing page url and call find_images() function.

### Note 

If you want only certain image types to be scraped then edit SUPPORTED_IMAGE_TYPES  in config.py according to your requirements.
I have added eight image types: ".jpg", ".jpeg", ".png", ".gif", ".svg", ".ico", ".eps", ".psd".
Also if you want to download images only located on specific tags, edit SUPPORTED_IMAGE_ATTRIBUTES  in config.py
Support for downloading base64 images will be added soon.
