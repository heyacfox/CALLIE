from . import Connections


#The amount of weight to add when getting a conection already created
weightToAdd = 1

#lossLimit
myLossLimit = 100

myExpansionMax = 0.1

conTypesForText = {"Next": Connections.ConnectionTypeList("Next"), "Previous": Connections.ConnectionTypeList("Previous"), "External": Connections.ConnectionTypeList("External")}
