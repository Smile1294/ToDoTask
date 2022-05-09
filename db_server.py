import threading
import time

import grpc
import concurrent
from concurrent import futures
import pymongo
from pymongo import MongoClient
import os
import grpc
import db_pb2
import db_pb2_grpc
os.environ["USER"] = "david123"
os.environ["PASSWORD"] = "david123"

USER = os.getenv('USER')
PASSWORD = os.environ.get('PASSWORD')

cluster = MongoClient("mongodb://"+USER+":"+PASSWORD+"@cluster0-shard-00-00.otcai.mongodb.net:27017,cluster0-shard-00-01.otcai.mongodb.net:27017,cluster0-shard-00-02.otcai.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-zkkws9-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = cluster["test"]
collection = mydb["test"]
class DatabaseServiceServicer(db_pb2_grpc.DatabaseServiceServicer):

    def GetBox(self,request,context):
        return  collection.find({request},{})

    def GetBoxes(self,request,context):
        print(collection.find({},{}))
        return  db_pb2.GetBoxesResponse(collection.find({},{}))

    def CreateBox(self, request, context):
        collection.insert_one(request)
        for data in collection.find():
            print(data)
        return db_pb2.CreateBoxResponse

    def UpdateBox(self, request, context):
        print("we got UpdateBox")


    def DeleteBox(self, request, context):
        print("we got DeleteBox")


    def GetBoxesInCategory(self, request, context):
        print("we got GetBoxesInCategory")


    def GetBoxesInTimeRange(self, request, context):
        print("we got GetBoxesInTimeRange")


def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    db_pb2_grpc.add_DatabaseServiceServicer_to_server(DatabaseServiceServicer(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("server on")
            time.sleep(10)
    except KeyboardInterrupt:
        print("key board interrupt")
        server.stop(0)
if __name__ == "__main__":
    main()