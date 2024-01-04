import happybase


def insert_data(connection):
    table_name = 'commande'
    table = connection.table(table_name)

    row_key = input("Enter the row key for insertion: ")
    nom = input("Enter client's name: ")
    ville = input("Enter client's city: ")
    produit = input("Enter product: ")
    prix = input("Enter price: ")

    data = {
        f'client:nom': nom,
        f'client:ville': ville,
        f'vente:produit': produit,
        f'vente:prix': prix
    }
    table.put(row_key, data)
    print(f"Inserted data with row key {row_key}")


def retrieve_data(connection):
    table_name = 'commande'
    table = connection.table(table_name)

    row_key = input("Enter the row key for retrieval: ")
    row = table.row(row_key)

    if row:
        print(f"Retrieved data for row key {row_key}:")
        for column, value in row.items():
            print(f"{column.decode('utf-8')} : {value.decode('utf-8')}")
    else:
        print(f"No data found for row key {row_key}")


def update_data(connection):
    table_name = 'commande'
    table = connection.table(table_name)

    row_key = input("Enter the row key for update: ")
    prix = input("Enter the updated price: ")

    data = {
        f'vente:prix': prix
    }
    table.put(row_key, data)
    print(f"Updated data for row key {row_key}")


def delete_data(connection):
    table_name = 'commande'
    table = connection.table(table_name)

    row_key = input("Enter the row key for deletion: ")
    table.delete(row_key)
    print(f"Deleted data with row key {row_key}")


def main():
    connection = happybase.Connection('localhost', port=9090)

    while True:
        print("\nOptions:")
        print("1. Insert data")
        print("2. Retrieve data")
        print("3. Update data")
        print("4. Delete data")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            insert_data(connection)
        elif choice == '2':
            retrieve_data(connection)
        elif choice == '3':
            update_data(connection)
        elif choice == '4':
            delete_data(connection)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

    connection.close()


if __name__ == "__main__":
    main()
