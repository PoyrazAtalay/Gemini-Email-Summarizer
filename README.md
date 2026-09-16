# 📧 Email Summarizer

A simple Python tool that uses Google's Gemini API via the OpenAI SDK to automatically create quick summaries and subject lines for your emails.

## ✨ Features

- 🎯 **Smart Summaries**: Extracts a clear subject line and 3 key action points.
- ⚡ **Fast & Lightweight**: Powered by `gemini-3.5-flash-lite`.
- 🔐 **Secure Configuration**: Uses a pre-configured `.env` file for credentials.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install openai python-dotenv
```

*(or using `uv`)*

```bash
uv pip install openai python-dotenv
```

### 2. Configure Your API Key

Open the existing `.env` file and replace `YOUR_API_KEY` with your actual Google Gemini API key:

```env
OPENAI_API_KEY="YOUR_API_KEY"
```

### 3. Run the App

Paste your email text inside `app.py` and run:

```bash
python app.py
```
