import google.generativeai as genai

# Configure API key
genai.configure(api_key="enter_the_key")

# Choose a model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Define query and context
query = "What does Confluence do?"
context = "Confluence is a collaboration tool that only allows to share file. Nothing else."

# Generate response with length control
response = model.generate_content(
    f"Question: {query}\nContext: {context}\nProvide a short and precise answer (maximum 2 sentence):"
)

# Print the answer
print("Answer:", response.text.strip())
