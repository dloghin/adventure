#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: ./$0 <accounts file>"
    exit 1
fi

. ./.env

ACCOUNTS_FILE=$1
rm -f balances.txt
while read -r PKK; do
    ADDRESS=`python3 pk2addr.py "$PKK"`
    BALANCE=`cast balance "$ADDRESS" --rpc-url "$LOCAL_RPC_URL"`
    echo "$ADDRESS: $BALANCE" >> balances.txt
done < $ACCOUNTS_FILE