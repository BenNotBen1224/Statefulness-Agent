import chromadb

class VectorMemoryStore:
    def __init__(self):
        # Updated client initialization to use current ChromaDB API
        self.client = chromadb.PersistentClient(path="vector_store")
        
        # Create collections for different types of vectorized memories
        self.episodic_memory = self.client.get_or_create_collection("episodic_memory")
        self.semantic_memory = self.client.get_or_create_collection("semantic_memory")
        self.procedural_memory = self.client.get_or_create_collection("procedural_memory")
    
    def add_memory(self, collection_name, text, metadata=None, id=None):
        collection = self.client.get_collection(collection_name)
        collection.add(
            documents=[text],
            metadatas=[metadata or {}],
            ids=[id or str(hash(text))]
        )
    
    def query_memories(self, collection_name, query_text, n_results=5):
        collection = self.client.get_collection(collection_name)
        results = collection.query(
            query_texts=[query_text],
            n_results=n_results
        )
        return results 