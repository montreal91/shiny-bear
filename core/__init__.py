# coding: utf-8

from __future__     import division
from math           import modf

from human          import AHuman
from code_constants import PRECISION

class AnAbstractBuilding( object ):
    """docstring for AnAbstractBuilding"""
    __slots__       = ( "__identifier", "__complexity", "__cost", "__progress" )
    def __init__( self, identifier=0, complexity=1, cost=1 ):
        super( AnAbstractBuilding, self ).__init__()
        self.__identifier   = identifier
        self.__cost         = cost
        self.__complexity   = complexity
        self.__progress     = 0 # Takes values from 0 to 1

    @property 
    def identifier( self ):
        return self.__identifier

    @property 
    def complexity( self ):
        return self.__complexity

    @property 
    def cost( self ):
        return self.__cost

    @property 
    def progress( self ):
        return round( self.__progress * 100, PRECISION )

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
        "__capacity", "__education_price",
        "_students", "__graduates", "__overall_graduates"
    )
    def __init__( self, capacity=100, **kwargs ):
        super( AnAbstractSchool, self ).__init__( **kwargs )
        self.__capacity             = capacity  # const 
        self.__education_price      = 5         # const

        self._students              = {}
        self.__graduates            = {}

        self.__overall_graduates    = 0

    @property 
    def capacity( self ):
        return self.__capacity

    @property 
    def educating_students( self ):
        return len(self._students)

    @property 
    def education_price( self ):
        return self.__education_price

    @property 
    def current_graduates( self ):
        return len( self.__graduates )

    @property 
    def overall_graduates( self ):
        return self.__overall_graduates

    def _Graduate( self, student_id ):
        graduate                                = self._students.pop( student_id )
        self.__graduates[ graduate.identifier ] = graduate
        self.__overall_graduates += 1

    def __AddStudentCondition( self, new_student ):
        try:
            is_human                = type( new_student ) == AHuman
            not_already_educating   = new_student.identifier not in self._students
            school_is_not_full      = len(self._students) < self.__capacity
            return is_human and not_already_educating and school_is_not_full
        except:
            return False

    def AddOneStudent( self, new_student ):
        if self.__AddStudentCondition( new_student ) is True:
            self._students[ new_student.identifier ] = new_student
        else:
            pass

    def RemoveOneStudent( self, student_id ):
        if student_id in self._students:
            return self._students.pop( student_id )
        else:
            return None

    def AddManyStudents( self, new_students_list ):
        for student in new_students_list:
            if self.__AddStudentCondition( student ) is True:
                self._students[ student.identifier ] = student
            else:
                pass

    def RemoveAllStudents( self ):
        students        = list( self._students.itervalues() )
        self._students = {}
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
