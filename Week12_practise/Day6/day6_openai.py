import openai

# Set OpenAI API key
openai.api_key = "sk-proj-tvu6XINWFJ_C7MbyW7xF1lf9NNTeB8TdHj_-N5mUtwIaATLHY1lE2UoaxB8sC5tuumS8FK7rlkT3BlbkFJVO8aNNmOsrGLQB_Ylb5UTxPvRZD9C2b1hM7hK-6CrJVHwPDeMoXCp9nrdtIRcdIRR2sjIoBPMA"

try:
    # Generate text using GPT-3.5 Turbo
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role":"system","content":"You are a helpful assistant."},
            {"role":"user","content":"Write a short story about a robot learning to cook."}
        ],
        max_tokens=150,
        temperature=0.7
    )

    print("Generated Text:\n", response["choices"][0]["message"]["content"].strip())

except Exception as e:
    print(f"An error occured: {e}")
