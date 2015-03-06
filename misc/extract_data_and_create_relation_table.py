import argparse
import sys
import MySQLdb
import csv
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="CSV file to read")
    args = parser.parse_args()
    csv_file = args.file
    try:
        db = MySQLdb.connect("localhost", "root", "admin", "product_relation", charset='utf8')
    except Exception, ex:
        print("Fatal Error: Unable to connect to database.\n{0}".format(ex.message))
        sys.exit(1)

    cursor = db.cursor()
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
    else:
        print("\nCompleted reading {0} lines from file {1}\n".format(dict_reader.line_num, csv_file))
        print ("Time taken to read the file: {0} seconds\n".format(str(read_end - read_start)))

    # # Get unique product, career ids
    # print("\nprocessing data....\n")
    # unique_product_id = list(set(product_id))
    # unique_career_id = list(set(career_id))

    # Create database entries for unique ids if not already exists
    print("\nInserting data to career table\n")
    sql_query_career = "insert ignore into career (id) values (%s)"
    career_start = time.time()
    for item in career_id:
        cursor.execute(sql_query_career, (item,))
    career_end = time.time()
    print("Completed inserting {0} items to career table in {1} seconds\
            \n".format(len(career_id), str(career_end-career_start)))

    print("\nInserting data to product table\n")
    sql_query_product = "insert ignore into product (id) values (%s)"
    product_start = time.time()
    for item in product_id:
        cursor.execute(sql_query_product, (item,))
    product_end = time.time()
    print("Completed inserting {0} items to product table in {1} seconds\
            \n".format(len(product_id), str(product_end - product_start)))

    print("\nInserting data to career_product table\n")
    sql_query_career_product = "insert ignore into career_product (weight, career_id, product_id) values (%s, %s, %s)"
    career_product_start = time.time()
    for value in career_product:
        cursor.execute(sql_query_career_product, (value[0], value[1], value[2]))
    career_product_end = time.time()
    print("Completed inserting {0} items to product table in {1} seconds\
            \n".format(len(career_product), str(career_product_end - career_product_start)))

    print("\nCompleted inserting data to database in {0} seconds\n".format(str(career_product_end - career_start)))
    print("\nCommitting database\n")
    db.commit()
    print("\nClosing database connection\n")
    db.close()
    db_closed = time.time()
    print("\nCompleted task in {0} seconds\n".format(str(db_closed - read_start)))
    print"\n+++++++++++++++++++++++++++++++++++++++++++++++++++\n"

main()