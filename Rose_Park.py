faceId_list = [{'faceId': 'f04acf0e-92cc-46f7-a9e9-6bccd6227792', 
'name': 'Rose Park Chaeyoung',
'profession':'Lead Singer',
'nationality': 'korean and New Zealander',
'group': 'BlackPink',
'faceRectangle': {'top': 290, 'left': 267, 'width': 187, 'height': 187}, 
'faceAttributes': {'smile': 0.998, 'headPose': {'pitch': 2.3, 'roll': -10.7, 'yaw': -7.9}, 'gender': 'female', 'age': 21.0, 
                    'facialHair': {'moustache': 0.0, 'beard': 0.0, 'sideburns': 0.0}, 'glasses': 'NoGlasses', 
                    'emotion': {'anger': 0.0, 'contempt': 0.0, 'disgust': 0.0, 'fear': 0.0, 'happiness': 0.998, 'neutral': 0.002, 'sadness': 0.0, 'surprise': 0.0}, 
                    'blur': {'blurLevel': 'low', 'value': 0.0}, 'exposure': {'exposureLevel': 'goodExposure', 'value': 0.67}, 'noise': {'noiseLevel': 'medium', 'value': 0.54}, 
                    'makeup': {'eyeMakeup': True, 'lipMakeup': True}, 
                    'accessories': [], 'occlusion': {'foreheadOccluded': False, 'eyeOccluded': False, 'mouthOccluded': False}, 'hair': 
                    {'bald': 0.02, 'invisible': False, 
                    'hair': 'blond', 'hairColor': [{'color': 'blond', 'confidence': 0.99}, {'color': 'red', 'confidence': 0.79}, {'color': 'other', 'confidence': 0.66}, {'color': 'gray', 'confidence': 0.2}, {'color': 'brown', 'confidence': 0.18}, {'color': 'black', 'confidence': 0.03}, {'color': 'white', 'confidence': 0.0}]}}}]

dic0= faceId_list[0]

dic0_faceRectangle= dic0['faceRectangle']
dic0_faceAttributes= dic0['faceAttributes']
dic0_name= dic0['name']
haircolor = dic0_faceAttributes['hair']
dic0_emotions= dic0_faceAttributes['emotion']
dic0_profession= dic0['profession']
dic0_nationality= dic0['nationality']
makeup= dic0_faceAttributes['makeup']
gender= dic0_faceAttributes['gender']
age= dic0_faceAttributes['age']
accessories= dic0_faceAttributes['accessories']
group= dic0['group']


print("El nombre de la persona es", dic0_name)
print("La edad de", dic0_name, "es", age)
print("El genero de", dic0_name,"es", gender)
print("La profesion de", dic0_name, "es", dic0_profession)
print(dic0_name, "pertenece al grupo", group)
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
