import os
from openai import OpenAI
from dotenv import load_dotenv

# Load Hugging Face token from .env file
load_dotenv()

# Initialize OpenAI-compatible client via Hugging Face router
client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ.get("HF_TOKEN"),
)

def summarize_text(text):
    """
    Summarize the input text using a Hugging Face-hosted OpenAI-compatible model.

    Parameters:
        text (str): The raw input text to summarize.

    Returns:
        str: The summary text or an error message.
    """
    try:
        if not text or text.strip() == "":
            return "❌ No text to summarize."

        prompt = f"Please summarize the following text:\n\n{text}"

        completion = client.chat.completions.create(
            model="openai/gpt-oss-120b:novita",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        return f"❌ Error during summarization: {str(e)}"
