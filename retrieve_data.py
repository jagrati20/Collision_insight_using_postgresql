import os
import urllib.request as url

download_file = "datasets.txt"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

createFolder('./datasets')

with open(download_file, 'r') as file_input:
    input_files = [line.rstrip('\n') for line in file_input]

url.urlretrieve(input_files[0], 'datasets/hospital_details.csv')
url.urlretrieve(input_files[1], 'datasets/hospital_types.csv')
url.urlretrieve(input_files[2], 'datasets/hospital_owners.csv')
url.urlretrieve(input_files[3], 'datasets/hospital_naics_code.csv')
url.urlretrieve(input_files[4], 'datasets/hospital_vals.csv')
url.urlretrieve(input_files[5], 'datasets/Vehicle_Repairs.csv')
url.urlretrieve(input_files[6], 'datasets/Vehicle_Business.csv')
url.urlretrieve(input_files[7], 'datasets/vehicle_collision.csv')
url.urlretrieve(input_files[8], 'datasets/liquor_shop_info.csv')
url.urlretrieve(input_files[9], 'datasets/location_combo.csv')