import os
import openai
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(
    base_url="https://api.studio.nebius.ai/v1/",
)

def read_json(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return {}

def write_comp_to_json(data, file_path="data.json"):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Data written to JSON successfully.")
    except Exception as e:
        print(f"Error writing to JSON file: {e}")

def parse_syllabus_with_ai(syllabus_text):
    prompt = (
        "You are an assistant designed to extract assignments, exams, due dates, and weights from a syllabus. "
        "The syllabus text is below. Please return a list of extracted items in the following format:\n"
        "Assignment/Exam, Due Date, Weight (%)\n\n"
        f"{syllabus_text}\n\n"
        "Ensure the response is structured as described, with each item on a new line."
    )

    try:
        # Make the API call
        response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct",
            max_tokens=512,
            temperature=0.6,
            top_p=0.9,
            extra_body={"top_k": 50},
            messages=[{"role": "user", "content": prompt}]
        )

        # Extract content from the response
        message_content = response.choices[0].message.content if hasattr(response.choices[0], 'message') else ''
        print(f"Raw AI Response: {message_content}")  # Debugging log
        
        # Parse the response content into a structured format
        return parse_ai_response(message_content)

    except Exception as e:
        print(f"Error during API call: {e}")
        return "Error processing syllabus. Please try again later."
    
def parse_ai_response(response_text):
    if not response_text:
        return json.dumps([])  # Return an empty list if no valid response

    response_lines = response_text.strip().split("\n")
    items = []

    for line in response_lines:
        parts = line.split(", ")
        if len(parts) >= 3:  # Ensure it has at least three parts
            name = parts[0].strip()
            due_date = parts[1].strip()
            weight = parts[2].strip()
            items.append({
                "Assignment": name,
                "Due Date": due_date,
                "Weight (%)": weight
            })

    # Convert list of items to JSON string
    return json.dumps(items)



    if items:
        print(f"Parsed Items: {json.dumps(items, indent=2)}")  # Debugging log
        return json.dumps(items, indent=2)
    else:
        print("No valid results found in response.")
        return "No valid results found."
