import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np

st.title("📈 Models Evaluation")

st.subheader("✏️ Results Table")

df = pd.read_csv("data/Result.csv")
st.dataframe(df)

metric_names = ["Accuracy", "Precision", "F1", "Recall"]
metric = st.radio("Choose an evaluation metric: ", metric_names, horizontal=True)

acc = Image.open("data/accuracy2.png")
prec = Image.open("data/precision2.png")
f1 = Image.open("data/f1_2.png")
rec = Image.open("data/recall2.png")

if metric == 'Accuracy':
    st.subheader("🟦 Accuracy")
    st.image(acc, caption="Models Accuracy Comparisons",width=600)

elif metric == 'Precision':
    st.subheader("🟧 Precision")
    st.image(prec, caption="Models Precision Comparisons",width=600)

elif metric == 'F1':
    st.subheader("⬜ F1")
    st.image(f1, caption="Models F1 Comparisons",width=600)

else:
    st.subheader("🟨 Recall")
    st.image(rec, caption="Models Recall Comparisons",width=600)
