import os
from dotenv import load_dotenv
import google.genai as genai

# Load environment variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("API key not found in .env (GOOGLE_API_KEY).")

# Create the client
client = genai.Client(api_key=api_key)

def generate_resume_entries(text):
    prompt = f"""
    Convert the following work experience into:
    1. A polished resume bullet point.
    2. A STAR-format version.
    3. A more technical, detailed version.

    Work experience: {text}
    """

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )

    return response.text


def main():
    print("\n=== Resume Bullet Point Generator (Gemini 2.0 Flash) ===\n")

    user_input = input("Describe your work/task/project: ")

    if len(user_input.split()) < 5:
        print("Please enter at least 5 words.")
        return

    print("\nGenerating optimized resume entries...\n")

    result = generate_resume_entries(user_input)

    print("=== Result ===\n")
    print(result)

    # Save result to file
    with open("resume_output.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("\nSaved to: resume_output.txt\n")


if __name__ == "__main__":
    main()
