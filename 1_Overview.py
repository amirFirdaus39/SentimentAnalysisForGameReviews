import streamlit as st
from PIL import Image
#streamlit run "d:/Sem 5/WIH3001 Data Science Project/streamlit/1_📖_Overview.py"

st.title("🎮 Game Reviews")
st.header("📝 Transformer-based Approach for Sentiment Analysis")

st.subheader("📋 About Project")
st.write("  Sentiment analysis has always been an important indicator for game reviews because it allows for the effective categorization of the overall sentiment expressed in a review as positive, negative, or neutral. This can be useful for game developers, publishers, and marketers to quickly understand the overall sentiment towards their game, and to identify areas of improvement or areas that are particularly well-liked. Additionally, sentiment analysis can be used to track the sentiment of reviews over time, which can help identify any changes in sentiment and provide insight into how the game is perceived by players.")
st.write("  Despite that, several techniques have been proposed, but the performance of current sentiment analysis techniques (NLTK, Stanford NLP, SentiStrength) do not performed well on game reviews (Viggiato et al, 2021).  Hence, this project is done to find out whether the new state-of-the-art Natural Language Processing technique, transformer-based approach will perform well and suitable for game reviews.")

st.subheader("🤖 About Transformer")
st.write("The transformer architecture is a neural network architecture that is primarily used for natural language processing tasks. The transformer architecture is based on the idea of self-attention, which allows the model to weigh the importance of different words in a sentence when making predictions. Unlike RNNs, which process text in a sequential manner, Transformers utilize self-attention to compute the attention weight of each word in the input text in parallel, enabling more efficient parallelization for training larger models as compared to RNNs (Vaswani et al., 2017).")
st.write("The transformer architecture consists of an encoder and a decoder. The encoder takes in a sequence of words and produces a fixed-length representation of the input sentence, also called the context vector. The decoder then takes this context vector and produces the output, which can be a translation, a summary, or a label in a classification task. The encoder and decoder are made up of multiple layers of self-attention mechanism and feed-forward neural networks.")

trans = Image.open("data/transformer.png")
st.image(trans, caption="General Transformer Architecture")

st.subheader("BERT 🆚 DeBERTa")
st.subheader("BERT (Bidirectional Encoder Representations from Transformers)")
st.write("BERT  is a pre-trained deep learning model that is used for natural language processing tasks such as sentiment analysis. BERT uses a transformer architecture that allows it to process the context of a word in a sentence by looking at the words that come before and after it (Kamath et al., 2022). This bi-directional approach allows BERT to understand the meaning of a word in a sentence more accurately than traditional models that only look at the context of a word in one direction.")
st.subheader("DeBERTa (Decoding-enhanced BERT with disentangled attention)")
st.write("DeBERTa enhances the BERT model by adding a decoding mechanism to the pre-training task. This decoding mechanism allows the model to generate text, which improves the ability of the model to understand the context and meaning of the text. Additionally, DeBERTa uses disentangled attention, which separates the self-attention mechanism into two parts: one for modelling the context and the other for modelling the dependencies between words. This allows the model to focus on different aspects of the text, leading to a more accurate understanding of the text. He et al., (2020) in his paper, unlike BERT, where each word is represented by a combination of its content embedding vector and its position embedding vector, DeBERTa separates semantic (content) and syntactic (position) representation by computing four different attention scores between words: content-to-content, content-to-position, position-to-content, and position-to-position.")

deb = Image.open("data/deberta.png")
st.image(deb, caption="Difference in DeBERTa Architecture")

st.subheader("⛏️ Aspect Term Extraction")
st.write("Aspect term extraction is a process in sentiment analysis that involves identifying specific terms or phrases within a text that express a particular sentiment or opinion. These terms, also known as aspect terms, can provide insight into the specific topics or features that are being discussed in the text and how they are being evaluated. This is an important step in sentiment analysis as it allows for a more detailed understanding of the opinions and attitudes expressed in the text beyond just a general positive or negative sentiment.")
st.write("After identifying the aspect terms, the next step is to determine the sentiment associated with each aspect term. This is often done using a pre-trained sentiment classifier, which can assign a positive, negative, or neutral sentiment label to each aspect term.")
st.write("Once the aspect terms and their associated sentiments have been identified, the information can be used for a variety of purposes. For example, it can be used to identify specific features of a product or service that customers are particularly satisfied or dissatisfied with, or to track changes in sentiment over time.")
#st.write("")


st.subheader("📜 References")
st.write("Viggiato, M., Lin, D., Hindle, A., & Bezemer, C. (2022). What causes wrong sentiment classifications of game reviews? IEEE Transactions on Games, 14(3), 350-363. doi:10.1109/tg.2021.3072545")
st.write("Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., and Polosukhin, I. Attention is all you need. In International Conference on Neural Information Processing Systems, pp. 6000–6010, 2017.")
st.write("Kamath, U., Graham, K. L., & Emara, W. (2022). Bidirectional encoder representations from transformers (BERT). Transformers for Machine Learning, 43-70. doi:10.1201/9781003170082-3")
st.write("He, P., Liu, X., Gao, J., and Chen, W. DeBERTa: Decoding-enhanced BERT with Disentangled Attention. In: arXiv, 2020. URL https://arxiv.org/abs/ 2006.03654.")
