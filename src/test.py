from src.memory.memory_manager import MemoryManager

def main():
    memory_manager = MemoryManager()
    
    # Store a new experience
    memory_manager.store_experience(
        content="User asked about Python programming",
        memory_type="interaction",
        context="Programming discussion"
    )
    
    # Retrieve relevant memories
    memories = memory_manager.retrieve_relevant_memories(
        "Python programming questions"
    )
    
    for memory in memories:
        print(f"Memory {memory.id}: {memory.content} ({memory.timestamp})")

if __name__ == "__main__":
    main() 