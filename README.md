Requirements:
-------------------------
Generic:
* Bitcoin >=0.8.5
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Running P2Pool-Sexcoin:
-------------------------
To use P2Pool, you must be running your own local sexcoind. For standard
configurations, using P2Pool should be as simple as:

    python run_p2pool.py --net sexcoin -a <defaultSxcAddress> -f <minerFee%> --give-author 0

Then run your miner program, connecting to 127.0.0.1 on port 9699 with any
username and password.

If you are behind a NAT, you should enable TCP port forwarding on your
router. Forward port 8699 to the host running P2Pool.

Run for additional options.

    python run_p2pool.py --help

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Full Installation instructions
=========================
Linux:
-------------------------
Performed on Ubuntu 12.04 Server

Prerequisites:

    sudo apt-get update
    sudo apt-get install python-software-properties screen git python-rrdtool python-pygame python-scipy 
    sudo apt-get install python-twisted python-twisted-web python-imaging build-essential libglib2.0-dev libglibmm-2.4-dev 
    sudo apt-get install python-dev libboost-all-dev libdb++-dev autoconf automake ncurses-dev

Download and install sexcoin client:

    git clone https://github.com/sexcoin-project/sexcoin.git
    cd /sexcoin/src
    make -f makefile.unix USE_UPNP=-
    cp sexcoind /usr/bin
    mkdir ~/.sexcoin
    nano ~/.sexcoin/sexcoin.conf

Paste into editor:

    server=1
    rpcuser=user
    rpcpassword=pass
    rpcport=9561
    daemon=1
    rpcallowip=*
    addnode=46.39.246.24:9560
    addnode=68.52.140.186:9560
    addnode=84.253.217.35:9560
    addnode=67.191.160.195:9560
    addnode=223.27.19.38:9560
    addnode=162.243.17.119:9560

Then press ctrl+x to save and close

    /usr/bin/sexcoind -daemon

This will start the daemon and begin downloading the blockchain.
Run this to test the daemon is working:

    sexcoind getinfo

Download & install P2pool:

    cd 
    git clone https://github.com/wedge905/p2pool-sexcoin.git
    cd p2pool/litecoin_scrypt
    sudo python setup.py install
    cd ..
    python run_p2pool.py --net sexcoin -a <DEFAULTPAYOUTADDRESS> --give-author 0

That will get P2pool up and running.  There might be a delay if the daemon is still downloading the blockchain.  Once that is done, workers can now connect on port 9699


Windows:
-------------------------    
Download and unzip the latest P2Pool-Sexcoin binaries

    https://github.com/wedge905/p2pool-sexcoin/raw/master/p2pool_sexcoin_win32_13.3.zip 

Minimum required command line:

    run_p2pool.exe --net sexcoin --give-author 0

By default it assumes sexcoind is running on the same machine.  You can specify an different location for sexcoind:

    run_p2pool.exe --net sexcoin --bitcoind-address <ipaddress> --bitcoind-p2p-port <port> --give-author 0

You can also run run_p2pool.exe -h for more command line options

Donations towards further development:
-------------------------
    Original P2Pool Dev forrestv: BTC 1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk
    P2Pool-Sexcoin Dev wedge: SXC SH6BeQUyNXXkSDNWuB8z1fAE7FC8L4n8i9
    Sexcoin Developer lavajumper: SXC