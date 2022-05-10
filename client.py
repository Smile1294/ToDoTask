import db_pb2_grpc as db_pb2_grpc
import db_pb2 as db_pb2
import grpc
from google.protobuf.timestamp_pb2 import Timestamp
timestamp = Timestamp()
timestamp.GetCurrentTime()
def run():
    with grpc.insecure_channel("localhost:9999") as channel:
        stub = db_pb2_grpc.DatabaseServiceStub(channel)
        try:
            box = db_pb2.Box(name="bob", id=0, price=23, description="ok", category="food", quantity=2,
                             created_at=timestamp)
            CreateBox = db_pb2.CreateBoxRequest(box=box)
            response = stub.CreateBox(CreateBox)
            print(response)
        except:
            print("fail")
        try:
            getBoxes = db_pb2.GetAllBoxesRequest()
            response = stub.GetBoxes(getBoxes)
            print(response)
        except:
            print("fail")
        try:
            getBox = db_pb2.GetBoxRequest(id=1)
            response = stub.GetBox(getBox)
            print(response)
        except:
            print("fail getbox")


def close(channel):
    channel.close()


if __name__ == "__main__":
    run()
