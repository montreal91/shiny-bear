# coding: utf-8

class AName( object ):
    """docstring for AName"""
    __slots__ = ( "__first_name", "__second_name", "__last_name" )
    def __init__( self, first_name="Guy", second_name="Ronald", last_name="Fawkes" ):
        super( AName, self ).__init__()
        self.__first_name   = first_name
        self.__second_name  = second_name
        self.__last_name    = last_name

    @property 
    def first_name( self ):
        return self.__first_name

    @property 
    def second_name( self ):
        return self.__second_name

    @property 
    def last_name( self ):
        return self.__last_name

    @property 
    def initials( self ):
        return self.__first_name[0], self.__second_name[0], self.__last_name[0]
        