# OpsTree_AI_Assignment

Architecture overview:

1. User uploads documents
        
        
2. Extract text from files
        
        
3. Split text into chunks
        
        
4. Generate embeddings for chunks
        
        
5. Store embeddings in FAISS
        
        
6. User asks question
        
        
7. Generate embedding for question
        
        
8. Search FAISS for relevant chunks
        
        
9. Pass chunks + question to LLM
   
        
10. Return answer
 ## Setup
```bash
#Generate your personal Gemini API key

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```
<img width="709" height="76" alt="image" src="https://github.com/user-attachments/assets/ecae986c-aa46-450e-ba8c-061268ed2cca" />
<img width="584" height="29" alt="image" src="https://github.com/user-attachments/assets/564fa9ca-a288-45db-89b3-e52db5a6049c" />  

# Sample output

<img width="1075" height="394" alt="image" src="https://github.com/user-attachments/assets/8ed595fb-5b69-4fe6-b504-fa2d7524479d" />
<img width="1025" height="865" alt="image" src="https://github.com/user-attachments/assets/0ea6d788-f235-4345-a054-3777e110a387" />

# Assumptions taken:

"User has sufficient tokens in their Gemini account" 

"Queries are relevant to the files uploaded"

"Uploaded Documents Contain Extractable Text"

"Documents are written english language"

"File size does not exceed 200MB"
