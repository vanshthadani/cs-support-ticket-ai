from unsloth import FastLanguageModel

MODEL_NAME = "vanshthadani/cs-support-v4"
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=MODEL_NAME,
    max_seq_length=1024,
    load_in_4bit = True,
    
)

FastLanguageModel.for_inference(model)