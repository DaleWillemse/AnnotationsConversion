import json

#  Image size is 640 x 480 

count = 0

def Calculate_Yolo(x, y, width, height): 
    center_x = x / 640
    center_y = y / 480
    normalized_width = width / 640
    normalized_height = height / 480

    return f"{center_x:.5f} {center_y:.5f} {normalized_width:.5f} {normalized_height:.5f}"

with open('Via_Annotations.json', 'r') as file:
    data = json.load(file)


for key, value in data.items():
    count += 1
    x = value['regions'][0]['shape_attributes']['x']
    y = value['regions'][0]['shape_attributes']['y']
    width = value['regions'][0]['shape_attributes']['width']
    height = value['regions'][0]['shape_attributes']['height']

    # print(value)

    print(count , " " , Calculate_Yolo(x, y, width, height))
