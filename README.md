Requirements:
-------------------------
Generic:
* Bitcoin >=0.8.5
* Python >=2.6
* Twisted >=10.0.0
* python-argparse (for Python =2.6)

Linux:
* sudo apt-get install python-zope.interface python-twisted python-twisted-web
* sudo apt-get install python-argparse # if on Python 2.6

Windows:
* Install Python 2.7: http://www.python.org/getit/
* Install Twisted: http://twistedmatrix.com/trac/wiki/Downloads
* Install Zope.Interface: http://pypi.python.org/pypi/zope.interface/3.8.0
* Install python win32 api: http://sourceforge.net/projects/pywin32/files/pywin32/Build%20218/
* Install python win32 api wmi wrapper: https://pypi.python.org/pypi/WMI/#downloads
* Unzip the files into C:\Python27\Lib\site-packages

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

Donations towards further development:
-------------------------
    BTC 1HNeqi3pJRNvXybNX4FKzZgYJsdTSqJTbk

Official wiki :
-------------------------
https://en.bitcoin.it/wiki/P2Pool

Notes for SexCoin:
=========================
Requirements:
-------------------------
In order to run P2Pool with the SexCoin network, you would need to build and install the
ltc_scrypt module that includes the scrypt proof of work code that SexCoin uses for hashes.

Linux:

    cd litecoin_scrypt
    sudo python setup.py install

Windows (mingw):
* Install MinGW: http://www.mingw.org/wiki/Getting_Started
* Install Python 2.7: http://www.python.org/getit/

In bash type this:

    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install

Windows (microsoft visual c++)
* Open visual studio console

In bash type this:

    SET VS90COMNTOOLS=%VS110COMNTOOLS%	           # For visual c++ 2012
    SET VS90COMNTOOLS=%VS100COMNTOOLS%             # For visual c++ 2010
    cd litecoin_scrypt
    C:\Python27\python.exe setup.py build --compile=mingw32 install
	
If you run into an error with unrecognized command line option '-mno-cygwin', see this:
http://stackoverflow.com/questions/6034390/compiling-with-cython-and-mingw-produces-gcc-error-unrecognized-command-line-o


Full Installation instructions
=========================
Linux:
-------------------------
Performed on Ubuntu 12.04 Server

Prerequisites:

    • sudo apt-get update
    • sudo apt-get install python-software-properties screen git python-rrdtool python-pygame python-scipy 
    • sudo apt-get install python-twisted python-twisted-web python-imaging build-essential libglib2.0-dev libglibmm-2.4-dev 
    • sudo apt-get install python-dev libboost-all-dev libdb++-dev autoconf automake ncurses-dev

Download and install sexcoin client:

    • git clone https://github.com/sexcoin-project/sexcoin.git
    • cd /sexcoin/src
    • make -f makefile.unix USE_UPNP=-
    • cp sexcoind /usr/bin
    • mkdir ~/.sexcoin
    • nano ~/.sexcoin/sexcoin.conf

    Paste:

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

    • /usr/bin/sexcoind -daemon

This will start the daemon and begin downloading the blockchain.
Run this to test the daemon is working:
    • sexcoind getinfo

Download & install P2pool:

    • cd 
    • git clone https://github.com/wedge905/p2pool-sexcoin.git
    • cd p2pool/litecoin_scrypt
    • sudo python setup.py install
    • cd ..
    • python run_p2pool.py --net sexcoin -a <PAYOUTADDRESS> --give-author 0

That will get P2pool up and running.  There might be a delay if the daemon is still downloading the blockchain.  Once that is done, workers can now connect on port 9699


Windows:
-------------------------    
    TBD