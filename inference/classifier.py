import json

from .model import model, tokenizer


def classify_email(email):
    messages = [
        {
            "role": "system",
            "content": "You Classify Customer Support Emails into a structured JSON tickets"
        },
        {
            "role": "user",
            "content": email
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_dict=True,
        return_tensors="pt"
    ).to(model.device)

    output = model.generate(
        **prompt,
        max_new_tokens=200,
        do_sample=False
    )

    generated_text = tokenizer.decode(
        output[0][prompt["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    print("MODEL OUTPUT:")
    print(generated_text)

    return json.loads(generated_text)


if __name__ == "__main__":
    email = """
    I sent my shoes back about two weeks ago and still haven't seen
    the money returned to my account. Could you check on the refund?
    """

    result = classify_email(email)

    print(result)