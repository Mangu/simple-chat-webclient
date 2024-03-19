import requests
import asyncio
import json
import aiohttp
import argparse

# Test Video Id - 06d98a2da3

# Define constants
CLIENT_ID = 'e9981a60-6e1f-489c-a871-b76be181e6e0'
API_ENDPOINT = 'https://api.videoindexer.ai'
ACCOUNT_ID = 'd2c1b9cd-eb31-475c-ae6b-90e6c1cf4525'
LOCATION = 'trial'
SUBSCRIPTION_KEY = 'a34eee2d6d0f4206974d5bc5902feef0'
AZURE_OPEN_AI_KEY = '76b77f8749a14af4b2ae0ff591bcf398'
AOAI_ENDPOINT = 'https://diazaoai-s.openai.azure.com/openai/deployments/gpt-4v/chat/completions?api-version=2023-03-15-preview'

async def get_video_index(videoId):
    async with aiohttp.ClientSession() as session:
        # Get access token
        token_url = f'{API_ENDPOINT}/auth/{LOCATION}/Accounts/{ACCOUNT_ID}/AccessToken'
        token_headers = {'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}
        async with session.get(token_url, headers=token_headers) as resp:
            access_token = await resp.text()
        access_token = access_token.replace('"', '')  # Remove quotes from token

        # Get video index
        url = f'{API_ENDPOINT}/{LOCATION}/Accounts/{ACCOUNT_ID}/Videos/{videoId}/Index'
        headers = {'Authorization': f'Bearer {access_token}'}
        async with session.get(url, headers=headers) as resp:
            data = await resp.json()

        # Generate logs
        logs = []
        async for log in generate_shots(data['videos'][0]['insights']['shots'], videoId, access_token):
            logs.append(log)
            try:
                cleaned_json = log['description'].replace('```json\n', '').replace('\n```', '')
                parsed_json = json.loads(cleaned_json)
                log['description'] = parsed_json
                if not parsed_json.get('similar'):
                    logs.append(log)
                else:
                    print(f"Skipping log with similar text: {log}")
            except Exception as e:
                print(f"Error: {e}")

        # Add logs to data
        data['logs'] = logs

        # Save data to a JSON file
        with open(f'{data['name']}_data.json', 'w') as f:
            json.dump(data, f)

        transcripts = data['videos'][0]['insights']['transcripts']
        return transcripts
    
async def generate_shots(shots, video_id, access_token):
    for shot in shots:
        for key_frame in shot['keyFrames']:
            if key_frame and 'instances' in key_frame and len(key_frame['instances']) > 0:
                instance = key_frame['instances'][0]
                text = await generate_description(video_id, instance['thumbnailId'], access_token) if 'thumbnailId' in instance else ''
                yield {
                    'start': instance['start'],
                    'end': instance['end'],
                    'description': text
                }

async def generate_description(video_id, thumbnail_id, access_token):
    image = f"{API_ENDPOINT}/{LOCATION}/Accounts/{ACCOUNT_ID}/Videos/{video_id}/Thumbnails/{thumbnail_id}?accessToken={access_token}"
    prompt = {
        "role": "user",
        "content": [
            {"type": "text", "text": "You are a video analyser. This image is a scene for a sport event. Provide the following: What is the sport? Is the event location indoors or outdoors? Title of the scene, A short decription of the scene as if you where a sports reporter. And always and only return back JSON with the following field: tittle, description, sport, location, similar. If the image is similar to the previous one, similar should be true. "},
            {
                "type": "image_url",
                "image_url": {"url": image,},
            },
        ],
    }
    headers = {
        'api-key': AZURE_OPEN_AI_KEY,
        'Content-Type': 'application/json'
    }
    try:
        response = requests.post(AOAI_ENDPOINT, json={
            'model': 'gpt-4-vision-preview',
            'messages': [prompt],
            'max_tokens': 300,
        }, headers=headers, timeout=500)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
        return None
    return response.json()['choices'][0]['message']['content']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process video ID.')
    parser.add_argument('video_id', type=str, help='The ID of the video to process')

    args = parser.parse_args()

    asyncio.run(get_video_index(args.video_id))