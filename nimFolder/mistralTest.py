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
