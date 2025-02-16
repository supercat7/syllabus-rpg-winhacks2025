import os
import openai

openai.api_key = "OPENAI_API_KEY=eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMTIzMDE1MDQzOTI1MDA4OTk2NCIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTg5NzM0MzM5OCwidXVpZCI6IjJiYmZjMzdiLWVkNzgtNGQ1Yy04ZWRiLTUwODJmZDQ3MjdlMSIsIm5hbWUiOiJMb2NrZWQgSW4iLCJleHBpcmVzX2F0IjoiMjAzMC0wMi0xNFQyMzo0OTo1OCswMDAwIn0.ymTecAW0gvQ10tELC-702wb2HcmEKBaNubDqYUrYPH4"

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
