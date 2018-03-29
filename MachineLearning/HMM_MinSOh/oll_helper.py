import math

def asset_list_to_stateN(asset_list):
    result = []
    for i in range(len(asset_list)):
        result.append(int(math.pow(2,asset_list[i])))
    return result

def asset_list_to_evidenceN(asset_list):
    result = []
    for i in range(1,len(asset_list)):
        result.append(int(math.pow(3,asset_list[i])))
    return result
