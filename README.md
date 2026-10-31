# 🕯️ Echoes of Yesterday

### Your memories are fragile. Their stories don't have to be.

**A privacy-first, local AI-powered memory preservation and storytelling application.**

What if an old photograph could become a story worth remembering?

Echoes of Yesterday transforms personal memories and photographs into meaningful stories using locally running AI models. It provides a digital space where people can preserve photographs, celebrate loved ones, and keep personal histories alive.

Built for the **DEV.to Open-Source AI Challenge – Week 4: Ghost in the Machine**.

---

## 🌟 The Problem

Photographs, handwritten memories, and family stories are important parts of our history. But over time, photographs fade, stories are forgotten, and meaningful moments can disappear.

Many AI storytelling applications depend on cloud-based services, requiring users to share personal information and photographs with external platforms.

**What if we could use AI to preserve memories without depending on external AI APIs?**

## 💡 Our Solution

Echoes of Yesterday is a local AI memory companion that transforms personal memories into meaningful digital experiences.

It brings together:

- AI-powered memory storytelling
- Photograph understanding
- Digital remembrance
- Personal memory archiving

The goal is simple: help people preserve not just photographs, but the stories and emotions behind them.

## ✨ Key Features

### 📷 1. Memory Revival

Turn personal memories into meaningful stories.

- Upload an old photograph.
- Describe the personal memory behind it.
- Use AI to analyse visible photographic details.
- Generate stories in different styles.
- Choose from Nostalgic, Heartwarming, Poetic, and Reflective styles.
- Save the original description alongside the generated story.

### 🌼 2. Digital Ofrenda

Inspired by the Día de los Muertos tradition of remembering and celebrating loved ones.

- Create a personal remembrance space.
- Add photographs and meaningful messages.
- Preserve special memories.
- Celebrate lives through digital remembrance.

### 👻 3. Ghost Story Mode

Explore the connection between memories, imagination, and storytelling.

- Generate mysterious fictional stories.
- Create atmospheric and suspenseful narratives.
- Explore creative storytelling inspired by the Ghost in the Machine theme.

### 📚 4. Memory Vault

A personal archive for saved memories.

- Store personal descriptions and generated stories.
- Preserve uploaded photographs locally.
- Browse saved memories.
- Download stories as text files.
- Delete memories and their associated photographs.

## 🧠 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Interactive user interface |
| Ollama | Local AI model execution |
| Qwen 2.5 3B | Memory storytelling |
| Qwen 2.5 VL 3B | Photograph understanding |
| SQLite | Memory database |
| Pillow | Image processing |

## 🏗️ System Architecture

```text
                    USER
                      |
                      v
             STREAMLIT APPLICATION
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
       Memory      Digital     Ghost Story
       Revival     Ofrenda        Mode
          |
          v
       AI ENGINE
          |
     +----+----------------+
     |                     |
     v                     v
 Qwen 2.5 3B          Qwen 2.5 VL 3B
 Text Generation     Image Analysis
     |                     |
     +----------+----------+
                |
                v
          MEMORY STORAGE
                |
          +-----+------+
          |            |
          v            v
        SQLite      Local Image
        Database     Storage
```

## 🔓 Why Open Innovation Matters

Personal memories deserve privacy, ownership, and accessibility.

Echoes of Yesterday explores how locally running open-weight AI models can make personal AI experiences more independent.

**Our principles:**

- **Privacy-first:** Photographs and memories are processed and stored locally by the application.
- **No external AI API dependency:** AI inference runs through Ollama.
- **User ownership:** Users control their local memory archive.
- **Model flexibility:** Compatible local models can be explored and integrated.
- **Accessibility:** No paid AI API subscription is required for local inference.

The Qwen models used in this project are open-weight models. Open-weight availability should not be confused with OSI-certified open-source licensing.

## 🚀 Getting Started

### Prerequisites

Install the following:

1. Python 3.10 or newer.
2. [Ollama](https://ollama.com/).
3. Git.

### 1. Clone the repository

```bash
git clone https://github.com/Neeraja-Pyla/Echoes-of-Yesterday.git

cd Echoes-of-Yesterday
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If you use Command Prompt:

```cmd
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the AI models

Open a terminal and run:

```bash
ollama pull qwen2.5:3b
```

```bash
ollama pull qwen2.5vl:3b
```

Make sure Ollama is running before launching the application.

### 5. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually:

```text
http://localhost:8501
```

You're ready to preserve your first memory!

**Note:** The first model download requires an internet connection. Local inference requires the downloaded models and sufficient system resources. Performance depends on your hardware.

## 📁 Project Structure

```text
Echoes-of-Yesterday/
│
├── app.py
├── ai_engine.py
├── database.py
├── memory_manager.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
│   └── style.css
│
├── uploads/       # Local uploaded photographs
├── memories.db    # Local SQLite database
└── venv/          # Python virtual environment
```

Local photographs, the database, and the virtual environment are excluded from version control.

## 🔐 Privacy and Responsible AI

Echoes of Yesterday is designed around responsible memory preservation.

- AI should not invent personal history.
- Photograph analysis should describe visible details without identifying people.
- AI-generated stories are creative interpretations, not verified historical records.
- The application does not claim to communicate with deceased people.
- Local files and databases are not automatically encrypted.
- Users should protect their computers and maintain their own backups.

**Important:** Local processing reduces external data sharing, but does not guarantee complete security. Offline operation should be verified separately.

## 🚧 Challenges and Learnings

Building a local AI application introduced several practical challenges:

- Running multiple AI models on CPU hardware.
- Balancing storytelling quality with generation speed.
- Connecting image analysis with text generation.
- Maintaining persistent memory storage using SQLite.
- Managing uploaded photographs safely.
- Designing an experience around an emotionally sensitive topic.

These challenges helped explore the practical value and limitations of locally running AI.

## 🔮 Future Possibilities

Some possibilities for future development include:

- Interactive chronological memory timelines.
- Exportable family memory books.
- Memory archive backup and restoration.
- Multilingual storytelling.
- Improved local photograph restoration.
- Family-controlled shared heritage archives.

## 🎃 Hackathon Submission

| Detail | Information |
|---|---|
| Challenge | DEV.to Open-Source AI Challenge – Week 4 |
| Theme | Ghost in the Machine |
| Project | Echoes of Yesterday |
| Category | Local AI / Memory Preservation |
| AI Runtime | Ollama |
| Models | Qwen 2.5 3B and Qwen 2.5 VL 3B |

**GitHub Repository:**  
https://github.com/Neeraja-Pyla/Echoes-of-Yesterday

**Project Demo:**  
https://drive.google.com/file/d/1dO8DOck0pCMQD3CVSQmMw87Lh2RmGXDw/view?usp=sharing

## ❤️ Final Thought

A photograph captures a moment.

A story gives that moment meaning.

And a memory gives it a place to live.

**Echoes of Yesterday — because some memories deserve to live forever.**

---

*Built with Python, Streamlit, Ollama, and Qwen.*
