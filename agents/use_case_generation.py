import openai

openai.api_key = "your_openai_api_key"

def generate_use_cases(insights):
    prompt = f"""Generate AI and GenAI use cases for a company in the {insights['industry']} industry 
    focusing on {', '.join(insights['focus_areas'])}. Suggest use cases for improving {', '.join(insights['trends'])}."""
    
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    use_cases = response['choices'][0]['text'].strip().split('\n')
    return use_cases

# Example Usage
use_cases = generate_use_cases(company_insights)
print(use_cases)
