import argparse
import sys
import MySQLdb
import csv


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
    product_career = []  # list of tuples (weight, career_id, product_id)

    # start reading the file
    print("\nReading file {0}\n".format(csv_file))
    print"+++++++++++++++++++++++++++++++++++++++++++++++++++\n"
    with open(csv_file, 'r') as file_handle:
        dict_reader = csv.DictReader(file_handle)
        for row in dict_reader:
            product_career.append((row['weight'], row['career_id'], row['product_id']))
            if row['product_id'] not in product_id:
                product_id.append(row['product_id'])
            if row['career_id'] not in career_id:
                career_id.append(row['career_id'])

    print("\nCompleted reading file {0}\n".format(csv_file))

    # # Get unique product, career ids
    # print("\nprocessing data....\n")
    # unique_product_id = list(set(product_id))
    # unique_career_id = list(set(career_id))

    # Create database entries for unique ids if not already exists
    print("\nInserting data to career table\n")
    sql_query_career = "insert ignore into career (id) values (%s)"
    for item in career_id:
        cursor.execute(sql_query_career, (item,))

    print("\nInserting data to product table\n")
    sql_query_product = "insert ignore into product (id) values (%s)"
    for item in product_id:
        cursor.execute(sql_query_product, (item,))

    print("\nInserting data to career_product table\n")
    sql_query_career_product = "insert ignore into career_product (weight, career_id, product_id) values (%s, %s, %s)"
    for value in product_career:
        cursor.execute(sql_query_career_product, (value[0], value[1], value[2]))

    print("\nCompleted inserting data\n")
    print("\nCommitting database\n")
    db.commit()
    print("\nClosing database connection\n")
    db.close()
    print"+++++++++++++++++++++++++++++++++++++++++++++++++++\n"

main()
