# Gemini Email Summarizer ✉️🤖

A clean, efficient, and user-friendly tool that leverages Google's Gemini API to automatically summarize email threads, extract key action items, and keep your inbox organized.

---

## ✨ Features

- **Automated Email Summarization:** Quickly generate concise summaries of long email chains.
- **Key Action Item Extraction:** Automatically highlight important tasks, deadlines, and follow-ups.
- **Powered by Gemini AI:** Uses Google's advanced Gemini models for natural, high-accuracy summaries.
- **Customizable & Flexible:** Easily configure summary length, tone, and processing parameters.
- **Secure & Fast:** Processes your email data safely with fast throughput.

---

## 🚀 Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- **Python 3.9+**
- A **Google Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/))

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/PoyrazAtalay/Gemini-Email-Summarizer.git
   cd Gemini-Email-Summarizer
   ```

2. **Set up a virtual environment:**

   *Using standard `venv`:*
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

   *Or using `uv`:*
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # Or using uv:
   uv pip install -r requirements.txt
   ```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root directory of the project and add your API credentials:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 🏃 Usage

Run the main application script:

```bash
python main.py
```

---

## 🛠️ Project Structure

```text
Gemini-Email-Summarizer/
├── .env.example          # Example environment variable setup
├── requirements.txt      # Project Python dependencies
├── main.py               # Application entry point
└── README.md             # Project documentation
