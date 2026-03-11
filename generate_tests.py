import openai

def generate_tests(code):

    prompt = f"""
You are a senior software engineer.

Generate Python unit tests using pytest for the following code.

Include:
- edge cases
- normal usage cases
- failure cases

Code:
{code}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )

    return response["choices"][0]["message"]["content"]


if __name__ == "__main__":
    with open("sample_code.py","r") as f:
        code = f.read()

    tests = generate_tests(code)
    print(tests)
