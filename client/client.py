import requests
import time
import json

def generate_animation(TTSSentence, isFirstChunk, voiceVector, speed, conversationIndex, currentConversationIndex):
    # Define the API endpoint
    remote_url = "http://34.91.82.222:8080/generate_animation"

    # Ensure TTSSentence is not empty
    if len(TTSSentence) == 0:
        print("TTSSentence is empty")
        return

    start_time = time.time()
    
    print("strings", TTSSentence)

    try:
        response = requests.post(
            remote_url,
            headers={
                'Content-Type': 'application/json'
            },
            data=json.dumps({
                "text": TTSSentence,
                "isFirstChunk": isFirstChunk,
                "add_post_padding": False,
                "voice_vector": voiceVector,
                "speed": speed
            })
        )
        
        # Check if the request was successful
        if response.status_code == 200:
            end_time = time.time()
            print(f'Duration: {end_time - start_time:.2f}s')
            # print("Response:", response.json())
        else:
            print("Failed with status code:", response.status_code)
            # print("Response:", response.text)
            
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

# Example usage
generate_animation(
    TTSSentence="I wonder how long this will take today.",
    isFirstChunk=True,
    voiceVector=[0, 0, 1],
    speed=1.0,
    conversationIndex=1,
    currentConversationIndex=0
)
