import json
from decimal import Decimal

# def Annotation_Conversion(region, size):
#         x = region['shape_attributes']['x']
#         y = region['shape_attributes']['y']
#         width = region['shape_attributes']['width']
#         height = region['shape_attributes']['height']

#         _x      = Decimal(x + width) / Decimal(2 * size[0]) 
#         _y      = Decimal(y + height) / Decimal(2 * size[1])
#         _width  = Decimal(width / size[0])
#         _height = Decimal(height / size[1])  # Image size

#         return "{0:.10f} {0:.10f} {0:.10f} {0:.10f}".format(_x, _y, _width, _height)


#  Image size is 640 x 480 

def Calculate_Yolo(x, y, width, height):
    _x      = Decimal(x + width) / Decimal(2 * 640) 
    _y      = Decimal(y + height) / Decimal(2 * 480)
    _width  = Decimal(width / 640)
    _height = Decimal(height / 480)  # Image size

    return "{0:.5f} {0:.5f} {0:.5f} {0:.5f}".format(_x, _y, _width, _height)

with open('Via_Annotations.json', 'r') as file:
    data = json.load(file)

for key, value in data.items():
    x = value['regions'][0]['shape_attributes']['x']
    y = value['regions'][0]['shape_attributes']['y']
    width = value['regions'][0]['shape_attributes']['width']
    height = value['regions'][0]['shape_attributes']['height']

    # print(value)

    print(Calculate_Yolo(x, y, width, height))
