prompt = 'tell me slogan for a home security company'


from openai import OpenAI

client = OpenAI()


output = client.completions.create(
    model= 'davinci-002',
    prompt= prompt,
    max_tokens=100,
    temperature=0
)

print(output)

'''from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)'''