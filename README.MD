# 🫁 Chest X-Ray Pneumonia Detection

A high-performance medical diagnostic tool leveraging deep learning to assist in the identification of pneumonia from chest radiographs. This project utilizes a fine-tuned **DenseNet121** architecture deployed through an intuitive **Streamlit** interface.

---

## 📑 Project Overview
This application streamlines the diagnostic process by automating the initial screening of chest X-rays. By employing transfer learning on the DenseNet121 architecture, the model achieves high sensitivity in identifying pathological patterns consistent with pneumonia.

### 🚀 Key Capabilities
* **Automated Classification:** Instant analysis of uploaded JPG/PNG images.
* **Deep Learning Engine:** Utilizes PyTorch and torchvision with pre-trained weights.
* **User-Centric UI:** Built with Streamlit for a seamless, interactive experience.
* **Production-Ready:** Fully Dockerized for consistent deployment across environments.
* **Robust Evaluation:** Performance validated via precision, recall, and F1-metrics.

---

## 🛠 Tech Stack
| Category | Technologies |
| :--- | :--- |
| **Deep Learning** | PyTorch, Torchvision, Scikit-learn |
| **Web Framework** | Streamlit |
| **Infrastructure** | Docker |
| **Data Analysis** | Pandas, Matplotlib, NumPy |

---

## 📊 Model Performance
The model has been optimized for clinical sensitivity, ensuring a high recall rate to minimize false negatives.

| Metric | Score |
| :--- | :--- |
| **Accuracy** | 68.65% |
| **Precision** | 59.21% |
| **Recall** | 99.74% |
| **F1 Score** | 74.31% |

> *Note: Metrics are based on the test subset of the [Chest X-Ray Images (Pneumonia) Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).*

---

## 🚦 Roadmap & Future Scope
- [ ] **Explainability:** Integrate **Grad-CAM** to visualize and highlight specific regions of interest in the lungs.
- [ ] **Multi-Disease Support:** Expand the classification scope to include other thoracic pathologies.
- [ ] **Medical Imaging Formats:** Implement native support for **DICOM** files.
- [ ] **Optimization:** Model quantization for faster inference on edge devices.
- [ ] **CI/CD:** Automate pipeline deployment to cloud providers (AWS/GCP).

---

## ⚠️ Disclaimer
**This application is strictly for educational and research purposes.** The predictions provided by this model should not be considered a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider regarding medical conditions.