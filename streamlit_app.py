import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("IHC Counter – AEC/Hematoxylin Analyse")

uploaded = st.file_uploader("Bild hochladen", type=["png", "jpg", "jpeg", "tif"])

if uploaded:
    img = Image.open(uploaded)
    st.image(img, caption="Originalbild")

    # Beispiel: Bild in OpenCV konvertieren
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

    st.write("Bild erfolgreich geladen!")
