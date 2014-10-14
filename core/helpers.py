# coding utf-8

class AStruct:
    pass


class ACounter( object ):
    """docstring for ACounter"""
    __slots__ = ( "__counter" )
    def __init__( self ):
        super( ACounter, self ).__init__()
        self.__counter = 0

    @property
    def counter( self ):
        return self.__counter

    def Next( self ):
        self.__counter += 1
        return self.__counter

    def DropCounter( self ):
        self.__counter = 0