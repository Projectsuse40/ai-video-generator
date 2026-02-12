def generate_seo(topic):
    title = f"{topic} Explained in 60 Seconds"
    description = (
        f"Learn about {topic} in this quick AI-generated video.\n\n"
        "This video was fully generated using AI tools including "
        "LLMs, text-to-speech, stock visuals, and Python automation."
    )
    tags = [
        topic,
        "AI generated video",
        "automation",
        "tech explained",
        "short documentary"
    ]

    return title, description, tags     