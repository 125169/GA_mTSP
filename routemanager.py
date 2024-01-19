# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 23:18:59 2024

@author: user
"""

from dustbin import *

class RouteManager:
    destinationDustbins = []

    @classmethod
    def addDustbin (cls, db):
        cls.destinationDustbins.append(db)

    @classmethod
    def getDustbin (cls, index):
        return cls.destinationDustbins[index]

    @classmethod
    def numberOfDustbins(cls):
        return len(cls.destinationDustbins)