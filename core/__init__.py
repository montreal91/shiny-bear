# coding: utf-8

from __future__     import division
from math           import modf

class AnAbstractBuilding(object):
    """docstring for AnAbstractBuilding"""
    __slots__       = ( "__complexity", "__cost", "__progress" )
    def __init__( self, complexity=1, cost=1 ):
        super( AnAbstractBuilding, self ).__init__()
        self.__cost         = cost
        self.__complexity   = complexity
        self.__progress     = 0 # Takes values from 0 to 1

    @property 
    def complexity( self ):
        return self.__complexity

    @property 
    def cost( self ):
        return self.__cost

    @property 
    def progress( self ):
        return round( self.__progress * 100, 2 )

    def Build( self, building_modules ):
        self.__progress += building_modules / self.__complexity
        if self.__progress > 1:
            self.__progress = 1

    def CalculateConstructionPeriod( self, building_modules ):
        period  = ( self.__complexity * ( 1 - self.__progress ) ) / building_modules
        fract   = modf( period )
        if fract[ 0 ] != 0:
            return int( period + 1 )
        else:
            return int( period )
