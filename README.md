# Chating with File Loading Application

This repository contains the implementation of a file-loading chatbot using Flask for the backend and HTML, CSS, and JavaScript for the frontend. The application allows users to upload files, create vector embeddings, and perform conversational retrieval with the data.

## Features

### 1. File Upload and Processing
- Supports `.pptx` file format only.
- Extracts text and images from slides and stores them in separate lists.
- Extracts text from images and stores it in a list.
- Merges extracted image text with other text.
- Converts the combined text into manageable chunks.
- Creates vector embeddings using FAISS and stores them locally in the project directory.

### 2. Conversational Chatbot
- Allows users to ask questions based on the uploaded documents.
- Uses a conversational retrieval chain with memory to provide context-aware responses.

### 3. Old Vector Deletion
- Deletes previous vector stores when a new file is uploaded.

### 4. Blueprint Architecture
- Modular structure with separate blueprints for file upload and chat.

### 5. Frontend Integration
- Uses HTML, CSS, and JavaScript for the user interface.
- JavaScript `fetch` API enables seamless integration with backend routes.

## Project Structure
```
├── mainapp
│   ├── routes
│   │   ├── conversation_route.py
│   │   ├── uploadfile_route.py
│   ├── utils
│   │   ├── file_loading_and_chunking.py
│   ├── __init__.py
├── app.py
├── requirements.txt
└── README.md
```

## Setup Instructions

### Prerequisites
1. Python 3.12+
2. Flask
3. FAISS
4. LangChain
5. Google Generative AI

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the following variable:
     ```env
     GEMINI_API_KEY=your_google_api_key
     ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Access the application at `http://127.0.0.1:5000`.

## API Routes

### 1. File Upload Route
**Endpoint:** `/upload_pptx`  
**Method:** `POST`

- Uploads a file and creates a vector store for it.
- Supported file types: `.pptx`

Example Request:
```bash
curl -X POST -F "file=@example.pptx" http://127.0.0.1:5000/upload_pptx
```

### 2. Chat Route
**Endpoint:** `/chat`  
**Method:** `POST`

- Handles user queries and provides AI-generated responses.
- Requires a vector store to be created first.

Example Request:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"query": "What is in the document?"}' http://127.0.0.1:5000/chat
```

## Core Functions

### 1. File Loading and Chunking
- **`load_file(file)`**: Loads and processes files based on their extensions.
- **`create_chunks(data)`**: Splits loaded text into smaller chunks for embedding creation.

### 2. Embedding and Vector Store
- **`create_vector_db(data)`**: Creates a FAISS vector database from the input data.
- **`retrievers()`**: Loads the vector database and sets up a retriever for similarity searches.

### 3. Chat Model
- **`chat_model(retriever)`**: Initializes a conversational chain using Google Generative AI and conversation memory.

## Frontend Integration
- **HTML and CSS**: Provide the structure and styling of the user interface.
- **JavaScript Fetch API**: Enables asynchronous communication with the backend for file uploads, chats, and deletions.

## Example Workflow
1. **Upload a File**
   - User uploads a `.pptx` file via the `/upload_pptx` route.
   - Backend saves the file, processes it, and creates a vector store.

2. **Start a Conversation**
   - User sends a query to the `/chat` route.
   - Backend retrieves relevant information from the vector store and provides a response.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

