# test_block.py
from YJChain import block


def test_new_block_creation():
    genesis_block = block.Block.genesis()
    new_block = block.Block.mine_block(genesis_block, "new_data")
    assert "newData", new_block.data
