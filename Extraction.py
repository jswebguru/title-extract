from openai import OpenAI
import os

def generate_response_new(input_Text):

    result = ''
    try:
        os.environ['OPENAI_API_KEY'] = 'your-openai-api-key'
        client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))  # Initialize with your API key
        completion = client.chat.completions.create(
            model='gpt-4o-2024-05-13',
            messages=[{"role": "user", "content": input_Text}],  # Assuming you want to provide a prompt
            max_tokens=150,
            stream=True,
            temperature=1
        )
        for chunk in completion:

            if chunk.choices[0].delta.content is not None:
                print(chunk.choices[0].delta.content, end='')
                result += chunk.choices[0].delta.content
    except Exception as e:
        print(f"An error occurred: {e}")
    return result


if __name__ == '__main__':
    input_text = ("From the below content, extract the name of the product and the price. Then only print fully analyzed name of the product, not the abbreviation and price.:"
                  "GTAV is available for $10 now.")
    generate_response_new(input_text)
