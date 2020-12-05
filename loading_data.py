import psycopg2
import pandas as pd
from dicttoxml import dicttoxml

# conn2 = psycopg2.connect(host='localhost', user='postgres')
# conn2.autocommit = True
# cur2 = conn2.cursor()
#
# cur2.execute("DROP DATABASE IF EXISTS collision_insight")
# cur2.execute("CREATE DATABASE collision_insight")
# sql = '''
# DROP USER IF EXISTS collision_insight;
# CREATE USER collision_insight WITH PASSWORD 'collision_insight';
#
# GRANT ALL PRIVILEGES ON SCHEMA collision_insight TO collision_insight;
# GRANT ALL PRIVILEGES ON DATABASE collision_insight TO collision_insight;
#
# ALTER USER collision_insight SET search_path = collision_insight;
# '''
# cur2.execute(sql)
# # with conn2.cursor() as cursor:
# #     with open('database-setup.sql', 'r') as setup:
# #         setup_queries = setup.read()
# #         cursor.execute(setup_queries)
# conn2.commit()
# conn2.close()

conn = psycopg2.connect("dbname=collision_insight host=localhost dbname=collision_insight user=collision_insight")
cur = conn.cursor()

with conn.cursor() as cursor:
    with open('project_schema.sql', 'r') as project:
        setup_queries = project.read()
        cursor.execute(setup_queries)

# Loading Hospital Datasets
with open('Datasets/Hospital datasets/hospital_details.csv', mode='r') as hospitalDetails:
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

# Loading vehicle collision dataset
with open('Datasets/Vehicle Collision datasets/vehicle_collision.csv', 'r') as collision:
    next(collision)
    cur.copy_from(collision, 'vehicle_collision', sep=',')

# Making XML file
data = pd.read_csv('Datasets/location_combo.csv', sep=',')
data_dict = data.to_dict(orient="records")
collision_xml_data = dicttoxml(data_dict).decode()
with open("locations.xml", "w+") as f:
    f.write(collision_xml_data)

conn.commit()

cur.close()
conn.close()
