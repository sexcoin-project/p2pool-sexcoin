from p2pool.bitcoin import networks

PARENT = networks.nets['sexcoin_testnet']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 24*60*60//10 # 20*60//3 <==wedge's calc # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # 20*60//3 <==wedge's calc # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 30 # blocks,(600/block time)*3
IDENTIFIER = 'cca5e24ec6408b1e'.decode('hex')
PREFIX = 'ad9614f6466a39cf'.decode('hex')
P2P_PORT = 19568 #Talk to other P2Pools?
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = False
WORKER_PORT = 19699
BOOTSTRAP_ADDRS = 'sexcoin-test.sexcoin.info'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: True
