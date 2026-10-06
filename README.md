# Customer Support AI

A fine-tuned small language model that converts customer-support emails into structured support tickets.

Built with **Qwen2.5-0.5B-Instruct + LoRA + Unsloth**, with a Streamlit interface for inference.

## Demo

The model takes a natural-language customer email and produces a structured ticket containing:

* Category & subcategory
* Urgency
* Sentiment
* Customer satisfaction
* Detected product
* Issue summary
* Requested action
* Human-escalation requirement

![Example 1](screenshots/screenshot-1.png)

![Example 2](screenshots/screenshot-2.png)

## How It Works

```text
Customer Email
      ↓
Qwen2.5-0.5B + LoRA
      ↓
Structured JSON Ticket
      ↓
Streamlit UI
```

## Model & Training

* **Base model:** Qwen/Qwen2.5-0.5B-Instruct
* **Fine-tuning:** LoRA
* **Training framework:** Unsloth + TRL
* **Dataset:** Synthetic customer-support emails generated with an LLM
* **Final version:** V4
* **Final training loss:** ~0.20

The model was iteratively improved from V1 → V4 by refining the dataset, taxonomy rules, and generation instructions.

## Evaluation

A blind test using **10 previously unseen customer-support emails** achieved:

**9.5 / 10 (95%)**

The evaluation focused on the correctness of the structured ticket fields rather than simply matching the wording of the generated issue summary.

## Project Structure

```text
cs-support-ticket-ai/
├── app.py
├── inference/
├── training/
├── data/
├── screenshots/
├── requirements.txt
└── README.md
```

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

> Training code and the final dataset are included in the repository to document the complete model-development process.

## Tech Stack

**Python · PyTorch · Transformers · Qwen · LoRA · Unsloth · TRL · Streamlit**

---

Built as a practical AI engineering project focused on fine-tuning, inference, structured outputs, and integrating an LLM into a usable application.
