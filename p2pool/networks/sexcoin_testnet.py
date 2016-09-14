from p2pool.bitcoin import networks

PARENT = networks.nets['sexcoin_testnet']
SHARE_PERIOD = 4 # seconds
CHAIN_LENGTH = 20*60//3 # shares
REAL_CHAIN_LENGTH = 20*60//3 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'cca5e24ec6408b1e'.decode('hex')
PREFIX = 'ad9614f6466a39cf'.decode('hex')
P2P_PORT = 19568
MIN_TARGET = 2**256//50 - 1
MAX_TARGET = 2**256//50 - 1
PERSIST = False
WORKER_PORT = 19569
BOOTSTRAP_ADDRS = 'sexcoin-test.sexcoin.info'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
