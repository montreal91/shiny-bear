# coding: utf-8
from random     import randint

from citizen    import ACitizen
from helpers        import ACounter
from game_constants import POPULATION, GENDERS

class APopulation( object ):
    """docstring for APopulation"""
    __slots__ = ( "__population", "__counter", "__growth", "__total_population" )
    def __init__( self, starting_population=0, growth=POPULATION.GROWTH ):
        super(APopulation, self).__init__()
        self.__population       = dict()
        self.__counter          = ACounter()
        self.__growth           = growth

        self.__total_population = 0
        self.__Invoke( starting_population=starting_population )

    @property
    def total_population( self ):
        return self.__total_population

    @property
    def ever_lived( self ):
        return self.__counter.counter

    @property 
    def military_aged( self ):
        res = 0
        for citizen in self.__population.itervalues():
            if citizen.age == POPULATION.MILITARY_AGE:
                res += 1
            else:
                pass
        return res

    def __AddCitizen( self, citizen ):
        self.__population[ self.__counter.Next() ] = citizen
        self.__total_population += 1

    def __Invoke( self, starting_population=0 ):
        starting_population = int(starting_population)
        if starting_population > 0:
            for i in xrange( starting_population ):
                if i % 2 == 0:
                    self.__AddCitizen( ACitizen( age=randint( 0, 50 ), gender=GENDERS[ "FEMALE" ] ) )
                else:
                    self.__AddCitizen( ACitizen( age=randint( 0, 50 ), gender=GENDERS[ "MALE" ] ) )
            self.__RemoveDead()
        else:
            pass

    def __RemoveDead( self ):
        population_c = self.__population.copy()
        for key in population_c:
            if not self.__population[ key ].alive:
                del self.__population[ key ]
                self.__total_population -= 1
            else:
                continue

    def LiveOneYear( self ):
        population_c = self.__population.copy()
        for citizen in population_c.itervalues():
            child = citizen.GiveBirth()
            if child is not None:
                self.__AddCitizen( child )
            else:
                pass
            citizen.AgeUp()
        self.__RemoveDead()

    def TakeMilitaryAged( self ):
        p_copy  = self.__population.copy()
        res     = [ self.__population.pop( key ) for key in p_copy if p_copy[ key ].age == POPULATION.MILITARY_AGE ]
        self.__total_population -= len( res )
        return res
