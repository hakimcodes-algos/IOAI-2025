# IOAI2025 GAITE: Synthetic Speech Detector

## Note: Please "join" the competition first. Then, you can mount the dataset to the GPU. Otherwise, the notebook may encounter an error because it cannot access the dataset until you have joined the competition.

## 1. Problem Description

In real life, synthetic speech (i.e., AI-generated speech) has been widely used. Although this technology has made significant progress, it has also raised concerns about potential misuse, such as fabricating fake audio of public figures and spreading misleading voice messages. The ability to distinguish synthetic speech from real human speech is crucial for various applications, including content verification, security, and ethical considerations in AI-generated media. The rapid development of generative models has made it increasingly difficult to distinguish between synthetic and real human recordings. This project aims to develop a model capable of effectively distinguishing between these two types of audio samples.

## 2. Dataset

The raw data used in this project consists of raw audio files of human speech and synthetic speech. However, since audio files cannot be directly used for training, the audio first needs to be converted into Mel spectrogram. Visually, it resembles a 2D image with time on the horizontal axis and Mel frequency on the vertical axis.  

![alt](https://minio-ioai.bohrium.com/bohrium/article/73760/ec7a27b861c745d9be29d86fe87a968f/7c69b573-30ea-4d51-9838-320ed505d5b4.png)

Due to the tedious nature of this conversion, the dataset provided in this project consists of pre-converted Mel spectrograms derived from raw audio files, rather than the raw audio itself. These spectrograms are all saved as tensors in `.pt` format. Training data is available at [dataset](https://ioai.bohrium.com/competitions/5115013137?tab=datasets). Files with filenames containing `bonafide` correspond to spectrograms of real human recordings, while the `spoof` folder stores all spectrograms of synthetic speech.

Note that the `SpectrogramDataset` in [baseline.ipynb](https://ioai.bohrium.com/notebooks/93479335231) is the class used to read training data. **Do not modify it to avoid errors in data loading**. This class is primarily designed to help load spectrograms and provides scripts to implement the `Dataset` interface for training models in PyTorch. It will traverse the subdirectories of each dataset and assist in labeling (with `bonafide` labeled as 0 and `spoof` labeled as 1). Its `__getitem__` magic method returns a dictionary in the form of `{ 'spectrogram': Tensor, 'label': Tensor, 'path': str }`, where `spectrogram` represents the spectrogram tensor, `label` is the label tensor, and `path` is the file path of the spectrogram.  

## 3. Task

(1) Your goal is to develop a model to distinguish between synthetic (AI-generated) speech and real human recordings. You may use a ResNet18 model. 

**(2) Hints:**  If you select visual models larger than ResNet18, you need to control the number of training epochs, as the baseline only trained for 1 epoch, which is insufficient. However, training for too many epochs may also be problematic, potentially leading to the inability to complete training within the allocated time. Alternatively, you can treat this task purely as a Computer Vision problem and solve it using a self-implemented CNN model. Do not get overly fixated on the implementation details of the Mel spectrogram conversion, as it might be irrelevant to the task.

## 4. Submission

Participants are required to submit a notebook file named "submission.ipynb", which may only include the trained model while omitting the training process to enable quick scoring. It should output a zip file containing prediction results, which includes two files:  

- "submissionA.csv": Contains the model's predicted labels for the validation set, with one 0 or 1 per line and without headers.  
- "submissionB.csv": Contains the model's predicted labels for the testing set, with one 0 or 1 per line and without headers.  

## 5. Scoring

The scoring is based on comparing the CSV file submitted by participants with the `ground_truth_labels.csv` file.  

The evaluation metric is **F1-score**. 

**Hint: you do not need to look at F1-score in details, you can intuitively understand that the more accurate the predicted position, the higher the score.** 

## 6. Baseline an Training Set

- The baseline is in [baseline.ipynb](https://ioai.bohrium.com/notebooks/93479335231).  
- The dataset is in [training set](https://ioai.bohrium.com/competitions/5115013137?tab=datasets).

## 7. Requirements

- Maximum submission limit: **50 times**. Only successful submissions (i.e., those receive a score on Leaderboard A) will be counted toward the submission limit.

- Testing environment restrictions: The test machine will run your Notebook within **20 minutes**. If the execution time exceeds **20 minutes**, the system will forcibly terminate and return a feedback of “Timeout” or “Failed”.

- Data and model submission: In this task, participants can submit a notebook and any mounted datasets or .pth files generated by themselves. 

- Network: For the on-site stage, the test machine cannot connect to the internet. In other words, downloading commands such as 'pip' and 'conda' or trying to call APIs will not work. 

- Pretrained Model: Any pre-trained model can be used in this task when it can be imported properly without network connection and downloading. 

## 8. Precautions

- Which score is effective: Contestants can select up to 2 submission results for scoring (√ - selected， □ - not selected). The score before unification for this task will be determined by the higher score on the Leaderboard B among the two selected submissions. Other cases of score calculation: please refer to **Appendix Platform Mechanisms and Restrictions for Individual Contest & GAITE**. 
  ![alt](https://minio-ioai.bohrium.com/bohrium/article/74628/7f7c800250dd4979aff0d7dce8fd6703/3a6274e4-dec9-445a-b899-4f429bec4256.jpeg)
  
- How to deal with ambiguity: Once there is a conflict between the task description and the training set, the validation set and test set , the dataset will be respected first, and the dataset will not be changed during the competition.
- Contestants can only access Leaderboard A during the contest and cannot access Leaderboard B. The final score will be calculated only based on the score in Leaderboard B.
- The highest score by the Scientific Committee for this task is 0.90 in Leaderboard B, this score is used for score unification.

- The baseline score by the Scientific Committee for this task is 0.70 in Leaderboard B, this score is used for score unification.

## 9. Hints

You may follow the steps below to complete this task: 

Run [baseline.ipynb](https://ioai.bohrium.com/notebooks/93479335231):
- In the model definition `class MyModel(nn.Module)`, set `model = resnet18(pretrained=ResNet18_Weights)`. Pre-trained parameters will be automatically imported when the model is instantiated; if necessary, you can also adjust the model structure. You can change `model = resnet18(pretrained=ResNet18_Weights)` to a better model to achieve a higher score, such as `model = resnet34(pretrained=ResNet34_Weights)`.
- In addition, you can also improve the number of epochs to achieve a higher score. Train the model for several epochs on training set. Normally, you should observe the validation loss continuously decreasing; if necessary, adjust the training parameters (e.g., number of epochs, batch size, learning rate).

