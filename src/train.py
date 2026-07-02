import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from trl import SFTTrainer, SFTConfig

def main():
    model_id = "Qwen/Qwen1.5-0.5B" 
    print(f"🤖 Loading Base Model: {model_id}...")
    
    model = AutoModelForCausalLM.from_pretrained(
        model_id, 
        device_map="auto", 
        torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
    )
    tokenizer = AutoTokenizer.from_pretrained(model_id)
    tokenizer.pad_token = tokenizer.eos_token

    print("📊 Loading Portfolio Custom Dataset...")
    dataset = load_dataset("json", data_files="data/portfolio_data.jsonl", split="train")

    # 🔥 NEW & SAFE: Dataset ko map karke ek single 'text' column bana dete hain
    # Isse TRL library bina kisi custom argument ke direct train karegi
    def merge_columns(example):
        return {"text": f"Instruction: {example['instruction']}\nResponse: {example['output']}"}
    
    dataset = dataset.map(merge_columns)

   # 🔥 FIXED: Agar GPU nahi hai toh use_cpu=True apne aap trigger ho jayega
    training_args = SFTConfig(
        output_dir="./training_outputs",
        per_device_train_batch_size=1, 
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        logging_steps=5,
        num_train_epochs=3,
        weight_decay=0.01,
        fp16=torch.cuda.is_available(), 
        save_strategy="no",
        max_length=256,         
        dataset_text_field="text",
        use_cpu=not torch.cuda.is_available() # 🛠️ AGAR GPU NAHI HAI TOH CPU USE KARO
    )

    # Supervised Fine-Tuning (SFT) Standard Implementation
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        args=training_args,
    )

    print("🚀 Fine-Tuning Portfolio-Genie-AI...")
    trainer.train()

    print("💾 Saving Your Custom Portfolio AI Model...")
    trainer.save_model("./portfolio_genie_model")
    tokenizer.save_pretrained("./portfolio_genie_model")
    print("✅ Training Completed Successfully!")

if __name__ == "__main__":
    main()