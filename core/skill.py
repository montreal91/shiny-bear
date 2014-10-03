from random import gauss, randint

class ASkill( object ):
    """docstring for ASkill"""
    __slots__ = ( "__talent", "__actual", "__maximum")
    def __init__( self ):
        super( ASkill, self ).__init__()
        self.__talent   = round( gauss( 2, 1 ) )
        if self.__talent <= 0:
            self.__talent = randint( 1, 2 )
        self.__maximum  = round( gauss( 15, 5 ) )
        if self.__maximum <= 0:
            self.__maximum = randint( 1, 9 )
        self.__actual    = 0

    @property 
    def actual( self ):
        return self.__actual

    @property 
    def maximum( self ):
        return self.__maximum

    @property 
    def talent( self ):
        return self.__talent

    def __Cut( self ):
        if self.__actual > self.__maximum:
            self.__actual = self.__maximum
        elif self.__actual < 0:
            self.__actual = 0

    def Increase( self ):
        self.__actual += self.__talent
        self.__Cut()

    def Decrease( self ):
        if self.__talent == 1:
            self.__actual -= 3
        elif self.__talent == 2:
            self.__actual -= 2
        else:
            self.__actual -= 1
        self.__Cut()
