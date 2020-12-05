from Application import *
import psycopg2
import psycopg2.extras
import loading_data
import lxml
from lxml import etree


class CollisionData:
    connection_string = "dbname='collision_insight' host='localhost' dbname='collision_insight' " \
                        "user='collision_insight' password='collision_insight'"

    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)

    def SetUp(self):
        xml_file = 'locations.xml'
        parser = etree.XMLParser(ns_clean=True)

        tree = etree.parse(xml_file, parser)
        self.conn.commit()
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
            print("\nThe value entered is not an int! Please try again.")
            self.check_collisions()

        if val == 1:
            print("Please enter the type of the vehicle")
            vehicle = input()
            # Should I check if value is a string?
            cursor.execute("SELECT collision_id, crash_date, crash_time, vehicle_type_code FROM "
                           "collision_insight.vehicle_collision WHERE vehicle_type_code iLIKE '%{}%'".format(
                str(vehicle.lower()), ))
            # cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
            self.check_collisions()

        if val == 2:
            print("Please enter the factor influencing the vehicle collision")
            factor = input()
            # Should I check if value is a string?
            cursor.execute("SELECT collision_id, crash_date, crash_time, contributing_factors FROM "
                           "collision_insight.vehicle_collision WHERE contributing_factors iLIKE '%{}%'".format(
                str(factor.lower()), ))
            # cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
                # print("\n")
            self.check_collisions()

        if val == 3:
            print("Please enter the Collision ID")
            id = input()
            # Should I check if value is a string?
            cursor.execute("SELECT collision_id, crash_date, crash_time, vehicle_type_code FROM "
                           "collision_insight.vehicle_collision WHERE collision_id = '{}'".format(
                str(id.lower()), ))
            # cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
            records = cursor.fetchall()
            print("Your search returned " + str(len(records)) + " records.\n")
            print("Collision ID" + " " + "Crash Date" + " " + "Crash Time" + " " + "Colliding Vehicles")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
            # print("\n")
            self.check_collisions()

        if val == 4:
            print("Hold tight...")
            print("Wait for it... sit back and relax while we populate the data for you!")
            cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
            records = cursor.fetchall()
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]) + "\t" + str(r[5]) + "\t" + str(r[6]) + "\t" + str(r[7]) + "\t" + str(r[8]) + "\t" + str(r[9]) + "\t" + str(r[10]) + "\t" + str(r[11]) + "\t" + str(r[12]) + "\t" + str(r[13]) + "\t" + str(r[14]) + "\t" + str(r[15]))

            self.check_collisions()

        if val == 5:
            RunApplication()
        self.conn.close()

    def check_hospital(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM collision_insight.hospital_details")
        records = cursor.fetchall()

        print(records)
        self.conn.close()
