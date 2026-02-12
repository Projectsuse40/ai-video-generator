# AI Video Automation Pipeline

This project is an end-to-end AI-powered video generation pipeline.

It automatically:
- Generates a YouTube-style script using an LLM (Groq)
- Converts the script to voice using Edge TTS
- Fetches relevant stock images from Pexels
- Creates a video using MoviePy
- Generates perfectly synced subtitles using Whisper
- Produces SEO metadata (title, description, tags)

## Features

- Automated script generation (LLM-based)
- Text-to-Speech narration
- Stock image fetching via API
- Automated video creation (1080p)
- Whisper-based accurate subtitles (SRT)
- SEO metadata generation
- Cross-platform support (Windows, macOS, Linux)

## Project Structure

ai-video-pipeline/
│
├── main.py                # Entry point of the application
├── script_generator.py    # Generates script using Groq LLM
├── voice_generator.py     # Converts script to speech (Edge TTS)
├── image_fetcher.py       # Fetches images from Pexels API
├── video_creator.py       # Creates video using MoviePy
├── whisper_subtitles.py   # Generates subtitles using Whisper
├── seo_generator.py       # Generates SEO metadata
│
├── assets/
    ├── images/            # Static assets 
├── fonts/                 # Custom fonts (if used in video/subtitles)
├── output/                # Final generated files (video, srt, etc.)
|   ├── subtitles.srt
|   ├── seo.txt 
|   |── video.mp4  
|   |── voice.mp3       
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
├── pyproject.toml         # Project configuration
├── README.md              # Project documentation
└── .gitignore

## Workflow

1. User enters a topic.
2. Script is generated using Groq LLM.
3. Script is converted to speech using Edge TTS.
4. Images related to the topic are fetched via Pexels API.
5. Video is generated using MoviePy.
6. Whisper transcribes the audio to generate accurate subtitles.
7. SEO metadata is created and saved.

## Installation

1. Clone the repository:

git clone <your-repo-url>
cd ai-video-pipeline

2. Create a virtual environment:

python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3. Install dependencies:

pip install -r requirements.txt

## Install FFmpeg

FFmpeg must be installed and added to your system PATH.

macOS:
brew install ffmpeg

Linux:
sudo apt install ffmpeg

Windows:
Download from https://ffmpeg.org and add to PATH.

## Environment Variables

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key
PEXELS_API_KEY=your_pexels_api_key

## Run

python main.py

## Output

After execution, the following files are generated:

- output/video.mp4
- output/subtitles.srt
- output/seo.txt
- output/voice.mp3