from openai import OpenAI

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

completion = client.chat.completions.create(
    model="meta/llama3-70b-instruct",
    messages=[{"role": "user",
               "content": "nvidia vs openai"}],
    temperature=0.5,
    top_p=1,
    max_tokens=1024,
    stream=True
)

for chunk in completion:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
