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
        students_dict = self._students.copy()
        for student in students_dict.itervalues():
            if student.discipline.actual == student.discipline.maximum:
                self._Graduate( student.identifier )
            else:
                pass

    def Educate( self ):
        education_costs = 0
        for student in self._students.itervalues():
            student.IncreaseSkill( skill=DISCIPLINE )
            education_costs += self.education_price 
        self.__FilterOutGraduatedStudents()
        return education_costs
