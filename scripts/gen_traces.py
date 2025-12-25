import json
import requests
from pathlib import Path

queries = [
    "I'm looking for a dairy-free English breakfast with eggs that I can make in about 20-30 minutes.",
    "Suggest an Indian lunch dish with mutton that takes roughly 30 to 60 minutes to cook.",
    "What's a good Mexican chicken dinner that takes under an hour?",
    "I want a quick Italian dessert with chocolate-something I can make in 15 to 20 minutes.",
    "Any American fast-food-style burger ideas for dinner, but without beef?",
    "Looking for a Middle Eastern lamb dish for lunch-no beef, and around an hour of cooking time.",
    "Can you recommend a Chinese chicken lunch recipe with no beef or seafood?",
    "I want an Indian vegetarian breakfast using rice that I can finish in about half an hour.",
    "I need a quick banana smoothie idea for breakfast—something under 20 minutes.",
    "Suggest an Italian vegetarian pasta for lunch that's a bit more involved, maybe 45 to 60 minutes.",
    "Any gluten-free Chinese shrimp dishes that work well for dinner?",
    "What's a vegetarian Mexican breakfast that uses avocado and doesn't take too long?",
    "I'm planning an Indian vegetarian dinner with lentils-dairy-free, and I don't mind a longer cook time.",
    "I want a quick, nut-free yogurt snack I can put together in 10 to 15 minutes.",
    "Any American fast-food-style lunch ideas with fries that I can make quickly?",
    "Looking for a Middle Eastern vegetarian dinner using chickpeas, with a cooking time under 70 minutes.",
    "Suggest an English fish dish for lunch that takes around half an hour.",
    "What's a vegetarian Chinese breakfast using tofu that takes about 25 to 35 minutes?",
    "I want an Italian chicken dinner that's both gluten-free and dairy-free.",
    "Need a quick vegetarian Mexican snack-something salsa-based.",
    "Any Indian vegetarian snacks made with potatoes that are also gluten-free?",
    "I'm looking for a sugar-free dessert using berries that's fast to make.",
    "What's a quick American-style pancake breakfast I can make in under 15 minutes?",
    "Suggest a vegetarian Middle Eastern breakfast that includes hummus.",
    "Any vegetarian Chinese snack ideas like spring rolls that don't take too long?",
    "I just want a simple Italian-style breakfast centered around coffee.",
    "Show me Italian dishes that feature chicken.",
    "I'm looking for Indian food ideas-just no beef.",
    "What can I make for dinner tonight?",
    "Give me some vegetarian ideas using lentils.",
    "I need a lunch recipe with rice that takes about 30 minutes.",
    "Any vegetarian Mexican dishes that use beans?",
    "Suggest a lunch idea with salmon that I can cook in 20-30 minutes.",
    "I'm looking for low-carb Chinese dinner options.",
]

def generate_traces(base_url: str = "http://localhost:8000"):
    """
    Call the /chat endpoint for each query and save traces to a JSON file.
    
    Args:
        base_url: The base URL of the backend server (default: http://localhost:8000)
    """
    traces = []
    
    for i, query in enumerate(queries, 1):
        print(f"Processing query {i}/{len(queries)}: {query[:60]}...")
        
        # Prepare the request payload
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": query
                }
            ]
        }
        
        try:
            # Call the /chat endpoint
            response = requests.post(
                f"{base_url}/chat",
                json=payload,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            
            # Get the response data
            response_data = response.json()
            
            # Store the trace in the desired format
            trace = {
                "request": query,
                "response": response_data["messages"][-1]["content"]  # Get the assistant's response
            }
            traces.append(trace)
            
            print(f"  ✓ Successfully processed query {i}")
            
        except requests.exceptions.RequestException as e:
            print(f"  ✗ Error processing query {i}: {e}")
            # Store error information
            trace = {
                "request": query,
                "response": f"ERROR: {str(e)}"
            }
            traces.append(trace)
    
    # Save traces to JSON file in the annotation folder
    annotation_dir = Path(__file__).parent.parent / "annotation"
    annotation_dir.mkdir(parents=True, exist_ok=True)
    
    output_file = annotation_dir / "traces.json"
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(traces, f, indent=2, ensure_ascii=False)
    
    print(f"\n✓ All traces saved to: {output_file}")
    print(f"Total traces: {len(traces)}")

if __name__ == "__main__":
    import sys
    
    # Allow custom base URL as command line argument
    base_url = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
    
    print(f"Starting trace generation...")
    print(f"Backend URL: {base_url}")
    print(f"Total queries: {len(queries)}\n")
    
    generate_traces(base_url)