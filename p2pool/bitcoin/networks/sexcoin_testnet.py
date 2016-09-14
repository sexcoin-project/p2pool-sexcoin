import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'face9696'.decode('hex')
P2P_PORT = 19560
ADDRESS_VERSION = 111
RPC_PORT = 19561
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'sexcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 100*100000000 >> (height + 1)//6000000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 150 # s
SYMBOL = 'tSXC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Sexcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Sexcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.sexcoin'), 'sexcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://nonexistent-litecoin-testnet-explorer/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://chain.so/address/SXCTEST/'
TX_EXPLORER_URL_PREFIX = 'https://chain.so/tx/SXCTEST/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 1e8
