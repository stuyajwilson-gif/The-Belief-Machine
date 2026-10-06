# The Belief Machine V2

Android-friendly AI character prototype.

## Deploy with Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py`, `requirements.txt`, and `17080.png`.
3. Deploy `app.py` on Streamlit Community Cloud.
4. In Settings → Secrets add:

```toml
OPENAI_API_KEY = "your-key"
OPENAI_MODEL = "gpt-5"
```

Never commit your API key to GitHub.

V2 includes AI conversation, session memory, personality modes, text-to-speech, and a mobile-friendly interface. The architecture is ready for a realistic talking-head/lip-sync renderer.
