This project utilizes the ResNet18 architecture for detecting faulty tyres in images. The model is trained and evaluated on a dataset of images containing defective and good tyres. This project was developed using Google Colab, and it leverages PyTorch for building and training the neural network.

**Table of Contents**: 
1.Project Overview 
2.Data preprocessing 
3.Model Training 
4.Evaluation

**Project Overview**: 
The goal of this project is to create an effective fault detection system in tyres using a pre-trained ResNet18 model. The system can identify images containing defective or good tyres, which is useful for detecting and replacing defective tyres to avoid safety incidents.

**Dataset**:
The dataset used in this project consists of images categorized into defective and good classes. The dataset is stored in a ZIP file and extracted for training and testing.
Link: 

**Model Training**: 
The training process involves loading the dataset, preprocessing the images, and training the ResNet18 model. The training and validation splits are handled within the script.

**Evaluation** : 
The trained model is evaluated using a separate test dataset. The evaluation metrics include loss and accuracy, and a confusion matrix is plotted to visualize the performance of the model.

![Confusion_matrix](https://github.com/Moseskota/Faulty_tyre_detection_ResNet/assets/76688024/d57ff839-2213-4f60-8343-81cf5d79888f)

