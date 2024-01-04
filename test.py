import happybase

try:
    connection = happybase.Connection('localhost', port=60030)
    print("HBase Thrift server is accessible.")
    connection.close()
except Exception as e:
    print("Could not connect to the HBase Thrift server:", e)
