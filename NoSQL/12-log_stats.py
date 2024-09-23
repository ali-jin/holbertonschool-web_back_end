#!/usr/bin/env python3
""" Stats about Nginx logs in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    nginx_collection = client.logs.nginx

    logs_count = nginx_collection.count_documents({})
    print(f"{logs_count} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{status_count} status check")
