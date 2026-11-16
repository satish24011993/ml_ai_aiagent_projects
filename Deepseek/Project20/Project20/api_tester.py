import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_API = "http://localhost:11434/api/generate"

def test_api(api_url, method = "GET", headers=None, payload=None, expected_fields=""):
    """
    Tests an API endpoint and validates the response.
    """
    try:
        headers = headers or {}
        payload = payload or {}

        # Send API request
        if method.upper() == "GET":
            response = requests.get(api_url, headers=headers)
        elif method.upper() == "POST":
            response = requests.post(api_url, json=payload, headers=headers)
        else:
            return "Unsupported method. Use GET or POST."
        
        # Extract response details
        response_time = response.elapsed.total_seconds()*1000 # Convert to milliseconds
        response_data = response.json()

        # AI-Based Validation Prompt
        prompt = f'Analyze the following API response and check if it contains the required fields: {expected_fields}\n\n'\
                f"Response:\n{response_data}\n\n"\
                f"Provide validation feedback and missing fields, if any."
        
        ai_payload = {
            'model':'deepseek-r1',
            'prompt':prompt,
            'stream':False
        }

        ai_response = requests.post(OLLAMA_API, json=ai_payload)

        if ai_response.status_code == 200:
            validation_feedback =  ai_response.json().get('ai_response','No API response')
        else:
            validation_feedback = "AI validation not available."
        
        # Construct final output
        output = f"API Test Result:\n"\
                f"-- Status Code: {response.status_code}\n"\
                f"-- Validation Feedback:\n {validation_feedback}"
        return output
    except Exception as e:
        return f"Error: {str(e)}"
    

interface = gr.Interface(
    fn=test_api,
    inputs=[
        gr.Textbox(label='API URL'),
        gr.Radio(['GET','POST'], label="Method"),
        gr.Textbox(label="Headers (JSON format, optional)"),
        gr.Textbox(label="Payload (JSON format, optional)"),
        gr.Textbox(label="Expected Fields (comma-separated)"),
    ],
    outputs=gr.TextArea(label='AI API TEST output'),
    title="AI-Powered API Tester",
    description="Enter an API endpoint and test its response validation."
)


if __name__ == '__main__':
    interface.launch()

# if __name__ == "__main__":
#     api = 'https://jsonplaceholder.typicode.com/posts/1'
#     print("### AI API Test Output ###")
#     print(test_api(api, "GET", expected_fields="userId, id, title, body"))