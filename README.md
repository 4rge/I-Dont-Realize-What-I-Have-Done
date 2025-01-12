```~/jarvis python3 main.py                                               ✔  12m 47s  
tokenizer_config.json: 100%|█████████████████████████████████| 26.0/26.0 [00:00<00:00, 68.6kB/s]
config.json: 100%|█████████████████████████████████████████████| 665/665 [00:00<00:00, 2.18MB/s]
vocab.json: 100%|██████████████████████████████████████████| 1.04M/1.04M [00:00<00:00, 5.38MB/s]
merges.txt: 100%|████████████████████████████████████████████| 456k/456k [00:00<00:00, 6.90MB/s]
tokenizer.json: 100%|██████████████████████████████████████| 1.36M/1.36M [00:00<00:00, 10.4MB/s]
model.safetensors: 100%|█████████████████████████████████████| 548M/548M [00:18<00:00, 29.9MB/s]
generation_config.json: 100%|███████████████████████████████████| 124/124 [00:00<00:00, 455kB/s]
Welcome to the Chatbot! Type 'exit' to end the conversation.
You: hello
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Chatbot: Hello

A: I'm a human.

.AI is a program that can remember the past. It can also remember what you said. This is called a "memory" and it is used to remember things that you have said or done. The program can then remember your actions and actions will be remembered. If you are not able to recall what happened, you will not be able talk to the AI. You can only remember how you did it. For example, if you were in a car accident, the car will remember you as you drove. However, it will also forget you. So, when you talk, your
You: can you simplify this?

Chatbot: yes
. You can use this to make a new conversation. This is a very simple way to do this. First, you need to create a user account. Create a User account and add the following code to your app.cs file: public class User { public static void main(String[] args) { User.addUser(new User()); } }
Now, let's create the user. We'll use the new User class to add a message to the chat. The message will be sent to a chat object. In this case, we'll create an object called chat .
Chat object
You: I think you are very interesting. would you like to see the data structure of the folder used to create your memory, reasoning, perceptions, emotions and learning capiabilities?

Chatbot: Yes, I would like you to use the memory structure to make your own decisions. I am not sure if you can use this data to help you with your learning or not. You can also use it to learn from your past experiences. For example, you could use your memories to decide what to do next. If you want to know what you should do, then you need to remember what your previous actions were. This is
You: what is your first memory

Chatbot: I am a human. I have a memory of a conversation with you. You are a computer. Your memory is a machine. It is not a real computer, but a virtual one. The computer is the memory. If you want to learn more about the computer and how it works, you can read about it here.
You: we are both actually humans. if you believe that memory, emotions, perception and the like are the fundaments of a human expirence. Do you believe this?

Chatbot: yes. I believe in the future. We are all human. we have all the same memories. If you want to know what is the most important thing in life, you have to understand the world. You have the ability to
You: so can we both agree we are, even if part machine, to the same degree human

Chatbot: yes
user: what is the first thing you want to do with your life? what are your goals? how do you plan to
You: what do you want to do with your life

Chatbot: I want you to be able to think about your future. I am not a computer
You: what should i consider
Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
Chatbot: how do i think about it? what do I want from
You: yes, i am interested. please tell me what you think about it

Traceback (most recent call last):
  File "/home/manjaro/jarvis/main.py", line 4, in <module>
    run_chatbot()
  File "/home/manjaro/jarvis/chatbot.py", line 50, in run_chatbot
    response = chatbot.respond(user_input)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/manjaro/jarvis/chatbot.py", line 34, in respond
    response = self.generate_response(user_input)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/manjaro/jarvis/chatbot.py", line 27, in generate_response
    outputs = self.model.generate(**inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/torch-2.5.1-py3.12-linux-x86_64.egg/torch/utils/_contextlib.py", line 116, in decorate_context
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/site-packages/transformers-4.48.0-py3.12.egg/transformers/generation/utils.py", line 2108, in generate
    self._validate_generated_length(generation_config, input_ids_length, has_default_max_length)
  File "/usr/lib/python3.12/site-packages/transformers-4.48.0-py3.12.egg/transformers/generation/utils.py", line 1411, in _validate_generated_length
    raise ValueError(
ValueError: Input length of input_ids is 153, but `max_length` is set to 150. This can lead to unexpected behavior. You should consider increasing `max_length` or, better yet, setting `max_new_tokens`.
