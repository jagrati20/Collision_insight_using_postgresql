import psycopg2
import pandas as pd
import dicttoxml
conn = psycopg2.connect("dbname=collision_insight host=localhost dbname=collision_insight user=collision_insight")

cur = conn.cursor()

# Loading Hospital Datasets
with open('Datasets/Hospital datasets/hospital_details.csv', mode='r') as hospitalDetails:
    #Skipping the header
    next(hospitalDetails)
    cur.copy_from(hospitalDetails, 'hospital_details', sep=',')

with open('Datasets/Hospital datasets/hospital_naics_code.csv', 'r') as hospitalNaics:
    next(hospitalNaics)
    cur.copy_from(hospitalNaics, 'hospital_naics', sep=',')

with open('Datasets/Hospital datasets/hospital_owners.csv', 'r') as hospitalOwner:
    next(hospitalOwner)
    cur.copy_from(hospitalOwner, 'hospital_owner', sep=',')

with open('Datasets/Hospital datasets/hospital_types.csv', 'r') as hospitalType:
    next(hospitalType)
    cur.copy_from(hospitalType, 'hospital_type', sep=',')

with open('Datasets/Hospital datasets/hospital_vals.csv', 'r') as hospitalVal:
    next(hospitalVal)
    cur.copy_from(hospitalVal, 'hospital_val', sep=',')

# Loading Liquor datasets
with open('Datasets/liquor datasets/liquor_shop_info.csv', 'r') as liquorInfo:
    next(liquorInfo)
    cur.copy_from(liquorInfo, 'liquor_shop_info', sep=',')

# Loading vehicle repair datasets
with open('Datasets/Vehicle Repair Datasets/Vehicle_Repairs.csv', 'r') as vehicleRepair:
    next(vehicleRepair)
    cur.copy_from(vehicleRepair, 'vehicle_repair_info', sep=',')

with open('Datasets/Vehicle Repair Datasets/Vehicle_Business.csv', 'r') as vehicleBusiness:
    next(vehicleBusiness)
    cur.copy_from(vehicleBusiness, 'vehicle_repair_business_type', sep=',')

# Populating location dataset
# with open('Datasets/location_combo.csv', 'r') as location:
#     next(location)
#     cur.copy_from(location, 'location_data', sep=',')

# print('finished loading')
data = pd.read_csv('Datasets/Vehicle Collision datasets/vehicle_collision.csv')
data_dict = data.to_dict(orient="records")
collision_xml_data = dicttoxml(data_dict).decode()
with open("collisions.xml", "w+") as f:
    f.write(collision_xml_data)

data = pd.read_csv('Datasets/location_combo.csv')
data_dict = data.to_dict(orient="records")
collision_xml_data = dicttoxml(data_dict).decode()
with open("locations.xml", "w+") as f:
    f.write(collision_xml_data)


conn.commit()

cur.close()

conn.close()
