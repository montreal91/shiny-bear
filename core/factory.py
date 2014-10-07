# coding: utf-8

from __future__     import division

from .              import AnAbstractBuilding
from code_constants import WEAPONS, ARMOURS

class AFactory( AnAbstractBuilding ):
    """docstring for AFactory"""
    __slots__ = (
        "__specialization",
        "__tech_level", "__prod_level",
        "__productivity", "__efficiency", "__cost",
        "__production",
    )
    def __init__( self, specialization ):
        super( AFactory, self ).__init__( complexity=25, cost=9000 )
        assert specialization == WEAPONS or specialization == ARMOURS
        self.__specialization   = specialization

        self.__tech_level       = 1
        self.__prod_level       = 1

        self.__productivity     = 1.0
        self.__efficiency       = 1
        self.__cost             = 100 # per one piece of production
        
        self.__production       = {}

    @property 
    def tech_level( self ):
        return self.__tech_level

    @property 
    def productivity( self ):
        return self.__productivity

    @property 
    def efficiency( self ):
        return self.__efficiency

    @property 
    def specialization( self ):
        return self.__specialization

    @property 
    def prod_level( self ):
        return self.__prod_level

    @property 
    def cost( self ):
        return self.__cost

    def __UpdateCost( self ):
        # 2, 1 and 100 are gameplay constants
        cost = ( 2 ** ( self.__prod_level - 1 ) * 100 ) / self.__efficiency # ??? 
        self.__cost = round( cost, 2 )
    
    def UpgradeProductivity( self ):
        self.__productivity += 0.1 #gp_const

    def UpgradeEfficiency( self ):
        self.__efficiency += 1 #gp_const
        self.__UpdateCost()

    def UpgradeTechLevel( self ):
        self.__tech_level   += 1 
        self.__efficiency   = 1
        self.__productivity = 1.0

    def DowngradeTechLevel( self ):
        if self.__tech_level > 1:
            self.__tech_level -= 1

    def SetProdLevel( self, level ):
        level = int( level )
        if level - self.__tech_level > 5: # 5 is a gameplay constant and questionable
            self.__prod_level = self.__tech_level + 5 
        elif level < 1:
            self.__prod_level = 1
        else:
            self.__prod_level = level
        self.__UpdateCost()

    def Produce( self ):
        production = int( self.__productivity * 100 ) # 100 is a gameplay constant
        if self.__prod_level in self.__production:
            self.__production[ self.__prod_level ] += production
        else:
            self.__production[ self.__prod_level ] = production
        return round( production * self.__cost, 2 )

    def GetProduction( self, prod_level, quantity ):
        prod_level  = int( prod_level )
        quantity    = int( quantity )
        if prod_level in self.__production:
            if quantity <= 0:
                return 0
            elif quantity > self.__production[ prod_level ]:
                amount = self.__production[ prod_level ]
                self.__production[ prod_level ] = 0
                return amount
            else:
                self.__production[ prod_level ] -= quantity
                return quantity
        else:
            return 0

    def PutProduction( self, prod_level, quantity ):
        assert prod_level > 0 and quantity > 0
        prod_level  = int( prod_level )
        quantity    = int( quantity )
        if prod_level in self.__production:
            self.__production[ prod_level ] += quantity
        else:
            self.__production[ prod_level ] = quantity
