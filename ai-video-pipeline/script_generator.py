import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def generate_script(topic):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
    You are writing a YouTube voiceover script.

    Topic: {topic}

    Write ONLY the spoken narration.

    Do NOT include:
    - Timelines
    - Titles
    - Headings
    - Labels like "Narrator:", "Script:", "Title:"
    - Explanations
    - Introductory phrases like "Here is your script"

    The output must be pure narration text that can be directly read by a text-to-speech engine.

    Length: 60–90 seconds.
    Tone: engaging, clear, natural.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content