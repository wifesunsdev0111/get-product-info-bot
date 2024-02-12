import mysql.connector

# Connection details
host = ''
user = ''
password = ''
database = ''

# Establish connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)


TABLE_NAME = "product_table"

def create_table():
    # Create a cursor object
    cursor = connection.cursor()
    # SQL query to create a table
    create_table_query = f'''
    CREATE TABLE {TABLE_NAME} (
        sku VARCHAR(255),
        name VARCHAR(255),
        short_description TEXT,
        description TEXT,
        stock VARCHAR(255),
        weight VARCHAR(255),
        length VARCHAR(255),
        width VARCHAR(255),
        height VARCHAR(255),
        sale_price VARCHAR(255),
        regular_price VARCHAR(255),
        categories VARCHAR(255),
        images TEXT,
        product_url TEXT,
        attribute_1_name TEXT, attribute_1_value TEXT, attribute_1_visibility TEXT, attribute_1_global TEXT,
        attribute_2_name TEXT, attribute_2_value TEXT, attribute_2_visibility TEXT, attribute_2_global TEXT,
        attribute_3_name TEXT, attribute_3_value TEXT, attribute_3_visibility TEXT, attribute_3_global TEXT,
        attribute_4_name TEXT, attribute_4_value TEXT, attribute_4_visibility TEXT, attribute_4_global TEXT,
        attribute_5_name TEXT, attribute_5_value TEXT, attribute_5_visibility TEXT, attribute_5_global TEXT,
        attribute_6_name TEXT, attribute_6_value TEXT, attribute_6_visibility TEXT, attribute_6_global TEXT,
        attribute_7_name TEXT, attribute_7_value TEXT, attribute_7_visibility TEXT, attribute_7_global TEXT,
        attribute_8_name TEXT, attribute_8_value TEXT, attribute_8_visibility TEXT, attribute_8_global TEXT,
        attribute_9_name TEXT, attribute_9_value TEXT, attribute_9_visibility TEXT, attribute_9_global TEXT,
        attribute_10_name TEXT, attribute_10_value TEXT, attribute_10_visibility TEXT, attribute_10_global TEXT,
        attribute_11_name TEXT, attribute_11_value TEXT, attribute_11_visibility TEXT, attribute_11_global TEXT,
        attribute_12_name TEXT, attribute_12_value TEXT, attribute_12_visibility TEXT, attribute_12_global TEXT,
        attribute_13_name TEXT, attribute_13_value TEXT, attribute_13_visibility TEXT, attribute_13_global TEXT,
        attribute_14_name TEXT, attribute_14_value TEXT, attribute_14_visibility TEXT, attribute_14_global TEXT,
        attribute_15_name TEXT, attribute_15_value TEXT, attribute_15_visibility TEXT, attribute_15_global TEXT,
        attribute_16_name TEXT, attribute_16_value TEXT, attribute_16_visibility TEXT, attribute_16_global TEXT,
        attribute_17_name TEXT, attribute_17_value TEXT, attribute_17_visibility TEXT, attribute_17_global TEXT,
        attribute_18_name TEXT, attribute_18_value TEXT, attribute_18_visibility TEXT, attribute_18_global TEXT,
        attribute_19_name TEXT, attribute_19_value TEXT, attribute_19_visibility TEXT, attribute_19_global TEXT,
        attribute_20_name TEXT, attribute_20_value TEXT, attribute_20_visibility TEXT, attribute_20_global TEXT,
        attribute_21_name TEXT, attribute_21_value TEXT, attribute_21_visibility TEXT, attribute_21_global TEXT,
        attribute_22_name TEXT, attribute_22_value TEXT, attribute_22_visibility TEXT, attribute_22_global TEXT,
        attribute_23_name TEXT, attribute_23_value TEXT, attribute_23_visibility TEXT, attribute_23_global TEXT,
        attribute_24_name TEXT, attribute_24_value TEXT, attribute_24_visibility TEXT, attribute_24_global TEXT
    )
    '''

    # Execute the query to create the table
    cursor.execute(create_table_query)

    # Commit the changes
    connection.commit()

    # Close the cursor and the connection
    # cursor.close()
    # connection.close()
try:
    cursor = connection.cursor()
    query = f"DROP TABLE {TABLE_NAME}"
    cursor.execute(query)
    # print(f"The table '{TABLE_NAME}' has been deleted successfully.")
except:
    pass

try:
    create_table()
except:
    pass

# Create a cursor object
# cursor = connection.cursor()

# SQL query to insert data into the table
insert_query = f'''
INSERT INTO {TABLE_NAME} (
        sku, name, short_description, description, stock, weight, length, width, height, sale_price, regular_price, categories, images, product_url,
        attribute_1_name, attribute_1_value, attribute_1_visibility, attribute_1_global,
        attribute_2_name, attribute_2_value, attribute_2_visibility, attribute_2_global,
        attribute_3_name, attribute_3_value, attribute_3_visibility, attribute_3_global,
        attribute_4_name, attribute_4_value, attribute_4_visibility, attribute_4_global,
        attribute_5_name, attribute_5_value, attribute_5_visibility, attribute_5_global,
        attribute_6_name, attribute_6_value, attribute_6_visibility, attribute_6_global,
        attribute_7_name, attribute_7_value, attribute_7_visibility, attribute_7_global,
        attribute_8_name, attribute_8_value, attribute_8_visibility, attribute_8_global,
        attribute_9_name, attribute_9_value, attribute_9_visibility, attribute_9_global,
        attribute_10_name, attribute_10_value, attribute_10_visibility, attribute_10_global,
        attribute_11_name, attribute_11_value, attribute_11_visibility, attribute_11_global,
        attribute_12_name, attribute_12_value, attribute_12_visibility, attribute_12_global,
        attribute_13_name, attribute_13_value, attribute_13_visibility, attribute_13_global,
        attribute_14_name, attribute_14_value, attribute_14_visibility, attribute_14_global,
        attribute_15_name, attribute_15_value, attribute_15_visibility, attribute_15_global,
        attribute_16_name, attribute_16_value, attribute_16_visibility, attribute_16_global,
        attribute_17_name, attribute_17_value, attribute_17_visibility, attribute_17_global,
        attribute_18_name, attribute_18_value, attribute_18_visibility, attribute_18_global,
        attribute_19_name, attribute_19_value, attribute_19_visibility, attribute_19_global,
        attribute_20_name, attribute_20_value, attribute_20_visibility, attribute_20_global,
        attribute_21_name, attribute_21_value, attribute_21_visibility, attribute_21_global,
        attribute_22_name, attribute_22_value, attribute_22_visibility, attribute_22_global,
        attribute_23_name, attribute_23_value, attribute_23_visibility, attribute_23_global,
        attribute_24_name, attribute_24_value, attribute_24_visibility, attribute_24_global
    )
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
'''
cursor = connection.cursor()
def insert_data(
            sku, name, short_description, description, stock, weight, length, width, height, sale_price, regular_price, categories, images, product_url,
            attribute_1_name, attribute_1_value, attribute_1_visibility, attribute_1_global,
            attribute_2_name, attribute_2_value, attribute_2_visibility, attribute_2_global,
            attribute_3_name, attribute_3_value, attribute_3_visibility, attribute_3_global,
            attribute_4_name, attribute_4_value, attribute_4_visibility, attribute_4_global,
            attribute_5_name, attribute_5_value, attribute_5_visibility, attribute_5_global,
            attribute_6_name, attribute_6_value, attribute_6_visibility, attribute_6_global,
            attribute_7_name, attribute_7_value, attribute_7_visibility, attribute_7_global,
            attribute_8_name, attribute_8_value, attribute_8_visibility, attribute_8_global,
            attribute_9_name, attribute_9_value, attribute_9_visibility, attribute_9_global,
            attribute_10_name, attribute_10_value, attribute_10_visibility, attribute_10_global,
            attribute_11_name, attribute_11_value, attribute_11_visibility, attribute_11_global,
            attribute_12_name, attribute_12_value, attribute_12_visibility, attribute_12_global,
            attribute_13_name, attribute_13_value, attribute_13_visibility, attribute_13_global,
            attribute_14_name, attribute_14_value, attribute_14_visibility, attribute_14_global,
            attribute_15_name, attribute_15_value, attribute_15_visibility, attribute_15_global,
            attribute_16_name, attribute_16_value, attribute_16_visibility, attribute_16_global,
            attribute_17_name, attribute_17_value, attribute_17_visibility, attribute_17_global,
            attribute_18_name, attribute_18_value, attribute_18_visibility, attribute_18_global,
            attribute_19_name, attribute_19_value, attribute_19_visibility, attribute_19_global,
            attribute_20_name, attribute_20_value, attribute_20_visibility, attribute_20_global,
            attribute_21_name, attribute_21_value, attribute_21_visibility, attribute_21_global,
            attribute_22_name, attribute_22_value, attribute_22_visibility, attribute_22_global,
            attribute_23_name, attribute_23_value, attribute_23_visibility, attribute_23_global,
            attribute_24_name, attribute_24_value, attribute_24_visibility, attribute_24_global
        ):
    # Data to be inserted
    data = (
            sku, name, short_description, description, stock, weight, length, width, height, sale_price, regular_price, categories, images, product_url,
            attribute_1_name, attribute_1_value, attribute_1_visibility, attribute_1_global,
            attribute_2_name, attribute_2_value, attribute_2_visibility, attribute_2_global,
            attribute_3_name, attribute_3_value, attribute_3_visibility, attribute_3_global,
            attribute_4_name, attribute_4_value, attribute_4_visibility, attribute_4_global,
            attribute_5_name, attribute_5_value, attribute_5_visibility, attribute_5_global,
            attribute_6_name, attribute_6_value, attribute_6_visibility, attribute_6_global,
            attribute_7_name, attribute_7_value, attribute_7_visibility, attribute_7_global,
            attribute_8_name, attribute_8_value, attribute_8_visibility, attribute_8_global,
            attribute_9_name, attribute_9_value, attribute_9_visibility, attribute_9_global,
            attribute_10_name, attribute_10_value, attribute_10_visibility, attribute_10_global,
            attribute_11_name, attribute_11_value, attribute_11_visibility, attribute_11_global,
            attribute_12_name, attribute_12_value, attribute_12_visibility, attribute_12_global,
            attribute_13_name, attribute_13_value, attribute_13_visibility, attribute_13_global,
            attribute_14_name, attribute_14_value, attribute_14_visibility, attribute_14_global,
            attribute_15_name, attribute_15_value, attribute_15_visibility, attribute_15_global,
            attribute_16_name, attribute_16_value, attribute_16_visibility, attribute_16_global,
            attribute_17_name, attribute_17_value, attribute_17_visibility, attribute_17_global,
            attribute_18_name, attribute_18_value, attribute_18_visibility, attribute_18_global,
            attribute_19_name, attribute_19_value, attribute_19_visibility, attribute_19_global,
            attribute_20_name, attribute_20_value, attribute_20_visibility, attribute_20_global,
            attribute_21_name, attribute_21_value, attribute_21_visibility, attribute_21_global,
            attribute_22_name, attribute_22_value, attribute_22_visibility, attribute_22_global,
            attribute_23_name, attribute_23_value, attribute_23_visibility, attribute_23_global,
            attribute_24_name, attribute_24_value, attribute_24_visibility, attribute_24_global
        )

    query = f"SELECT * FROM {TABLE_NAME} WHERE name = %s"
    cursor.execute(query, (name,))
    # Fetch the result
    result = cursor.fetchone()

    # Check if the result is not empty
    if result:
        print("Data already exists in the database.")
        # Handle the case where the data already exists
    else:
        # Execute the query to insert data
        cursor.execute(insert_query, data)

        # Commit the changes
        connection.commit()
    

    # Close the cursor and the connection

def close_db():
    cursor.close()
    connection.close()

    