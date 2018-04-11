# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 17:20:49 2018

@author: CX
"""

def DPchange(money,coins):
    MinNumCoins=[0]*(money+1)
    
    for m in range(1,money+1):
        MinNumCoins[m] = float('inf')
        for i in range(len(coins)):
            if m>=coins[i]:
                NumCoins = MinNumCoins[m-coins[i]]+1
                if NumCoins<MinNumCoins[m]:
                    MinNumCoins[m] = NumCoins
                    
    return MinNumCoins[money]


coins = [1,5,20,25]
money = 40
print(DPchange(money,coins))