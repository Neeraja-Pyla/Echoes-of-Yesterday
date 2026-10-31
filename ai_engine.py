
import ollama

TEXT_MODEL = "qwen2.5:3b"
VISION_MODEL = "qwen2.5vl:3b"


def generate_memory_story(memory, style="Nostalgic"):

    prompt = f"""
    You are Echoes of Yesterday, a thoughtful AI storyteller.

    Create a meaningful story based on the user's memory.

    User's memory:
    {memory}

    Story style: {style}

    Instructions:
    - Preserve the details provided by the user.
    - Do not invent factual personal history.
    - Make the writing emotional and beautiful.
    - Never claim to communicate with deceased people.
    - Give the story a meaningful title.
    """

    try:
        response = ollama.chat(
            model=TEXT_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as error:
        return f"AI Error: {error}"


def analyze_photograph(image_bytes):

    prompt = """
    Carefully describe this photograph.

    Identify only visible details such as:
    - Objects
    - Clothing
    - Environment
    - Activities
    - Background
    - Approximate visual setting

    Important:
    - Do not identify or guess people's identities.
    - Do not guess relationships between people.
    - Do not invent dates, locations or events.
    - Clearly mention when something is uncertain.

    Provide a short, meaningful visual description.
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
            ]
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
    VISUAL OBSERVATIONS FROM THE PHOTOGRAPH:
    {visual_description}

    PERSONAL DETAILS PROVIDED BY THE USER:
    {user_memory}

    Use the visual observations and personal details
    together to create a meaningful story.

    Do not treat visual guesses as confirmed facts.
    """

    story = generate_memory_story(
        combined_memory,
        style
    )

    return story
