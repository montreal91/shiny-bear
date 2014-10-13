# coding: utf-8

from __future__     import division

from .              import AnAbstractBuilding

from code_constants import PRECISION
from game_constants import SPECIALIZATIONS, FACTORY

class AFactory( AnAbstractBuilding ):
    """docstring for AFactory"""
    __slots__ = (
        "__specialization",
        "__tech_level", "__prod_level",
        "__productivity", "__efficiency", "__product_price",
        "__production",
    )
    def __init__( self, specialization ):
        super( AFactory, self ).__init__( complexity=25, cost=9000 )
        assert specialization in SPECIALIZATIONS.itervalues()
        self.__specialization   = specialization

        self.__tech_level       = FACTORY[ "DEFAULT_TECH_LEVEL" ]
        self.__prod_level       = FACTORY[ "DEFAULT_PROD_LEVEL" ]

        self.__productivity     = FACTORY[ "DEFAULT_PRODUCTIVITY" ]
        self.__efficiency       = FACTORY[ "DEFAULT_EFFICIENCY" ]
        self.__product_price    = FACTORY[ "PRODUCT_PRICE" ] # per one piece of production
        
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
    def product_price( self ):
        return self.__product_price

    def __UpdateProductPrice( self ):
        price = ( FACTORY[ "EXPONENT" ] ** ( self.__prod_level - FACTORY[ "DEFAULT_PROD_LEVEL" ] ) * FACTORY[ "PRICE_FACTOR" ] ) / self.__efficiency # ??? 
        self.__product_price = round( price , PRECISION )
    
    def UpgradeProductivity( self ):
        self.__productivity += FACTORY[ "PRODUCTIVITY_GROWTH_FACTOR" ]

    def UpgradeEfficiency( self ):
        self.__efficiency += FACTORY[ "EFFICIENCY_GROWTH_FACTOR" ]
        self.__UpdateProductPrice()

    def UpgradeTechLevel( self ):
        self.__tech_level   += FACTORY[ "TECH_LEVEL_GROWTH_FACTOR" ]
        self.__efficiency   = FACTORY[ "DEFAULT_EFFICIENCY" ]
        self.__productivity = FACTORY[ "DEFAULT_PRODUCTIVITY" ]

    def DowngradeTechLevel( self ):
        if self.__tech_level > FACTORY[ "DEFAULT_TECH_LEVEL" ]:
            self.__tech_level -= FACTORY[ "TECH_LEVEL_GROWTH_FACTOR" ]

    def SetProdLevel( self, level ):
        level = int( level )
        if level - self.__tech_level > 5: # ???
            self.__prod_level = self.__tech_level + 5 
        elif level < FACTORY[ "DEFAULT_PROD_LEVEL" ]:
            self.__prod_level = FACTORY[ "DEFAULT_PROD_LEVEL" ]
        else:
            self.__prod_level = level
        self.__UpdateProductPrice()

    def Produce( self ):
        production = int( self.__productivity * FACTORY[ "PRODUCTIVITY_FACTOR" ] )
        if self.__prod_level in self.__production:
            self.__production[ self.__prod_level ] += production
        else:
            self.__production[ self.__prod_level ] = production
        return round( production * self.__product_price, PRECISION )

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
