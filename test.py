from pyyoutube import Api
from pyyoutube import VideoListResponse

api_key = "AIzaSyD3VB5Cwmkr8X9rfI5vmy1qTppqRzifFwU"

api = Api(api_key=api_key)

result: VideoListResponse = api.get_video_by_id(video_id="ePyc0W5vJOM")
print(type(result))
print(result.model_dump_json(indent=2))
