import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'face6969'.decode('hex')
P2P_PORT = 9560
ADDRESS_VERSION = 62
RPC_PORT = 9561
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'sexcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 100*100000000 >> (height + 1)//600000
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data))
BLOCK_PERIOD = 60 # s
SYMBOL = 'SXC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Sexcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Sexcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.sexcoin'), 'sexcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://be.lavajumper.com/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://be.lavajumper.com/address/'
TX_EXPLORER_URL_PREFIX = 'http://be.lavajumper.com/tx/'
SANE_TARGET_RANGE = (2**256//1000000000 - 1, 2**256//1000 - 1)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.03e8
