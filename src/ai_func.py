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

    # Make the API call
    response = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct",
        max_tokens=512,
        temperature=0.6,
        top_p=0.9,
        extra_body={"top_k": 50},
        messages=[{"role": "user", "content": prompt}]
    )

    # Now access the content directly as an attribute
    message_content = response.choices[0].message.content if hasattr(response.choices[0], 'message') else ''
    print(f"Extracted Content: {message_content}")
    
    # Parse the response content into a structured format
    return parse_ai_response(message_content)

def parse_ai_response(response_text):
    response_text = response_text.strip().split("\n")[1:]

    items = {}
    for line in response_text:
        parts = line.split(", ")
        if len(parts) == 3:
            name = parts[0].strip()
            due_date = parts[1].strip()
            weight = parts[2].strip()

            items[name] = {
                "Date": due_date,
                "weight": weight,
                "grade": ""  # empty grade field
            }
    
    return json.dumps(items, indent=2)
