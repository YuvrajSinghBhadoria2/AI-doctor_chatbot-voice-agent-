import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#image_path = "image.png"
import base64 
def encode_image(image_path):
    
    image_file=open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")


from groq import Groq


   



query = "is this something wrong with my face"
model="meta-llama/llama-4-scout-17b-16e-instruct"

def analyze_image_with_query(query,model,encoded_image):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }]

    chat_completion=client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return  chat_completion.choices[0].message.content
 