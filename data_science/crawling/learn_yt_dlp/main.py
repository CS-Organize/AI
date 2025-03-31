import os

import yt_dlp


def download_video(url, quality="high"):
    """
    영상을 다운로드합니다.

    quality 옵션:
    - 'high': 가장 좋은 비디오+오디오 품질
    - '1080p': 1080p 해상도 (가능한 경우)
    - '720p': 720p 해상도
    - 'audio': 오디오만 다운로드
    """
    if quality == "high":
        format_option = "bestvideo+bestaudio/best"
    elif quality == "1080p":
        format_option = "bestvideo[height<=1080]+bestaudio/best[height<=1080]"
    elif quality == "720p":
        format_option = "bestvideo[height<=720]+bestaudio/best[height<=720]"
    elif quality == "audio":
        format_option = "bestaudio/best"
    else:
        format_option = "best"

    output_dir = "downloaded_videos"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": format_option,
        "outtmpl": output_path,
        "merge_output_format": "mp4",  # 비디오와 오디오를 mp4로 병합
    }

    print(f"다운로드 중... 선택한 품질: {quality}")
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    url = input("영상 URL을 입력하세요: ")
    print("\n품질 옵션:")
    print("1. 최고 품질 (high)")
    print("2. 1080p")
    print("3. 720p")
    print("4. 오디오만 (audio)")

    choice = input("\n원하는 품질 옵션 번호를 선택하세요 (기본: 1): ")

    quality_options = {
        "1": "high",
        "2": "1080p",
        "3": "720p",
        "4": "audio",
    }

    quality = quality_options.get(choice, "high")
    download_video(url, quality)
    print("다운로드가 완료되었습니다!")


if __name__ == "__main__":
    main()
