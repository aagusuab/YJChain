# test_blockchain.py
from YJChain.block import Block
from YJChain.blockchain import BlockChain
import logging

bc = BlockChain()
bc2 = BlockChain()


def test_starts_with_genesis():
    genesis_block = Block.genesis()
    assert bc.chain[0].to_string(), genesis_block.to_string()
    assert bc2.chain[0].to_string(), genesis_block.to_string()


def test_add_block():
    new_data = "new_data_1"
    bc.add_block(new_data)
    assert new_data, bc.chain[len(bc.chain) - 1].data


def test_validate():
    bc2.add_block("new_data_2")
    bc2.is_valid()
    # assert bc2.is_valid(), 0


def test_replace():
    bc2.add_block("new_data_3")
    bc.replace(bc2)
    assert bc.chain, bc2.chain


if __name__ == '__main__':
    test_validate()