from p2pool.bitcoin import networks

PARENT = networks.nets['sexcoin']
SHARE_PERIOD = 15 # seconds
CHAIN_LENGTH = 24*60*60//30 # shares
REAL_CHAIN_LENGTH = 24*60*60//30 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 10 # blocks
IDENTIFIER = 'e037d5b8c6923410'.decode('hex')
PREFIX = '7208c1a53ef629b0'.decode('hex')
P2P_PORT = 8698
MIN_TARGET = 0                 # Share difficulty
MAX_TARGET = 2**256//2**20 - 1 # Share difficulty
PERSIST = False
WORKER_PORT = 9699
BOOTSTRAP_ADDRS = 'sxc.newco.in'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: None if 060406 <= v else 'Sexcoin version too old. Upgrade to 0.10.4 or newer!'
VERSION_WARNING = lambda v: None
