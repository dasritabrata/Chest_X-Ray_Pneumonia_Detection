import streamlit as st
import torch
import torch.nn as nn
from torchvision.models import densenet121
from torchvision import transforms
from PIL import Image

# --------------------------
# Page Configuration
# --------------------------
st.set_page_config(
    page_title="Pneumonia Detection AI",
    page_icon="🫁",
    layout="centered"
)

# Professional CSS Styling
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; }
    .reportview-container .main .block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --------------------------
# Load Model
# --------------------------
@st.cache_resource
def load_model():
    model = densenet121(weights=None)
    model.classifier = nn.Linear(model.classifier.in_features, 1)
    # Ensure the model file path is correct
    model.load_state_dict(torch.load("best_model_1.pth", map_location="cpu"))
    model.eval()
    return model

model = load_model()

# --------------------------
# Transforms
# --------------------------
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# --------------------------
# Sidebar & Header
# --------------------------
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3304/3304567.png", width=100)
    st.title("AI Diagnostics")
    st.info("This tool uses a DenseNet121 architecture to assist in identifying potential pneumonia from Chest X-ray images.")
    st.divider()
    st.caption("Disclaimer: This tool is for educational purposes and not a substitute for professional medical diagnosis.")

st.title("🫁 Chest X-Ray Analysis")
st.write("Upload a diagnostic image below to begin the analysis.")

# --------------------------
# UI Interaction
# --------------------------
uploaded_file = st.file_uploader("Upload Chest X-ray (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns([1, 1])
    
    image = Image.open(uploaded_file).convert("RGB")
    
    with col1:
        st.image(image, caption="Radiograph Input", use_container_width=True)
        
    with col2:
        with st.spinner('Analyzing scan...'):
            img_tensor = transform(image).unsqueeze(0)
            with torch.no_grad():
                output = model(img_tensor)
                probability = torch.sigmoid(output).item()
            
            prediction = 1 if probability >= 0.5 else 0

        st.subheader("Result")
        if prediction == 1:
            st.error("### ⚠️ Pneumonia Detected")
            st.metric("Confidence Score", f"{probability:.2%}")
        else:
            st.success("### ✅ Normal")
            st.metric("Confidence Score", f"{(1-probability):.2%}")
            
        st.progress(probability if prediction == 1 else (1-probability))

else:
    st.info("Please upload an image to see the diagnostic results.")