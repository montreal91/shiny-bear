# coding: utf-8

from unittest   import TestCase

from core import AnAbstractSchool
from core.human import AHuman

class AnAbstractSchoolTestCase( TestCase ):
    def test_constructor( self ):
        school = AnAbstractSchool( complexity=10, cost=2000,)
        self.assertEqual( school.complexity, 10 )
        self.assertEqual( school.cost, 2000 )

        self.assertEqual( school.max_students, 0 )
        self.assertEqual( school.educating_students, 0 )
        self.assertEqual( school.education_price, 5 )
        self.assertEqual( school.current_graduates, 0 )
        self.assertEqual( school.overall_graduates, 0 )

    def test_add_remove_one_student( self ):
        school = AnAbstractSchool()
        student = AHuman( identifier=3 )
        school.AddOneStudent( student )
        self.assertEqual( school.educating_students, 1 )
        self.assertEqual( school.RemoveOneStudent( 2 ), None )
        self.assertEqual( school.RemoveOneStudent( 3 ), student )
        self.assertEqual( school.RemoveOneStudent( 3 ), None )
        self.assertEqual( school.educating_students, 0 )
        with self.assertRaises( AssertionError ):
            school.AddOneStudent( 1984 )

    def test_add_remove_many_students( self ):
        school      = AnAbstractSchool()
        entrants    =  [AHuman( identifier=i ) for i in xrange( 1, 21 ) ]
        school.AddManyStudents( entrants )
        self.assertEqual( school.educating_students, 20 )

        entrants2   = [ AHuman( identifier=i ) for i in xrange( 10, 31 ) ]
        entrants2.append( "New Student" )
        school.AddManyStudents( entrants2 )
        self.assertEqual( school.educating_students, 30 )

        students    = school.RemoveAllStudents()
        self.assertEqual( len( students ), 30 )
        self.assertEqual( school.educating_students, 0 )
