# coding: utf-8

from unittest               import TestCase
from random                 import seed

from core.soldier_school    import ASoldierSchool
from core.human             import AHuman

class ASoldierSchoolTestCase( TestCase ):
    def setUp( self ):
        seed( 42 )

    def test_educate( self ):
        school      = ASoldierSchool()
        entrants    = [ AHuman( identifier=i ) for i in xrange( 20 ) ]
        school.AddManyStudents( entrants )
        self.assertEqual( school.educating_students, 20 )
        self.assertEqual( school.Educate(), 100 )

        students    = school.RemoveAllStudents()
        for student in students:
            self.assertEqual( student.discipline.actual, student.discipline.talent )

        school.AddManyStudents( entrants )
        for i in xrange( 10 ):
            school.Educate()
        self.assertEqual( school.current_graduates, 17 )
        self.assertEqual( school.overall_graduates, 17 )
        self.assertEqual( school.educating_students, 3 )

        self.assertEqual( school.TakeOneGraduate( 5 ), entrants[ 5 ] )
        self.assertEqual( school.current_graduates, 16 )

        self.assertEqual( len( school.TakeAllGraduates() ), 16 )
        self.assertEqual( school.current_graduates, 0 )
        self.assertEqual( school.overall_graduates, 17 )

        entrants    = [ AHuman( identifier=i ) for i in xrange( 20, 30 ) ]
        school.AddManyStudents( entrants )
        for i in xrange( 10 ):
            school.Educate()
        self.assertEqual( school.educating_students, 2 )
        self.assertEqual( school.current_graduates, 11 )
        self.assertEqual( school.overall_graduates, 28 )

        graduates   = school.TakeAllGraduates()
        for graduate in graduates:
            self.assertEqual( graduate.discipline.actual, graduate.discipline.maximum )
        self.assertEqual( school.current_graduates, 0 )
