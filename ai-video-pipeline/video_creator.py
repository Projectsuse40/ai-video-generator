from moviepy import (
    ImageClip,
    AudioFileClip,
    concatenate_videoclips,
)

def create_video(images, audio_path, output_path, script):
    audio = AudioFileClip(audio_path)
    duration_per_image = audio.duration / len(images)

    clips = []

    for img in images:
        image_clip = ImageClip(img).with_duration(duration_per_image)
        clips.append(image_clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.with_audio(audio)

    video.write_videofile(output_path, fps=24)