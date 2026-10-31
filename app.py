
import streamlit as st

from memory_manager import (
    save_uploaded_image,
    delete_uploaded_image
)

from ai_engine import (
    generate_memory_story,
    generate_visual_memory_story
)
from database import (
    initialize_database,
    save_memory,
    get_all_memories,
    delete_memory
)


st.set_page_config(
    page_title="Echoes of Yesterday",
    page_icon="🕯️",
    layout="wide"
)


# Initialize session state
if "latest_story" not in st.session_state:
    st.session_state["latest_story"] = ""

if "latest_person" not in st.session_state:
    st.session_state["latest_person"] = ""

if "latest_description" not in st.session_state:
    st.session_state["latest_description"] = ""

if "latest_image" not in st.session_state:
    st.session_state["latest_image"] = None

st.set_page_config(
    page_title="Echoes of Yesterday",
    page_icon="🕯️",
    layout="wide"
)

# Initialize database
initialize_database()

# Styling
st.markdown("""
<style>
.stApp {
    background: #101014;
    color: #F5EBDD;
}

section[data-testid="stSidebar"] {
    background: #19171C;
}

h1, h2, h3 {
    color: #E9B96E !important;
}

p {
    color: #D6CCBE;
}

.stButton button {
    background: #A65D36;
    color: white;
    border-radius: 10px;
    border: none;
}

.stButton button:hover {
    background: #C47A4B;
    color: white;
}

div[data-testid="stTextArea"] textarea,
div[data-testid="stTextInput"] input {
    background: #211F25;
    color: white;
}
</style>
""", unsafe_allow_html=True)


# Sidebar
st.sidebar.title("🕯️ Echoes")
st.sidebar.caption("Some memories deserve to live forever.")

page = st.sidebar.radio(
    "EXPLORE",
    [
        "🏠 Home",
        "📷 Memory Revival",
        "🌼 Digital Ofrenda",
        "👻 Ghost Story Mode",
        "📚 Memory Vault"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Powered by Ollama + Qwen")


# HOME
if page == "🏠 Home":

    st.title("Echoes of Yesterday")
    st.subheader("Some memories deserve to live forever.")

    st.write("""
    Welcome to a place where forgotten stories
    find their way home.

    Preserve meaningful memories, transform them
    into stories, and keep the past alive.
    """)

    memories = get_all_memories()

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Memories Preserved", len(memories))

    with col2:
        st.metric("AI Model", "Qwen 2.5 3B")

    st.divider()

    st.markdown("### Explore Your Memories")

    st.write("📷 Memory Revival")
    st.write("🌼 Digital Ofrenda")
    st.write("👻 Ghost Story Mode")
    st.write("📚 Memory Vault")


# MEMORY REVIVAL


# MEMORY REVIVAL
elif page == "📷 Memory Revival":

    st.title("📷 Memory Revival")
    st.write("Every photograph holds a story waiting to be remembered.")

    uploaded_image = st.file_uploader(
        "Upload an old photograph",
        type=["jpg", "jpeg", "png"],
        key="revival_image"
    )

    image_bytes = None

    if uploaded_image:
        image_bytes = uploaded_image.getvalue()
        st.image(
            image_bytes,
            caption="A moment from the past",
            width=400
        )

    person = st.text_input(
        "Who is this memory about?",
        placeholder="Enter a name or nickname"
    )

    memory = st.text_area(
        "Describe your memory",
        placeholder="Tell us about this special moment...",
        height=130
    )

    style = st.selectbox(
        "Choose storytelling style",
        ["Nostalgic", "Heartwarming", "Poetic", "Reflective"]
    )

    # GENERATE STORY
    if st.button("✨ Generate My Memory Story", key="generate_memory"):

        if not memory.strip():
            st.warning("Please describe your memory first.")

        else:
            with st.spinner("Bringing your memories to life..."):

                try:
                    st.session_state["latest_person"] = person
                    st.session_state["latest_description"] = memory
                    st.session_state["latest_image"] = image_bytes

                    if image_bytes:
                        story = generate_visual_memory_story(
                            image_bytes,
                            memory,
                            style
                        )
                    else:
                        story = generate_memory_story(
                            memory,
                            style
                        )

                    st.session_state["latest_story"] = story

                except Exception as error:
                    st.session_state["latest_story"] = f"AI Error: {error}"

    # DISPLAY GENERATED STORY
    if st.session_state["latest_story"]:

        st.divider()
        st.markdown("### 🕯️ Your Memory, Reimagined")

        st.write(st.session_state["latest_story"])

        # SAVE STORY
        if st.button("💾 Save to Memory Vault", key="save_memory_revival"):

            story = st.session_state["latest_story"]

            if story.startswith(("AI Error:", "Vision AI Error:")):
                st.error("Cannot save an unsuccessful generation.")

            else:
                try:
                    image_path = None

                    saved_image = st.session_state["latest_image"]

                    if saved_image:
                        image_path = save_uploaded_image(saved_image)

                    save_memory(
                        title="A Memory from Yesterday",
                        person=st.session_state["latest_person"],
                        description=st.session_state["latest_description"],
                        story=story,
                        memory_type="Memory Revival",
                        image_path=image_path
                    )

                    st.success("Your memory and photograph have been preserved!")

                except Exception as error:
                    st.error(f"Could not save memory: {error}")

        st.download_button(
            "📥 Download Story",
            data=st.session_state["latest_story"],
            file_name="my_memory.txt",
            mime="text/plain",
            key="download_latest_memory"
        )


# DIGITAL OFRENDA

# DIGITAL OFRENDA
elif page == "🌼 Digital Ofrenda":

    st.title("🌼 A Place of Remembrance")

    st.markdown(
        "### Every life leaves behind beautiful memories."
    )

    st.write(
        "Create a personal space to celebrate someone special."
    )

    person = st.text_input(
        "Name or nickname"
    )

    uploaded_image = st.file_uploader(
        "Choose a photograph",
        type=["jpg", "jpeg", "png"],
        key="ofrenda_image"
    )

    if uploaded_image:

        st.image(
            uploaded_image,
            caption="A cherished memory",
            width=350
        )

    remembrance = st.text_area(
        "Write a message or remembrance",
        placeholder="Share a beautiful memory, a lesson, or something you wish to remember...",
        height=150
    )

    st.markdown("### 🌼 Your remembrance altar")

    st.markdown(
        "🕯️ 🌼 🕯️ 🌼 🕯️"
    )

    if st.button("Create My Remembrance"):

        if not person.strip() or not remembrance.strip():

            st.warning(
                "Please provide a name and remembrance."
            )

        else:

            try:

                image_path = None

                if uploaded_image:

                    image_path = save_uploaded_image(
                        uploaded_image.getvalue()
                    )

                save_memory(
                    title=f"Remembering {person}",
                    person=person,
                    description=remembrance,
                    story=remembrance,
                    memory_type="Digital Ofrenda",
                    image_path=image_path
                )

                st.success(
                    f"Your remembrance for {person} has been preserved."
                )

                st.balloons()

            except Exception as error:

                st.error(
                    f"Could not save remembrance: {error}"
                )


# GHOST STORY MODE
elif page == "👻 Ghost Story Mode":

    st.title("👻 Ghost Story Mode")

    st.write("Where memories meet mystery.")

    idea = st.text_area(
        "Describe your story idea",
        placeholder="It was a dark night when..."
    )

    if st.button("Generate Ghost Story"):

        if idea.strip():

            with st.spinner("Something is awakening..."):

                story = generate_memory_story(
                    idea,
                    "Spooky, mysterious and suspenseful fictional horror"
                )

                st.session_state["ghost_story"] = story
                st.session_state["ghost_idea"] = idea

        else:
            st.warning("Enter a story idea first.")

    if "ghost_story" in st.session_state:

        st.divider()

        st.markdown("### 👻 Your Ghost Story")

        st.write(st.session_state["ghost_story"])

        if st.button("💾 Save Ghost Story"):

            save_memory(
                title="A Story from the Shadows",
                person="",
                description=st.session_state["ghost_idea"],
                story=st.session_state["ghost_story"],
                memory_type="Ghost Story"
            )

            st.success("Your story has been saved!")


# MEMORY VAULT

# MEMORY VAULT
elif page == "📚 Memory Vault":

    st.title("📚 Memory Vault")

    st.write(
        "A personal archive of photographs, stories and remembrance."
    )

    memories = get_all_memories()

    if not memories:

        st.info(
            "Your Memory Vault is waiting for its first memory."
        )

    else:

        st.success(
            f"{len(memories)} memories preserved."
        )

        for item in memories:

            (
                memory_id,
                title,
                person,
                description,
                story,
                memory_type,
                created_at,
                image_path
            ) = item

            with st.expander(
                f"🕯️ {title} · {created_at}"
            ):

                st.caption(
                    f"Category: {memory_type}"
                )

                if person:
                    st.write(f"**Remembering:** {person}")

                if image_path:

                    try:
                        st.image(
                            image_path,
                            width=350
                        )

                    except Exception:
                        st.warning(
                            "The stored photograph could not be displayed."
                        )

                st.markdown("**Original Memory**")
                st.write(description)

                st.markdown("**Preserved Story**")
                st.write(story)

                st.download_button(
                    "Download Story",
                    data=story,
                    file_name=f"memory_{memory_id}.txt",
                    key=f"download_{memory_id}"
                )

                if st.button(
                    "Delete Memory",
                    key=f"delete_{memory_id}"
                ):

                    deleted_image = delete_memory(memory_id)

                    if deleted_image:
                        delete_uploaded_image(deleted_image)

                    st.success("Memory deleted.")

                    st.rerun()
