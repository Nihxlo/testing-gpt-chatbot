import openai
import re
import random

openai.api_key = "Insert API Key Here"  # Replace with your OpenAI API key

# Define greeting and response functions
GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
sent_tokens = []

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

def get_response(prompt):
    response = openai.Completion.create(
        engine="davinci", 
        prompt=prompt, 
        max_tokens=2024,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    message = re.sub(r'[^\w\s]', '', message)  # Remove punctuation
    return message

# Define main function
def main():
    flag=True
    print("BOT: My name is Bot. I will answer your queries about Chatbots. If you want to exit, type Bye!")
    while(flag==True):
        user_response = input().lower()
        sent_tokens.append(user_response)
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                print("BOT: You are welcome..")
            else:
                if(greeting(user_response)!=None):
                    print("BOT: "+greeting(user_response))
                else:
                    print("BOT: ",end="")
                    print(get_response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag=False
            print("BOT: Bye! take care..")

# Call main
if __name__ == "__main__":
    main()
