from flask import Flask, render_template, request, jsonify, redirect, url_for
import re
import math
import json
import random
from difflib import get_close_matches
import requests

app = Flask(__name__)


def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def find_best_match(user_question: str, questions: list) -> str | None:
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.7)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q['answer']
@app.route('/')
def hello_world():
    return render_template('index2.html')

@app.route('/AIlury')
def index_page():
    return render_template('index.html')
@app.route('/profile')
def index_page2():
    return render_template('index2.html')
@app.route('/privacy-policy-user-regulations')
def get_bot_response():
    return render_template('index3.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    data = request.get_json()
    knowledge_base = load_knowledge_base('knowledge_base.json')
    user_question = data['user_input'].lower()
    best_match = find_best_match(user_question, [q["question"] for q in knowledge_base["questions"]])
    if 'fuck' in user_question:
        response = {'message': 'Please watch your language'}
    elif "sex" in user_question:
         response = {'message': 'Please watch your language'}
    elif "bitch" in user_question:
        response = {'message': 'Please watch your language'}
    elif " ass" in user_question:
        response = {'message': 'Please watch your language'}
    elif "arschloch" in user_question:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hurensohn" in user_question:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hurentochter" in user_question:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hure" in user_question:
        response = {'message': 'Please watch your language'}
    elif "von deutsch zu hyraphisch" in user_question:
         user_question = user_question.replace("von deutsch zu hyraphisch", "")
         ersetzung_dict = {'A': '=', 'a': '=', 'B': '&', 'b': '&', 'C': '%', 'c': '%', 'D': '_', 'd': '_', 'E': '€', 'e': '€', 'F': '|', 'f': '|',  'G': '(',  'g': '(', 'H': ')',  'h': ')', 'I': '!', 'i': '!', 'J': ''', 'j': ''', 'K': '^', 'k': '^', 'L': '#', 'l': '#', 'M': '„', 'm': '„', 'N': '•', 'n': '•', 'O': '0', 'o': '0', 'P': '~', 'p': '~', 'Q': '@', 'q': '@', 'R': '<', 'r': '<', 'S': '>', 's': '>', 'T': '+', 't': '+', 'U': '3', 'u': '3', 'V': '7', 'v': '7', 'W': '5', 'w': '5', 'X': '*', 'x': '*', 'Y': '¥', 'y': '¥', 'Z': '/', 'z': '/', 'Ä': '1', 'ä': '1', 'Ö': ';', 'ö': ';', 'Ü': '$', 'ü': '$', ' ': ' ',}

         # Gehe durch jeden Buchstaben im Benutzereingabetext und ersetze ihn entsprechend
         ersetzer = str.maketrans(ersetzung_dict)
         neuer_text = user_question.translate(ersetzer)

         response = {'message': f'Der übersetzte Text: {neuer_text}'}
    elif "von hyraphisch zu deutsch" in user_question:
         user_question = user_question.replace("von hyraphisch zu deutsch", "")
         ersetzung_dict = {
             '=': 'A', '&': 'B', '%': 'C', '_': 'D', '€': 'E', '|': 'F', '(': 'G', ')': 'H',
             '!': 'I', "'": 'J', '^': 'K', '#': 'L', '„': 'M', '•': 'N', '0': 'O', '~': 'P',
             '@': 'Q', '<': 'R', '>': 'S', '+': 'T', '3': 'U', '7': 'V', '5': 'W', '*': 'X',
             '¥': 'Y', '/': 'Z', '1': 'Ä', ';': 'Ö', '$': 'Ü', ' ': ' '
         }

         # Gehe durch jeden Buchstaben im Benutzereingabetext und ersetze ihn entsprechend
         ersetzer = str.maketrans(ersetzung_dict)
         neuer_text = user_question.translate(ersetzer)

         response = {'message': f'Der übersetzte Text: {neuer_text}'}
    elif "wähle eine zahl" in user_question and "von" in user_question and "bis" in user_question:
      trash1, word1 = user_question.split("von", 1)
      trash2, word2 = word1.split("bis", 1)
      uword = re.findall(r'\b\d+\b', trash2)
      uword2 = re.findall(r'\b\d+\b', word2)
      uword = int(uword[0])
      uword2 = int(uword2[0])
      if uword > uword2:
          zahl = random.randint(uword2, uword)
      elif uword < uword2:
          zahl = random.randint(uword, uword2)
      else:
          zahl = uword
      response = {'message': f'ich wähle: {zahl}'}
    elif "choose a number" in user_question and "from" in user_question and "to" in user_question:
      trash1, word1 = user_question.split("from", 1)
      trash2, word2 = word1.split("to", 1)
      uword = re.findall(r'\b\d+\b', trash2)
      uword2 = re.findall(r'\b\d+\b', word2)
      uword = int(uword[0])
      uword2 = int(uword2[0])
      if uword > uword2:
          zahl = random.randint(uword2, uword)
      elif uword < uword2:
          zahl = random.randint(uword, uword2)
      else:
          zahl = uword
      response = {'message': f'i choose: {zahl}'}
    elif "choose a number" in user_question and "from" in user_question and "-" in user_question:
      trash1, word1 = user_question.split("from", 1)
      trash2, word2 = word1.split("-", 1)
      uword = re.findall(r'\b\d+\b', trash2)
      uword2 = re.findall(r'\b\d+\b', word2)
      uword = int(uword[0])
      uword2 = int(uword2[0])
      if uword > uword2:
          zahl = random.randint(uword2, uword)
      elif uword < uword2:
          zahl = random.randint(uword, uword2)
      else:
          zahl = uword
      response = {'message': f'i choose: {zahl}'}
    elif "choose a number" in user_question and "through" in user_question:
      trash1, word1 = user_question.split("number", 1)
      trash2, word2 = word1.split("through", 1)
      uword = re.findall(r'\b\d+\b', trash2)
      uword2 = re.findall(r'\b\d+\b', word2)
      uword = int(uword[0])
      uword2 = int(uword2[0])
      if uword > uword2:
          zahl = random.randint(uword2, uword)
      elif uword < uword2:
          zahl = random.randint(uword, uword2)
      else:
          zahl = uword
      response = {'message': f'i choose: {zahl}'}
    elif "ersetze" in user_question and "mit" in user_question and "in" in user_question:
      user_question = user_question.strip()
      teil1, teil2 = user_question.split("ersetze", 1)
      teil1 = teil1.strip()
      teil1 = teil1.replace("ersetze", "")
      teil3, teil4 = teil2.split("mit", 1)
      teil3 = teil3.strip()
      teil3 = teil3.replace("mit", "")
      teil5, teil6 = teil4.split("in", 1)
      teil5 = teil5.strip()
      teil5 = teil5.replace("in", "")
      if teil3 in teil6:
        teil6 = teil6.replace(teil3, teil5)
        response = {'message': f'Der bearbeitete Text: {teil6}'}
      else:
        response = {'message': f'sorry aber {teil5} ist nicht in {teil6}'}
    elif "replace" in user_question and "with" in user_question and "in" in user_question:
      user_question = user_question.strip()
      teil1, teil2 = user_question.split("replace", 1)
      teil1 = teil1.strip()
      teil1 = teil1.replace("replace", "")
      teil3, teil4 = teil2.split("with", 1)
      teil3 = teil3.strip()
      teil3 = teil3.replace("with", "")
      teil5, teil6 = teil4.split("in", 1)
      teil5 = teil5.strip()
      teil5 = teil5.replace("in", "")
      if teil3 in teil6:
        teil6 = teil6.replace(teil3, teil5)
        response = {'message': f'the edited Text: {teil6}'}
      else:
        response = {'message': f'sorry but {teil5} is not in {teil6}'}
    elif "gib mir" in user_question and "name" in user_question:

      Mnamen = ["Mia", "Laura", "Lara", "Lina", "Lisa", "Jana", "Lena", "Selena", "Sophia", "Emma", "Maja", "Lea", "Tina", "Helena", "Anna", "Sarah", "Maria", "Anna", "Sophie", "Emily", "Maya", "Melina", "Alice", "Olivia", "Isabella", "Ava", "Charlotte", "Cristina", "Laura", "Anne", "Julia", "Klara", "Bella", "Theresia", "Andrea", "Sofia", "Elena", "Nina", "Nicole", "Amelie", "Leane", "Elia", "Nya", "Naya", "Nora", "Sabrina", "Sabine", "Angelika", "Vanda", "Melinda", "Viktoria", "Liv", "Livia", "Liviana", "Matilda", "Victoria", "Fransiska"]
      Jnamen = ["Elias", "Jonas", "Jakob", "Johannes", "Johann", "Karl", "Kevin", "Linus", "Max", "Maximus", "Maximilian", "Moritz", "Moritz", "Moritz", "Moritz", "Paulo", "Paul", "Fritz", "Anton", "Franz", "Andre", "Andreas", "Peter", "Louis", "Leo", "Lukas", "Holger", "Jonathan", "Willi", "William", "Wilhelm", "Willy", "Viktor", "Victor", "Marcus", "Markus", "Marko", "Mark", "Michael", "Martin", "Kai", "Aleksander", "Alexander", "Alex", "Werner", "Otto", "Uwe", "Ulrich", "Uli", "Bernd", "Bernhard", "Igor", "Ivan", "Ivo", "Sven", "Stefan", "Hans", "Henrik", "Henry", "Herbert", "Herman", "Heinrich"]
      Anamen = [Mnamen, Jnamen]
      if "männlich" in user_question:
        response = {'message': f'wie wäre es mit: {random.choice(Jnamen)}.'}
      elif "jung" in user_question:
        response = {'message': f'wie wäre es mit: {random.choice(Jnamen)}.'}
      elif "weiblich" in user_question:
        response = {'message': f'wie Wäre es mit: {random.choice(Mnamen)}.'}
      elif "mädchen" in user_question:
        response = {'message': f'wie Wäre es mit: {random.choice(Mnamen)}.'}
      else:
        allenamen = random.choice(Anamen)
        response = {'message': f'wie wäre es mit: {random.choice(allenamen)}.'}
    elif "give me" in user_question and "name" in user_question:
      Mnamen = ["Mia", "laura", "Lara", "Lina", "Lisa", "Jenna", "Lena", "Selena", "Sophia", "Emma", "Skylor", "Lea", "Tina", "Dora", "Anna", "Sarah", "Maria", "Sophie", "Emily", "Melina", "Alice", "Olivia", "Isabella", "Ava", "Isabell", "Cristina", "Laura", "Julia", "Bella", "Theresa", "Andrea", "Sofia", "Elena", "Nina", "Nicole", "Elia", "Nya", "Naya", "Nora", "Sabrina", "Angelika", "Vanda", "Viktoria", "Liv", "Livia", "Liviana", "Matilda", "Victoria", "Carmen", "Fransiska"]
      Jnamen = ["Elias", "Cole", "Kevin", "Zane", "Max", "Maximus", "Maximilian", "Paulo", "Paul", "Andre", "Peter", "Louis", "Leo", "Lukas", "Jonathan", "Willi", "William", "Willy", "Viktor", "Victor", "Marcus", "Markus", "Marko", "Mark", "Michael", "Martin", "Kai", "Aleksander", "Alexander", "Alex", "Igor", "Ivan", "Sven", "Henrik", "Henry", "Robert", "Jimmy", "Cris"]
      Anamen = [Mnamen, Jnamen]
      if "girl" in user_question:
        response = {'message': f'what about this: {random.choice(Mnamen)}.'}
      elif "woman" in user_question:
        response = {'message': f'what about this: {random.choice(Mnamen)}.'}
      elif "female" in user_question:
        response = {'message': f'what about this: {random.choice(Mnamen)}.'}
      elif "feminine" in user_question:
        response = {'message': f'what about this: {random.choice(Mnamen)}.'}
      elif "boy" in user_question:
        response = {'message': f'what about this: {random.choice(Jnamen)}.'}
      elif "man" in user_question:
        response = {'message': f'what about this: {random.choice(Jnamen)}.'}
      elif "male" in user_question:
        response = {'message': f'what about this: {random.choice(Jnamen)}.'}
      elif "masculine" in user_question:
        response = {'message': f'what about this: {random.choice(Jnamen)}.'}
      else:
        allenamen = random.choice(Anamen)
        response = {'message': f'what about this: {random.choice(allenamen)}.'}
    elif "was wäre" in user_question and "ein" in user_question and "name für" in user_question:

      Mnamen = [
          "Mia", "Laura", "Lara", "Lina", "Lisa", "Jana", "Lena", "Selena", "Sophia", "Emma", "Maja", "Lea", "Tina", "Helena", "Anna", "Sarah", "Maria", "Anna", "Sophie", "Emily", "Maya", "Melina", "Alice", "Olivia", "Isabella", "Ava", "Charlotte", "Cristina", "Laura", "Anne", "Julia", "Klara", "Bella", "Theresia", "Andrea", "Sofia", "Elena", "Nina", "Nicole", "Amelie", "Leane", "Elia", "Nya", "Naya", "Nora", "Sabrina", "Sabine", "Angelika", "Vanda", "Melinda", "Viktoria", "Liv", "Livia", "Liviana", "Matilda", "Victoria", "Fransiska"
      ]
      Jnamen = [
          "Elias", "Jonas", "Jakob", "Johannes", "Johann", "Karl", "Kevin", "Linus", "Max", "Maximus", "Maximilian", "Moritz", "Moritz", "Moritz", "Moritz", "Paulo", "Paul", "Fritz", "Anton", "Franz", "Andre", "Andreas", "Peter", "Louis", "Leo", "Lukas", "Holger", "Jonathan", "Willi", "William", "Wilhelm", "Willy", "Viktor", "Victor", "Marcus", "Markus", "Marko", "Mark", "Michael", "Martin", "Kai", "Aleksander", "Alexander", "Alex", "Werner", "Otto", "Uwe", "Ulrich", "Uli", "Bernd", "Bernhard", "Igor", "Ivan", "Ivo", "Sven", "Stefan", "Hans", "Henrik", "Henry", "Herbert", "Herman", "Heinrich"
      ]
      Anamen = [Mnamen, Jnamen]
      user2 = user_question
      trash, word1 = user2.split("name für", 1)
      word1 = word1.replace("?", "")
      word1 = word1.replace("meine", "deine")
      word1 = word1.replace("mein", "dein")
      word1 = word1.replace("dein", "mein")
      word1 = word1.replace("deine", "meine")
      word = word1.replace("dich", "mich")
        
      if "männlich" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Jnamen)}" sein.'}
      elif "jung" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Jnamen)}" sein.'}
      elif "weiblich" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Mnamen)}" sein.'}
      elif "mädchen" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Mnamen)}" sein.'}
      else:
        allenamen = random.choice(Anamen)
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(allenamen)}" sein.'}
    elif "wie sollte" in user_question and "ich" in user_question and "nennen" in user_question:

      Mnamen = [
          "Mia", "Laura", "Lara", "Lina", "Lisa", "Jana", "Lena", "Selena", "Sophia", "Emma", "Maja", "Lea", "Tina", "Helena", "Anna", "Sarah", "Maria", "Anna", "Sophie", "Emily", "Maya", "Melina", "Alice", "Olivia", "Isabella", "Ava", "Charlotte", "Cristina", "Laura", "Anne", "Julia", "Klara", "Bella", "Theresia", "Andrea", "Sofia", "Elena", "Nina", "Nicole", "Amelie", "Leane", "Elia", "Nya", "Naya", "Nora", "Sabrina", "Sabine", "Angelika", "Vanda", "Melinda", "Viktoria", "Liv", "Livia", "Liviana", "Matilda", "Victoria", "Fransiska"
      ]
      Jnamen = [
          "Elias", "Jonas", "Jakob", "Johannes", "Johann", "Karl", "Kevin", "Linus", "Max", "Maximus", "Maximilian", "Moritz", "Moritz", "Moritz", "Moritz", "Paulo", "Paul", "Fritz", "Anton", "Franz", "Andre", "Andreas", "Peter", "Louis", "Leo", "Lukas", "Holger", "Jonathan", "Willi", "William", "Wilhelm", "Willy", "Viktor", "Victor", "Marcus", "Markus", "Marko", "Mark", "Michael", "Martin", "Kai", "Aleksander", "Alexander", "Alex", "Werner", "Otto", "Uwe", "Ulrich", "Uli", "Bernd", "Bernhard", "Igor", "Ivan", "Ivo", "Sven", "Stefan", "Hans", "Henrik", "Henry", "Herbert", "Herman", "Heinrich"
      ]
      Anamen = [Mnamen, Jnamen]
      user2 = user_question
      trash, word1 = user2.split("ich", 1)
      word1 = word1.replace("?", "")
      word1 = word1.replace("meine", "deine")
      word1 = word1.replace("mein", "dein")
      word1 = word1.replace("dein", "mein")
      word1 = word1.replace("deine", "meine")
      word = word1.replace("dich", "mich")
      word = word.replace("nennen", "")

      if "männlich" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Jnamen)}" sein.'}
      elif "jung" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Jnamen)}" sein.'}
      elif "weiblich" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Mnamen)}" sein.'}
      elif "mädchen" in user_question:
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(Mnamen)}" sein.'}
      else:
        allenamen = random.choice(Anamen)
        response = {'message': f'ich glaube ein guter name für {word} könnte: "{random.choice(allenamen)}" sein.'}
    elif "what would be" in user_question and "a" in user_question and "name for" in user_question:

      Mnamen = ["Mia", "laura", "Lara", "Lina", "Lisa", "Jenna", "Lena", "Selena", "Sophia", "Emma", "Skylor", "Lea", "Tina", "Dora", "Anna", "Sarah", "Maria", "Sophie", "Emily", "Melina", "Alice", "Olivia", "Isabella", "Ava", "Isabell", "Cristina", "Laura", "Julia", "Bella", "Theresa", "Andrea", "Sofia", "Elena", "Nina", "Nicole", "Elia", "Nya", "Naya", "Nora", "Sabrina", "Angelika", "Vanda", "Viktoria", "Liv", "Livia", "Liviana", "Matilda", "Victoria", "Carmen", "Fransiska"]
      Jnamen = ["Elias", "Cole", "Kevin", "Zane", "Max", "Maximus", "Maximilian", "Paulo", "Paul", "Andre", "Peter", "Louis", "Leo", "Lukas", "Jonathan", "Willi", "William", "Willy", "Viktor", "Victor", "Marcus", "Markus", "Marko", "Mark", "Michael", "Martin", "Kai", "Aleksander", "Alexander", "Alex", "Igor", "Ivan", "Sven", "Henrik", "Henry", "Robert", "Jimmy", "Cris"]
      Anamen = [Mnamen, Jnamen]
      user2 = user_question
      trash, word = user2.split("name for", 1)
      word = word.replace("?", "")
      word = word.replace("my self", "you")
      word = word.replace("my ", "your ")
      word = word.replace("your ", "my ")
      word = word.replace("you", "me")

      if "male" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Jnamen)}".'}
      elif "boy" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Jnamen)}".'}
      elif "female" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Mnamen)}".'}
      elif "girl" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Mnamen)}".'}
      else:
        allenamen = random.choice(Anamen)
        response = {'message': f'i think a good name for {word} could be: "{random.choice(allenamen)}".'}
    elif "how should" in user_question and "i" in user_question and "call" in user_question:

      Mnamen = ["Mia", "laura", "Lara", "Lina", "Lisa", "Jenna", "Lena", "Selena", "Sophia", "Emma", "Skylor", "Lea", "Tina", "Dora", "Anna", "Sarah", "Maria", "Sophie", "Emily", "Melina", "Alice", "Olivia", "Isabella", "Ava", "Isabell", "Cristina", "Laura", "Julia", "Bella", "Theresa", "Andrea", "Sofia", "Elena", "Nina", "Nicole", "Elia", "Nya", "Naya", "Nora", "Sabrina", "Angelika", "Vanda", "Viktoria", "Liv", "Livia", "Liviana", "Matilda", "Victoria", "Carmen", "Fransiska"]
      Jnamen = ["Elias", "Cole", "Kevin", "Zane", "Max", "Maximus", "Maximilian", "Paulo", "Paul", "Andre", "Peter", "Louis", "Leo", "Lukas", "Jonathan", "Willi", "William", "Willy", "Viktor", "Victor", "Marcus", "Markus", "Marko", "Mark", "Michael", "Martin", "Kai", "Aleksander", "Alexander", "Alex", "Igor", "Ivan", "Sven", "Henrik", "Henry", "Robert", "Jimmy", "Cris"]
      Anamen = [Mnamen, Jnamen]
      user2 = user_question
      trash, word = user2.split("call", 1)
      word = word.replace("?", "")
      word = word.replace("my self", "you")
      word = word.replace("my ", "your ")
      word = word.replace("your ", "my ")
      word = word.replace("you", "me")

      if "male" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Jnamen)}".'}
      elif "boy" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Jnamen)}".'}
      elif "female" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Mnamen)}".'}
      elif "girl" in user_question:
        response = {'message': f'i think a good name for {word} could be: "{random.choice(Mnamen)}".'}
      else:
        allenamen = random.choice(Anamen)
        response = {'message': f'i think a good name for {word} could be: "{random.choice(allenamen)}".'}
    elif "gib mir" in user_question and "passwort" in user_question:
          random_number = random.randint(100000, 999999)
          random_index = random.randint(0, 5)
          random_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
          random_number2 = random.randint(100000, 999999)
          random_index2 = random.randint(0, 5)
          random_letter2 = random.choice("abcdefghijklmnopqrstuvwxyz")
          random_lr = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6))
          password_with_letter = str(random_number).replace(str(random_number)[random_index], random_letter)
          password_with_letter2 = str(random_number2).replace(str(random_number2)[random_index2], str(random_number2))
          random_number3 = str(random_number).replace(str(random_number2)[random_index2], str(random_number))
          random_letter3 = random_lr.replace(random_letter2, random_letter)
          if 'nummer' in user_question:
              response = {'message': f'Bitte beachten Sie, dass das Passwort zufällig generiert ist. Hier ist das Passwort: {password_with_letter2}'}
          elif 'buchstabe' in user_question:
              response = {'message': f'Bitte beachten Sie, dass das Passwort zufällig generiert ist. Hier ist das Passwort: {random_letter3}'}
          else:
              response = {'message': f'Bitte beachten Sie, dass das Passwort zufällig generiert ist. Hier ist das Passwort: {password_with_letter}'}
    elif "give me" in user_question and "password" in user_question:
          random_number = random.randint(100000, 999999)
          random_index = random.randint(0, 5)
          random_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
          random_number2 = random.randint(100000, 999999)
          random_index2 = random.randint(0, 5)
          random_letter2 = random.choice("abcdefghijklmnopqrstuvwxyz")
          random_lr = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(6))
          password_with_letter = str(random_number).replace(str(random_number)[random_index], random_letter)
          password_with_letter2 = str(random_number2).replace(str(random_number2)[random_index2], str(random_number2))
          random_number3 = str(random_number).replace(str(random_number2)[random_index2], str(random_number))
          random_letter3 = random_lr.replace(random_letter2, random_letter)
          if 'number' in user_question:
              response = {'message': f'Please note that the password is randomly generated. Here is the password: {password_with_letter2}'}
          elif 'letter' in user_question:
              response = {'message': f'Please note that the password is randomly generated. Here is the password: {random_letter3}'}
          else:
              response = {'message': f'Please note that the password is randomly generated. Here is the password: {password_with_letter}'}
    elif "sag:" in user_question:
      text = user_question.replace("sag:", "")
      response = {'message': f'{text}'}
    elif "sag mir:" in user_question:
      text = user_question.replace("sag mir:", "")
      response = {'message': f'{text}'}
    elif "say:" in user_question:
      text = user_question.replace("say:", "")
      response = {'message': f'{text}'}
    elif "ich bin " in user_question:
      try:
          age = int(user_question.split("ich bin")[1].strip())
          max_human_age = 122  # Maximales dokumentiertes Alter eines Menschen
          if age > max_human_age:
              response = {'message': 'So alt kann ein Mensch nicht werden.'}
          else:
              response = {'message': 'Cool!'}
      except ValueError:
          response = {'message': 'okay'}
    elif "i am " in user_question:
      try:
          age = int(user_question.split("i am")[1].strip())
          max_human_age = 122  # Maximales dokumentiertes Alter eines Menschen
          if age > max_human_age:
              response = {'message': 'A Human can not get that old'}
          else:
              response = {'message': 'Cool!'}
      except ValueError:
          response = {'message': 'okay'}
    elif "zähle bis" in user_question:
      try:
          #number = int(user_question.split("zähle bis")[1].strip())
          number = re.findall(r'\b\d+\b', user_question)
          number = int(number[0])
          if number > 0:
              count_list = ", ".join(str(i) for i in range(1, number + 1))
              response = {'message': f'Ich zähle bis {number}: {count_list}'}
          else:
              response = {'message': 'Bitte geben Sie eine positive Zahl an.'}
      except ValueError:
          response = {'message': 'Bitte geben Sie eine gültige Zahl an.'}
    elif "count till" in user_question:
      try:
        #number = int(user_question.split("count till")[1].strip())
        number = re.findall(r'\b\d+\b', user_question)
        number = int(number[0])
        if number > 0:
            count_list = ", ".join(str(i) for i in range(1, number + 1))
            response = {'message': f'okay, i will count till {number}: {count_list}'}
        else:
            response = {'message': 'Please enter a positive number.'}
      except ValueError:
        response = {'message': 'Please enter a valid number.'}
    elif "count to" in user_question:
      try:
        number = re.findall(r'\b\d+\b', user_question)
        number = int(number[0])
        if number > 0:
            count_list = ", ".join(str(i) for i in range(1, number + 1))
            response = {'message': f'okay, i will count till {number}: {count_list}'}
        else:
            response = {'message': 'Please enter a positive number.'}
      except ValueError:
        response = {'message': 'Please enter a valid number.'}
    elif "zähl bis" in user_question:
      try:
          #number = int(user_question.split("zähle bis")[1].strip())
          number = re.findall(r'\b\d+\b', user_question)
          number = int(number[0])
          if number > 0:
              count_list = ", ".join(str(i) for i in range(1, number + 1))
              response = {'message': f'Ich zähle bis {number}: {count_list}'}
          else:
              response = {'message': 'Bitte geben Sie eine positive Zahl an.'}
      except ValueError:
          response = {'message': 'Bitte geben Sie eine gültige Zahl an.'}
    elif "nimm" in user_question and "aus" in user_question:
        userR = user_question.strip()
        userR = userR.replace("heraus", "")
        # Ersetzung durchführen und das Ergebnis zuweisen
        if "aus" in userR:
            userS1, userS2 = userR.split("aus", 1)
            userS1 = userS1.strip()
            userS2 = userS2.strip()
            nimm_keyword, userS1 = userS1.split(" ", 1)  # Trenne das erste Wort vom Rest des Satzes
            userRS = userS2.replace(userS1, "").strip()  # Entferne das Wort aus userS1 aus userS2
            response = {'message': f'Okay, "{userS1}" aus "{userS2}" ist "{userRS}".'}

        else:
            response = {'message': 'I dont know the answer. Please enter my answer to that question'}
    elif "take" in user_question and "out of" in user_question:
      userR = user_question.strip()
      if "out of" in userR:
          userS1, userS2 = userR.split("out of", 1)
          userS1 = userS1.strip()
          userS2 = userS2.strip()
          nimm_keyword, userS1 = userS1.split(" ", 1)  # Trenne das erste Wort vom Rest des Satzes
          userRS = userS2.replace(userS1, "").strip()  # Entferne das Wort aus userS1 aus userS2
          response = {'message': f'Okay, "{userS1}" out of "{userS2}" is "{userRS}".'}

      else:
            response = {'message': 'sorry but i cant answer to that'}
    elif "ist " in user_question and " in " in user_question:
      userR = user_question.strip()
      userR = userR.replace("?", "")
      # Ersetzung durchführen und das Ergebnis zuweisen
      if "in" in userR:
          userS1, userS2 = userR.split("in", 1)
          userS1 = userS1.strip()
          userS2 = userS2.strip()
          userS1 = userS1.replace('“', '')
          userS1 = userS1.replace('„', '')
          nimm_keyword, userS1 = userS1.split(" ", 1)  # Trenne das erste Wort vom Rest des Satzes
            # Entferne das Wort aus userS1 aus userS2
          if userS1 in userS2:
            response = {'message': f'ja, "{userS1}" ist in "{userS2}"'}
          else:
            response = {'message': f'nein, "{userS1}" ist nicht in "{userS2}"'}
    elif '√' in user_question:
        zahlen = re.findall(r'\b\d+\b', user_question)
        if len(zahlen) != 1:
            response = {'message': 'I dont know the answer. Please enter my answer to that question'}
        else:
            number = int(zahlen[0])
            ergebnis = math.sqrt(number)
            response = {'message': f'√{number} = {ergebnis}.'}
    elif '=' in user_question:
        zahlen = re.findall(r'\b\d+\b', user_question)
        if len(zahlen) != 2:
            response = {'message': 'sorry but i didnt find a mathematical operation'}
        else:
            question, answer = zahlen
            ergebnis1 = int(question)
            ergebnis2 = int(answer)
            if ergebnis1 == ergebnis2:
                response = {'message': f'{question} = {answer} = True'}
            else:
                response = {'message': f'{question} = {answer} = False.'}
    elif '>' in user_question:
        zahlen = re.findall(r'\b\d+\b', user_question)
        if len(zahlen) != 2:
            response = {'message': 'sorry but i didnt find a mathematical operation'}
        else:
            question, answer = zahlen
            ergebnis1 = int(question)
            ergebnis2 = int(answer)
            if ergebnis1 == ergebnis2:
                response = {'message': f'{question} = {answer}'}
            elif ergebnis1 >= ergebnis2:
                response = {'message': f'{question} > {answer} = True'}
            elif ergebnis1 == ergebnis2:
                response = {'message': f'{question} = {answer}'}
            else:
                response = {'message': f'{question} > {answer} = False.'}
    elif '<' in user_question:
        zahlen = re.findall(r'\b\d+\b', user_question)
        if len(zahlen) != 2:
            response = {'message': 'sorry but i didnt find a mathematical operation'}
        else:
            question, answer = zahlen
            ergebnis1 = int(question)
            ergebnis2 = int(answer)
            if ergebnis1 == ergebnis2:
                response = {'message': f'{question} = {answer}'}
            elif ergebnis1 <= ergebnis2:
                response = {'message': f'{question} < {answer} = True'}
            else:
                response = {'message': f'{question} < {answer} = False.'}
    elif "is " in user_question and " in " in user_question:
        userR = user_question.strip()
        userR = userR.replace("?", "")
        # Ersetzung durchführen und das Ergebnis zuweisen
        if "in" in userR:
            userS1, userS2 = userR.split("in", 1)
            userS1 = userS1.strip()
            userS2 = userS2.strip()
            userS1 = userS1.replace('“', '')
            userS1 = userS1.replace('„', '')
            nimm_keyword, userS1 = userS1.split(" ", 1)
            if userS1 in userS2:
              response = {'message': f'yes, "{userS1}" is in "{userS2}"'}
            else:
              response = {'message': f'no, "{userS1}" is not in "{userS2}"'}

        else:
              response = {'message': 'I dont know the answer. Please enter my answer to that question'}
    elif "korrigiere:" in user_question:
      user_question = user_question.replace("korrigiere:", "")
      from difflib import SequenceMatcher

      question_answers = {
          "ersetze": "ersetzt",
          "ersetzen": "ersetzen",
          "ersetzt": "ersetzt",
          "ersetz": "ersetz",
          "halli hallo hallöchen": "hallo",
          "hallo": "hallo",
          "gehts": "gehts",
          "geht": "geht",
          "mir": "mir",
          "dir": "dir",
          "ich": "ich",
          "du": "du",
          "er": "er",
          "sie": "sie",
          "es": "es",
          "wir": "wir",
          "ihr": "ihr",
          "alle": "alle",
          "jeder": "jeder",
          "jemand": "jemand",
          "jemanden": "jemanden",
          "manche ": "manche ",
          "mancher ": "mancher ",
          "manches ": "manches ",
          "manchen ": "manchen ",
          "manchmal ": "manchmal ",
          "allen ": "allen ",
          "wer": " wer",
          "gott": " gott",
          "göttin": " göttin",
          "mama": "mama",
          "mami": "mama",
          "sauer": "sauer",
          "sau": "sau",
          "sauen": "sauen",
          "lila": "lila",
          "rosa": "rosa",
          "rot": "rot",
          "grün": "grün",
          "blau": "blau",
          "gelb": "gelb",
          "schwarz": "schwarz",
          "weiß": "weiß",
          "braun": "braun",
          "orange": "orange",
          "pink": "pink",
          "violett": "violett",
          "kühlschrank": "kühlschrank",
          "tisch": "tisch",
          "stool": "stool",
          "sofa": "sofa",
          "schrank": "schrank",
          "maus": "maus",
          "mausi": "mausi",
          "lol": "lol",
          "lolli": "lolli",
          "schlafen": "schlafen",
          "träumen": "träumen",
          "schwimmen": "schwimmen",
          "tauchen": "tauchen",
          "fliegen": "fliegen",
          "rennen": "rennen",
          "spazieren": "spazieren",
          "klettern": "klettern",
          "springen": "springen",
          "tanzen": "tanzen",
          "sing": "sing",
          "musik": "musik",
          "kunst": "kunst",
          "malen": "malen",
          "zeichnen": "zeichnen",
          "basteln": "basteln",
          "kreieren": "kreieren",
          "entdecken": "entdecken",
          "erforschen": "erforschen",
          "experimentieren": "experimentieren",
          "lernen": "lernen",
          "lehren": "lehren",
          "studieren": "studieren",
          "ausprobieren": "ausprobieren",
          "entwickeln": "entwickeln",
          "verbessern": "verbessern",
          "ändern": "ändern",
          "anpassen": "anpassen",
          "vorstellen": "vorstellen",
          "fantasieren": "fantasieren",
          "hoffen": "hoffen",
          "wünschen": "wünschen",
          "planen": "planen",
          "organisieren": "organisieren",
          "verwalten": "verwalten",
          "koordinieren": "koordinieren",
          "führen": "führen",
          "folgen": "folgen",
          "nachfolgen": "nachfolgen",
          "befolgen": "befolgen",
          "anführen": "anführen",
          "geleiten": "geleiten",
          "begleiten": "begleiten",
          "unterstützen": "unterstützen",
          "helfen": "helfen",
          "beobachten": "beobachten",
          "erkunden": "erkunden",
          "wandern": "wandern",
          "fotografieren": "fotografieren",
          "filmen": "filmen",
          "aufnehmen": "aufnehmen",
          "dokumentieren": "dokumentieren",
          "analysieren": "analysieren",
          "interpretieren": "interpretieren",
          "bewerten": "bewerten",
          "bewundern": "bewundern",
          "anbeten": "anbeten",
          "schätzen": "schätzen",
          "genießen": "genießen",
          "freuen": "freuen",
          "lachen": "lachen",
          "glücklich": "glücklich",
          "fröhlich": "fröhlich",
          "traurig": "traurig",
          "weinen": "weinen",
          "lächeln": "lächeln",
          "schmunzeln": "schmunzeln",
          "grinsen": "grinsen",
          "gähnen": "gähnen",
          "schluchzen": "schluchzen",
          "schrei": "schrei",
          "brüllen": "brüllen",
          "flüstern": "flüstern",
          "singen": "singen",
          "bewegen": "bewegen",
          "laufen": "laufen",
          "gehen": "gehen",
          "kriechen": "kriechen",
          "rutschen": "rutschen",
          "stolpern": "stolpern",
          "fallen": "fallen",
          "aufstehen": "aufstehen",
          "sitzen": "sitzen",
          "liegen": "liegen",
          "ruhen": "ruhen",
          "atmen": "atmen",
          "abenteuer": "abenteuer",
          "erleben": "erleben",
          "wachsen": "wachsen",
          "trainieren": "trainieren",
          "üben": "üben",
          "meistern": "meistern",
          "perfektionieren": "perfektionieren",
          "weiterentwickeln": "weiterentwickeln",
          "erfinden": "erfinden",
          "erschaffen": "erschaffen",
          "gestalten": "gestalten",
          "entwerfen": "entwerfen",
          "modellieren": "modellieren",
          "formen": "formen",
          "herstellen": "herstellen",
          "produzieren": "produzieren",
          "aufbauen": "aufbauen",
          "konstruieren": "konstruieren",
          "installieren": "installieren",
          "konfigurieren": "konfigurieren",
          "einstellen": "einstellen",
          "präsentieren": "präsentieren",
          "darstellen": "darstellen",
          "visualisieren": "visualisieren",
          "beschreiben": "beschreiben",
          "erklären": "erklären",
          "verstehen": "verstehen",
          "begreifen": "begreifen",
          "nachvollziehen": "nachvollziehen",
          "verinnerlichen": "verinnerlichen",
          "anwenden": "anwenden",
          "nutzen": "nutzen",
          "einsetzen": "einsetzen",
          "verwenden": "verwenden",
          "auswerten": "auswerten",
          "beurteilen": "beurteilen",
          "klassifizieren": "klassifizieren",
          "kategorisieren": "kategorisieren",
          "identifizieren": "identifizieren",
          "erkennen": "erkennen",
          "diagnostizieren": "diagnostizieren",
          "zuordnen": "zuordnen",
          "vergleichen": "vergleichen",
          "kontrastieren": "kontrastieren",
          "unterscheiden": "unterscheiden",
          "untersuchen": "untersuchen",
          "nachforschen": "nachforschen",
          "ergründen": "ergründen",
          "prüfen": "prüfen",
          "testen": "testen",
          "überprüfen": "überprüfen",
          "validieren": "validieren",
          "verifizieren": "verifizieren",
          "bestätigen": "bestätigen",
          "abgleichen": "abgleichen",
          "überwachen": "überwachen",
          "kontrollieren": "kontrollieren",
          "aufpassen": "aufpassen",
          "überblicken": "überblicken",
          "verfolgen": "verfolgen",
          "nachverfolgen": "nachverfolgen",
          "aufzeichnen": "aufzeichnen",
          "protokollieren": "protokollieren",
          "registrieren": "registrieren",
          "notieren": "notieren",
          "aufschreiben": "aufschreiben",
          "merken": "merken",
          "erinnern": "erinnern",
          "sich erinnern": "sich erinnern",
          "gedenken": "gedenken",
          "memorieren": "memorieren",
          "abspeichern": "abspeichern",
          "speichern": "speichern",
          "archivieren": "archivieren",
      }

      def find_similar_word(word):
          max_similarity = 0
          similar_word = None
          for question, answer in question_answers.items():
              similarity = SequenceMatcher(None, word, question).ratio()
              if similarity >= 0.8 and similarity > max_similarity:
                  max_similarity = similarity
                  similar_word = answer
          return similar_word

      def replace_similar_word(text):
          words = text.split()
          replaced_text = []
          for word in words:
              similar_word = find_similar_word(word)
              if similar_word:
                  replaced_text.append(similar_word)
              else:
                  replaced_text.append(word)
          return " ".join(replaced_text)
      result = replace_similar_word(user_question)
      response = {'message': f'hier ist der text: {result}'}
    elif "correct:" in user_question:
      user_question = user_question.replace("correct:", "")
      from difflib import SequenceMatcher

      question_answers = {
          "have": "have",
          "has": "has",
          "having": "having",
          "had": "had",
          "do": "do",
          "does": "does",
          "did": "did",
          "will": "will",
          "would": "would",
          "shall": "shall",
          "should": "should",
          "can": "can",
          "could": "could",
          "may": "may",
          "might": "might",
          "must": "must",
          "need": "need",
          "ought": "ought",
          "are": "are",
          "were": "were",
          "where": "where",
          "be": "be",
          "been": "been",
          "being": "being",
          "become": "become",
          "became": "became",
          "you": "you",
          "your": "your",
          "you're": "you're",
          "you've": "you've",
          "you'll": "you'll",
          "you'd": "you'd",
          "youuu": "you",
          "replaced": "replaced",
          "replace": "replace",
          "hello hi howdy": "hello",
          "hello": "hello",
          "how are you": "how are you",
          "go": "go",
          "to me": "to me",
          "to you": "to you",
          "I": "I",
          "you": "you",
          "he": "he",
          "she": "she",
          "it": "it",
          "we": "we",
          "all": "all",
          "everyone": "everyone",
          "someone": "someone",
          "some": "some",
          "sometimes": "sometimes",
          "who": "who",
          "god": "god",
          "goddess": "goddess",
          "mom": "mom",
          "mommy": "mom",
          "sour": "sour",
          "sow": "sow",
          "lilac": "lilac",
          "pink": "pink",
          "red": "red",
          "green": "green",
          "blue": "blue",
          "yellow": "yellow",
          "black": "black",
          "white": "white",
          "brown": "brown",
          "orange": "orange",
          "purple": "purple",
          "refrigerator": "refrigerator",
          "table": "table",
          "stool": "stool",
          "couch": "couch",
          "cabinet": "cabinet",
          "mouse": "mouse",
          "mousey": "mousey",
          "lol": "lol",
          "lollipop": "lollipop",
          "sleep": "sleep",
          "dream": "dream",
          "swim": "swim",
          "dive": "dive",
          "fly": "fly",
          "run": "run",
          "walk": "walk",
          "climb": "climb",
          "jump": "jump",
          "dance": "dance",
          "sing": "sing",
          "music": "music",
          "art": "art",
          "paint": "paint",
          "draw": "draw",
          "craft": "craft",
          "create": "create",
          "explore": "explore",
          "experiment": "experiment",
          "learn": "learn",
          "teach": "teach",
          "study": "study",
          "try out": "try out",
          "develop": "develop",
          "improve": "improve",
          "change": "change",
          "adapt": "adapt",
          "imagine": "imagine",
          "fantasize": "fantasize",
          "hope": "hope",
          "wish": "wish",
          "plan": "plan",
          "organize": "organize",
          "manage": "manage",
          "coordinate": "coordinate",
          "lead": "lead",
          "follow": "follow",
          "succeed": "succeed",
          "follow up": "follow up",
          "guide": "guide",
          "accompany": "accompany",
          "support": "support",
          "help": "help",
          "observe": "observe",
          "hike": "hike",
          "photograph": "photograph",
          "film": "film",
          "record": "record",
          "document": "document",
          "analyze": "analyze",
          "interpret": "interpret",
          "evaluate": "evaluate",
          "admire": "admire",
          "worship": "worship",
          "appreciate": "appreciate",
          "enjoy": "enjoy",
          "rejoice": "rejoice",
          "laugh": "laugh",
          "happy": "happy",
          "cheerful": "cheerful",
          "sad": "sad",
          "cry": "cry",
          "smile": "smile",
          "grin": "grin",
          "yawn": "yawn",
          "sob": "sob",
          "scream": "scream",
          "roar": "roar",
          "whisper": "whisper",
          "move": "move",
          "crawl": "crawl",
          "slide": "slide",
          "stumble": "stumble",
          "fall": "fall",
          "get up": "get up",
          "sit": "sit",
          "lie": "lie",
          "rest": "rest",
          "breathe": "breathe",
          "adventure": "adventure",
          "experience": "experience",
          "grow": "grow",
          "train": "train",
          "practice": "practice",
          "master": "master",
          "perfect": "perfect",
          "invent": "invent",
          "shape": "shape",
          "design": "design",
          "model": "model",
          "form": "form",
          "manufacture": "manufacture",
          "produce": "produce",
          "build": "build",
          "construct":  "construct",
          "install": "install",
          "configure": "configure",
          "adjust": "adjust",
          "present": "present",
          "depict": "depict",
          "visualize": "visualize",
          "describe": "describe",
          "explain": "explain",
          "understand": "understand",
          "comprehend": "comprehend",
          "grasp": "grasp",
          "apply": "apply",
          "use": "use",
          "employ": "employ",
          "utilize": "utilize",
          "assess": "assess",
          "classify": "classify",
          "categorize": "categorize",
          "identify": "identify",
          "recognize": "recognize",
          "diagnose": "diagnose",
          "assign": "assign",
          "compare": "compare",
          "contrast": "contrast",
          "distinguish": "distinguish",
          "examine": "examine",
          "research": "research",
          "investigate": "investigate",
          "probe": "probe",
          "scrutinize": "scrutinize",
          "test": "test",
          "check": "check",
          "verify": "verify",
          "validate": "validate",
          "confirm": "confirm",
          "match": "match",
          "monitor": "monitor",
          "control": "control",
          "watch out": "watch out",
          "oversee": "oversee",
          "track": "track",
          "trace": "trace",
          "log": "log",
          "register": "register",
          "note": "note",
          "write down": "write down",
          "remember": "remember",
          "recall": "recall",
          "memorize": "memorize",
          "save": "save",
          "store": "store",
          "archive": "archive",
      }

      def find_similar_word(word):
          max_similarity = 0
          similar_word = None
          for question, answer in question_answers.items():
              similarity = SequenceMatcher(None, word, question).ratio()
              if similarity >= 0.8 and similarity > max_similarity:
                  max_similarity = similarity
                  similar_word = answer
          return similar_word

      def replace_similar_word(text):
          words = text.split()
          replaced_text = []
          for word in words:
              similar_word = find_similar_word(word)
              if similar_word:
                  replaced_text.append(similar_word)
              else:
                  replaced_text.append(word)
          return " ".join(replaced_text)
      result = replace_similar_word(user_question)
      response = {'message': f'hier ist der text: {result}'}
    elif "how do" in user_question and "spell" in user_question:
      # spell the word after the found text and put a , after each letter
      trashword, word = user_question.split("spell", 1)
      word = word.replace(':', '')
      word = word.strip()
      # , here
      word = ",".join(word)
      response = {'message': f'{word}'}
    elif "how can" in user_question and "spell" in user_question:
      # spell the word after the found text and put a , after each letter
      trashword, word = user_question.split("spell", 1)
      word = word.replace(':', '')
      word = word.strip()
      # , here
      word = ",".join(word)
      response = {'message': f'{word}'}
    elif "wie buchstabiert man" in user_question:
      trashword, word = user_question.split("wie buchstabiert man", 1)
      word = word.replace(':', '')
      word = word.strip()
      # , here
      word = ",".join(word)
      response = {'message': f'{word}'}
    elif "wie buchstabiere ich" in user_question:
      trashword, word = user_question.split("wie buchstabiere ich", 1)
      word = word.replace(':', '')
      word = word.strip()
      # , here
      word = ",".join(word)
      response = {'message': f'{word}'}
    elif "wie kann ich" in user_question and "buchstabieren" in user_question:
      trashword, word = user_question.split("wie kann ich", 1)
      word = word.replace(':', '')
      word = word.strip()
      # , here
      word = ",".join(word)
      response = {'message': f'{word}'}
    elif any(char.isdigit() or char in "+-*/" for char in user_question):
      try:
          # Berechne und gib das Ergebnis aus
          expression = re.sub('[a-zA-Z\s]', '', user_question)

          # Finde alle Zahlen und mathematischen Operationen
          numbers = re.findall(r'\d+', user_question)
          operations = re.findall(r'[-+*/]', user_question)

          # Führe die mathematischen Operationen durch
          result = int(numbers[0])
          num_index = 1
          for op in operations:
              num = int(numbers[num_index])
              if op == '+':
                  result += num
              elif op == '-':
                  result -= num
              elif op == '*':
                  result *= num
              elif op == '/':
                  result /= num
              num_index += 1

          response = {'message': f'{result}.'}
      except Exception as e:
          answer = get_answer_for_question(best_match, knowledge_base)
          response = {'message': f'{answer}'}

    elif best_match:
      answer = get_answer_for_question(best_match, knowledge_base)
      response = {'message': f'{answer}'}

    else:
        response = {'message': 'I dont know the answer. Please enter my answer to that question'}

    return jsonify(response)

@app.route('/new_knowledge', methods=['POST'])
def new_knowledge():
    data = request.get_json()
    knowledge_base = load_knowledge_base('knowledge_base.json')
    new_question = data['new_question'].lower()
    new_answer = data['user_input'].lower()
    if 'fuck' in new_question:
        response = {'message': 'Please watch your language'}
    elif "sex" in new_question:
         response = {'message': 'Please watch your language'}
    elif "bitch" in new_question:
        response = {'message': 'Please watch your language'}
    elif " ass" in new_question:
        response = {'message': 'Please watch your language'}
    elif "i dont know the answer. please enter my answer to that question" in new_question:
        response = {'message': 'sorry, this input ist not eccepted'}
    elif "arschloch" in new_question:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hurensohn" in new_question:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hurentochter" in new_question:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hure" in new_question:
        response = {'message': 'Please watch your language'}
    elif 'fuck' in new_answer:
        response = {'message': 'Please watch your language'}
    elif "sex" in new_answer:
         response = {'message': 'Please watch your language'}
    elif "bitch" in new_answer:
        response = {'message': 'Please watch your language'}
    elif " ass" in new_answer:
        response = {'message': 'Please watch your language'}
    elif "i dont know the answer. please enter my answer to that question" in new_answer:
      response = {'message': 'sorry, this input ist not eccepted'}
    elif "arschloch" in new_answer:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hurensohn" in new_answer:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hurentochter" in new_answer:
        response = {'message': 'wir erlauben keine schimpfwörter, bitte achten sie auf ihre wortwahl.'}
    elif "hure" in new_answer:
        response = {'message': 'Please watch your language'}
    else:
      knowledge_base["questions"].append({"question": new_question, "answer": new_answer})

      save_knowledge_base('knowledge_base.json', knowledge_base)
      response = {"message": "Thank you for teaching me!"}  # Formatierung der Antwort als Dictionary
    return jsonify(response)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
