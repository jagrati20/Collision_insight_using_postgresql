import psycopg2
import pandas as pd
from dicttoxml import dicttoxml

conn = psycopg2.connect("dbname=collision_insight host=localhost user=collision_insight password=collision_insight")
cur = conn.cursor()

with conn.cursor() as cursor:
    with open('schema.sql', 'r') as project:
        setup_queries = project.read()
        cursor.execute(setup_queries)

# Loading Hospital Datasets
with open('datasets/hospital_details.csv', mode='r') as hospitalDetails:
    next(hospitalDetails)
    cur.copy_from(hospitalDetails, 'hospital_details', sep=',')

with open('datasets/hospital_naics_code.csv', 'r') as hospitalNaics:
    next(hospitalNaics)
    cur.copy_from(hospitalNaics, 'hospital_naics', sep=',')

with open('datasets/hospital_owners.csv', 'r') as hospitalOwner:
    next(hospitalOwner)
    cur.copy_from(hospitalOwner, 'hospital_owner', sep=',')

with open('datasets/hospital_types.csv', 'r') as hospitalType:
    next(hospitalType)
    cur.copy_from(hospitalType, 'hospital_type', sep=',')

with open('datasets/hospital_vals.csv', 'r') as hospitalVal:
    next(hospitalVal)
    cur.copy_from(hospitalVal, 'hospital_val', sep=',')

# Loading Liquor datasets
with open('datasets/liquor_shop_info.csv', 'r') as liquorInfo:
    next(liquorInfo)
    cur.copy_from(liquorInfo, 'liquor_shop_info', sep=',')

# Loading vehicle repair datasets
with open('datasets/Vehicle_Repairs.csv', 'r') as vehicleRepair:
    next(vehicleRepair)
    cur.copy_from(vehicleRepair, 'vehicle_repair_info', sep=',')

with open('datasets/Vehicle_Business.csv', 'r') as vehicleBusiness:
    next(vehicleBusiness)
    cur.copy_from(vehicleBusiness, 'vehicle_repair_business_type', sep=',')

# Loading vehicle collision dataset
with open('datasets/vehicle_collision.csv', 'r') as collision:
    next(collision)
    cur.copy_from(collision, 'vehicle_collision', sep=',')

# Making XML file
data = pd.read_csv('datasets/location_combo.csv', sep=',')
data_dict = data.to_dict(orient="records")
collision_xml_data = dicttoxml(data_dict).decode()
with open("datasets/locations.xml", "w+") as f:
    f.write(collision_xml_data)

print('Data Loading Completed')

conn.commit()

cur.close()
conn.close()
