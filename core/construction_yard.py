# coding: utf-8

from helpers        import AStruct
from code_constants import STATUS_CODES

class AConstructionYard( object ):
    """docstring for AConstructionYard"""
    def __init__( self ):
        super( AConstructionYard, self ).__init__()
        self.__yard = {}

    @property
    def busy_building_modules( self ):
        mod_list = [ slot.b_modules for slot in self.__yard.itervalues() ]
        return sum( mod_list )

    @property
    def buildings_under_construction( self ):
        return len( self.__yard )


    def AddBuilding( self, building, b_modules=0 ):
        if building.identifier not in self.__yard:
            slot                                = AStruct()
            slot.building                       = building
            slot.b_modules                      = b_modules
            self.__yard[ building.identifier ]  = slot
            return STATUS_CODES.SUCCESS
        else:
            return STATUS_CODES.FAILURE

    def RemoveBuilding( self, building_id=0 ):
        result = AStruct()
        if building_id in self.__yard:
            slot = self.__yard.pop( building_id )
            result.b_modules = slot.b_modules
            result.remainder = slot.building.cost * ( ( 100 - slot.building.progress) / 100 )
            result.remainder = int( round( result.remainder ) )
        else:
            result.b_modules = 0
            result.remainder = 0
        return result

    def AddBuildingModulesToBuilding( self, building_id=0, b_modules=0 ):
        b_modules = int( b_modules )
        if building_id in self.__yard and b_modules > 0:
            self.__yard[ building_id ].b_modules += b_modules
            return STATUS_CODES.SUCCESS
        else:
            return STATUS_CODES.FAILURE

    def TakeBuildingModulesFromBuilding( self, building_id=0, b_modules=0, all_modules=False ):
        b_modules = int( b_modules )
        if building_id not in self.__yard or b_modules < 0:
            return 0
        else:
            slot = self.__yard[ building_id ]
            if b_modules > slot.b_modules or all_modules:
                modules         = slot.b_modules
                slot.b_modules  = 0
                return modules
            elif b_modules <= slot.b_modules:
                slot.b_modules -= b_modules
                return b_modules
            else:
                raise StandardError

    def Construct( self ):
        for slot in self.__yard.itervalues():
            slot.building.Build( slot.b_modules )
    
    def PopReadyBuildings( self ):
        result              = AStruct()
        result.b_modules    = 0
        result.buildings    = []
        for building_id in self.__yard.copy():
            slot = self.__yard[ building_id ]
            if slot.building.progress == 100:
                self.__yard.pop( building_id )
                result.b_modules += slot.b_modules
                result.buildings.append( slot.building )
            else:
                continue
        return result
