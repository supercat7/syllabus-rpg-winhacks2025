import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
)

def parse_syllabus_with_ai(syllabus_text):
    prompt = (
        "You are an assistant designed to extract assignments, exams, due dates, and weights from a syllabus. "
        "The syllabus text is below. Please return a list of extracted items in the following format:\n"
        "Assignment/Exam, Due Date, Weight (%)\n\n"
        f"{syllabus_text}\n\n"
        "Please ensure the response is in a structured format with each item on a new line."
    )

    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct",
        max_tokens=512,
        temperature=0.6,
        top_p=0.9,
        extra_body={"top_k": 50},
        messages=[{"role": "user", "content": prompt}]
    )

    message_content = response.choices[0].message.content if hasattr(response.choices[0], 'message') else ''
    
    return parse_ai_response(message_content)

def parse_ai_response(response_text):
    if not response_text:
        return []

    response_lines = response_text.strip().split("\n")
    items = []

    for line in response_lines:
        if line.count(",") < 2:
            continue

        parts = line.split(", ")

        name = parts[0].strip()
        weight = parts[-1].strip()
        if len(parts) > 2:
            due_date = ", ".join(parts[1:-1]).strip()
        else:
            continue

        items.append({
            "Assignment": name,
            "Due Date": due_date,
            "Weight (%)": weight
        })

    return items