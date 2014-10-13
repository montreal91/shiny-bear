# coding: utf-8

from unittest               import TestCase

from core.factory           import AFactory
from core                   import AnAbstractBuilding

from core.game_constants    import SPECIALIZATIONS

class AFactoryTestCase( TestCase ):
    def setUp( self ):
        self.weapons = SPECIALIZATIONS[ "WEAPONS" ]
        self.armours = SPECIALIZATIONS[ "ARMOURS" ]

    def test_constructor( self ):
        factory1 = AFactory( self.weapons, complexity=25, cost=9000 )
        self.assertEqual( factory1.complexity, 25 )
        self.assertEqual( factory1.cost, 9000 )
        self.assertEqual( factory1.specialization, self.weapons )
        self.assertEqual( factory1.tech_level, 1 )
        self.assertEqual( factory1.prod_level, 1 )
        self.assertEqual( factory1.productivity, 1.0 )
        self.assertEqual( factory1.efficiency, 1 )
        self.assertEqual( factory1.product_price, 100 )
        self.assertEqual( factory1.amount, 0 )
        self.assertEqual( factory1.capacity, 1000 )

        factory2 = AFactory( self.armours )
        self.assertEqual( factory2.specialization, self.armours )
        self.assertEqual( factory2.tech_level, 1 )
        self.assertEqual( factory2.prod_level, 1 )
        self.assertEqual( factory2.productivity, 1.0 )
        self.assertEqual( factory2.efficiency, 1 )
        self.assertEqual( factory2.product_price, 100 )

        with self.assertRaises( AssertionError ):
            factory3 = AFactory( 85 )
        with self.assertRaises( TypeError ):
            factory3 = AFactory()

    def test_upgrade_productivity( self ):
        factory = AFactory( self.armours )
        self.assertEqual( factory.productivity, 1 )
        factory.UpgradeProductivity()
        self.assertEqual( factory.productivity, 1.1 )
        self.assertEqual( factory.product_price, 100 )

    def test_upgrade_efficiency( self ):
        factory = AFactory( self.weapons )
        self.assertEqual( factory.efficiency, 1)
        self.assertEqual( factory.product_price, 100 )

        factory.UpgradeEfficiency()
        self.assertEqual(factory.efficiency, 2)
        self.assertEqual(factory.product_price, 50)

        factory.UpgradeEfficiency()
        self.assertEqual(factory.efficiency, 3)
        self.assertEqual(factory.product_price, 33.33)

    def test_upgrade_downgrade_tech_level( self ):
        factory = AFactory( self.armours )
        self.assertEqual( factory.efficiency, 1 )
        self.assertEqual( factory.productivity, 1 )
        self.assertEqual( factory.tech_level, 1 )

        factory.UpgradeTechLevel()
        self.assertEqual( factory.efficiency, 1 )
        self.assertEqual( factory.productivity, 1 )
        self.assertEqual( factory.tech_level, 2 )

        factory.UpgradeEfficiency()
        factory.UpgradeProductivity()
        factory.UpgradeTechLevel()
        self.assertEqual( factory.efficiency, 1 )
        self.assertEqual( factory.productivity, 1.0 )
        self.assertEqual( factory.tech_level, 3 )

        factory.UpgradeEfficiency()
        factory.UpgradeProductivity()
        self.assertEqual( factory.efficiency, 2 )
        self.assertEqual( factory.productivity, 1.1 )

        factory.DowngradeTechLevel()
        self.assertEqual( factory.efficiency, 2 )
        self.assertEqual( factory.productivity, 1.1 )
        self.assertEqual( factory.tech_level, 2 )

    def test_set_prod_level( self ):
        factory = AFactory( self.weapons )

        factory.SetProdLevel( 2 )
        self.assertEqual( factory.prod_level, 2 )
        self.assertEqual( factory.product_price, 200 )

        factory.SetProdLevel( 10 )
        self.assertEqual( factory.prod_level, 6 )
        self.assertEqual( factory.product_price, 3200 )

        factory.SetProdLevel( -4 )
        self.assertEqual( factory.prod_level, 1 )
        self.assertEqual( factory.product_price, 100 )

        factory.SetProdLevel( 4 )
        self.assertEqual( factory.prod_level, 4 )
        self.assertEqual( factory.product_price, 800 )

    def test_produce( self ):
        factory = AFactory( self.armours )
        self.assertEqual( factory.Produce(), 10000 )

        for i in xrange( 5 ):
            factory.UpgradeTechLevel()
        factory.SetProdLevel( 10 )
        for i in xrange( 10 ):
            factory.UpgradeProductivity()
        self.assertEqual(factory.Produce(), 10240000 )
        self.assertEqual(factory.product_price, 51200 )
        for i in xrange( 8 ):
            factory.UpgradeEfficiency()
        self.assertEqual( factory.product_price, 5688.89 )
        self.assertEqual( factory.Produce(), 1137778 )

    def test_take_production( self ):
        factory = AFactory( self.weapons )
        for i in xrange( 1, 6 ):
            factory.SetProdLevel( i )
            factory.Produce()
            factory.Produce()

        self.assertEqual( factory.amount, factory.capacity )
        self.assertEqual( factory.TakeProduction( prod_level=1, number_of_items=20 ), 20 )
        self.assertEqual( factory.amount, 980 )
        self.assertEqual( factory.TakeProduction( prod_level=1, all_items=True ), 180 )
        self.assertEqual( factory.amount, 800 )
        self.assertEqual( factory.TakeProduction( prod_level=6, number_of_items=20 ), 0 )
