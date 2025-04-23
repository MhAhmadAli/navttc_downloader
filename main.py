import requests
import os
from urllib.parse import urlparse
from pathlib import Path

def download_file(url, output_dir='downloads'):
    try:
        # Create output directory if it doesn't exist
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # Get filename from URL or use a default name
        filename = os.path.basename(urlparse(url).path)
        if not filename:
            filename = 'downloaded_file'
        
        # Full path for the output file
        output_path = os.path.join(output_dir, filename)
        
        # Download the file
        print(f"Downloading: {url}")
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Save the file
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        
        print(f"Successfully downloaded: {filename}")
        return True
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected error while downloading {url}: {str(e)}")
        return False

def main():
    # Check if links.txt exists
    if not os.path.exists('links.txt'):
        print("Error: links.txt file not found!")
        return
    
    # Read links from file
    with open('links.txt', 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    
    if not links:
        print("No links found in links.txt!")
        return
    
    # Download each file
    successful_downloads = 0
    for link in links:
        if download_file(link):
            successful_downloads += 1
    
    # Print summary
    print(f"\nDownload Summary:")
    print(f"Total links: {len(links)}")
    print(f"Successful downloads: {successful_downloads}")
    print(f"Failed downloads: {len(links) - successful_downloads}")

if __name__ == "__main__":
    main()
