# from Application import *
import psycopg2
import psycopg2.extras
import loading_data
import lxml
from lxml import etree


class CollisionData:
    connection_string = "dbname='collision_insight' host='localhost' dbname='collision_insight' " \
                        "user='collision_insight' password='collision_insight'"

    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)

    xml_file = 'locations.xml'
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(xml_file, parser)
    # self.conn.commit()
    # self.conn.close()
    print('here 2')

    def check_collisions(self):
        cursor = self.conn.cursor()
        print('\nPlease select your Collision query:\n1. Collisions corresponding to a type of vehicle\n2. Collisions '
              'due to a factor\n3. Got a Collision ID?\n4. Wanna have it all?!\n5 Back to the Menu')
        selection = input()
        try:
            val = int(selection)
        except ValueError:
            print("\nThe value entered is not an integer value! Please try again.")
            self.check_collisions()

        if val == 1:
            print("Please enter the type of the vehicle")
            vehicle = input()
            # checks if value is a string
            try:
                if vehicle.isnumeric() | vehicle.isalnum() & (vehicle.isalpha() != True):
                    raise ValueError
            except ValueError:
                print("\nThe value entered is not a correct vehicle type! Please try again.")
                self.check_collisions()

            cursor.execute("SELECT collision_id, crash_date, crash_time, vehicle_type_code FROM "
                           "collision_insight.vehicle_collision WHERE vehicle_type_code iLIKE '%{}%'".format(
                str(vehicle.lower()), ))
            # cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
            self.check_collisions()

        elif val == 2:
            print("Please enter the factor influencing the vehicle collision")
            factor = input()
            try:
                if factor.isnumeric() | factor.isalnum() & (factor.isalpha() != True):
                    raise ValueError
            except ValueError:
                print("\nThe value entered is not a valid cause for collision! Please try again.")
                self.check_collisions()
            cursor.execute("SELECT collision_id, crash_date, crash_time, contributing_factors FROM "
                           "collision_insight.vehicle_collision WHERE contributing_factors iLIKE '%{}%'".format(
                            str(factor.lower()), ))

            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))

            self.check_collisions()

        elif val == 3:
            print("Please enter the Collision ID")
            id = input()
            try:
                if (id.isalnum() | id.isalpha()) & (id.isnumeric() != True):
                    raise ValueError
            except ValueError:
                print("\nThe entered ID is not valid! Please try again.")
                self.check_collisions()
            cursor.execute("SELECT collision_id, crash_date, crash_time, vehicle_type_code FROM "
                           "collision_insight.vehicle_collision WHERE collision_id = '{}'".format(
                             str(id.lower()), ))
            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            print("Collision ID" + " " + "Crash Date" + " " + "Crash Time" + " " + "Colliding Vehicles")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
            # print("\n")
            self.check_collisions()

        elif val == 4:
            print("Hold tight...")
            print("Wait for it... sit back and relax while we populate the data for you!")
            cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
            records = cursor.fetchall()
            for r in records:
                print(
                    str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]) + "\t" + str(
                        r[5]) + "\t" + str(r[6]) + "\t" + str(r[7]) + "\t" + str(r[8]) + "\t" + str(r[9]) + "\t" + str(
                        r[10]) + "\t" + str(r[11]) + "\t" + str(r[12]) + "\t" + str(r[13]) + "\t" + str(
                        r[14]) + "\t" + str(r[15]))

            self.check_collisions()

        elif val == 5:
            self.check_collisions()

        else:
            print("The entered int value does not exist in the database.\nPlease enter again.")
            self.check_collisions()
        self.conn.close()

    def check_repairs(self):
        cursor = self.conn.cursor()
        print('\nPlease select your Vehicle Repair shop query:\n1. Repair Shops in a particular zip code\n2. '
              'Know the owner of a repair shop? Search by Owner name.\n3. Got a Facility ID?\n4. Wanna have it '
              'all?!\n5. Back to the Menu')
        selection = input()
        try:
            val = int(selection)
        except ValueError:
            print("\nThe value entered is not an int! Please try again.")
            self.check_repairs()

        if val == 1:
            print("Please enter the zip code ")
            zip_repair = input()
            # checks if value is a string
            try:
                if (zip_repair.isalnum() | zip_repair.isalpha()) & (zip_repair.isnumeric() != True):
                    raise ValueError
            except ValueError:
                print("\nThe value entered is not a correct zipcode! Please try again.")
                self.check_repairs()

            cursor.execute("SELECT vr.zipcode, vr.facility_name, vr.facility_name_overflow, vr.facility_street, "
                           "vb.business_type FROM collision_insight.vehicle_repair_info vr, "
                           "collision_insight.vehicle_repair_business_type vb WHERE vr.facility_id = vb.facility_id "
                           "AND vr.zipcode = CAST('{}' AS INTEGER)".format(zip_repair, ))

            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]))
            self.check_repairs()

        elif val == 2:
            print("Please enter the Owner name")
            name = input()
            try:
                if name.isnumeric():
                    raise ValueError
            except ValueError:
                print("\nYou must be remembering it wrong! Please try again.")
                self.check_repairs()
            cursor.execute("SELECT vr.zipcode, vr.facility_name, vr.facility_street, "
                           "vr.owner_name, vr.owner_name_overflow FROM collision_insight.vehicle_repair_info vr, "
                           "collision_insight.vehicle_repair_business_type vb WHERE vr.owner_name iLIKE '%{}%' OR "
                           "vr.owner_name_overflow iLIKE '%{}%' LIMIT 10".format(str(name.lower()),
                                                                                 str(name.lower()), ))

            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]))
                # print("\n")
            self.check_repairs()

        elif val == 3:
            print("Please enter the Facility ID")
            id = input()
            try:
                if (id.isalnum() | id.isalpha()) & (id.isnumeric() != True):
                    raise ValueError
            except ValueError:
                print("\nThe value entered is not a valid Facility ID! Please try again.")
                self.check_repairs()
            cursor.execute("SELECT vr.facility_id, vr.facility_name, vr.facility_street, "
                           "vb.business_type FROM collision_insight.vehicle_repair_info vr, "
                           "collision_insight.vehicle_repair_business_type vb WHERE vr.facility_id = vb.facility_id "
                           "AND vr.facility_id = CAST('{}' AS INTEGER)".format(id, ))
            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            print("Facility ID" + " " + "Facility Name" + " " + "Street Address" + " " + "Business Type")
            for r in records:
                print(str(r[0]) + " " + str(r[1]) + " " + str(r[2]) + " " + str(r[3]))
            # print("\n")
            self.check_repairs()

        elif val == 4:
            print("Hold tight...")
            print("sit back and relax while we populate the data for you!")
            print("Wait for it...")
            cursor.execute("SELECT * FROM collision_insight.vehicle_repair_info vr, "
                           "collision_insight.vehicle_repair_business_type vb WHERE vr.facility_id = vb.facility_id "
                           "LIMIT 500")
            records = cursor.fetchall()
            if len(records) == 500:
                print("A large amount of data requested. Showing the first 500 valid records.\n")
            else:
                print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                # print(r)
                print(
                    str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]) + "\t" + str(
                        r[5]) + "\t" + str(r[6]) + "\t" + str(r[7]) + "\t" + str(r[8]) + "\t" + str(r[9]) + "\t" + str(
                        r[11]))

            self.check_repairs()

        elif val == 5:
            self.check_repairs()

        else:
            print("The entered int value does not exist in the database.\nPlease enter again.")
            self.check_repairs()
        self.conn.close()

    def check_hospital(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM collision_insight.hospital_details")
        records = cursor.fetchall()

        print(records)
        print(self.get_county)
        self.conn.close()

    def run_query(self, query):
        return self.tree.xpath(query)

    def get_county(self):
        c = self.run_query('/root/item[ZIP/text()=91706]/COUNTY/text()')
        print(c)
        return c
