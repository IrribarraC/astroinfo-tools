
import requests
import bz2
from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

path_git = "/mnt/c/Users/Chemito/Documents/GitHub/astroinfo-tools"
path_astro = "/mnt/c/Users/Chemito/Desktop/astrostuff"

# Define URLs for FITS files
fits_urls = [
    f"https://data.sdss.org/sas/dr16/eboss/photoObj/frames/301/1000/6/frame-r-001000-6-00{28 + i}.fits.bz2" for i in range(50)
]

# Function to download and decompress FITS files
def download_fits(url, filename):
    response = requests.get(url)
    compressed_filename = filename + '.bz2'
    with open(compressed_filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {compressed_filename}")
    
    # Decompress the file
    with bz2.BZ2File(compressed_filename, 'rb') as compressed_file:
        with open(filename, 'wb') as decompressed_file:
            decompressed_file.write(compressed_file.read())
    print(f"Decompressed {filename}")

# Download and decompress the FITS files
for i, url in enumerate(fits_urls):
    download_fits(url, f"image_{i+1}.fits")

# Open, apply Gaussian filter, and save FITS files
for i in range(len(fits_urls)):
    try:
        with fits.open(f"image_{i+1}.fits") as hdul:
            hdul.info()
            image_data = hdul[0].data
            
            # Apply Gaussian filter
            filtered_image_data = gaussian_filter(image_data, sigma=2)
            
            # Save the filtered image
            plt.figure()
            plt.imshow(filtered_image_data, cmap='gray')
            plt.savefig(f"filtered_image_{i+1}.png")  # Save the plot as a PNG file
            plt.close()  # Close the plot to free memory
            print(f"Saved filtered_image_{i+1}.png")
    except OSError as e:
        print(f"Error opening image_{i+1}.fits: {e}")