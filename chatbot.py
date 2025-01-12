from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import perception.sensory_input as sensory_input
import perception.feature_extraction as feature_extraction
from memory.short_term_memory import ShortTermMemory
from memory.long_term_memory import LongTermMemory

class Chatbot:
    def __init__(self, model_name='gpt2'):
        # Load the tokenizer and model from Hugging Face
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.stm = ShortTermMemory()  # Short-term memory
        self.ltm = LongTermMemory()    # Long-term memory

    def generate_response(self, user_input):
        # Include stored memory in the context
        memory_context = "\n".join(self.ltm.memory.keys())  # Context from long-term memory
        prompt = (
            f"You are an AI assistant that remembers previous conversations.\n"
            f"Previous memories:\n{memory_context}\n\n"
            f"User: {user_input}\nAI:"
        )

        # Tokenize the input prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)

        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response.split("AI:")[-1].strip()  # Extract the AI's response

    def respond(self, user_input):
        self.stm.store(user_input)  # Store user input in short-term memory
        response = self.generate_response(user_input)

        # Optionally store meaningful content in long-term memory
        self.ltm.store(user_input, response)

        return response

def run_chatbot():
    chatbot = Chatbot()
    print("Welcome to the Chatbot! Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    run_chatbot()
