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

    def check_connectivity(self):
        cursor = self.conn.cursor()
        print('HERE')
        cursor.execute("SELECT * FROM collision_insight.vehicle_collision")
        records = cursor.fetchall()
        print(records)
        self.conn.close()

    def check_hospital(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM collision_insight.hospital_details")
        records = cursor.fetchall()
        print(records)
        self.conn.close()
