# VIDCHATAI

VIDCHATAI is a GitHub repository that provides an interactive web application built with Streamlit. It utilizes the power of LangChain and ChatGPT to generate captions for YouTube videos and allows users to query information about the video content. The application leverages natural language processing techniques to process user queries and provide relevant responses.

## Features
- Video Information Retrieval: Users can submit queries about the video content through the application's user-friendly interface. VIDCHATAI employs ChatGPT, an advanced language model, to understand and respond to user queries effectively. Users can ask questions about specific timestamps, video topics, or any other relevant information.

- Interactive Web Interface: The application provides a simple and intuitive web interface built with Streamlit. Users can easily navigate through the different functionalities, input YouTube video links, and interact with the generated captions and query system.

## Installation

To run VIDCHATAI locally, follow the steps below:

1. Clone the GitHub repository:

```
git clone https://github.com/talhajaleel/VidChatAI.git
```

2. Change into the project directory:

```
cd VIDCHATAI
```

3. Install the required dependencies using pip:

```
pip install -r requirements.txt
```

4. Run the Streamlit application:

```
streamlit run app.py
```

5. Access the application by opening the following URL in your web browser:

```
http://localhost:8501
```

## Configuration

VIDCHATAI requires API keys for ChatGPT. Make sure you have obtained the necessary key and credentials before running the application.

To configure the API key, follow these steps:

1. Open the `.env` file and replace the placeholder values with your actual API keys (recommended)

```
CHATGPT_API_KEY=your_chatgpt_api_key
```

Make sure to save the changes to the `.env` file.

## Limitations

- VIDCHATAI depends on third-party APIs for speech recognition and language processing. Any limitations or restrictions imposed by these APIs will affect the functionality of the application.

- The accuracy of caption generation and query responses depends on the performance of LangChain and ChatGPT models. In some cases, the generated captions may not be perfect, and the query system may not comprehend certain complex queries accurately.

- VIDCHATAI's current version only supports YouTube video links for caption generation. Support for additional video platforms may be added in future updates.

## Contributions

Contributions to VIDCHATAI are welcome! If you want to contribute to the project, please follow these guidelines:

- Fork the repository and create a new branch for your contribution.

- Make your changes

- Submit a pull request describing your changes and the problem or feature they address.


## Disclaimer

VIDCHATAI is an open-source project developed by contributors. It is provided as-is, without any warranty or guarantee of its performance or suitability for any particular purpose. The developers of VIDCHATAI are not responsible for any misuse or damages arising from the use of this application.

Please use VIDCHATAI responsibly and

 comply with the terms of service of the APIs used by the application.

## Contact

If you have any questions, suggestions, or concerns about VIDCHATAI, please feel free to contact the project maintainer at talha.jaleel255@example.com.
