import random
import json
import numpy as np
import torch
from nltk.corpus import stopwords

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "../../../../PycharmProjects/chatbot/venv/data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"


def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    print(prob.item(),tag)
    if prob.item() > 0.30:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    return "I do not understand..."


def cosine(X, Y, all_words):
    X_list = tokenize(X)
    Y_list = tokenize(Y)

    # sw contains the list of stopwords
    # sw = stopwords.words('english')
    l1 = [];
    l2 = []

    l1 = bag_of_words(X_list, all_words)
    l2 = bag_of_words(Y_list, all_words)

    c = 0

    cos_sim = np.dot(l1, l2) / (np.linalg.norm(l1) * np.linalg.norm(l2))
    return cos_sim


def max_sim(y):
    max = -1
    max2 = -1

    for intent in intents['intents']:
        tag = intent['tag']
        resp = random.choice(intent['responses'])
        for pattern in intent["patterns"]:
            ans = cosine(pattern, y, all_words)
            if ans > max:
                max = ans
                # idx=tag
                respa = resp
    try:
        return respa
    except:
        str = "I apologize"
        return str


def answering(sen):
        # sentence = "do you use credit cards?"
        sentence = sen


        resp = get_response(sentence)
        return resp