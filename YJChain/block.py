import datetime as dt
import hashlib


class Block:
    def __init__(self, data, prev_hash, hash, timestamp):
        self.data = data
        self.prev_hash = prev_hash
        self.hash = hash
        self.timestamp = timestamp

    def to_string(self):
        return str(self.data) + str(self.prev_hash)[0:10] + str(self.hash)[0:10] + str(self.timestamp)

    @staticmethod
    def genesis():
        return Block("Genesis Time", "----------", "f1r57-h45h", dt.datetime(2021, 1, 1, 0, 0, 0).timestamp())

    @staticmethod
    def to_hash(time, last_hash, data):
        new_string = str(time) + str(last_hash) + str(data)
        return hashlib.sha512(new_string.encode()).digest()

    @staticmethod
    def mine_block(last_block, data):
        new_time = dt.datetime.now().timestamp()
        prev_hash = last_block.hash
        new_hash = Block.to_hash(new_time, prev_hash, data)
        return Block(data, prev_hash, new_hash, new_time)
