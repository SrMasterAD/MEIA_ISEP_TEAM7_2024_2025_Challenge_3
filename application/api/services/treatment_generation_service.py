import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from fastapi import HTTPException  # Import HTTPException for error handling

# ----------- SETTINGS -------------
model_path = "./application/api/ai_models/bart-wheat-reports-clean"  # Your fine-tuned model folder
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

# Load model and tokenizer
try:
    tokenizer = BartTokenizer.from_pretrained(model_path)
    model = BartForConditionalGeneration.from_pretrained(model_path).to(device)
    model.eval()
except Exception as e:
    raise HTTPException(status_code=500, detail=f"Failed to load model or tokenizer: {e}")

# ----------- PREDICT FUNCTION -------------
def generate_answer(question):
    try:
        inputs = tokenizer(
            question,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=64
        ).to(device)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during tokenization: {e}")
    
    try:
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_length=512,
                num_beams=8,
                no_repeat_ngram_size=6,
                early_stopping=True
            )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during generation: {e}")
    
    try:
        decoded = tokenizer.decode(outputs[0], skip_special_tokens=True)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error during decoding the output: {e}")
    
    if not decoded.strip():
        raise HTTPException(status_code=404, detail=f"No answer found for question: {question}")
    
    return decoded


async def generate_treatment(disease):
    # Construct questions for treatment, cause, and management
    question_treatment = f"{disease} treatment"
    question_cause = f"{disease} cause"
    question_management = f"{disease} management"

    # Generate the answer for each question with exception handling
    try:
        treatment = generate_answer(question_treatment)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating treatment: {e}")
        
    if not treatment:
        raise HTTPException(status_code=404, detail="Treatment not found")

    try:
        cause = generate_answer(question_cause)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating cause: {e}")
        
    if not cause:
        raise HTTPException(status_code=404, detail="Cause not found")

    try:
        management = generate_answer(question_management)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating management: {e}")
        
    if not management:
        raise HTTPException(status_code=404, detail="Management not found")

    # Return the treatment, cause, and management as a dictionary
    return {
        "treatment": treatment,
        "cause": cause,
        "management": management
    }
