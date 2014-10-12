# coding: utf-8

from . import AnAbstractSchool

class AMilitaryUniversity( AnAbstractSchool ):
    """docstring for AMilitaryUniversity"""
    def __init__( self, **kwargs ):
        super( AMilitaryUniversity, self ).__init__( **kwargs )

    def __ConditionOfGraduating( self, student ):
        discipline  = student.discipline.actual == student.discipline.maximum
        attack      = student.attack.actual == student.attack.maximum
        defence     = student.defence.actual == student.defence.maximum
        logistics   = student.logistics.actual == student.logistics.maximum
        leadership  = student.leadership.actual == student.leadership.maximum
        return discipline and attack and defence and logistics and leadership
    
    def __FilterOutGraduatedStudents( self ):
        students_dict = self._students.copy()
        for student in students_dict.itervalues():
            if self.__ConditionOfGraduating( student ) is True:
                self._Graduate( student.identifier )
            else:
                pass

    def Educate( self ):
        costs = 0
        for student in self._students.itervalues():
            student.IncreaseSkill( all_skills=True )
            costs += self.education_price
        self.__FilterOutGraduatedStudents()
        return costs
