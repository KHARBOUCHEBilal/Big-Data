# Project Title: HBase Data Storage and Retrieval Application

## Description
This project involves the development of an application that facilitates the storage and retrieval of data from an HBase cluster using Python. HBase is a distributed, scalable, NoSQL database that runs on top of the Hadoop Distributed File System (HDFS). The application will demonstrate how to efficiently interact with HBase, including operations such as inserting, querying, and updating records.

### Objectives
- To design a Python application capable of connecting to an HBase cluster.
- To implement data storage mechanisms for efficient data retrieval.
- To perform CRUD (Create, Read, Update, Delete) operations on HBase.
- To showcase the scalability and performance benefits of using HBase for large datasets.

## Technologies Used
- **HBase**: NoSQL database for storing large volumes of data.
- **Python**: Programming language for developing the application.
- **HappyBase**: A Python library to interact with HBase.
- **Apache Hadoop**: Distributed file system for handling big data storage.

## Features
- **Data Ingestion**: Ability to store large datasets into HBase tables.
- **Data Retrieval**: Efficiently query data from HBase based on various conditions.
- **Data Update and Deletion**: Modify or remove records as necessary.
- **Connection Management**: Handle connections to the HBase cluster seamlessly.

## Getting Started

### Prerequisites
- Python 3.x installed
- HBase installed and running on a Hadoop cluster
- Required Python libraries:
  ```bash
  pip install happybase
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hbase-data-storage-retrieval.git
   cd hbase-data-storage-retrieval
   ```

2. Set up your HBase configuration in the application:
   - Update the HBase connection parameters in the `config.py` file.

### Usage
To run the application:
```bash
python app.py
```

- Use the command line interface to enter data and execute queries.
- Follow the prompts to insert, retrieve, update, or delete records.

## Code Structure
- `app.py`: Main application file for interacting with HBase.
- `config.py`: Configuration file for HBase connection settings.
- `data_operations.py`: Contains functions for performing CRUD operations.
- `README.md`: Documentation for the project.

## References
- [HBase Documentation](https://hbase.apache.org/)
- [HappyBase Documentation](https://happybase.readthedocs.io/en/latest/)

## Author
- **Kharbouche Bilal**  
  Email: bilal.kharbouche99@gmail.com
