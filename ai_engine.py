
import ollama

TEXT_MODEL = "qwen2.5:3b"
VISION_MODEL = "qwen2.5vl:3b"


def generate_memory_story(memory, style="Nostalgic"):

    prompt = f"""
    You are Echoes of Yesterday, a thoughtful AI storyteller.

    Create a beautiful, emotional story from this memory.

    Memory: {memory}
    Style: {style}

    Rules:
    - Preserve the user's original details.
    - Do not invent personal facts.
    - Never claim to communicate with deceased people.
    - Write a meaningful title.
    - Keep the story between 120 and 180 words.
    """

    try:
        response = ollama.chat(
            model=TEXT_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            options={
                "num_predict": 220,
                "temperature": 0.7
            }
        )

        return response["message"]["content"]

    except Exception as error:
        return f"AI Error: {error}"


def analyze_photograph(image_bytes):

    prompt = """
    Briefly describe visible objects, clothing,
    environment and activities in this photograph.

    Do not identify people or guess relationships,
    dates, locations or personal history.
    Keep the description under 80 words.
    """

    try:
        response = ollama.chat(
            model=VISION_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [image_bytes]
                }
            ],
            options={
                "num_predict": 100
            }
        )

        return response["message"]["content"]

    except Exception as error:
        return f"Vision AI Error: {error}"


def generate_visual_memory_story(
    image_bytes,
    user_memory,
    style="Nostalgic"
):

    visual_description = analyze_photograph(image_bytes)

    if visual_description.startswith("Vision AI Error:"):
        return visual_description

    combined_memory = f"""
    Visible photograph details:
    {visual_description}

    Personal memory provided by the user:
    {user_memory}

    Use both carefully. Do not treat visual observations
    as confirmed personal facts.
    """

    return generate_memory_story(combined_memory, style)
