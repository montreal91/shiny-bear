# coding: utf-8
from __future__     import division
from math           import modf

from .              import AnAbstractSchool
from code_constants import DISCIPLINE
from human          import AHuman

class ASoldierSchool( AnAbstractSchool ):
    """docstring for ASoldierSchool"""
    def __init__( self, **kwargs ):
        super( ASoldierSchool, self ).__init__( **kwargs )

    def __FilterOutGraduatedStudents( self ):
        for student in self.__students.itervalues():
            if student.discipline.actual == student.discipline.actual:
                self.__Graduate( student.identifier )
            else:
                pass

    def Educate( self ):
        education_costs = 0
        for student in self.__students.itervalues():
            student.IncreaseSkill( skill=DISCIPLINE )
            education_costs += self.__education_price 
        self.__FilterOutGraduatedStudents()
        return education_costs
