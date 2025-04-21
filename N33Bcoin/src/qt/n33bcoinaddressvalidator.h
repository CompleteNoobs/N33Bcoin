// Copyright (c) 2011-2014 The N33Bcoin Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef BITCOIN_QT_BITCOINADDRESSVALIDATOR_H
#define BITCOIN_QT_BITCOINADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class N33BcoinAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit N33BcoinAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

/** N33Bcoin address widget validator, checks for a valid n33bcoin address.
 */
class N33BcoinAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit N33BcoinAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

#endif // BITCOIN_QT_BITCOINADDRESSVALIDATOR_H
