# coding: utf-8

from random         import gauss, choice

from helpers        import LoadedToss
from game_constants import GENDERS, CITIZEN 

class ACitizen( object ):
    """docstring for ACitizen"""
    __slots__ = ( "__age", "__gender", "__max_age")
    def __init__( self, age=0, gender=GENDERS[ "MALE" ] ):
        super( ACitizen, self ).__init__()
        self.__gender       = gender
        self.__age          = age
        self.__max_age      = int( gauss( CITIZEN.AVERAGE_AGE, CITIZEN.AGE_VARIETY ) )

    @property
    def gender( self ):
        return self.__gender

    @property
    def age( self ):
        return self.__age

    @property
    def max_age( self ):
        return self.__max_age

    @property
    def alive( self ):
        return self.__age <= self.__max_age

    def __ConditionOfBirth( self, chance ):
        age_condition       = CITIZEN.CHILDBEARING_AGE.LOWER < self.__age < CITIZEN.CHILDBEARING_AGE.UPPER
        gender_condition    = self.__gender == GENDERS[ "FEMALE" ]
        return age_condition and gender_condition and chance

    def AgeUp( self ):
        self.__age += 1

    def GiveBirth( self ):
        toss = LoadedToss( CITIZEN.PREGNANCY_PROBABILITY )
        if self.__ConditionOfBirth( toss ) is True:
            return ACitizen( gender=choice( [ GENDERS[ "MALE" ], GENDERS[ "FEMALE" ] ] ) )
        else:
            return None
