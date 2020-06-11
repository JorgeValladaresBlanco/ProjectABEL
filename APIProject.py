import sys
import requests
import json

import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

subscription_key = "7783ee962116400d9334835d998ea4ae"
assert subscription_key

face_api_url = 'https://myfaceapi-project.cognitiveservices.azure.com/face/v1.0/detect'

image_url = 'https://i.pinimg.com/originals/9f/03/b8/9f03b815508309bd6d3951364c0baff9.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}


params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})


def create_group(group_id, group_name):

    CF.person_group.create(group_id, group_name)
    print("Grupo creado")

def create_person(name, profession, picture, group_id):

    response = CF.person.create(group_id, name, profession)

    person_id = response['personId']
  
    CF.person.add_face(picture, group_id, person_id)

    
  
    CF.person_group.train(group_id)
    
    response = CF.person_group.get_status(group_id)
    status = response['status']
    print(status)


def print_people(group_id):
 
    print(CF.person.lists(group_id))


def recognize_person(picture, group_id):
  
    response = CF.face.detect(picture)
    face_ids = [d['faceId'] for d in response]

    identified_faces = CF.face.identify(face_ids, group_id)
    personas = identified_faces[0]
    candidates_list = personas['candidates']
    candidates = candidates_list[0]

    person = candidates['personId']

    person_data = CF.person.get(group_id, person)

    person_name = person_data['name']
    print(person_name)
    
  
    response = CF.face.detect(picture)

    dic = response[0]
 
    faceRectangle = dic['faceRectangle']
    print(faceRectangle)
    width = faceRectangle['width']
    top = faceRectangle['top']
    height = faceRectangle['height']
    left = faceRectangle['left']
    print(top)

def emotions(picture):

    image_path = picture

    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
    'Content-Type': 'application/octet-stream'}
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    response = requests.post(
                             BASE_URL + "detect/", headers=headers, params=params, data=image_data)
    analysis = response.json()
    print(analysis)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        case = int(sys.argv[1])
        if case == 1 and len(sys.argv) == 4:    
            group_id = sys.argv[2]
            group_name = sys.argv[3]
            create_group(group_id, group_name)
        elif case == 2 and len(sys.argv) == 6:
            name = sys.argv[2]
            profession = sys.argv[3]
            picture = sys.argv[4]
            group_id = sys.argv[5]
            create_person(name, profession, picture, group_id)
        elif case == 3 and len(sys.argv) == 4:
            picture = sys.argv[2]
            group_id = sys.argv[3]
            recognize_person(picture, group_id)
        elif case == 4 and len(sys.argv) == 3:
            group_id = sys.argv[2]
            print_people(group_id)
        elif case == 5 and len(sys.argv) == 3:
            picture = sys.argv[2]
            emotions(picture)
        else:
            print("Ayuda")
    else:
        print("Ayuda");
        print("Crear un grupo")
        print("Crear persona en un grupo")
        print("Crear persona en un grupo ")
        print("Consultar si una persona existe")
        print("Consultar todas las personas de un grupo ")
        print("Consultar emociones")


faces = response.json()
print(faces)