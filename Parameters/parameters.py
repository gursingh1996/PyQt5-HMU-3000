import json

class param:
    def getData():
        with open('./Parameters/parameters.json', 'r') as openfile:
            json_object = json.load(openfile)

        return json_object

    def setData(parameters):
        json_object = json.dumps(parameters, indent = 4)
  
        # Writing to sample.json
        with open("./Parameters/parameters.json", "w") as outfile:
            outfile.write(json_object)

    def getDataName():
        with open('./Parameters/parameter_name.json', 'r') as openfile:
            json_object = json.load(openfile)

        return json_object