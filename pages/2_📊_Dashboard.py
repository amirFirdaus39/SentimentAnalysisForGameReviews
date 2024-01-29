import streamlit as st
from PIL import Image

st.title("📊 Game Reviews Dashboard")

st.header("🗯️ Word Clouds")
labels = ['Positive',"Neutral", "Negative"]
cloud = st.radio("Choose word cloud type:", labels,horizontal=True)

pos = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/poscloud.png")
neu = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/neutralcloud.png")
neg = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/negativecloud.png")

if cloud == 'Positive':
    st.subheader("🟢 Positive")
    st.image(pos, caption="Positive Word Cloud", width=900)

elif cloud == 'Neutral':
    st.subheader("🟡 Neutral")
    st.image(neu, caption="Neutral Word Cloud", width=900)

else:
    st.subheader("🟠 Negative")
    st.image(neg, caption="Negative Word Cloud", width=900)


st.header("🆖 N-Grams")
ngram = ['Unigram',"Bigram","Trigram"]
sentiment_labels = ['Overall','Positive',"Neutral", "Negative"]

gram = st.radio("Choose n-grams:", ngram,horizontal=True)
gram_labels = st.radio("Choose sentiment type:", sentiment_labels,horizontal=True)

all1 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/OveralUni.png")
pos1 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/PositiveUni.png")
neu1 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/NeutralUni.png")
neg1 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/NegativeUni.png")

all2 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/OveralBi.png")
pos2 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/PositiveBi.png")
neu2 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/NeutralBi.png")
neg2 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/NegativeBi.png")

all3 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/OveralTri.png")
pos3 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/PositiveTri.png")
neu3 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/NeutralTri.png")
neg3 = Image.open("D:/Sem 5/WIH3001 Data Science Project/findings/ngram/NegativeTri.png")


if gram == 'Unigram' and gram_labels == 'Positive':
    st.image(pos1, caption="Top 20 Positive Unigram", width=700)

elif gram == 'Unigram' and gram_labels == 'Neutral':
    st.image(neu1, caption="Top 20 Neutral Unigram", width=700)

elif gram == 'Unigram' and gram_labels == 'Negative':
    st.image(neg1, caption="Top 20 Negative Unigram", width=700)

elif gram == 'Bigram' and gram_labels == 'Positive':
    st.image(pos2, caption="Top 20 Positive Bigram", width=700)
    
elif gram == 'Bigram' and gram_labels == 'Neutral':
    st.image(neu2, caption="Top 20 Neutral Bigram", width=700)

elif gram == 'Bigram' and gram_labels == 'Negative':
    st.image(neg2, caption="Top 20 Negative Bigram", width=700)
    
elif gram == 'Trigram' and gram_labels == 'Positive':
    st.image(pos3, caption="Top 20 Positive Trigram", width=700)

elif gram == 'Trigram' and gram_labels == 'Neutral':
    st.image(neu3, caption="Top 20 Neutral Trigram", width=700)

elif gram == 'Trigram' and gram_labels == 'Negative':
    st.image(neg3, caption="Top 20 Negative Trigram", width=700)

elif gram == 'Unigram' and gram_labels == 'Overall':
    st.image(all1, caption="Top 20 Overall Unigram", width=700)

elif gram == 'Bigram' and gram_labels == 'Overall':
    st.image(all2, caption="Top 20 Overall Bigram", width=700)

else:
    st.image(all3, caption="Top 20 Overall Trigram", width=700)
