import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) == 1:
        print("You need to add a prompt")
        exit(1)
    prompt = sys.argv[1]
    messages = [
    types.Content(role="user", parts=[types.Part(text=prompt)]),
    ]
    response = client.models.generate_content(model = 'gemini-2.0-flash-001', contents = messages)
    if "--verbose" in sys.argv:
        print(f"User prompt: {prompt}")
        X = response.usage_metadata.prompt_token_count
        Y = response.usage_metadata.candidates_token_count
        print(f"Prompt tokens: {X}")
        print(f"Response tokens: {Y}")
    print(response.text)

if __name__ == "__main__":
    main()
