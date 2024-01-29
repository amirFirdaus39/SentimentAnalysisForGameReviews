import pandas as pd
import requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification, DebertaV2Tokenizer
import torch
import streamlit as st
# from pyabsa import ATEPCCheckpointManager
# from pyabsa import AspectTermExtraction as ATEPC
#streamlit run "d:/Sem 5/WIH3001 Data Science Project/streamlit/1_📖_Overview.py"
#"D:\Sem 5\WIH3001 Data Science Project\datasets\debertabsa"

st.title("Sentiment Analysis :grinning: :neutral_face: :angry: on Game Reviews :video_game:")

game = st.text_input("Name of the Game","DOTA 2")

review = st.text_input("Your review","nice animation")

# model = AutoModelForSequenceClassification.from_pretrained("D:\Sem 5\WIH3001 Data Science Project\datasets\models\DebertaV2")
model = AutoModelForSequenceClassification.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
#tokenizer = DebertaV2Tokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")
#model = AutoModelForSequenceClassification.from_pretrained("D:\Sem 5\WIH3001 Data Science Project\datasets\models\balancedDebYH")
tokenizer = DebertaV2Tokenizer.from_pretrained("yangheng/deberta-v3-base-absa-v1.1")

def predict():
    token = tokenizer.encode(review, return_tensors='pt')
    result = model(token)
    score = int(torch.argmax(result.logits))
        
    # response = requests.post("https://yangheng-multilingual-aspect-based-sentiment-analysis.hf.space/run/inference", json={
    #   "data": [review,"English",]}).json()
#https://yangheng-multilingual-aspect-based-sentiment-analysis.hf.space/queue/join?__theme=light&fn_index=2&session_hash=p874kj39h5
    #"https://yangheng-multilingual-aspect-based-sentim-6aa230e.hf.space/run/inference"
    # data = response["data"]
    # lst = data[0]["data"]
    # df = pd.DataFrame(lst, columns =["aspect","sentiment","confidence","position"])
    # df = df[["aspect","sentiment"]]

    if score == 0:
        st.error("Your review is Negative :angry: ")
    elif score == 1:
        st.warning("Your review is Mixed/Neutral :neutral_face:")
    else:
        st.success("Your review is Positive :grinning: ")

    # st.dataframe(df) 
    

#result = extract_aspect(review)

st.button("Analyse", on_click=predict)

#concept is decent but the players are very toxic 
