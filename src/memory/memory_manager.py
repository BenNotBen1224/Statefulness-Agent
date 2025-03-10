from src.database.sql_store import Memory, init_sql_database
from src.database.vector_store import VectorMemoryStore

class MemoryManager:
    def __init__(self):
        self.sql_session = init_sql_database()
        self.vector_store = VectorMemoryStore()
    
    def store_experience(self, content, memory_type, context=None):
        # Store in SQL database
        memory = Memory(
            content=content,
            type=memory_type,
            context=context
        )
        self.sql_session.add(memory)
        self.sql_session.commit()
        
        # Store in vector database
        self.vector_store.add_memory(
            collection_name="episodic_memory",
            text=content,
            metadata={
                "type": memory_type,
                "context": context,
                "timestamp": str(memory.timestamp)
            },
            id=str(memory.id)
        )
    
    def retrieve_relevant_memories(self, query, n_results=5):
        # Query vector store for semantic similarity
        vector_results = self.vector_store.query_memories(
            "episodic_memory",
            query,
            n_results=n_results
        )
        
        # Get full context from SQL database
        memory_ids = [int(id) for id in vector_results['ids'][0]]
        sql_memories = self.sql_session.query(Memory).filter(
            Memory.id.in_(memory_ids)
        ).all()
        
        return sql_memories 