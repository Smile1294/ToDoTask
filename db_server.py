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
os.environ['USER'] = 'david123'
os.environ['PASSWORD'] = 'david123'

USER = os.getenv('USER')
PASSWORD = os.environ.get('PASSWORD')

cluster = MongoClient(
    "mongodb://" + USER + ":" + PASSWORD + "@cluster0-shard-00-00.otcai.mongodb.net:27017,cluster0-shard-00-01.otcai.mongodb.net:27017,cluster0-shard-00-02.otcai.mongodb.net:27017/myFirstDatabase?ssl=true&replicaSet=atlas-zkkws9-shard-0&authSource=admin&retryWrites=true&w=majority")
mydb = cluster.get_default_database()
collection = mydb.get_collection('test')


class DatabaseServiceServicer(db_pb2_grpc.DatabaseServiceServicer):

    def GetBox(self, request, context):

        box = db_pb2.Box(name="bob", id=0, price=23, description="ok", category="food", quantity=2,
                         created_at=timestamp)
        return db_pb2.GetBoxResponse(box=box, status=db_pb2.RequestStatus.OK)

    def GetBoxes(self, request, context):
        box =  {"name":"name1","id":0,"price":23,"description":"des","cetgory":"food","quantity":2,
                "created_at":timestamp}
        print(box)
        return db_pb2.GetBoxesResponse(box = box,status=db_pb2.RequestStatus.OK)

    def CreateBox(self, request, context):
        collection.insert_one({"name": request.box.name, "_id": request.box.id, "price": request.box.price,
                               "description": request.box.description, "category": request.box.category,
                               "quantity": request.box.quantity,
                               "created_at": {"seconds": request.box.created_at.seconds, "nanos": request.box.created_at.nanos}})
        return db_pb2.CreateBoxResponse(status=db_pb2.RequestStatus.OK)

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
