import requests
import gradio as gr

# DeepSeek API URL
OLLAMA_URL = "http://localhost:11434/api/generate"

# Sample Product Dataset
PRODUCT_DB = {
    "laptop": [
        "Apple MacBook Air M2 - Lightweight, powerful, and great battery life.",
        "Dell XPS 13 - High performance with a sleek design.",
        "Lenovo ThinkPad X1 Carbon - Ideal for business professionals."
    ],
    "smartphone":[
        "iPhone 14 -  Great camera and iOS experience.",
        "Samsung Galaxy S23 - High-performance Android flagship.",
        "Google Pixel 7 - Best AI-powered camera features."
    ]
}


def recommend_product(query):
    """
    Uses DeepSeek AI to analyze user intent and suggest relevant products.
    """
    prompt = f"Analyze the following user query and recommend the best matching products:\n\n{query}"\
            f"Available product categories: {list(PRODUCT_DB.keys())}\n" \
            f"Provide a list of top recommendations."
    
    payload = {
        'model':'deepseek-r1',
        'prompt':prompt,
        'stream':False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    if response.status_code == 200:
        response = response.json().get("response", "I'm sorry, I don't have recommendations for that.")

        # Find matching category in dataset
        for category in PRODUCT_DB:
            if category in query.lower():
                return "\n".join(PRODUCT_DB[category])
        return response
    else:
        return f"Error: {response.text}"


interface = gr.Interface(
    fn=recommend_product,
    inputs=gr.Textbox(lines=2, placeholder="Ask for product recommendations (e.g., best smart phone under $500)"),
    outputs=gr.Textbox(label="Recommended Products"),
    title="AI-Powered E-commerce Recommendation Bot",
    description="Enter your query and get AI-generated product suggestions.",
)


if __name__ == "__main__":
    interface.launch()

# # Test Product Recommender
# if __name__ == "__main__":
#     test_query = "Recommend a good budget laptop."
#     print("### AI Product Recommendations ###")
#     print(recommend_product(test_query))