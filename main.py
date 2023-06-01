import os

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

# os.environ['open_api_key'] = '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'


def gpt_interaction(video_subs):

    os.environ["OPENAI_API_KEY"] = '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'

    # read data from the file and put them into a variable called raw_text
    raw_text = video_subs

    # We need to split the text that we read into smaller chunks so that
    # during information retrieval we don't hit the token size limits.

    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    texts = text_splitter.split_text(raw_text)

    # Download embeddings from OpenAI
    embeddings = OpenAIEmbeddings()

    docsearch = FAISS.from_texts(texts, embeddings)
    chain = load_qa_chain(OpenAI(), chain_type="stuff")
    query = 'what is this youtube video about and write its summary in 100 words'
    docs = docsearch.similarity_search(query)
    res = chain.run(input_documents=docs, question=query)
    return res


st.title('Talktube')
vid_url = st.text_input('Enter your URL here')
move_on = st.button('Lets go!!! ')
if move_on and vid_url:
    vid_id = vid_url.split('v=')[1]
    srt = YouTubeTranscriptApi.get_transcript(vid_id)
    captions = [i['text'] for i in srt]
    captions = ' '.join(captions)
    res = gpt_interaction(captions)
    st.write(res)
    st.stop()

