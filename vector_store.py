import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.index = faiss.IndexFlatL2(384)
        self.chunks=[]
    
    def add_documents(self, chunks):
        embeddings= self.model.encode(chunks)
        self.index.add(np.array(embeddings).astype('float32'))
        self.chunks.extend(chunks)

    def search(self, query, top_k=4):
        query_embedding = self.model.encode([query])

        distances,indices= self.index.search(np.array(query_embedding),top_k)

        results = []
        for idx in indices[0]:
            results.append(self.chunks[idx])
        return results



