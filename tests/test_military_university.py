# coding: utf-8

from unittest                   import TestCase
from random                     import seed

from core.military_university   import AMilitaryUniversity
from core.human                 import AHuman

class AMilitaryUniversityTestCase( TestCase ):
    def setUp( self ):
        seed( 42 )

    def test_educate( self ):
        mit         = AMilitaryUniversity( capacity=10 )
        self.assertEqual( mit.capacity, 10 )
        entrants    = [ AHuman( identifier=i ) for i in xrange( 5 ) ]

        mit.AddManyStudents( entrants )
        mit.Educate()
        self.assertEqual( mit.educating_students, 5 )
        self.assertEqual( mit.current_graduates, 0 )
        self.assertEqual( mit.overall_graduates, 0 )

        students    = mit.RemoveAllStudents()
        for a_student in students:
            self.assertEqual( a_student.discipline.actual, a_student.discipline.talent )
            self.assertEqual( a_student.attack.actual, a_student.attack.talent )
            self.assertEqual( a_student.defence.actual, a_student.defence.talent )
            self.assertEqual( a_student.logistics.actual, a_student.logistics.talent )
            self.assertEqual( a_student.leadership.actual, a_student.leadership.talent )


        mit.AddManyStudents( students )
        for i in xrange( 10 ):
            mit.Educate()
        self.assertEqual( mit.educating_students, 3 )
        self.assertEqual( mit.current_graduates, 2 )

        self.assertNotEqual( entrants[ 0 ].defence.actual, entrants[ 0 ].defence.maximum )

        self.assertEqual( entrants[ 1 ].discipline.actual, entrants[ 1 ].discipline.maximum )
        self.assertEqual( entrants[ 1 ].attack.actual, entrants[ 1 ].attack.maximum )
        self.assertEqual( entrants[ 1 ].defence.actual, entrants[ 1 ].defence.maximum )
        self.assertEqual( entrants[ 1 ].logistics.actual, entrants[ 1 ].logistics.maximum )
        self.assertEqual( entrants[ 1 ].leadership.actual, entrants[ 1 ].leadership.maximum )
