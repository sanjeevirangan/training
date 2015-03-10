import argparse
import sys
import csv
import time
import requests
import json


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="CSV file to read")
    args = parser.parse_args()
    csv_file = args.file
    product_id = []
    career_id = []
    career_product = []  # list of tuples (weight, career_id, product_id)

    # start reading the file
    print("\nReading file {0}\n".format(csv_file))
    print"+++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    try:
        read_start = time.time()
        with open(csv_file, 'r') as file_handle:
            dict_reader = csv.DictReader(file_handle)
            for row in dict_reader:
                career_product.append((row['weight'], row['career_id'], row['product_id']))
                if row['product_id'] not in product_id:
                    product_id.append(row['product_id'])
                if row['career_id'] not in career_id:
                    career_id.append(row['career_id'])
        read_end = time.time()
    except Exception, ex:
        print("\nError while reading file: {0}".format(ex.message))
        sys.exit(1)
    else:
        print("\nCompleted reading {0} lines from file {1}\n".format(dict_reader.line_num, csv_file))
        print ("Time taken to read the file: {0} seconds\n".format(str(read_end - read_start)))

    # Construct requests and call APIs for each unique records
    headers = {'content-type': 'application/x-www-form-urlencoded'}

    # Career table
    career_url = 'http://localhost/cgi-bin/api/insert_career_api.py'
    career_payload = {'action': 'career'}
    print("\nInserting data to career table\n")
    career_start = time.time()
    career_pass_counter = 0
    career_fail_counter = 0
    career_error = []
    for item in career_id:
        try:
            career_payload['career_id'] = item
            career_response = requests.post(career_url, data=career_payload, headers=headers)
            try:
                career_response_dict = json.loads(career_response.text)
            except:
                career_fail_counter += 1
                career_error.append(career_response.reason)
                continue
            if career_response.status_code == 200:
                career_pass_counter += 1
            else:
                career_fail_counter += 1
                if career_response_dict['Is_Error'] == "True":
                    career_error.append(career_response_dict['Error'])
        except Exception, ex:
            print ("\nError while inserting data to career table:\n{0}".format(ex.message))
    career_end = time.time()
    print("Successfully ingested {0} items to 'career' table in {1} seconds\
        \n".format(career_pass_counter, str(career_end - career_start)))
    if career_fail_counter >= 1:
        print("{0} ingestion failed to 'career' table  with errors: \
              \n\n{1}".format(career_fail_counter, str(career_error)))

    # Product table
    print("\nInserting data to product table\n")
    product_url = 'http://localhost/cgi-bin/api/insert_product_api.py'
    product_payload = {'action': 'product'}
    product_start = time.time()
    product_pass_counter = 0
    product_fail_counter = 0
    product_error = []
    for item in product_id:
        try:
            product_payload['product_id'] = item
            product_response = requests.post(product_url, data=product_payload, headers=headers)
            try:
                product_response_dict = json.loads(product_response.text)
            except:
                product_fail_counter += 1
                product_error.append(product_response.reason)
                continue
            if product_response.status_code == 200:
                product_pass_counter += 1
            else:
                product_fail_counter += 1
                if product_response_dict['Is_Error'] == "True":
                    product_error.append(product_response_dict['Error'])
        except Exception, ex:
            print ("\nError while inserting data to product table:\n{0}".format(ex.message))
    product_end = time.time()
    print("Successfully ingested {0} items to 'product' table in {1} seconds\
        \n".format(product_pass_counter, str(product_end - product_start)))
    if product_fail_counter >= 1:
        print("{0} ingestion failed to 'product' table  with errors: \
              \n\n{1}".format(product_fail_counter, str(product_error)))

    #  career_product table
    career_product_url = 'http://localhost/cgi-bin/api/insert_career_product_api.py'
    career_product_payload = {'action': "career_product"}
    print("\nInserting data to career_product table\n")
    career_product_start = time.time()
    career_product_pass_counter = 0
    career_product_fail_counter = 0
    career_product_error = []
    for value in career_product:
        try:
            career_product_payload['weight'] = value[0]
            career_product_payload['career_id'] = value[1]
            career_product_payload['product_id'] = value[2]
            career_product_response = requests.post(career_product_url, data=career_product_payload, headers=headers)
            try:
                career_product_response_dict = json.loads(career_product_response.text)
            except:
                career_product_fail_counter += 1
                career_product_error.append(career_product_response.reason)
                continue
            if career_product_response.status_code == 200:
                career_product_pass_counter += 1
            else:
                career_product_fail_counter += 1
                if career_product_response_dict['Is_Error'] == "True":
                    career_product_error.append(career_product_response_dict['Error'])
        except Exception, ex:
            print ("\nError while inserting data to career_product table:\n{0}".format(ex.message))
    career_product_end = time.time()
    print("Successfully ingested {0} items to 'career_product' table in {1} seconds\
        \n".format(career_product_pass_counter, str(career_product_end - career_product_start)))
    if career_product_fail_counter >= 1:
        print("{0} ingestion failed to 'career_product' table  with errors: \
              \n\n{1}".format(career_product_fail_counter, str(career_product_error)))

    # Done with all 3 tables
    print("\n\nTotal time taken: {0} seconds\n".format(str(time.time() - read_start)))
    print"\n+++++++++++++++++++++++++++++++++++++++++++++++++++\n"


if __name__ == '__main__':
    main()