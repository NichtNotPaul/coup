import ollama
from config import systemprompt
def generate_response(prompt):

    model = "huggingface.co/HauhauCS/Qwen3.5-4B-Uncensored-HauhauCS-Aggressive:Q6_K"
    
    # Simple prompt
    

    try:
        # Generate response
        response = ollama.generate(
    model=model,
    system=systemprompt,
    prompt=prompt,
    think=False,
    options={
        "temperature": 0.7,
        "top_p": 0.8,
        "top_k": 20,
        "min_p": 0,
    }
)       
        
        print(f"\033[1;30mPrompt: {prompt}\033[0m")
        print("-"*50)

        print(response['response'])
        print("-"*50)

        print(f"\033[1;37mModel: {response['model']}")
        print(f"Total duration: {response['total_duration'] / 1e9:.2f} seconds")
        print(f"Load duration: {response['load_duration'] / 1e9:.2f} seconds")
        print(f"Prompt eval count: {response['prompt_eval_count']}")
        print(f"Eval count: {response['eval_count']}\033[0m")
        
        return(response['response'])
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__generate_response__":
    generate_response()
