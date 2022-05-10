import time
from concurrent import futures
from pymongo import MongoClient
import os
import grpc
import db_pb2
import db_pb2_grpc
import pymongoarrow.monkey
from google.protobuf.timestamp_pb2 import Timestamp
timestamp = Timestamp()
timestamp.GetCurrentTime()
pymongoarrow.monkey.patch_all()

USER = os.getenv('USER')
PASSWORD = os.environ.get('PASSWORD')

cluster = MongoClient(
    "mongodb://" + USER + ":" + PASSWORD + "@cluster0-shard-00-00.otcai.mongodb.net:27017,cluster0-shard-00-01.otcai.mongodb.net:27017,cluster0-shard-00-02.otcai.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-zkkws9-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = cluster.get_default_database()
collection = mydb.get_collection('test')

class DatabaseServiceServicer(db_pb2_grpc.DatabaseServiceServicer):

    def GetBox(self, request, context):
        try:
            db_pb2.Box = collection.find_one({"id": request.id},{"_id":0})
            if db_pb2.Box is not None:
                return db_pb2.GetBoxResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.OK)
            else:
                return db_pb2.GetBoxResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.ERROR)

        except:
            return db_pb2.GetBoxResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.ERROR)



    def GetBoxes(self, request, context):
        try:
            db_pb2.Box = collection.find({}, {"_id": 0})
            return db_pb2.GetBoxesResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.OK)
        except:
            return db_pb2.GetBoxesResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.ERROR)



    def CreateBox(self, request, context):
        try:
            db_pb2.Box = collection.find_one({"id": request.box.id}, {"_id": 0})
            if db_pb2.Box is None:
                collection.insert_one({"name": request.box.name, "id": request.box.id, "price": request.box.price,
                                       "description": request.box.description, "category": request.box.category,
                                       "quantity": request.box.quantity,
                                       "created_at": {"seconds": request.box.created_at.seconds,
                                                      "nanos": request.box.created_at.nanos}})
                return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.OK)
            else:
                return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.ERROR)
        except:
            return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.ERROR)


    def UpdateBox(self, request, context):

        try:
            db_pb2.Box = collection.find_one({"id": request.box.id}, {"_id": 0})
            if db_pb2.Box is None:
                return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.ERROR)
            else:
                box = {"name": request.box.name, "id": request.box.id, "price": request.box.price,
                       "description": request.box.description, "category": request.box.category,
                       "quantity": request.box.quantity,
                       "created_at": {"seconds": request.box.created_at.seconds,
                                      "nanos": request.box.created_at.nanos}}
                collection.replace_one({"id": request.box.id}, box)
                return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.OK)
        except:
            return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.ERROR)




    def DeleteBox(self, request, context):
        try:
            db_pb2.Box = collection.find_one({"id": request.id}, {"_id": 0})
            if db_pb2.Box is None:
                return db_pb2.DeleteBoxResponse(status=db_pb2.RequestStatus.ERROR)
            else:
                collection.delete_one({"id": request.id})
                return db_pb2.DeleteBoxResponse(status=db_pb2.RequestStatus.OK)
        except:
            return db_pb2.DeleteBoxResponse(status=db_pb2.RequestStatus.ERROR)


    def GetBoxesInCategory(self, request, context):
        try:
            db_pb2.Box = collection.find({"category":request.category}, {"_id": 0})
            return db_pb2.GetBoxesResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.OK)
        except:
            return db_pb2.GetBoxesResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.ERROR)


    def GetBoxesInTimeRange(self, request, context):
        try:
            db_pb2.Box = collection.find({"created_at.seconds": {"$gte":request.start_time.seconds},"created_at.nanos": {"$gte":request.start_time.nanos},
                                          "created_at.seconds": {"$lte":request.end_time.seconds},"created_at.nanos": {"$lte":request.end_time.nanos}},
                                          {"_id": 0})
            return db_pb2.GetBoxesResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.OK)
        except:
            return db_pb2.GetBoxesResponse(box=db_pb2.Box, status=db_pb2.RequestStatus.ERROR)


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
