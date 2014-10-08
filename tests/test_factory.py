# coding: utf-8

from unittest               import TestCase

from core.factory           import AFactory
from core                   import AnAbstractBuilding
from core.code_constants    import WEAPONS, ARMOURS

class AFactoryTestCase( TestCase ):
    def test_constructor( self ):
        factory1 = AFactory( WEAPONS )
        self.assertEquals( factory1.complexity, 25 )
        self.assertEquals( factory1.cost, 9000 )
        self.assertEquals( factory1.specialization, WEAPONS )
        self.assertEquals( factory1.tech_level, 1 )
        self.assertEquals( factory1.prod_level, 1 )
        self.assertEquals( factory1.productivity, 1.0 )
        self.assertEquals( factory1.efficiency, 1 )
        self.assertEquals( factory1.product_price, 100 )

        factory2 = AFactory( ARMOURS )
        self.assertEquals( factory2.specialization, ARMOURS )
        self.assertEquals( factory2.tech_level, 1 )
        self.assertEquals( factory2.prod_level, 1 )
        self.assertEquals( factory2.productivity, 1.0 )
        self.assertEquals( factory2.efficiency, 1 )
        self.assertEquals( factory2.product_price, 100 )

        with self.assertRaises( AssertionError ):
            factory3 = AFactory( 85 )
        with self.assertRaises( TypeError ):
            factory3 = AFactory()

    def test_upgrade_productivity( self ):
        factory = AFactory( ARMOURS )
        self.assertEquals( factory.productivity, 1 )
        factory.UpgradeProductivity()
        self.assertEquals( factory.productivity, 1.1 )
        self.assertEquals( factory.product_price, 100 )

    def test_upgrade_efficiency( self ):
        factory = AFactory( WEAPONS )
        self.assertEquals( factory.efficiency, 1)
        self.assertEquals( factory.product_price, 100 )

        factory.UpgradeEfficiency()
        self.assertEquals(factory.efficiency, 2)
        self.assertEquals(factory.product_price, 50)

        factory.UpgradeEfficiency()
        self.assertEquals(factory.efficiency, 3)
        self.assertEquals(factory.product_price, 33.33)

    def test_upgrade_downgrade_tech_level( self ):
        factory = AFactory( ARMOURS )
        self.assertEquals( factory.efficiency, 1 )
        self.assertEquals( factory.productivity, 1 )
        self.assertEquals( factory.tech_level, 1 )

        factory.UpgradeTechLevel()
        self.assertEquals( factory.efficiency, 1 )
        self.assertEquals( factory.productivity, 1 )
        self.assertEquals( factory.tech_level, 2 )

        factory.UpgradeEfficiency()
        factory.UpgradeProductivity()
        factory.UpgradeTechLevel()
        self.assertEquals( factory.efficiency, 1 )
        self.assertEquals( factory.productivity, 1.0 )
        self.assertEquals( factory.tech_level, 3 )

        factory.UpgradeEfficiency()
        factory.UpgradeProductivity()
        self.assertEquals( factory.efficiency, 2 )
        self.assertEquals( factory.productivity, 1.1 )

        factory.DowngradeTechLevel()
        self.assertEquals( factory.efficiency, 2 )
        self.assertEquals( factory.productivity, 1.1 )
        self.assertEquals( factory.tech_level, 2 )

    def test_set_prod_level( self ):
        factory = AFactory( WEAPONS )

        factory.SetProdLevel( 2 )
        self.assertEquals( factory.prod_level, 2 )
        self.assertEquals( factory.product_price, 200 )

        factory.SetProdLevel( 10 )
        self.assertEquals( factory.prod_level, 6 )
        self.assertEquals( factory.product_price, 3200 )

        factory.SetProdLevel( -4 )
        self.assertEquals( factory.prod_level, 1 )
        self.assertEquals( factory.product_price, 100 )

        factory.SetProdLevel( 4 )
        self.assertEquals( factory.prod_level, 4 )
        self.assertEquals( factory.product_price, 800 )

    def test_produce( self ):
        factory = AFactory( ARMOURS )
        self.assertEquals( factory.Produce(), 10000 )

        for i in range( 5 ):
            factory.UpgradeTechLevel()
        factory.SetProdLevel( 10 )
        for i in range( 10 ):
            factory.UpgradeProductivity()
        self.assertEquals(factory.Produce(), 10240000 )
        self.assertEquals(factory.product_price, 51200 )
        for i in range( 8 ):
            factory.UpgradeEfficiency()
        self.assertEquals( factory.product_price, 5688.89 )
        self.assertEquals( factory.Produce(), 1137778 )

    def test_get_put_production( self ):
        factory = AFactory( WEAPONS )
        factory.PutProduction( 1, 110 )
        self.assertEquals( factory.GetProduction( 1, 50 ), 50 )
        self.assertEquals( factory.GetProduction( 1, 50 ), 50 )
        self.assertEquals( factory.GetProduction( 1, 50 ), 10 )
        self.assertEquals( factory.GetProduction( 2, 200 ), 0 )

        factory.Produce()
        self.assertEquals( factory.GetProduction( 1, -150 ), 0 )

        factory.PutProduction( 3, 100 )
        factory.PutProduction( 4, 200 )
        self.assertEquals( factory.GetProduction( 2, 50 ), 0 )
        self.assertEquals( factory.GetProduction( 3, 250 ), 100 )
        self.assertEquals( factory.GetProduction( 4, 150 ), 150 )

        factory.PutProduction( 4, 150 )
        self.assertEquals( factory.GetProduction( 4, 300 ), 200 )

        with self.assertRaises( AssertionError ):
            factory.PutProduction( -1, 39 )
        with self.assertRaises( AssertionError ):
            factory.PutProduction( 1, -1 )
        with self.assertRaises( AssertionError ):
            factory.PutProduction( 0, 0 )
