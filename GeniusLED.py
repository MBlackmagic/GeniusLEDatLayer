# Created by Mehmet Ali Ersoez

from ..Script import Script

class GeniusLED(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Genius LED at layer",
            "key": "GeniusLED",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "layer_at":
                {
                    "label": "Insert at Layer",
                    "description": "Artillery Genius LED settings at layer. ",
                    "type": "str",
                    "default_value": "0"
                },
                "gcode_to_add":
                {
                    "label": "GCODE to insert:",
                    "description": "GGCODE to insert at layer.",
                    "type": "str",
                    "default_value": ""
                },
                 "red":
                {
                    "label": "Red:",
                    "description": "Value for red  0 - 255",
                    "type": "str",
                    "default_value": "0"
                },
                  "green":
                {
                    "label": "Green:",
                    "description": "Value for green 0 - 255",
                    "type": "str",
                    "default_value": "0"
                },
                  "blue":
                {
                    "label": "Blue:",
                    "description": "Value for blue 0 - 255",
                    "type": "str",
                    "default_value": "0"
                }
            }
        }"""

    def execute(self, data):
        gcode_to_add = self.getSettingValueByKey("gcode_to_add") + "\n"
        led_green = ";Genius LED\nM42 P4 S" + self.getSettingValueByKey(green") + "\n"
        led_red = "M42 P5 S" + self.getSettingValueByKey("red") + "\n"
        led_blue = "M42 P6 S" + self.getSettingValueByKey("blue") + "\n"

        mygcode_to_add = gcode_to_add + led_red + led_green + led_blue

        my_layer = ";LAYER:" + self.getSettingValueByKey("layer_at")
        for layer in data:
            # Check that a layer is being printed
            lines = layer.split("\n")
            for line in lines:
                if line == my_layer:
                    index = data.index(layer)
                    layer = mygcode_to_add + layer 
                   
                    data[index] = layer
                    break
        return data

