import ollama

def main():
    # Model name
    model = "huggingface.co/HauhauCS/Qwen3.5-4B-Uncensored-HauhauCS-Aggressive:Q4_K_M"
    
    # Simple prompt
    prompt = "Explain quantum computing in 2-3 sentences."
    
    print(f"Using model: {model}")
    print(f"Prompt: {prompt}\n")
    print("-" * 50)
    
    try:
        # Generate response
        response = ollama.generate(
    model="gpt-oss:20b",
    prompt=prompt,
    options={
        "temperature": 0.7,
        "top_p": 0.8,
        "top_k=20"
        "min_p": 0,
        "thinking": False
    }
)
        
        # Print the response
        print(response['response'])
        print("-" * 50)
        
        # Optional: Print metadata
        print(f"\nModel: {response['model']}")
        print(f"Total duration: {response['total_duration'] / 1e9:.2f} seconds")
        print(f"Load duration: {response['load_duration'] / 1e9:.2f} seconds")
        print(f"Prompt eval count: {response['prompt_eval_count']}")
        print(f"Eval count: {response['eval_count']}")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
