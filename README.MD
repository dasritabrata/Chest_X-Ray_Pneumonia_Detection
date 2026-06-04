Chest X-Ray Pneumonia Detection

This project is a medical image classification application that detects pneumonia from chest X-ray images using a pretrained DenseNet121 model fine-tuned with PyTorch.

Users can upload a chest X-ray image through a Streamlit web interface, and the model predicts whether the scan is NORMAL or PNEUMONIA, along with a confidence score.

Features
Chest X-ray image classification
Transfer learning using DenseNet121
Built with PyTorch
Interactive Streamlit web application
Dockerized for reproducible deployment
Evaluation using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix
Ready for deployment on platforms such as Render
Tech Stack
Python
PyTorch
Torchvision
Streamlit
Docker
Scikit-learn
Pandas
Matplotlib
Dataset

The model was trained on the widely used Chest X-Ray Images (Pneumonia) Dataset containing chest radiographs categorized into Normal and Pneumonia classes.

Model Performance

Example metrics on the test dataset:

Accuracy : 0.6865
Precision: 0.5921
Recall   : 0.9974
F1 Score : 0.7431

(Replace with your final results after training.)

Future Improvements
Grad-CAM visual explanations
Multi-class thoracic disease detection
Model quantization and optimization
Cloud deployment and CI/CD pipeline
Support for DICOM medical images