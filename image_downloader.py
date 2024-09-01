import requests
from astropy.io import fits
import matplotlib.pyplot as plt

# Define URLs for FITS files
fits_urls = [
    "https://data.sdss.org/sas/dr16/eboss/photoObj/frames/301/0000/6/frame-r-000006-1-0123.fits.bz2",
    "https://data.sdss.org/sas/dr16/eboss/photoObj/frames/301/0000/6/frame-g-000006-1-0123.fits.bz2"
]

# Function to download FITS files
def download_fits(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {filename}")

# Download the FITS files
for i, url in enumerate(fits_urls):
    download_fits(url, f"image_{i+1}.fits.bz2")

# Open and display FITS files
for i in range(len(fits_urls)):
    with fits.open(f"image_{i+1}.fits.bz2") as hdul:
        hdul.info()
        image_data = hdul[0].data
        plt.figure()
        plt.imshow(image_data, cmap='gray')
        plt.colorbar()
        plt.title(f"Image {i+1}")
        plt.show()