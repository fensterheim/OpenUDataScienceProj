import os
import cv2
import json

def seperate_images(img_count=5000):
    INF = r'C:\Users\Joseph\Desktop\OpenU\DataInfo\git\OpenUDataScienceProj\Project\Data\malaria\separated\infected'
    UNINF = r'C:\Users\Joseph\Desktop\OpenU\DataInfo\git\OpenUDataScienceProj\Project\Data\malaria\separated\uninfected'
    os.chdir(r'C:\Users\Joseph\Desktop\OpenU\DataInfo\git\OpenUDataScienceProj\Project\Data\malaria')
    data = json.load(open(r'C:\Users\Joseph\Desktop\OpenU\DataInfo\git\OpenUDataScienceProj\Project\Data\malaria\training.json'))

    global_c_i = 0
    global_c_ui = 0
    for img_data in data: 
        img_obj = cv2.imread(img_data['image']['pathname'].replace('/', '\\')[1:])
        for blc in img_data['objects']:
            if blc['category'] == 'red blood cell':
                if global_c_ui > img_count:
                    continue
                x1 = blc['bounding_box']['minimum']['r']
                y1 = blc['bounding_box']['minimum']['c']
                x2 = blc['bounding_box']['maximum']['r']
                y2 = blc['bounding_box']['maximum']['c']            
                cv2.imwrite(UNINF + '\\' + str(global_c_ui) + '.' + img_data['image']['pathname'].split('.')[-1], img_obj[x1:x2, y1:y2])
                global_c_ui += 1
            else:
                x1 = blc['bounding_box']['minimum']['r']
                y1 = blc['bounding_box']['minimum']['c']
                x2 = blc['bounding_box']['maximum']['r']
                y2 = blc['bounding_box']['maximum']['c']
                cv2.imwrite(INF + '\\' + str(global_c_i) + '.' + img_data['image']['pathname'].split('.')[-1], img_obj[x1:x2, y1:y2])
                global_c_i += 1


"""
global_c_i = 0
global_c_ui = 0
for img_data in data:
    for blc in img_data['objects']:
        if blc['category'] == 'red blood cell':
            global_c_ui += 1
        else:
            global_c_i += 1



x1 = img_data['objects'][0]['bounding_box']['minimum']['r']
y1 = img_data['objects'][0]['bounding_box']['minimum']['c']
x2 = img_data['objects'][0]['bounding_box']['maximum']['r']
y2 = img_data['objects'][0]['bounding_box']['maximum']['c']
"""