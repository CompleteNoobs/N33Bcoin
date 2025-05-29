# N33Bcoin 
N33Bcoin learning about bitcoin by creating a fork and tinkering about.

## Start up HardWare 

* OS (local) Ubuntu-Mate 24.04 - this tut is done on a clean install of ubuntu-mate 24.04
* Hardware: HP EliteDesk G1 - ram = 8GB - HD = 120GB ssd - CPU = i5-4590S CPU @ 3.00GHz
* Hardware: Thinkpad X270 - Ram - HD - CPU
* Server VPS ubuntu-server 24.04
* vultr.com

## Software OS

* Will be using Ubuntu 24.04 as main OS - but to build this version of litecoin 0.14.2 we will be using ubuntu 18.04 in a lxc container - trying to build in 24.04 was a huge side quest that is not that much fun.

## Coin Params for N33Bcoin 0.1 POW 

Are Coin Params:
* Name of coin = N33Bcoin
* Symbol coin = N33B
* Premined Coins= 33% 11,111,111 coins to be used to rewards contributors. the how is currently unknown, will work out as we go.
* MaxCoins = 33,333,333
* Rewards = 333
* Halving Period = 33,333 blocks = every 231 days
* Block interval = 10 mins # will leave at 10 for starters
* Time Stamp 1733333333 2024-12-04 17:28:53
* Time Stamp Message "N33B's for Noob's at CompleteNoobs.com"
* Genesis Block for are Coin

## Genesis Keys

First we are going to need a public private key pair.  <br>
[Python3 Generate Public Private Key Pair](https://www.completenoobs.com/noobs/Python_Generate_Public_Private_Key_Pair_Crypto_Bitcoin "Python3 Generate Public Private Key Pair")



* Public Key
<code>049bd17782313a0263154a37b7adb5f773e3a95e08eba879d6a8f1c9e614e41b33f85129d0f9820a464d2ae136abaa4144d258df6729dfd7c6a18498148b59fadf</code>
* Keep private key safe, you just need pub key for now

We then use are public key along with are coin parameter with [GenesisH0](https://www.completenoobs.com/noobs/GenesisH0_Creating_Genesis_Hash) to create a 'Nonce', 'Merkel hash' and 'Genesis hash'.
For are 'MainNet', 'TestNet' and 'RegNet'

### Main Net parameters 
```python2 genesis.py -a SHA256 -z "N33B's for Noob's at CompleteNoobs.com" -t 1733333333 -b 0x1d00ffff -p 049bd17782313a0263154a37b7adb5f773e3a95e08eba879d6a8f1c9e614e41b33f85129d0f9820a464d2ae136abaa4144d258df6729dfd7c6a18498148b59fadf -v 33300000000```
 
* <strong>TimeStampMessage</strong>: <code>N33B's for Noob's at CompleteNoobs.com</code>
* <strong>UnixTimeStamp</strong>: <code>1733333333</code>
* <strong>Nonce</strong>: <code>221118658</code>
* <strong>nBits</strong>: <code>0x1d00ffff</code>
* <strong>Merkel</strong>: <code>96908dea6891a3cc8751ed962736bbc1f4129c5c2fa7f44333def15ce86c4388</code>
* <strong>Genesis</strong>: <code>0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4</code>

### Test Net parameters 
<code>python2.5 genesis.py -a SHA256 -z "N33B's for Noob's at CompleteNoobs.com" -t 1733333334 -b 0x1e0ffff0 -p 049bd17782313a0263154a37b7adb5f773e3a95e08eba879d6a8f1c9e614e41b33f85129d0f9820a464d2ae136abaa4144d258df6729dfd7c6a18498148b59fadf -v 33300000000</code>

* <strong>TimeStampMessage</strong>: <code>N33B's for Noob's at CompleteNoobs.com</code>
* <strong>UnixTimeStamp</strong>: <code>1733333334</code>
* <strong>Nonce</strong>: <code>511144</code>
* <strong>nBits</strong>: <code>0x1e0ffff0</code>
* <strong>Merkel</strong>: <code>96908dea6891a3cc8751ed962736bbc1f4129c5c2fa7f44333def15ce86c4388</code>
* <strong>Genesis</strong>: <code>000001b7cbb2e5ae084fdd6934c9962fd8ff27cb7c27e02e415d2da6fe214a8c</code>

### Reg Net parameters 
<code>python2.5 genesis.py -a SHA256 -z "N33B's for Noob's at CompleteNoobs.com" -t 1733333335 -b 0x207fffff -p 049bd17782313a0263154a37b7adb5f773e3a95e08eba879d6a8f1c9e614e41b33f85129d0f9820a464d2ae136abaa4144d258df6729dfd7c6a18498148b59fadf -v 33300000000</code>

* <strong>TimeStampMessage</strong>: <code>N33B's for Noob's at CompleteNoobs.com</code>
* <strong>UnixTimeStamp</strong>: <code>1733333335</code>
* <strong>Nonce</strong>: <code>0</code>
* <strong>nBits</strong>: <code>0x207fffff</code>
* <strong>Merkel</strong>: <code>96908dea6891a3cc8751ed962736bbc1f4129c5c2fa7f44333def15ce86c4388</code>
* <strong>Genesis</strong>: <code>65ea097e012bad431eb912fc43abcc7c809d648a85cda433e73a0a9f9409a127</code>

Now we have are parameters, we can start creating are own coin, but first lets change some file names to match the name of are coin.

## Source we are forking from Bitcoin 0.14.3
https://bitcoincore.org/bin/bitcoin-core-0.14.3/
### Home Directory
<code>cd ~</code>
### Download bitcoin 0.14.3
* https://bitcoincore.org/bin/bitcoin-core-0.14.3/
<code>wget https://bitcoincore.org/bin/bitcoin-core-0.14.3/bitcoin-0.14.3.tar.gz</code>
* sha256sum bitcoin-0.14.3.tar.gz <code>416717ab5ef94f8458da2b12e4cd742ca08f5ad3817b65fc73811e06ac949f87</code>

### extract
<code>tar xvf bitcoin-0.14.3.tar.gz</code>

### Change Directory Name to new/forked coin name
<code>mv bitcoin-0.14.3 N33Bcoin</code>

<code>cd N33Bcoin</code>
* Current work director path is <code>/home/$USER/N33Bcoin/</code>

## Renaming

### Renaming Bitcoin to N33Bcoin
<strong>Run these command in the /home/$USER/N33Bcoin/ Directory</strong>
* Lowercase
<code>find . -type f -exec sed -i 's/bitcoin/n33bcoin/g' {} + </code>
* UpperCase
<code>find . -type f -exec sed -i 's/Bitcoin/N33Bcoin/g' {} + </code>
* Name.1
<code>find . -type f -exec sed -i -e 's/bitcoin/noobcoin/g' -e 's/bitcoind\.1/n33bcoind.1/g' {} + </code>

### Change Name for Docs

To rename files in a directory (e.g., <code>/home/$USER/N33B/N33Bcoin/doc/man/</code>):

* <strong>Before:</strong>
<pre>
  bitcoin-cli.1  bitcoind.1  bitcoin-qt.1  bitcoin-tx.1  Makefile.am
</pre>

* <strong>After:</strong>
<pre>
  n33bcoin-cli.1  n33bcoind.1  n33bcoin-qt.1  n33bcoin-tx.1  Makefile.am
</pre>

* <strong>Manual Way:</strong>
<pre>
mv -v bitcoin-cli.1 n33bcoin-cli.1
</pre>

* <strong>Using mv with a for Loop:</strong>
<code>cd /home/$USER/N33B/N33Bcoin/doc/man</code><br>
<code>for file in bitcoin*; do mv -v "$file" "${file/bitcoin/n33bcoin}"; done</code>
</pre>
* <code>-v</code> shows each rename action.

### Change Names for Files

Unlike forking litecoin, the method we just used to rename all bitcoin words to n33bcoin created some problems, unlike litecoin 0.14.2, the word 'bitcoin' can be found in a lot of file names.

Example: the file <code>libbitcoinconsensus.pc.in</code> is still called <code>libbitcoinconsensus.pc.in</code> but inside make and config files, it is now know as <code>libn33bcoinconsensus.pc.in</code> so it will look for a file called <code>libn33bcoinconsensus.pc.in</code> and not <code>libbitcoinconsensus.pc.in</code>, still will lead to a lot of breakages.

* Easy Fix: Change all file names which include the word <code>bitcoin</code> to <code>n33bcoin</code>

* install <code>rename</code>
<code>sudo apt install rename</code>
* Run commands in <code>/home/$USER/N33Bcoin/</code> Directory
* See all file which contain the name <code>bitcoin</code>
<code>find . -type f -name "*bitcoin*"</code>

* Rename/convert all <code>bitcoin</code> in file names to <code>n33bcoin</code>
<code>find . -type f -name "*bitcoin*" -exec rename 's/bitcoin/n33bcoin/' {} +</code>

## Editing Files

Are Files are located in path:<code>/home/$USER/N33B/N33Bcoin</code><br>
Example: <code>src/amount.h</code> full path would be <code>/home/$USER/N33B/N33Bcoin/src/amount.h</code> 

### OverView of Files to edit
* Comment Out <code>** Lines: 74 - 77 Comment Out</code>
These are Lines we Don't need, but are not deleting just commenting out, so line numbers remain the same.  <br>
Comment out by placing a <code>//</code> at the beginning of the line.

* <strong>src/amount.h</strong>  <br>
** Line 31: Edit Max Coins

* <strong>src/validation.cpp</strong>  <br>
** Line 1166: This BLOCK of code will contain premined and Block rewards

* <strong>src/qt/bitcoinunits.cpp</strong>  <br>
** Line 39 Block: change coin symbol LTC to N33B
* <strong>src/chainparams.cpp<strong>  <br>
** Line 53: '''Global''' Change Time Stamp Message  <br>
** Line 54: '''Global''' Change Pub Key  <br>
** Line 73: '''MainNet''' Change Halving Interval  <br>
** Line 74: '''MainNet''' BIP34Height  <br>
** Line 75: '''MainNet''' BIP34Hash  <br> 
** Line 76: '''MainNet''' BIP65Height  <br>
** Line 77: '''MainNet''' BIP66Height  <br>
** Lines 85 - 103: '''MainNet''' Deployment and Chain Work Section  <br>
** Line 110: '''MainNet''' Change Magic Bytes - Script included  <br>
** Line 114: '''MainNet''' Change Main Net Default Port  <br>
** Line 117: '''MainNet''' Change Main Net Nonce TimeStamp Coin_Rewards  <br>
** Line 119: '''MainNet''' Change Genesis Hash  <br>
** Line 120: '''MainNet''' Change Merkel Hash  <br>
** Line 144: '''MainNet'''Change Coin Number and Genesis Hash  <br>
** Lines 145 - 156 Comment Out  <br>
** Line 161: '''MainNet''' Change Time Stamp  <br>
** Line 162: '''MainNet''' Change Number Of Transa ctions  <br>
** Line 177: '''TestNet''' Halving Interval  <br>
** Line 178: '''TestNet''' BIP34Height  <br>
** Line 179: '''TestNet''' BIP34Hash  <br>
** Line 180: '''TestNet''' BIP65Height  <br>
** Line 181: '''TestNet''' BIP66Height  <br>
** Line 184: '''TestNet''' Block Times  <br>
** Lines 189 - 207: '''TestNet''' Deployment Section  <br>
** Line 213: '''TestNet''' Default Port  <br>
** Line 216: '''TestNet''' Time Stamp and Nonce  <br>
** Line 218: '''TestNet''' Genesis Hash Block  <br>
** Line 219: '''TestNet''' Merkel Hash Block  <br>
** Line 245: '''TestNet''' CheckPointData Genesis Hash Block Number  <br>
** Line 250: '''TestNet''' Time Stamp  <br>
** Line 251: '''TestNet''' Block Number  <br>
** Lines 267 - 270 '''RegressionNet''' BIP Consensus  <br>
** Line 301: '''RegressionNet''' Default Port  <br>
** Line 304: '''RegressionNet''' Time Stamp Nonce Coin_Rewards  <br>
** Line 306: '''RegressionNet''' Genesis Block Hash  <br>
** Line 307: '''RegressionNet''' Merkel Hash  <br>
** Line 319: '''RegressionNet''' Genesis Hash  <br>
* <strong>src/chainparamsbase.cpp</strong>  <br>
** Line 35: MainNet RCP Port  <br>
** Line 48: TestNet RPC Port  <br>
** Line 62: Regession Net RPC Port  <br>

### src/amount.h

On line 31 we will edit are Max coins:
<pre>
static const CAmount MAX_MONEY = 21000000 * COIN;
</pre>

will change this to 33,333,333 coins

<pre>
static const CAmount MAX_MONEY = 33333333 * COIN;
</pre>

### src/validation.cpp

Path <code>/home/$USER/N33B/N33Bcoin/src/validation.cpp</code>

The block of code we are looking for starts on line 1166:
<pre>
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
    int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
    // Force block reward to zero when right shift is undefined.
    if (halvings >= 64)
        return 0;

    CAmount nSubsidy = 50 * COIN;
    // Subsidy is cut in half every 210,000 blocks which will occur approximately every 4 years.
    nSubsidy >>= halvings;
    return nSubsidy;
}
</pre>


On line 1173 you should see this line:
<pre>
    CAmount nSubsidy = 50 * COIN;
</pre>

This is the rewards for mining coins, the default is 50, we are changinf rewards to 333 coins per block mined.

<pre>
    CAmount nSubsidy = 333 * COIN;
</pre>

#### Premined coins

We also need to add a contidtion for are premined coins - in the first block will mine 33%, thats 11,111,111 coins

<pre>
CAmount GetBlockSubsidy(int nHeight, const Consensus::Params& consensusParams)
{
    int halvings = nHeight / consensusParams.nSubsidyHalvingInterval;
    // Force block reward to zero when right shift is undefined.
    if (halvings >= 64)
        return 0;
    CAmount nSubsidy;
    if (nHeight == 1)
            nSubsidy = 11111111 * COIN;
    else
        nSubsidy = 333 * COIN;
    // Subsidy is cut in half every 33,333 blocks which will occur approximately every 231 days. 
    nSubsidy >>= halvings;
    return nSubsidy;
}
</pre>

This condition means IF first block reward 11,111,111 coins, Else(after first blocked mined) rewards per block are 333 coins.

### src/qt/n33bcoinunits.cpp
* Line 39: Code Block
<pre>
QString N33BcoinUnits::name(int unit)
{
    switch(unit)
    {
    case BTC: return QString("BTC");
    case mBTC: return QString("mBTC");
    case uBTC: return QString::fromUtf8("μBTC");
    default: return QString("???");
    }
}
</pre>

* Change BTC your coin symbol to N33B

<pre>
QString N33BcoinUnits::name(int unit)
{
    switch(unit)
    {
    case BTC: return QString("N33B");
    case mBTC: return QString("mN33B");
    case uBTC: return QString::fromUtf8("μN33B");
    default: return QString("???");
    }
}
</pre>

### src/chainparams.cpp

#### Line 53 Change Time Stamp Message

<code>     const char* pszTimestamp = "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks";</code>

To

<code>     const char* pszTimestamp = "N33B's for Noob's at CompleteNoobs.com";</code>

#### Line 54 Change Genesis Pub Key

<code> 54     const CScript genesisOutputScript = CScript() << ParseHex("04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f") << OP_CHECKSIG;
</code>

We are going to change to the public key we used to create are genesis block.

<code>     const CScript genesisOutputScript = CScript() << ParseHex("049bd17782313a0263154a37b7adb5f773e3a95e08eba879d6a8f1c9e614e41b33f85129d0f9820a464d2ae136abaa4144d258df6729dfd7c6a18498148b59fadf") << OP_CHECKSIG;</code>

#### Line 73 HalvingInterval

<code>         consensus.nSubsidyHalvingInterval = 210000;</code>

Block intervals of bitcoin is every 10 mins, as you can see on '''[[#Line 80 Target Block Creation''']] 

* 60 mins per hour x 24 hours per day = 1440 mins a day
* 1440 mins at one block each 10 mins =  144 block per day ish
* 144 * 365 = 52,560 blocks per year ish
* 52,560 * 4 = 210,240 blocks every four years ish
So bitcoin halves its rewards every 4 years ish as it passes 210,000 blocks and carrys on halving every 210,000 blocks later.

We reward 333 coins per block and will be out of coins around 667,334 blocks.
* Preminded 11,111,111 coins
* 22,222,222 left
* at 333 per block all will be gone in 66,733 blocks time unless we halve before then
* We are going to keep are block time of 10 mins and have a halving at 33,333 blocks so it will halve around 231 days
<code>         consensus.nSubsidyHalvingInterval = 33333;</code>

#### Line 74 - 77 MainNet BIP Section

<pre>
 74         consensus.BIP34Height = 227931;
 75         consensus.BIP34Hash = uint256S("0x000000000000024b89b42a942fe0d9fea3bb44ab7bd1b19115dd6a759c0808b8");
 76         consensus.BIP65Height = 388381; // 000000000000000004c2b624ed5d7756c508d90fd0da2c7c679febfa6c4735f0
 77         consensus.BIP66Height = 363725; // 00000000000000000379eaa19dce8c9b722d46ae6a57c2f1a988119488b50931
</pre>
* Set BIP34/65/66 to 0 for new chain—modern rules from genesis. Adjust BIP34 to 100 if mining fails.
* Replace with your Hash on line 75 BIPHash
<pre>
74         consensus.BIP34Height = 0;
75         consensus.BIP34Hash = uint256S("0x0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4");
76         consensus.BIP65Height = 0;
77         consensus.BIP66Height = 0;
</pre>

#### Line 85 - 103 '''MainNet''' Deployment and Chain Work Section 
##### Line 86 
Default:  <br> <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 1199145601; // January 1, 2008</code>
* Reason changed: Bitcoin’s 2008 start date is irrelevant—set to 0 for immediate activation on new chain.
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 0;</code>

##### Line 87 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 1230767999; // December 31, 2008</code>
* Reason changed: 2008 timeout disables it—set to far future so test deployment never expires.
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 9999999999;</code>

##### Line 91 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nStartTime = 1462060800; // May 1st, 2016</code>
* Reason changed: Bitcoin’s 2016 start is moot—set to 0 for CSV active from genesis.
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nStartTime = 0;</code>

##### Line 92 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nTimeout = 1493596800; // May 1st, 2017</code>
* Reason changed: 2017 timeout disables it—set to far future so CSV stays active.
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nTimeout = 9999999999;</code>

##### Line 96 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 1479168000; // November 15th, 2016</code>
* Reason changed: Bitcoin’s 2016 start doesn’t apply—set to 0 for SegWit from genesis.
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 0;</code>

##### Line 97 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 1510704000; // November 15th, 2017</code>
* Reason changed: 2017 timeout disables it—set to far future so SegWit stays active.
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 9999999999;</code>

##### Line 100 
Default: <code>consensus.nMinimumChainWork = uint256S("0x0000000000000000000000000000000000000000003f94d1ad391682fe038bf5");</code>
* Reason changed: Bitcoin’s 2017 work is massive—set to 0 for a new chain with no work yet.
Changed: <code>consensus.nMinimumChainWork = uint256S("0x00");</code>

##### Line 103 
Default: <code>consensus.defaultAssumeValid = uint256S("0x00000000000000000013176bf8d7dfeab4e1db31dc93bc311b436e82ab226b90"); //453354</code>
* Reason changed: Bitcoin’s block 453354 is irrelevant—set to N33Bcoin’s genesis hash for fast sync from block 0.
Changed: <code>consensus.defaultAssumeValid = uint256S("0x0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4");</code>

###### Before and After Changes


<pre>
85         consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].bit = 28;
86         consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 1199145601; // January 1, 2008
87         consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 1230767999; // December 31, 2008
89         // Deployment of BIP68, BIP112, and BIP113.
90         consensus.vDeployments[Consensus::DEPLOYMENT_CSV].bit = 0;
91         consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nStartTime = 1462060800; // May 1st, 2016
92         consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nTimeout = 1493596800; // May 1st, 2017
94         // Deployment of SegWit (BIP141, BIP143, and BIP147)
95         consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].bit = 1;
96         consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 1479168000; // November 15th, 2016
97         consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 1510704000; // November 15th, 2017
99         // The best chain should have at least this much work.
100         consensus.nMinimumChainWork = uint256S("0x0000000000000000000000000000000000000000003f94d1ad391682fe038bf5");
102         // By default assume that the signatures in ancestors of this block are valid.
103         consensus.defaultAssumeValid = uint256S("0x00000000000000000013176bf8d7dfeab4e1db31dc93bc311b436e82ab226b90"); //453354
</pre>
* Set CSV/SegWit to active from genesis (nStartTime = 0, nTimeout = far future). Reset chain work to minimal. Set assume valid to genesis hash.
<pre>
85         consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].bit = 28;
86         consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 0;
87         consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 9999999999;
89         // Deployment of BIP68, BIP112, and BIP113.
90         consensus.vDeployments[Consensus::DEPLOYMENT_CSV].bit = 0;
91         consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nStartTime = 0;
92         consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nTimeout = 9999999999;
94         // Deployment of SegWit (BIP141, BIP143, and BIP147)
95         consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].bit = 1;
96         consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 0;
97         consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 9999999999;
99         // The best chain should have at least this much work.
100         consensus.nMinimumChainWork = uint256S("0x00");
102         // By default assume that the signatures in ancestors of this block are valid.
103         consensus.defaultAssumeValid = uint256S("0x0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4");
</pre>


#### Line 110 Magic Bytes

* [Link to Hex numbers explaned](https://www.completenoobs.com/noobs/Hex_numbers_explained) 
* [Link to python script for random values](https://www.completenoobs.com/noobs/Python3_Script_for_Random_Magic_Bytes)

The pchMessageStart array is a crucial component in cryptocurrency network protocols, often referred to as the "magic bytes" or "network magic." It serves as a unique identifier for a specific cryptocurrency network.

These values are in hexadecimal format, representing four bytes that form a sequence unlikely to occur in normal data.

If you're creating a new cryptocurrency by forking Bitcoin, you should change these values.

Using unique values prevents your new coin's network from interfering with Bitcoin's network or other existing networks.

<pre>
110         pchMessageStart[0] = 0xf9;
111         pchMessageStart[1] = 0xbe;
112         pchMessageStart[2] = 0xb4;
113         pchMessageStart[3] = 0xd9;
</pre>

* Gonna change mine to 
<pre>
pchMessageStart[0] = 0xfe;
pchMessageStart[1] = 0x93;
pchMessageStart[2] = 0xd2;
pchMessageStart[3] = 0xe2;
</pre>

#### Line 114 Change Main Net Default Port

* Line 114  <br>
<code>nDefaultPort = 8333;</code>
* Changing to port 3333  <br>
<code>nDefaultPort = 3333;</code>

#### Line 117 Change Main Net Nonce TimeStamp Coin_Rewards
* Original  <br>
<code>         genesis = CreateGenesisBlock(1231006505, 2083236893, 0x1d00ffff, 1, 50 * COIN);</code>
* Syntax of line 117  <br>
<code>genesis = CreateGenesisBlock(<UNIX_TIME_STAMP>, <NONCE>, <DIFF_BITS>, <NHEIGHT>, <AMOUNT_OF_COINS_REWARD> * COIN);</code>  <br>
* we are just going to append/change are UnixTimeStamp, Nonce and CoinReward
<code>         genesis = CreateGenesisBlock(1733333333, 221118658, 0x1d00ffff, 1, 333 * COIN);</code>

#### Line 119 Change Genesis Hash

<code>assert(consensus.hashGenesisBlock == uint256S("0x000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"));</code>  <br>
* Change to your genesis hash for Main Net  <br>
<code>         assert(consensus.hashGenesisBlock == uint256S("0x0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4"));</code>

#### Line 120 Change Merkel Hash

<code>         assert(genesis.hashMerkleRoot == uint256S("0x4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"));</code>   <br>
* Change to your merkel hsh for Main net   <br>
<code>         assert(genesis.hashMerkleRoot == uint256S("0x96908dea6891a3cc8751ed962736bbc1f4129c5c2fa7f44333def15ce86c4388"));</code>

#### Check Point - Lines 142 - 157 

<pre>
142         checkpointData = (CCheckpointData) {
143             boost::assign::map_list_of
144             ( 11111, uint256S("0x0000000069e244f73d78e8fd29ba2fd2ed618bd6fa2ee92559f542fdb26e7c1d"))
145             ( 33333, uint256S("0x000000002dd5588a74784eaa7ab0507a18ad16a236e7b1ce69f00d7ddfb5d0a6"))
146             ( 74000, uint256S("0x0000000000573993a3c9e41ce34471c079dcf5f52a0e824a81e7f953b8661a20"))
147             (105000, uint256S("0x00000000000291ce28027faea320c8d2b054b2e0fe44a773f3eefb151d6bdc97"))
148             (134444, uint256S("0x00000000000005b12ffd4cd315cd34ffd4a594f430ac814c91184a0d42d2b0fe"))
149             (168000, uint256S("0x000000000000099e61ea72015e79632f216fe6cb33d7899acb35b75c8303b763"))
150             (193000, uint256S("0x000000000000059f452a5f7340de6682a977387c17010ff6e6c3bd83ca8b1317"))
151             (210000, uint256S("0x000000000000048b95347e83192f69cf0366076336c639f9b7228e9ba171342e"))
152             (216116, uint256S("0x00000000000001b4f4b433e81ee46494af945cf96014816a4e2370f11b23df4e"))
153             (225430, uint256S("0x00000000000001c108384350f74090433e7fcf79a606b8e797f065b130575932"))
154             (250000, uint256S("0x000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214"))
155             (279000, uint256S("0x0000000000000001ae8c72a0b0c301f67e3afca10e819efa9041e458e9bd7e40"))
156             (295000, uint256S("0x00000000000000004d9b4ef50f0f9d686fd69db2e03af35a100370c64632a983"))
157         };

</pre>

These lines contain a blocknumber and there hash value, we are starting a new coin and these have no value to us.

We have one genesis block.

<code>             ( 11111, uint256S("0x0000000069e244f73d78e8fd29ba2fd2ed618bd6fa2ee92559f542fdb26e7c1d"))</code>   <br>
* We are going to append/change line 144, to block zero and are Main net genesis block hash.   <br>
<code>             ( 0, uint256S("0x0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4"))</code>

and comment out the remaining lines in this code block. lines 145 - 156

<pre>
142         checkpointData = (CCheckpointData) {
143             boost::assign::map_list_of
144             ( 0, uint256S("0x0000000091635cd5cc6736960f1fb22d91475b7835a55793bd034342be5ed2c4"))
145 //            ( 33333, uint256S("0x000000002dd5588a74784eaa7ab0507a18ad16a236e7b1ce69f00d7ddfb5d0a6"))
146 //            ( 74000, uint256S("0x0000000000573993a3c9e41ce34471c079dcf5f52a0e824a81e7f953b8661a20"))
147 //            (105000, uint256S("0x00000000000291ce28027faea320c8d2b054b2e0fe44a773f3eefb151d6bdc97"))
148 //            (134444, uint256S("0x00000000000005b12ffd4cd315cd34ffd4a594f430ac814c91184a0d42d2b0fe"))
149 //            (168000, uint256S("0x000000000000099e61ea72015e79632f216fe6cb33d7899acb35b75c8303b763"))
150 //            (193000, uint256S("0x000000000000059f452a5f7340de6682a977387c17010ff6e6c3bd83ca8b1317"))
151 //            (210000, uint256S("0x000000000000048b95347e83192f69cf0366076336c639f9b7228e9ba171342e"))
152 //            (216116, uint256S("0x00000000000001b4f4b433e81ee46494af945cf96014816a4e2370f11b23df4e"))
153 //            (225430, uint256S("0x00000000000001c108384350f74090433e7fcf79a606b8e797f065b130575932"))
154 //            (250000, uint256S("0x000000000000003887df1f29024b06fc2200b55f8af8f35453d7be294df2d214"))
155 //            (279000, uint256S("0x0000000000000001ae8c72a0b0c301f67e3afca10e819efa9041e458e9bd7e40"))
156 //            (295000, uint256S("0x00000000000000004d9b4ef50f0f9d686fd69db2e03af35a100370c64632a983"))
157         };

</pre>

#### Line 161 Change Time Stamp

<pre>
161             1483472411, // * UNIX timestamp of last known number of transactions
</pre>

* Change to the time stamp we are using

<pre>            1733333333, // * UNIX timestamp of last known number of transactions</pre>

#### Line 162 Change Number Of Transactions

<pre>            184495391,  // * total number of transactions between genesis and that timestamp</pre>

* Change to Zero

<pre>            0,  // * total number of transactions between genesis and that timestamp</pre>

#### TestNet Halving Interval

<code>177         consensus.nSubsidyHalvingInterval = 210000;</code>   <br>
* Change to same as are main net   <br>
<code>         consensus.nSubsidyHalvingInterval = 33333;</code>


#### Lines 178 - 181 TestNet BIP section

<pre>
178         consensus.BIP34Height = 21111;
179         consensus.BIP34Hash = uint256S("0x0000000023b3a96d3484e5abb3755c413e7d41500f8e2a5c3f0dd01299cd8ef8");
180         consensus.BIP65Height = 581885; // 00000000007f6655f22f98e72ed80d8b06dc761d5da09df0fa1dc4be4f861eb6
181         consensus.BIP66Height = 330776; // 000000002104c8c45e99a8853285a3b592602a3ccde2b832481da85e9e4ba182
</pre>

* Change values to zero and replace TestNet Genesis Hash

<pre>
178         consensus.BIP34Height = 0;
179         consensus.BIP34Hash = uint256S("0x000001b7cbb2e5ae084fdd6934c9962fd8ff27cb7c27e02e415d2da6fe214a8c");
180         consensus.BIP65Height = 0;
181         consensus.BIP66Height = 0; 
</pre>

#### Lines 189 - 207 TestNet Deployment Section 

##### Line 190 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 1199145601; // January 1, 2008</code>  <br>
* Reason changed: Bitcoin’s 2008 start is irrelevant—set to 0 for immediate activation on TestNet.  <br>
Changed:  <br> <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 0;</code>

##### Line 191 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 1230767999; // December 31, 2008</code>  <br>
* Reason changed: 2008 timeout disables it—set to far future so test deployment never expires.  <br>
Changed:   <br><code>consensus.vDeployments[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 9999999999;</code>

##### Line 195 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nStartTime = 1456790400; // March 1st, 2016</code>  <br>
* Reason changed: Litecoin’s 2016 start doesn’t apply—set to 0 for CSV from genesis.  <br>
Changed:  <br> <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nStartTime = 0;</code>

##### Line 196 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nTimeout = 1493596800; // May 1st, 2017</code>  <br>
* Reason changed: 2017 timeout disables it—set to far future so CSV stays active.  <br>
Changed:  <br> <code>consensus.vDeployments[Consensus::DEPLOYMENT_CSV].nTimeout = 9999999999;</code>

##### Line 200 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 1462060800; // May 1st 2016</code>  <br>
* Reason changed: Litecoin’s 2016 start doesn’t apply—set to 0 for SegWit from genesis.  <br>
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 0;</code>

##### Line 201 
Default: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 1493596800; // May 1st 2017</code>  <br>
* Reason changed: 2017 timeout disables it—set to far future so SegWit stays active.  <br>
Changed: <code>consensus.vDeployments[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 9999999999;</code>

##### Line 204 
Default: <code>consensus.nMinimumChainWork = uint256S("0x00000000000000000000000000000000000000000000001f057509eba81aed91");</code>  <br>
* Reason changed: Litecoin’s work is irrelevant—set to 0 for a new TestNet chain.  <br>
Changed: <code>consensus.nMinimumChainWork = uint256S("0x00");</code>

##### Line 207 
Default: <code>consensus.defaultAssumeValid = uint256S("0x00000000000128796ee387cf110ccb9d2f36cffaf7f73079c995377c65ac0dcc"); //1079274</code>  <br>
* Reason changed: Litecoin’s block 1079274 doesn’t apply—set to TestNet genesis for fast sync.  <br>
Changed: <code>consensus.defaultAssumeValid = uint256S("0x000001b7cbb2e5ae084fdd6934c9962fd8ff27cb7c27e02e415d2da6fe214a8c");</code>

#### TestNet Default Port - Line 213

<code>213         nDefaultPort = 18333;</code>  <br>
* Change to another port , picking 13333  <br>
<code>nDefaultPort = 13333;</code>

#### Line 216: TestNet Time Stamp and Nonce

<code>216         genesis = CreateGenesisBlock(1296688602, 414098458, 0x1d00ffff, 1, 50 * COIN);</code>  <br>
* change/append timestamp, nonce and coin rewards - TimeStamp, Nonce, nBits and CoinRewards from your Test Net   <br>
<code>         genesis = CreateGenesisBlock(1733333334, 511144, 0x1e0ffff0, 1, 333 * COIN);</code>

#### Line 218: TestNet Genesis Hash Block

<code>218         assert(consensus.hashGenesisBlock == uint256S("0x000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943"));</code>  <br>
* Changed to   <br>
<code>218         assert(consensus.hashGenesisBlock == uint256S("0x000001b7cbb2e5ae084fdd6934c9962fd8ff27cb7c27e02e415d2da6fe214a8c"));</code>

#### Line 219: TestNet Merkel Hash Block

<code>219         assert(genesis.hashMerkleRoot == uint256S("0x4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"));</code>  <br>
* Changed to   <br>
<code>         assert(consensus.hashGenesisBlock == uint256S("0x96908dea6891a3cc8751ed962736bbc1f4129c5c2fa7f44333def15ce86c4388"));</code>

#### Line 245 TestNet checkpointData 
Default: <code>( 546, uint256S("000000002a936ca763904c3c35fce2f3556c559c0214345d31b1bcebf76acb70")),</code>  <br>
* Reason changed: Bitcoin TestNet checkpoint irrelevant—set to height 0 with N33Bcoin TestNet genesis hash for new chain.  <br>
Changed: <code>( 0, uint256S("000001b7cbb2e5ae084fdd6934c9962fd8ff27cb7c27e02e415d2da6fe214a8c")),</code>  <br>
* Note: Removed "0x" from hash string—matches Bitcoin style, prevents parsing error in uint256S.

#### Line 250 - Testnet chainTxData TimeStamp

<code>             1483546230,</code>

* Change to your timestamp  <br>
<code>1733333334,</code>

#### Line 251 - Testnet chainTxData block count

<code>251             12834668,</code>  <br>
* change block count to zero  <br>
<code>             0,</code>

#### RegTest BIP Section 

##### Line 267 
Default: <code>consensus.BIP34Height = 100000000; // BIP34 has not activated on regtest (far in the future so block v1 are not rejected in tests)</code>  <br>
* Reason changed: Delays BIP34—set to 0 for modern rules from genesis, consistent with MainNet/TestNet.  <br>
Changed: <code>consensus.BIP34Height = 0;</code>

##### Line 268 
Default: <code>consensus.BIP34Hash = uint256();</code>  <br>
* Reason changed: Empty hash irrelevant—set to RegTest genesis for BIP34 activation at block 0.  <br>
* NOTE: the <code>S</code> at the end of <code>uint256S</code> append the '''S''', remove the <code>0x</code> or it would be too long and make sure RegNet Hash is wrapped in "comment-hash".  <br>
* The quotes <code>""</code> tell the compiler that this is a string, not a number.  <br>
* '''uint256S''' will parse the string as a hexadecimal value and construct the '''uint256''' object accordingly.  <br>
Changed: <code>consensus.BIP34Hash = uint256S("65ea097e012bad431eb912fc43abcc7c809d648a85cda433e73a0a9f9409a127");</code>

##### Line 269 
Default: <code>consensus.BIP65Height = 1351; // BIP65 activated on regtest (Used in rpc activation tests)</code>  <br>
* Reason changed: Bitcoin’s test height—set to 0 for BIP65 from genesis, matches MainNet/TestNet.  <br>
Changed: <code>consensus.BIP65Height = 0;</code>

##### Line 270 
Default: <code>consensus.BIP66Height = 1251; // BIP66 activated on regtest (Used in rpc activation tests)</code>  <br>
* Reason changed: Bitcoin’s test height—set to 0 for BIP66 from genesis, matches MainNet/TestNet.  <br>
Changed: <code>consensus.BIP66Height = 0;</code>

#### Line 298: RegressionNet Default Port

<code>         nDefaultPort = 18444;</code>  <br>
* change port number   <br>
<code>         nDefaultPort = 13337;</code>

#### Line 301 RegressionNet Time Stamp Nonce Coin_Rewards 

<code>301         genesis = CreateGenesisBlock(1296688602, 2, 0x207fffff, 1, 50 * COIN);</code>

* Change to your timestamp , nonce and coin rewards

<code>         genesis = CreateGenesisBlock(1733333335, 0, 0x207fffff, 1, 333 * COIN);</code>

#### Line 303: RegressionNet Genesis Block Hash

<code>303         assert(consensus.hashGenesisBlock == uint256S("0x0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206"));</code>  <br>
* replace with your reg net genesis hash  <br>
<code>         assert(consensus.hashGenesisBlock == uint256S("0x65ea097e012bad431eb912fc43abcc7c809d648a85cda433e73a0a9f9409a127"));</code>

#### Line 304 RegressionNet Merkel Hash

<code>304         assert(genesis.hashMerkleRoot == uint256S("0x4a5e1e4baab89f3a32518a88c31bc87f618f76673e2cc77ab2127b7afdeda33b"));</code>  <br>
* replace with your reg net merkel hash  <br>
<code>         assert(genesis.hashMerkleRoot == uint256S("0x96908dea6891a3cc8751ed962736bbc1f4129c5c2fa7f44333def15ce86c4388"));</code>

#### Line 316: RegressionNet Genesis Hash
<code>316             ( 0, uint256S("0f9188f13cb7b2c71f2a335e3a4fc328bf5beb436012afca590b1a11466e2206"))</code>  <br>
* change to your reg nets genesis hash  <br>
<code>            ( 0, uint256S("0x65ea097e012bad431eb912fc43abcc7c809d648a85cda433e73a0a9f9409a127"))</code>


#### line 35 - Main net RCP port

<pre>
        nRPCPort = 8332;
</pre>

RPC port is used to connect to coin api, its used to create a web wallet and moblie wallet.

<pre>
        nRPCPort = 3366;
</pre>

#### Line 48 - test net RPC port

<pre>
        nRPCPort = 18332;
</pre>

Changing to 12333

<pre>
        nRPCPort = 12333;
</pre>

#### line 62 - regession net RPC port

<pre>
        nRPCPort = 18332;
</pre>

Changing to 12345

<pre>
        nRPCPort = 12345;
</pre>

* We are pretty much done with customizing the code base, we just need an IP address to append to chainparams.cpp and we are good to go.

### src/chainparamsseeds.h

* Delete content of <code>src/chainparamsseeds.h</code> and replace with just:   <br>
<pre>
#ifndef BITCOIN_CHAINPARAMSSEEDS_H
#define BITCOIN_CHAINPARAMSSEEDS_H
static SeedSpec6 pnSeed6_main[] = {};
static SeedSpec6 pnSeed6_test[] = {};
#endif // BITCOIN_CHAINPARAMSSEEDS_H
</pre>

The <code>chainparamsseeds.h</code> file contains hardcoded seed nodes for the main network (pnSeed6_main), which are currently set to Bitcoin’s seed nodes (e.g., IPs like 2.7.8.12 on port 8333). These seeds will cause your node to attempt connections to Bitcoin peers, which isn’t what we want for N33Bcoin.
* By modifying the seed arrays for both mainnet and testnet to empty, we can keep the file structure intact while removing the Bitcoin seed nodes,  preventing are node from trying to connect to them.


## Container and VPS Setup 

Most VPS providers frown on mining unless it’s their explicit service, fair enough, it hogs resources! To work around this, we’ll:
* Spin up an Ubuntu 18.04 container locally (18.04 keeps coin building simple).
* Pair it with a low-cost VPS running Ubuntu 24.04, tunneling all traffic from the container to the VPS’s public IP.
This setup gives us:
* A public-facing IP without poking holes in our home router.
* Local mining control, keeping private keys secure—because a VPS is just someone else’s machine, and we don’t trust it with our keys!

### LXD Quick Container Setup

The rest of this tut is on [completenoobs.com - the downloadable wiki](https://www.completenoobs.com/noobs/N33Bcoin)
