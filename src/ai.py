import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
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

    response_text = response.to_json()["choices"][0]["message"]["content"]
    return parse_ai_response(response_text)

def parse_ai_response(response_text):
    lines = response_text.split("\n")
    data = []
    for line in lines:
        parts = line.split(", ")
        if len(parts) == 3:
            data.append({"name": parts[0], "dueDate": parts[1], "weight": parts[2]})
    return data
