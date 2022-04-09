from chatterbot import ChatBot

barbie_bot = ChatBot('Zuri',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

barbie_bot = ChatBot(
    'Zuri',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
    ],
    database_uri='sqlite:///database.sqlite3'
)

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(barbie_bot)

trainer.train([
'Hi',
'Hello',
'I need your help regarding a refund',
'Please Provide a reference number for your order',
'I have a complaint.',
'Please elaborate',
'How long it will take to receive my order ?',
'An order takes approximately 5 to 7 business days.',
'Okay Thanks',
'No Problem! Have a nice day! :)'
])

response = barbie_bot.get_response('I have a complaint.')



print("Zuri:", response)

name=input("Enter Your Name: ")
print("Welcome to the Bot Service! Let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='I need your help regarding a refund' or request =='bye':
        print('Zuri: Please provide your order reference')
        break
    else:
        response=barbie_bot.get_response(request)
        print('Zuri:',response)


