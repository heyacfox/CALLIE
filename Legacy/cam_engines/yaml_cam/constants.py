from . import connections


#The amount of weight to add when getting a conection already created
WEIGHT_TO_ADD = 1

#lossLimit
MY_LOSS_LIMIT = 100000000000

MY_EXPANSION_MAX = 0.1

CON_TYPES_FOR_TEXT = {"Next": connections.ConnectionTypeList("Next"),
                      "Previous": connections.ConnectionTypeList("Previous"),
                      "External": connections.ConnectionTypeList("External")}
