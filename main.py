import os
import sys

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


def gpt_interaction(video_subs, user_query):
    # uncomment this and add your opanaiapi key
    # os.environ["OPENAI_API_KEY"] = 'your-openai-api-key'

    # read data from the file and put them into a variable called raw_text
    raw_text = video_subs

    # We need to split the text that we read into smaller chunks so that
    # during information retrieval we don't hit the token size limits.

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=800,
        chunk_overlap=100,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)
    # print(texts)
    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings()

    docsearch = FAISS.from_texts(texts, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    # query = 'what is this youtube video about and write main points in bullets'
    docs = docsearch.similarity_search(user_query)
    res = chain.run(input_documents=docs, question=user_query)
    return res


st.title('VIDCHATAI')
vid_url = st.text_input('Enter your URL here')
query = st.text_input('Your query')
move_on = st.button('Lets go!!! ')
if move_on and vid_url:
    vid_id = vid_url.split('v=')[1]
    srt = YouTubeTranscriptApi.get_transcript(vid_id)
    captions = [i['text'] for i in srt]
    # print(captions)
    captions = '\n'.join(captions)
    # curr_query = st.text_input('Ask your question')
    res = gpt_interaction(captions, query)
    st.write(res)

sys.exit()
