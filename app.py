def generate_plan(text):
    response = client.chat.completions.create(
        model="llama-3.1-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a senior career advisor. Provide clear, structured, actionable guidance."},
            {"role": "user", "content": text}
        ]
    )

    msg = response.choices[0].message

    # Extract content safely across all Groq versions
    if isinstance(msg, dict):
        return msg.get("content", "No content returned.")
    return msg
