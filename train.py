from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import nltk
nltk.download('all')
chatbot = ChatBot('Fall')
trainer= ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hi there!",
    "How are you doing",
    "I'm doing great, how about you",
    "That is good to hear",
    "Thank you",
    "You're welcome"
])
trainer.train([
    "Good bye!",
    "See you soon!"
])
trainer.train(
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations"
)
