# coding: utf-8

from __future__     import division

from .              import AnAbstractBuilding
from .warehouse     import AWarehouse

from code_constants import PRECISION
from game_constants import SPECIALIZATIONS, FACTORY

class AFactory( AnAbstractBuilding ):
    """docstring for AFactory"""
    __slots__ = (
        "__specialization",
        "__tech_level", "__prod_level",
        "__productivity", "__efficiency", "__product_price",
        "__storage",
    )
    def __init__( self, specialization, **kwargs ):
        super( AFactory, self ).__init__( **kwargs )
        assert specialization in SPECIALIZATIONS.itervalues()
        self.__specialization   = specialization

        self.__tech_level       = FACTORY[ "DEFAULT_TECH_LEVEL" ]
        self.__prod_level       = FACTORY[ "DEFAULT_PROD_LEVEL" ]

        self.__productivity     = FACTORY[ "DEFAULT_PRODUCTIVITY" ]
        self.__efficiency       = FACTORY[ "DEFAULT_EFFICIENCY" ]
        self.__product_price    = FACTORY[ "PRODUCT_PRICE" ] # per one piece of production
        
        self.__storage          = AWarehouse( specialization=self.__specialization, capacity=FACTORY[ "DEFAULT_STORAGE_CAPACITY" ] )

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

    @property
    def amount( self ):
        return self.__storage.amount

    @property 
    def capacity( self ):
        return self.__storage.capacity

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
        self.__storage.PutItems( items_level=self.__prod_level, number_of_items=production )
        return round( production * self.__product_price, PRECISION )

    def TakeProduction( self, prod_level=0, number_of_items=0, all_items=False ):
        prod_level      = int( prod_level )
        number_of_items = int( number_of_items )
        all_items       = bool( all_items )
        return self.__storage.TakeItems( items_level=prod_level, number_of_items=number_of_items, all_items=all_items )
