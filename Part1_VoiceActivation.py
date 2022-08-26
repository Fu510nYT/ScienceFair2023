from assistant import Assistant
from dataset import Dataset
from respond import Respond

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

while True:
    print("Listening")
    text = input()
    if text != "":
        # print(f"Text: {text}")
        for res in respond.get_respond(text):
            if res["type"] == "say":
                print(f"Robot: {res['text']}")
