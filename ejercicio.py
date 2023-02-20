# gryffindor: valor
# hufflepuff: lealtad
# ravenclaw: sabiduría
# slytherin: ambición

import random

class HatQuestion:
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers

def get_answer():
    respuesta = input("Debes seleccionar una opción (1, 2, 3, 4): ")
    if respuesta == "1" or respuesta == "2" or respuesta =="3" or respuesta == "4":
        return int(respuesta)
    
    return get_answer()





hay_questions = [HatQuestion("¿Cómo te definirías", 
                            [("1. Valiente", "gryffindor"), 
                            ("2. Leal", "hufflepuff"), 
                            ("3. Sabio", "ravenclaw"), 
                            ("4. Ambicioso", "slytherin")]),
                HatQuestion("¿Cúal es tu clase favorita?", 
                            [("1. Vuelo", "gryffindor"), 
                            ("2. Pociones", "ravenclaw"), 
                            ("3. Defensa contra las clases oscuras", "slytherin"), 
                            ("4. Animales fantásticos", "hufflepuff")])]

houses = {
    "gryffindor": 0,
    "hufflepuff": 0,
    "ravenclaw": 0,
    "slytherin": 0
}

for hat_question in hay_questions:

    print(hat_question.question)


    for answer in hat_question.answers:
        print(answer[0])

    house = hat_question.answers[get_answer() -1][1]

    houses[house] += 1

    print()

print(houses)

selected_house = []
max_points = 0
for house, points in houses.items():

    if points > max_points:
        selected_house.clear()
        selected_house.append(house)
        max_points = points
    elif points == max_points:
        selected_house.append(house)
        max_points = points

if len(selected_house) == 1:
    print(f"lo tengo claro {selected_house[0].capitalize()}")

else:
    print(f"lo tengo claro {random.choice(selected_house).capitalize()}")
    

print(f"La casa ganadora es {selected_house}")

