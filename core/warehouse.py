# coding: utf-8

from .              import AnAbstractBuilding

from game_constants import SPECIALIZATIONS, WAREHOUSE

class AWarehouse( AnAbstractBuilding ):
    """docstring for AWarehouse"""
    __slots__ = ( "__storage", "__capacity", "__specialization" )
    def __init__( self, specialization=SPECIALIZATIONS[ "WEAPONS" ], capacity=100, **kwargs ):
        super( AWarehouse, self ).__init__( **kwargs )
        assert specialization in SPECIALIZATIONS.itervalues()

        self.__storage          = {}
        self.__capacity         = capacity
        self.__specialization   = specialization

    @property
    def capacity( self ):
        return self.__capacity

    @property
    def specialization( self ):
        return self.__specialization

    @property
    def amount( self ):
        return sum( self.__storage.itervalues() )

    def __Put( self, items_level, number_of_items ):
        if not items_level in self.__storage:
            self.__storage[items_level] = number_of_items
        else:
            self.__storage[items_level] += number_of_items

    def IncreaseCapacity( self ):
        self.__capacity += WAREHOUSE[ "CAPACITY_FACTOR" ]
        return WAREHOUSE[ "INCREASE_CAPACITY_COST" ]

    def DecreaseCapacity( self ):
        self.__capacity -= WAREHOUSE[ "CAPACITY_FACTOR" ]
        if self.__capacity < self.amount:
            self.__capacity = self.amount
        return WAREHOUSE[ "DECREASE_CAPACITY_COST" ]

    def PutItems( self, items_level=0, number_of_items=0 ):
        items_level     = int( items_level )
        number_of_items = int( number_of_items )
        free_space      = self.__capacity - self.amount
        if free_space == 0:
            return number_of_items
        elif number_of_items > free_space:
            self.__Put( items_level, free_space )
            return number_of_items - free_space
        else:
            self.__Put( items_level, number_of_items )
            return 0

    def TakeSomeItems( self, items_level=0, number_of_items=0 ):
        items_level     = int( items_level )
        number_of_items = int( number_of_items )
        if number_of_items <= 0 or items_level not in self.__storage:
            # If number_of_items is an invalid value
            # Or if this warehouse never stored such items
            return 0
        elif number_of_items > self.__storage[ items_level ]:
            items                           = self.__storage[ items_level ]
            self.__storage[ items_level ]   = 0
            return items
        else:
            self.__storage[ items_level ] -= number_of_items
            return number_of_items

    def TakeAllItems( self, items_level=0 ):
        items_level = int( items_level )
        if items_level in self.__storage:
            items                           = self.__storage[ items_level ]
            self.__storage[ items_level ]   = 0
            return items
        else:
            return 0
