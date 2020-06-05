import sys
import requests
import json

import cognitive_face as CF
from PIL import Image, ImageDraw, ImageFont

subscription_key = "7783ee962116400d9334835d998ea4ae"

SUBSCRIPTION_KEY = '7783ee962116400d9334835d998ea4ae'
BASE_URL = 'https://myfaceapi-project.cognitiveservices.azure.com'
CF.BaseUrl.set(BASE_URL)
CF.Key.set(SUBSCRIPTION_KEY)

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
    width = faceRectangle['width']
    top = faceRectangle['top']
    height = faceRectangle['height']
    left = faceRectangle['left']

def emotions(picture):
    image_path = picture
    image_data = open(image_path, "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': "38b89ea72f394ff48413a3675fe4c151",
    'Content-Type': 'application/octet-stream'}

image_orig = open(image_path, "rb").read()
image = Image.open(BytesIO(image_orig))

plt.figure(figsize=(12, 12))
ax = plt.imshow(image, alpha=1)
for face in faces:
    fr = face["faceRectangle"]
    fa = face["faceAttributes"]
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(
        origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
    plt.text(origin[0], origin[1], "%s, %d , %s" % (fa["gender"], fa["age"], fa["glasses"]),
             fontsize=20, color='w', weight="bold", va="bottom")
    ax.axes.add_patch(p)

_ = plt.axis("off")
plt.show()

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'true',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }
    response = requests.post(
                             BASE_URL + "detect/", headers=headers, params=params, data=image_data)
    analysis = response.json()
    print(analysis)

    image_orig = open(image_path, "rb").read()
image = Image.open(BytesIO(image_orig))

plt.figure(figsize=(12, 12))
ax = plt.imshow(image, alpha=1)
for face in faces:
    fr = face["faceRectangle"]
    fa = face["faceAttributes"]
    origin = (fr["left"], fr["top"])
    p = patches.Rectangle(
        origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
    plt.text(origin[0], origin[1], "%s, %d , %s" % (fa["gender"], fa["age"], fa["glasses"]),
             fontsize=20, color='w', weight="bold", va="bottom")
    ax.axes.add_patch(p)

_ = plt.axis("off")
plt.show()

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
        print("Digite 1 para Ayuda");
        print("Digite 2 Crear un grupo")
        print("Digite 3 para crear a persona dentro de un grupo")
        print("Digite 4 para conocer si la persona existe, o ya esta dentro del grupo")
        print("Digite 5 para saber todas las personas de un grupo")
        print("Digite 6 para saber cuales son las emociones")