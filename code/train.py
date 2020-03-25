from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import pickle
import glob


#this will train the SOCRATES with the dialogues data and wil be store inside a sqlite database 
dialogues_path = "../tidy_data/books/"
dialogues_list = glob.glob(dialogues_path  + "*.pickle")   
dialogues = []
for x in dialogues_list:
    with open(x, 'rb') as f:
        dialogue_x = pickle.load(f)
    dialogues += dialogue_x

print("Silence! Socrates is learning\n")
chatbot = ChatBot('SOCRATES',trainer='chatterbot.trainers.ListTrainers')
trainer = ListTrainer(chatbot)
trainer.train(dialogues)
