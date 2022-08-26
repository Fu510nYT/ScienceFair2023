from assistant import Assistant
from dataset import Dataset
from respond import Respond
import pyttsx3
import speech_recognition as sr

assistant = Assistant()
tar_name = "assistant.tar"
retrain_nlu = True
if retrain_nlu:
    assistant.set_dataset(Dataset().from_yaml("dataset.yaml"))
    assistant.save(tar_name)
else:
    assistant.load(tar_name)

respond = Respond(assistant)
respond.from_yaml("example_respond.yaml")

engine = pyttsx3.init()
r = sr.Recognizer()

while True:
    print("Listening")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        text = r.listen(source, 10, 3)

    if text is None:
        continue
    text = r.recognize_google(text)
    print(text)
    if text != "":
        # print(f"Text: {text}")
        for res in respond.get_respond(text):
            if res["type"] == "say":
                print(f"Robot: {res['text']}")
                engine.say(res["text"])
                engine.runAndWait()
