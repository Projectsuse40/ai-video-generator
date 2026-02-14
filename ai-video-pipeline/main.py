from script_generator import generate_script
from seo_generator import generate_seo
from voice_generator import text_to_speech
from whisper_subtitles import generate_srt
from image_fetcher import fetch_images
from video_creator import create_video
from thumbnail_generator import generate_thumbnail
import os

def main():
    topic = input("Enter video topic: ").strip()

    print("Generating script...")
    script = generate_script(topic)

    title, desc, tags = generate_seo(topic)
    os.makedirs("output", exist_ok=True)
    with open("output/seo.txt", "w", encoding="utf-8") as f:
        f.write(f"TITLE:\n{title}\n\n")
        f.write(f"DESCRIPTION:\n{desc}\n\n")
        f.write(f"TAGS:\n{', '.join(tags)}")

    audio_path = os.path.join("output", "voice.mp3")
    print("Generating voice...")
    text_to_speech(script, audio_path)   

    srt_path = os.path.join("output","subtitles.srt")
    print("Generating subtitles with Whisper...")
    generate_srt(audio_path, srt_path)

    print("Fetching images...")
    images = fetch_images(topic)
    
    thumbnail_path = generate_thumbnail(
    title=topic,
    image_path=images[0])

    print("Creating video...")
    create_video(images, audio_path, "output/video.mp4", script)

    print("✅ Video generation complete!")

if __name__ == "__main__":
    main()
