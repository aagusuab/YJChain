from YJChain.block import Block
import logging
import json


class BlockChain:
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        curr_chain = self.chain
        new_block = Block.mine_block(curr_chain[(len(curr_chain) - 1)], data)
        self.chain.append(new_block)
        return new_block

    def is_valid(self):
        curr_chain = self.chain
        if curr_chain[0].to_string() != Block.genesis().to_string():
            return False

        for index, block in enumerate(curr_chain):
            print(block.data)
            print(str(block.prev_hash))
            print(str(block.hash))
            print(block.timestamp)
            if index != 0:
                last_block = curr_chain[index - 1]
                if block.prev_hash != last_block.hash or block.hash != Block.to_hash(block.timestamp, block.prev_hash,
                                                                                     block.data):
                    logging.error("incorrect hash")
                    return False
        return True

    def replace(self, new_chain):
        if len(new_chain.chain) <= len(self.chain):
            logging.error("Chain size not long enough")
        elif not new_chain.is_valid:
            logging.error("chain not valid")
        self.chain = new_chain.chain

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=1)
