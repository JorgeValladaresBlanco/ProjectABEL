faceId_list = [{'faceId': 'c9fe29e4-dcd8-4141-aa09-ee9fa135b127',
'name': 'Lalisa Manoban',
'profession':'raper',
'nationality': 'korean',
'group': 'BlackPink',
'faceRectangle': {'top': 95, 'left': 88, 'width': 223, 'height': 223}, 
'faceAttributes':  {'smile': 1.0, 'headPose': {'pitch': -5.2, 'roll': -15.2, 'yaw': -6.9}, 'gender': 'female', 'age': 21.0, 
                    'facialHair': {'moustache': 0.0, 'beard': 0.0, 'sideburns': 0.0}, 'glasses': 'NoGlasses', 
                    'emotion': {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 1.0, 'neutral': 0.0, 'sadness': 0.0, 'surprise': 0.0}, 
                    'blur': {'blurLevel': 'low', 'value': 0.15}, 'exposure': {'exposureLevel': 'goodExposure', 'value': 0.67}, 'noise': {'noiseLevel': 'low', 'value': 0.22}, 
                    'makeup': {'eyeMakeup': True, 'lipMakeup': True}, 'accessories': [], 
                    'occlusion': {'foreheadOccluded': False, 'eyeOccluded': False, 'mouthOccluded': False}, 
                    'hair': 'brown', 'haircolor': {'bald': 0.07, 'invisible': False, 'hairColor': [{'color': 'brown', 'confidence': 1.0}, {'color': 'blond', 'confidence': 0.78}, {'color': 'red', 'confidence': 0.33}, {'color': 'black', 'confidence': 0.24}, {'color': 'gray', 'confidence': 0.08}, {'color': 'other', 'confidence': 0.02}, {'color': 'white', 'confidence': 0.0}]}}}]

dic0= faceId_list[0]

dic0_faceRectangle= dic0['faceRectangle']
dic0_faceAttributes= dic0['faceAttributes']
dic0_name= dic0['name']
haircolor = dic0_faceAttributes['hair']
dic0_emotions= dic0_faceAttributes['emotion']
dic0_profession= dic0['profession']
print(dic0_name, "pertenece al grupo", group)
dic0_nationality= dic0['nationality']
makeup= dic0_faceAttributes['makeup']
gender= dic0_faceAttributes['gender']
age= dic0_faceAttributes['age']
accessories= dic0_faceAttributes['accessories']


print("El nombre de la persona es", dic0_name)
print("La edad de", dic0_name, "es", age)
print("El genero de", dic0_name,"es", gender)
print("La profesion de", dic0_name, "es", dic0_profession)
print("La nacionalidad de", dic0_name, "es", dic0_nationality)
print("El color del pelo de", dic0_name, "es", haircolor)
print("Los accesorios de", dic0_name,"son", accessories)
print("El maquillaje de", dic0_name, "es", makeup)
print("Las emociones escaneadas de", dic0_name, "son", dic0_emotions)


sizes_top = dic0_faceRectangle['top']
sizes_left = dic0_faceRectangle['left']
sizes_width = dic0_faceRectangle['width']
sizes_height = dic0_faceRectangle['height']

print(sizes_top, "Es el top del rectangulo en la foto de la cara" )
print(sizes_left, "Es el left del rectangulo en la foto de la cara" )
print(sizes_width, "Es el width del rectangulo en la foto de la cara")
print(sizes_height, "Es el height del rectangulo en la foto de la cara")










