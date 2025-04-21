N33Bcoin Core 0.14.2
=====================

Setup
---------------------
N33Bcoin Core is the original N33Bcoin client and it builds the backbone of the network. However, it downloads and stores the entire history of N33Bcoin transactions (which is currently several GBs); depending on the speed of your computer and network connection, the synchronization process can take anywhere from a few hours to a day or more.

To download N33Bcoin Core, visit [n33bcoincore.org](https://n33bcoincore.org/en/releases/).

Running
---------------------
The following are some helpful notes on how to run N33Bcoin on your native platform.

### Unix

Unpack the files into a directory and run:

- `bin/n33bcoin-qt` (GUI) or
- `bin/n33bcoind` (headless)

### Windows

Unpack the files into a directory, and then run n33bcoin-qt.exe.

### OS X

Drag N33Bcoin-Core to your applications folder, and then run N33Bcoin-Core.

### Need Help?

* See the documentation at the [N33Bcoin Wiki](https://en.n33bcoin.it/wiki/Main_Page)
for help and more information.
* Ask for help on [#n33bcoin](http://webchat.freenode.net?channels=n33bcoin) on Freenode. If you don't have an IRC client use [webchat here](http://webchat.freenode.net?channels=n33bcoin).
* Ask for help on the [N33BcoinTalk](https://n33bcointalk.org/) forums, in the [Technical Support board](https://n33bcointalk.org/index.php?board=4.0).

Building
---------------------
The following are developer notes on how to build N33Bcoin on your native platform. They are not complete guides, but include notes on the necessary libraries, compile flags, etc.

- [OS X Build Notes](build-osx.md)
- [Unix Build Notes](build-unix.md)
- [Windows Build Notes](build-windows.md)
- [OpenBSD Build Notes](build-openbsd.md)
- [Gitian Building Guide](gitian-building.md)

Development
---------------------
The N33Bcoin repo's [root README](/README.md) contains relevant information on the development process and automated testing.

- [Developer Notes](developer-notes.md)
- [Release Notes](release-notes.md)
- [Release Process](release-process.md)
- [Source Code Documentation (External Link)](https://dev.visucore.com/n33bcoin/doxygen/)
- [Translation Process](translation_process.md)
- [Translation Strings Policy](translation_strings_policy.md)
- [Travis CI](travis-ci.md)
- [Unauthenticated REST Interface](REST-interface.md)
- [Shared Libraries](shared-libraries.md)
- [BIPS](bips.md)
- [Dnsseed Policy](dnsseed-policy.md)
- [Benchmarking](benchmarking.md)

### Resources
* Discuss on the [N33BcoinTalk](https://n33bcointalk.org/) forums, in the [Development & Technical Discussion board](https://n33bcointalk.org/index.php?board=6.0).
* Discuss project-specific development on #n33bcoin-core-dev on Freenode. If you don't have an IRC client use [webchat here](http://webchat.freenode.net/?channels=n33bcoin-core-dev).
* Discuss general N33Bcoin development on #n33bcoin-dev on Freenode. If you don't have an IRC client use [webchat here](http://webchat.freenode.net/?channels=n33bcoin-dev).

### Miscellaneous
- [Assets Attribution](assets-attribution.md)
- [Files](files.md)
- [Fuzz-testing](fuzzing.md)
- [Reduce Traffic](reduce-traffic.md)
- [Tor Support](tor.md)
- [Init Scripts (systemd/upstart/openrc)](init.md)
- [ZMQ](zmq.md)

License
---------------------
Distributed under the [MIT software license](/COPYING).
This product includes software developed by the OpenSSL Project for use in the [OpenSSL Toolkit](https://www.openssl.org/). This product includes
cryptographic software written by Eric Young ([eay@cryptsoft.com](mailto:eay@cryptsoft.com)), and UPnP software written by Thomas Bernard.
