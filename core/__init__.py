# coding: utf-8

from __future__     import division
from math           import modf

from human          import AHuman

class AnAbstractBuilding( object ):
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


class AnAbstractSchool( AnAbstractBuilding ):
    """docstring for AnAbstractSchool"""
    __slots__ = (
        "__max_students", "__education_price",
        "__students", "__graduates", "__overall_graduates"
    )
    def __init__( self, **kwargs ):
        super( AnAbstractSchool, self ).__init__( **kwargs )
        self.__max_students     = 0 # const 
        self.__education_price  = 5 # const

        self.__students         = {}
        self.__graduates        = {}

        self.__overall_graduates = 0

    @property 
    def max_students( self ):
        return self.__max_students

    @property 
    def educating_students( self ):
        return len(self.__students)

    @property 
    def education_price( self ):
        return self.__education_price

    @property 
    def current_graduates( self ):
        return len( self.__graduates )

    @property 
    def overall_graduates( self ):
        return self.__overall_graduates

    def __Graduate( self, student_id ):
        graduate                                = self.__students.pop( student_id )
        self.__graduates[ graduate.identifier ] = graduate
        self.__overall_graduates += 1

    def AddOneStudent( self, new_student ):
        assert type( new_student ) == AHuman
        assert new_student.identifier not in self.__students
        self.__students[ new_student.identifier ] = new_student

    def RemoveOneStudent( self, student_id ):
        if student_id in self.__students:
            return self.__students.pop(student_id)
        else:
            return None

    def AddManyStudents( self, new_students_list ):
        for student in new_students_list:
            if type( student ) == AHuman and student.identifier not in self.__students:
                self.__students[ student.identifier ] = student
            else:
                pass

    def RemoveAllStudents( self ):
        students        = list( self.__students.itervalues() )
        self.__students = {}
        if len( students ) == 0:
            return None
        else:
            return students

    def TakeOneGraduate( self, graduate_id ):
        if graduate_id in self.__graduates:
            return self.__graduates.pop( graduate_id )
        else:
            return None

    def TakeAllGraduates( self ):
        graduates           = list( self.__graduates.itervalues() )
        self.__graduates    = {}
        if len(graduates) == 0:
            return None
        else:
            return graduates
