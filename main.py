import os
import requests

def get_weather():
    # Lấy API key bảo mật từ môi trường GitHub Secrets
    api_key = os.getenv("WEATHER_API_KEY")
    city = "Can Tho"
    
    if not api_key:
        print("Lỗi: Chưa tìm thấy WEATHER_API_KEY trong cấu hình Secrets!")
        return

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&lang=vi"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        location = data['location']['name']
        temp_c = data['current']['temp_c']
        condition = data['current']['condition']['text']
        humidity = data['current']['humidity']
        
        print("=" * 40)
        print(f" THÔNG TIN THỜI TIẾT TẠI {location.upper()}")
        print(f" Nhiệt độ: {temp_c}°C")
        print(f" Trạng thái: {condition}")
        print(f" Độ ẩm: {humidity}%")
        print("=" * 40)
        
    except Exception as e:
        print(f"Đã xảy ra lỗi khi lấy dữ liệu: {e}")

if __name__ == "__main__":
    get_weather()
