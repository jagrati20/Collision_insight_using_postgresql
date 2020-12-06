import psycopg2
import psycopg2.extras
import loading_data
from lxml import etree
from tabulate import tabulate


class CollisionData:
    connection_string = "dbname='collision_insight' host='localhost' dbname='collision_insight' " \
                        "user='collision_insight' password='collision_insight'"

    conn = psycopg2.connect(connection_string, cursor_factory=psycopg2.extras.DictCursor)

    xml_file = 'locations.xml'
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(xml_file, parser)

    def check_collisions(self):
        cursor = self.conn.cursor()
        print('\nPlease select your Collision query:'
              '\n1. Collisions corresponding to a type of vehicle'
              '\n2. Collisions due to a factor'
              '\n3. Got a Collision ID?'
              '\n4. Wanna have it all?!'
              '\n5. Back to the Collision Menu'
              '\n6. Exit the application'
              '\n7. Any other number to explore other datasets')

        selection = input()
        try:
            val = int(selection)
        except ValueError:
            print("\nThe value entered is not an integer value! Please try again.")
            self.check_collisions()

        # Collisions corresponding to a type of vehicle
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
                           "collision_insight.vehicle_collision WHERE vehicle_type_code iLIKE '%{}%'".
                           format(str(vehicle.lower()), ))
            records = cursor.fetchall()

            if len(records) == 0:
                print('Try with different value')
                self.check_collisions()

            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
            self.check_collisions()

        # Collisions due to a factor
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
                           "collision_insight.vehicle_collision WHERE contributing_factors iLIKE '%{}%'".
                           format(str(factor.lower()), ))

            records = cursor.fetchall()

            if len(records) == 0:
                print('Try with different value')
                self.check_collisions()

            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))

            self.check_collisions()

        # Got a Collision ID?
        elif val == 3:
            print("Please enter the Collision ID")
            collision_id = input()
            try:
                if (collision_id.isalnum() | collision_id.isalpha()) & (collision_id.isnumeric() != True):
                    raise ValueError
            except ValueError:
                print("\nThe entered ID is not valid! Please try again.")
                self.check_collisions()
            cursor.execute("SELECT collision_id, crash_date, crash_time, vehicle_type_code FROM "
                           "collision_insight.vehicle_collision WHERE collision_id = '{}'".
                           format(str(collision_id.lower()), ))
            records = cursor.fetchall()

            if len(records) == 0:
                print('Try with different value')
                self.check_collisions()

            print("Your search returned " + str(len(records)) + " records.\n")
            print("Collision ID" + " " + "Crash Date" + " " + "Crash Time" + " " + "Colliding Vehicles")
            # r->row
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]))
            self.check_collisions()

        # Wanna have it all?!'
        elif val == 4:
            print("Hold tight...")
            print("Wait for it... sit back and relax while we populate the data for you!")
            cursor.execute("SELECT * FROM collision_insight.vehicle_collision LIMIT 500")
            records = cursor.fetchall()
            if len(records) == 500:
                print("A large amount of data requested. Showing the first 500 valid records.\n")
            else:
                print("Your search returned " + str(len(records)) + " records.\n")
            # r->row
            for r in records:
                print(
                    str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]) + "\t" + str(
                        r[5]) + "\t" + str(r[6]) + "\t" + str(r[7]) + "\t" + str(r[8]) + "\t" + str(r[9]) + "\t" + str(
                        r[10]) + "\t" + str(r[11]) + "\t" + str(r[12]) + "\t" + str(r[13]) + "\t" + str(
                        r[14]) + "\t" + str(r[15]))

            self.check_collisions()

        # Back to the Collision Menu
        elif val == 5:
            self.check_collisions()

        elif val == 6:
            self.conn.close()
            exit()

        # else:
        #     print("The entered int value does not exist in the database.\nPlease enter again.")
        #     self.check_collisions()

    def check_repairs(self):
        cursor = self.conn.cursor()
        print('\nPlease select your Vehicle Repair shop query:'
              '\n1. Repair Shops in a particular zip code'
              '\n2. Know the owner of a repair shop? Search by Owner name.'
              '\n3. Got a Facility ID?'
              '\n4. Wanna have it all?!'
              '\n5. Back to the Menu'
              '\n6. Exit the application'
              '\n7. any other number to explore other datasets')
        selection = input()
        try:
            val = int(selection)
        except ValueError:
            print("\nThe value entered is not an int! Please try again.")
            self.check_repairs()

        # Repair Shops in a particular zip code
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

            if len(records) == 0:
                print('Try with different value')
                self.check_repairs()

            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]))
            self.check_repairs()

        # Know the owner of a repair shop? Search by Owner name.
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

            if len(records) == 0:
                print('Try with different name/options')
                self.check_repairs()

            print("Your search returned " + str(len(records)) + " records.\n")
            for r in records:
                print(str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]))
                # print("\n")
            self.check_repairs()

        # Got a Facility ID?
        elif val == 3:
            print("Please enter the Facility ID")
            facility_id = input()
            try:
                if (facility_id.isalnum() | facility_id.isalpha()) & (facility_id.isnumeric() != True):
                    raise ValueError
            except ValueError:
                print("\nThe value entered is not a valid Facility ID! Please try again.")
                self.check_repairs()
            cursor.execute("SELECT vr.facility_id, vr.facility_name, vr.facility_street, "
                           "vb.business_type FROM collision_insight.vehicle_repair_info vr, "
                           "collision_insight.vehicle_repair_business_type vb WHERE vr.facility_id = vb.facility_id "
                           "AND vr.facility_id = CAST('{}' AS INTEGER)".format(facility_id, ))
            records = cursor.fetchall()

            if len(records) == 0:
                print('Try with different name/options')
                self.check_repairs()

            print("Your search returned " + str(len(records)) + " records.\n")
            print("Facility ID" + " " + "Facility Name" + " " + "Street Address" + " " + "Business Type")
            for r in records:
                print(str(r[0]) + " " + str(r[1]) + " " + str(r[2]) + " " + str(r[3]))
            # print("\n")
            self.check_repairs()

        # Wanna have it all?!
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
                print(
                    str(r[0]) + "\t" + str(r[1]) + "\t" + str(r[2]) + "\t" + str(r[3]) + "\t" + str(r[4]) + "\t" + str(
                        r[5]) + "\t" + str(r[6]) + "\t" + str(r[7]) + "\t" + str(r[8]) + "\t" + str(r[9]) + "\t" + str(
                        r[11]))

            self.check_repairs()

        elif val == 5:
            self.check_repairs()

        elif val == 6:
            self.conn.close()
            exit()

    def hospital_query(self):
        cursor = self.conn.cursor()
        print('\nWhat you want to search in hospital data today?:'
              '\n1. Search Hospitals by name'
              '\n2. Search Hospitals by State/County/City/ZIP'
              '\n3. Search Hospitals by Type'
              '\n4. Search Hospital by Naics Code'
              '\n5. Exit the application'
              '\n6. Any other number to Explore other datasets')

        selection = input()

        try:
            user_input = int(selection)
        except ValueError:
            print('\nThe value entered is not an int! Please try again.')
            self.check_collisions()

        # Search Hospitals by name
        if user_input == 1:
            print('Please enter the name of the Hospital you want to search')
            hospital_name = input()

            try:
                if hospital_name.isnumeric():
                    raise ValueError
            except ValueError:
                print("\nYou must be remembering it wrong! Please try again.")
                self.hospital_query()

            query = 'SELECT name, address, telephone, website ' \
                    'FROM collision_insight.hospital_details ' \
                    'WHERE name iLIKE %(name)s OR alt_name iLIKE %(alt)s' \
                    'LIMIT 100'

            cursor.execute(query, {'name': '%' + hospital_name + '%', 'alt': '%' + hospital_name + '%'})

            records = cursor.fetchall()
            print('Your search returned ' + str(len(records)) + ' records.\n')

            if len(records) == 0:
                print('Try with different name/options')
                self.hospital_query()

            else:
                print('The following hospitals matched your input: ')
            # print (tabulate(records, headers=["Liquor Shop Name", "Liquor Shop Address", "Collision BOROUGH"]))
            for rows in records:
                print('\n\n-----------HERE ARE THE DETAILS ABOUT ' + str(rows[0]) + '----------- '
                                                                                    '\n Address: ' + str(rows[1]) +
                      '\n Telephone: ' + str(rows[2]) +
                      '\n Website: ' + str(rows[3]))
            self.hospital_query()

        # Search Hospitals by State/County/City/ZIP
        elif user_input == 2:
            print('Please enter how you want to search for the Hospitals'
                  '\n 1. All the Hospitals in a State by State code (Example - NY for New York)'
                  '\n 2. City Name'
                  '\n 3. County Name'
                  '\n 4. ZIP Code'
                  '\n 5. Go back to previous menu for Hospital'
                  '\n 6. Exit the application')
            location_input = input()
            check = location_input.isdigit()
            if check:
                # State
                if int(location_input) == 1:
                    print('Please enter 2 Letter State Code: ')
                    state = input()
                    if state.isdigit() | state.isalnum():
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Hospital menu ')
                        self.hospital_query()
                    else:
                        state = state.upper()
                        # Searching in XML using XPATH
                        all_zipcode = self.tree.xpath("/root/item[STATE/text()='" + state + "']/ZIP/text()")
                        for zip_search in all_zipcode:
                            query = 'SELECT name, address, telephone, website, zipcode ' \
                                    'FROM collision_insight.hospital_details ' \
                                    'WHERE zipcode = %(zip)s' \
                                    'LIMIT 100'
                            cursor.execute(query, {'zip': zip_search})
                            records = cursor.fetchall()

                            print(tabulate(records, headers=["Hospital Name", "Hospital Address", "Hospital Telephone",
                                                             "Hospital Website", "Hospital ZipCode"]))
                    self.hospital_query()

                # City
                elif int(location_input) == 2:
                    print('Please enter City: ')
                    city = input()
                    if city.isdigit() | city.isalnum():
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Hospital menu ')
                        self.hospital_query()
                    else:
                        city = city.upper()
                        all_zipcode = self.tree.xpath("/root/item[CITY/text()='" + city + "']/ZIP/text()")
                        for zip_search in all_zipcode:
                            query = 'SELECT name, address, telephone, website, zipcode ' \
                                    'FROM collision_insight.hospital_details ' \
                                    'WHERE zipcode = %(zip)s'
                            cursor.execute(query, {'zip': zip_search})
                            records = cursor.fetchall()

                            print(tabulate(records, headers=["Hospital Name", "Hospital Address", "Hospital Telephone",
                                                             "Hospital Website", "Hospital ZipCode"]))
                    self.hospital_query()

                # County
                elif int(location_input) == 3:
                    print('Please enter County: ')
                    county = input()
                    if county.isdigit():
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Hospital menu ')
                        self.hospital_query()
                    else:
                        county = county.upper()
                        all_zipcode = self.tree.xpath("/root/item[COUNTY/text()='" + county + "']/ZIP/text()")
                        for zip_search in all_zipcode:
                            query = 'SELECT name, address, telephone, website, zipcode ' \
                                    'FROM collision_insight.hospital_details ' \
                                    'WHERE zipcode = %(zip)s'
                            cursor.execute(query, {'zip': zip_search})
                            records = cursor.fetchall()

                            print(tabulate(records, headers=["Hospital Name", "Hospital Address", "Hospital Telephone",
                                                             "Hospital Website", "Hospital ZipCode"]))
                    self.hospital_query()

                # ZIP
                elif int(location_input) == 4:
                    print('Please 5 digit ZIP: ')
                    zip_code = input()
                    if zip_code.isdigit() and len(zip_code) == 5:
                        query = 'SELECT name, address, telephone, website ' \
                                'FROM collision_insight.hospital_details ' \
                                'WHERE zipcode = %(zip_code)s'

                        cursor.execute(query, {'zip_code': zip_code})
                        records = cursor.fetchall()
                        if len(records) == 0:
                            print('Try with a different option')
                            self.hospital_query()
                        else:
                            print('The following are hospital(s) are in the ZIPCODE you entered: ')

                        print(tabulate(records, headers=["Hospital Name", "Hospital Address", "Hospital Telephone",
                                                         "Hospital Website", "Hospital ZipCode"]))

                    else:
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Hospital menu ')

                    self.hospital_query()

                # Hospital MENU
                elif int(location_input) == 5:
                    self.hospital_query()

                # exit
                elif int(location_input) == 6:
                    self.conn.close()
                    exit()

            else:
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Hospital menu ')
                self.hospital_query()

        # Search Hospitals by Type
        elif user_input == 3:
            print("There are following types of hospitals available - "
                  "\n1. GENERAL ACUTE CARE"
                  "\n2. PSYCHIATRIC"
                  "\n3. CHILDREN"
                  "\n4. LONG TERM CARE CRITICAL ACCESS"
                  "\n5. REHABILITATION"
                  "\n6. MILITARY"
                  "\n7. WOMEN"
                  "\n8. SPECIAL"
                  "\n9. CHRONIC DISEASE")
            print("Type the number you want to search the hospitals for - ")
            dictionary = {
                1: "GENERAL ACUTE CARE",
                2: "PSYCHIATRIC",
                3: "CHILDREN",
                4: "LONG TERM CARE CRITICAL ACCESS",
                5: "REHABILITATION",
                6: "MILITARY",
                7: "WOMEN",
                8: "SPECIAL",
                9: "CHRONIC DISEASE"
            }
            hospital_type = input()
            if hospital_type.isdigit() and 1 <= int(hospital_type) <= 9:
                hospital_type = dictionary.get(int(hospital_type))
                query = 'SELECT id from collision_insight.hospital_type ' \
                        'where type = %(type)s'
                cursor.execute(query, {'type': hospital_type})
                hospital_ids = cursor.fetchall()

                print('The following are hospital(s) are in the type you selected: ')

                for hospital in hospital_ids:
                    to_search = int(str(hospital[0]))
                    query = 'SELECT name, address, telephone, website ' \
                            'FROM collision_insight.hospital_details ' \
                            'WHERE id = %(ID)s'
                    cursor.execute(query, {'ID': to_search})
                    hospitals = cursor.fetchall()
                    print(tabulate(hospitals, headers=["Hospital Name", "Hospital Address", "Hospital Telephone",
                                                       "Hospital Website"]))

                self.hospital_query()

            else:
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Hospital menu ')
                self.hospital_query()

        # Search Hospital by Naics Code
        elif user_input == 4:
            print("There are following NAICS code for the hospitals - "
                  "\n1. 622110"
                  "\n2. 622210"
                  "\n3. 622310")
            print("Type the number you want to search the hospitals for - ")
            dictionary = {
                1: "622110",
                2: "622210",
                3: "622310",
            }
            hospital_naics_code = input()
            if hospital_naics_code.isdigit() and 1 <= int(hospital_naics_code) <= 3:
                hospital_naics_code = dictionary.get(int(hospital_naics_code))
                query = 'SELECT id from collision_insight.hospital_naics ' \
                        'where naics_code = %(type)s'
                cursor.execute(query, {'type': hospital_naics_code})
                hospital_ids = cursor.fetchall()

                print('The following are hospital(s) are in the NAICS Code you selected: ')

                for hospital in hospital_ids:
                    to_search = int(str(hospital[0]))
                    query = 'SELECT name, address, telephone, website, naics_desc ' \
                            'FROM collision_insight.hospital_details as details, ' \
                            'collision_insight.hospital_naics as naics ' \
                            'WHERE details.id = %(ID)s ' \
                            'AND details.id = naics.id' \
                            'LIMIT 100'
                    cursor.execute(query, {'ID': to_search})
                    hospitals = cursor.fetchall()

                    print(tabulate(hospitals, headers=["Hospital Name", "Hospital Address", "Hospital Telephone",
                                                       "Hospital Website", "Naics Type Description"]))

                self.hospital_query()

            else:
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Hospital menu ')
                self.hospital_query()

        # Exit the application
        elif user_input == 5:
            self.conn.close()
            exit()

    def liquor_query(self):
        cursor = self.conn.cursor()

        print('\nWhat you want to search in Liquor data today?:'
              '\n1. Search Liquor Shops by name'
              '\n2. Search Liquor Shops by State/County/City/ZIP'
              '\n3. Search a Liquor Shop and how they are during their business'
              '\n4. Exit the application'
              '\n5. Any number to Explore other datasets')

        selection = input()

        try:
            user_input = int(selection)
        except ValueError:
            print('\nThe value entered is not an integer! Please try again.')
            self.liquor_query()

        # Shop name
        if user_input == 1:
            print('Please enter the name of the Liquor shop you want to search')
            liquor_shop = input()

            try:
                if liquor_shop.isnumeric():
                    raise ValueError
            except ValueError:
                print("\nYou must be remembering it wrong! Please try again.")
                self.liquor_query()

            query = 'SELECT premise_name, premise_address, license_expiration_date, days_hours_of_operation ' \
                    'FROM collision_insight.liquor_shop_info ' \
                    'WHERE premise_name iLIKE %(name)s' \
                    'LIMIT 100'

            cursor.execute(query, {'name': '%' + liquor_shop + '%'})
            records = cursor.fetchall()
            print('Your search returned ' + str(len(records)) + ' records.\n')

            if len(records) == 0:
                print('Try with different name/options')
                self.liquor_query()
            else:
                print('The following Liquor shops matched your input: ')

            print(tabulate(records, headers=["Liquor Shop Name", "Liquor Address", "Liquor Expiration Date",
                                             "Days and Hours of Operation"]))
            self.liquor_query()

        # Shop name by Location
        elif user_input == 2:
            print('Please enter how you want to search for the Liquor Shop'
                  '\n 1. State code (Example - NY for New York)'
                  '\n 2. City Name'
                  '\n 3. County Name'
                  '\n 4. ZIP Code'
                  '\n 5. Go back to previous menu for Liquor'
                  '\n 6. Exit the application')

            location_input = input()
            check = location_input.isdigit()
            if check:
                # State
                if int(location_input) == 1:
                    print('Please enter 2 Letter State Code: ')
                    state = input()
                    if state.isdigit():
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Liquor menu ')
                        self.liquor_query()
                    else:
                        state = state.upper()

                        all_zipcode = self.tree.xpath("/root/item[STATE/text()='" + state + "']/ZIP/text()")

                        for zip_search in all_zipcode:
                            query = 'SELECT premise_name, premise_address, zipcode, certificate_number, ' \
                                    'method_of_operation, ' \
                                    'days_hours_of_operation ' \
                                    'FROM collision_insight.liquor_shop_info ' \
                                    'WHERE zipcode = %(zip)s'
                            cursor.execute(query, {'zip': zip_search})
                            records = cursor.fetchall()

                            print(tabulate(records, headers=["Liquor Shop Name", "Liquor Address", "Zip Code",
                                                             "Certificate number",
                                                             "Method of Operation",
                                                             "Days and Hours of Operation"]))
                    self.liquor_query()

                # City
                elif int(location_input) == 2:
                    print('Please enter City: ')
                    city = input()
                    if city.isdigit():
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Liquor menu ')
                        self.liquor_query()
                    else:
                        city = city.upper()
                        all_zipcode = self.tree.xpath("/root/item[CITY/text()='" + city + "']/ZIP/text()")
                        for zip_search in all_zipcode:
                            query = 'SELECT premise_name, premise_address, zipcode, certificate_number, ' \
                                    'method_of_operation, ' \
                                    'days_hours_of_operation ' \
                                    'FROM collision_insight.liquor_shop_info ' \
                                    'WHERE zipcode = %(zip)s'
                            cursor.execute(query, {'zip': zip_search})
                            records = cursor.fetchall()

                            print(tabulate(records, headers=["Liquor Shop Name", "Liquor Address", "Zip Code",
                                                             "Certificate number",
                                                             "Method of Operation",
                                                             "Days and Hours of Operation"]))
                    self.liquor_query()

                # County
                elif int(location_input) == 3:
                    print('Please enter County: ')
                    county = input()
                    if county.isdigit():
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Liquor menu ')
                        self.liquor_query()
                    else:
                        county = county.upper()
                        all_zipcode = self.tree.xpath("/root/item[COUNTY/text()='" + county + "']/ZIP/text()")
                        for zip_search in all_zipcode:
                            query = 'SELECT premise_name, premise_address, zipcode, certificate_number, ' \
                                    'method_of_operation, ' \
                                    'days_hours_of_operation ' \
                                    'FROM collision_insight.liquor_shop_info ' \
                                    'WHERE zipcode = %(zip)s'
                            cursor.execute(query, {'zip': zip_search})
                            records = cursor.fetchall()

                            print(tabulate(records, headers=["Liquor Shop Name", "Liquor Address", "Zip Code",
                                                             "Certificate number",
                                                             "Method of Operation",
                                                             "Days and Hours of Operation"]))
                    self.liquor_query()

                # ZIP
                elif int(location_input) == 4:
                    print('Please the ZIP Code: ')
                    zip_code = input()
                    if zip_code.isdigit() and len(zip_code) == 5:

                        query = 'SELECT premise_name, premise_address, zipcode, certificate_number, ' \
                                'method_of_operation, ' \
                                'days_hours_of_operation ' \
                                'FROM collision_insight.liquor_shop_info ' \
                                'WHERE zipcode = %(zip)s'

                        cursor.execute(query, {'zip': zip_code})
                        records = cursor.fetchall()

                        if len(records) == 0:
                            print('Try with a different option')
                            self.liquor_query()
                        else:
                            print('The following are liquor shop(s) are in the ZIPCODE you entered: ')

                        print(tabulate(records, headers=["Liquor Shop Name", "Liquor Address", "Zip Code",
                                                         "Certificate number",
                                                         "Method of Operation",
                                                         "Days and Hours of Operation"]))

                    else:
                        print('\nYou did not select a valid input. '
                              '\nRedirecting back to the Liquor menu ')

                    self.liquor_query()

                # Liquor MENU
                elif int(location_input) == 5:
                    self.liquor_query()

                # exit
                elif int(location_input) == 6:
                    self.conn.close()
                    exit()

            else:
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Liquor menu ')
                self.liquor_query()

        # DBA
        elif user_input == 3:
            print('Please enter the related business name')
            doing_business_as = input()

            query = 'SELECT premise_name, premise_address, dba, days_hours_of_operation ' \
                    'FROM collision_insight.liquor_shop_info ' \
                    'WHERE dba iLIKE %(name)s'

            cursor.execute(query, {'name': '%' + doing_business_as + '%'})

            records = cursor.fetchall()

            print('Your search returned ' + str(len(records)) + ' records.\n')

            if len(records) == 0:
                print('Try with different name/options')
                self.liquor_query()
            else:
                print('The following Liquor shops matched your input: ')

            print(tabulate(records, headers=["Liquor Shop Name", "Liquor Address",
                                             "Doing Business As",
                                             "Days and Hours of Operation"]))

            self.liquor_query()

        elif user_input == 4:
            self.conn.close()
            exit()

    def search_all(self):
        cursor = self.conn.cursor()

        print('\nThis option will show only if they are present in Liquor and Collision:'
              '\n1. Search by Zip'
              '\n2. Search by State'
              '\n3. Search by County'
              '\n4. Search by City'
              '\n5. To exit the Application'
              '\n6. Any number to Explore other datasets')

        selection = input()
        try:
            user_input = int(selection)
        except ValueError:
            print('\nThe value entered is not an integer! Please try again.')
            self.search_all()

        # Search by ZIP
        if user_input == 1:
            print('Please enter ZIP code: ')
            zip_code = input()
            if zip_code.isdigit() and len(zip_code) == 5:

                query = 'SELECT liquor.premise_name, liquor.premise_address, ' \
                        'collision.BORO ' \
                        'FROM collision_insight.liquor_shop_info as liquor, ' \
                        'collision_insight.vehicle_collision as collision ' \
                        'WHERE liquor.zipcode = %(zip)s ' \
                        'AND liquor.zipcode = collision.zipcode ' \
                        'LIMIT 20'

                cursor.execute(query, {'zip': zip_code})
                records = cursor.fetchall()

                if len(records) == 0:
                    print('Try with a different option')
                    self.search_all()
                else:
                    print('The following are results for the ZIPCODE you entered: ')

                print(tabulate(records, headers=["Liquor Shop Name", "Liquor Shop Address", "Collision BOROUGH"]))

            else:
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Search with All menu ')
            self.search_all()

        # Search by State
        if user_input == 2:
            print('Please enter 2 Letter State Code: ')

            state = input()

            if state.isdigit():
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to Search for all menu ')

            else:
                state = state.upper()
                all_zipcode = self.tree.xpath("/root/item[STATE/text()='" + state + "']/ZIP/text()")

                for zip_search in all_zipcode:
                    query = 'SELECT liquor.premise_name, liquor.premise_address, ' \
                            'collision.BORO ' \
                            'FROM collision_insight.liquor_shop_info as liquor, ' \
                            'collision_insight.vehicle_collision as collision ' \
                            'WHERE liquor.zipcode = %(zip)s ' \
                            'AND liquor.zipcode = collision.zipcode ' \
                            'LIMIT 20'

                    cursor.execute(query, {'zip': zip_search})
                    records = cursor.fetchall()

                    if len(records) == 0:
                        print('Try with a different option')
                        self.search_all()
                    else:
                        print('The following are results for the STATE you entered: ')
                    print(tabulate(records, headers=["Liquor Shop Name", "Liquor Shop Address", "Collision BOROUGH"]))
            self.search_all()

        # Search by County
        if user_input == 3:
            print('Please enter County: ')
            county = input()
            if county.isdigit():
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Search for all menu ')
            else:
                county = county.upper()
                all_zipcode = self.tree.xpath("/root/item[COUNTY/text()='" + county + "']/ZIP/text()")
                for zip_search in all_zipcode:
                    query = 'SELECT liquor.premise_name, liquor.premise_address, ' \
                            'collision.BORO ' \
                            'FROM collision_insight.liquor_shop_info as liquor, ' \
                            'collision_insight.vehicle_collision as collision ' \
                            'WHERE liquor.zipcode = %(zip)s ' \
                            'AND liquor.zipcode = collision.zipcode ' \
                            'LIMIT 20'

                    cursor.execute(query, {'zip': zip_search})
                    records = cursor.fetchall()

                    if len(records) == 0:
                        print('Try with a different option')
                        self.search_all()
                    else:
                        print('The following are results for the COUNTY you entered: ')
                    print(tabulate(records, headers=["Liquor Shop Name", "Liquor Shop Address", "Collision BOROUGH"]))
            self.search_all()

        # Search by City
        if user_input == 4:
            print('Please enter City: ')
            city = input()
            if city.isdigit():
                print('\nYou did not select a valid input. '
                      '\nRedirecting back to the Search for All menu ')
            else:
                city = city.upper()
                all_zipcode = self.tree.xpath("/root/item[CITY/text()='" + city + "']/ZIP/text()")
                for zip_search in all_zipcode:
                    query = 'SELECT liquor.premise_name, liquor.premise_address, ' \
                            'collision.BORO ' \
                            'FROM collision_insight.liquor_shop_info as liquor, ' \
                            'collision_insight.vehicle_collision as collision ' \
                            'WHERE liquor.zipcode = %(zip)s ' \
                            'AND liquor.zipcode = collision.zipcode ' \
                            'LIMIT 20'

                    cursor.execute(query, {'zip': zip_search})
                    records = cursor.fetchall()

                    if len(records) == 0:
                        print('Try with a different option')
                        self.search_all()
                    else:
                        print('The following are results for the CITY you entered: ')
                    print(tabulate(records, headers=["Liquor Shop Name", "Liquor Shop Address", "Collision BOROUGH"]))
            self.search_all()

        # Exit the Application
        if user_input == 5:
            self.conn.close()
            exit()
