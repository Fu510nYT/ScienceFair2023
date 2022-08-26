# Science Fair 2023
This repository is for the 2023 Macau inter school science fair.
This project's flowchart is essentially the following:

1. Voice Activation using NLU
2. Extract Objective
3. Face Recognition to see who the user is
4. Use word embedding to find most possible places
5. Use G-Mapping to go to the aforementioned location
6. Using YOLOv5 from Pytorch Hub to find the objective
7. G-Map back to the user

Part1
Voice Activation using NLU => Part1_VoiceActivation.py (File Name)

Part2
Extract Objective => Part2_ExtractObjective.py

Part3
Face Rec (without dlib)
1. Extract Data for dataset => Part3A_ExtractFeatures.py
2. Train Data for trained_data/trainer.yml => Part3B_TrainData.py
3. Use Trained Data => Part3_FaceRecognition.py


NOTE: File names may not be exactly correct
