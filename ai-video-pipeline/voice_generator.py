import edge_tts
import asyncio

async def generate_voice(text, output_path):
    voice = "en-IN-NeerjaNeural"
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(output_path)

def text_to_speech(text, output_path):
    asyncio.run(generate_voice(text, output_path))