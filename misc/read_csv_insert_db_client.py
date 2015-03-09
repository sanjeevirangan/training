import argparse
import sys
import csv
import time
import requests


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="CSV file to read")
    #parser.add_argument("--action", "-a", help="Action to call the web API", required=True)
    args = parser.parse_args()
    csv_file = args.file
    career_payload = {}
    product_payload = {}
    career_product_payload = {}
    weight_career_product_str = ""
    career_id_str = ""
    product_id_str = ""

    print("\nReading file {0}\n".format(csv_file))
    print"+++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    try:
        read_start = time.time()
        with open(csv_file, 'r') as file_handle:
            dict_reader = csv.DictReader(file_handle)
            for row in dict_reader:
                weight_career_product_str += row['weight'] + ";" + row['career_id'] + ";" + row['product_id'] + ","
                #career_product.append((row['weight'], row['career_id'], row['product_id']))
                if row['product_id'] not in product_id_str:
                    product_id_str += row['product_id'] + ","
                    #product_id.append(row['product_id'])
                if row['career_id'] not in career_id_str:
                    career_id_str += row['career_id'] + ","
                    #career_id.append(row['career_id'])
        read_end = time.time()
    except Exception, ex:
        print("\nError while reading file: {0}".format(ex.message))
        sys.exit(1)
    else:
        print("\nCompleted reading {0} lines from file {1}\n".format(dict_reader.line_num, csv_file))
        print ("Time taken to read the file: {0} seconds\n".format(str(read_end - read_start)))

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    #headers = {'content-type': 'application/text'}

    career_url = 'http://localhost/cgi-bin/api/insert_career_api.py'
    career_payload['action'] = 'career'
    career_payload['career_id'] = career_id_str

    #print career_url
    #print career_payload
    career_response = requests.post(career_url, data=career_payload, headers=headers)
    print career_response.text

    product_url = 'http://localhost/cgi-bin/api/insert_product_api.py'
    product_payload['action'] = 'product'
    product_payload['product_id'] = product_id_str
    #print product_url
    #print product_payload
    product_response = requests.post(product_url, data=product_payload, headers=headers)
    print product_response.text

    career_product_url = 'http://localhost/cgi-bin/api/insert_careeer_product_api.py'
    career_product_payload['action'] = 'career_product'
    career_product_payload['weight_career_product'] = weight_career_product_str[:-1]
    #print career_product_url
    #print career_product_payload
    career_product_response = requests.post(career_product_url, data=career_product_payload, headers=headers)
    print career_product_response.text
    print"\n+++++++++++++++++++++++++++++++++++++++++++++++++++\n"


if __name__ == '__main__':
    main()
