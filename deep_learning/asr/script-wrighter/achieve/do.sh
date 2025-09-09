#!/bin/bash

# URL 배열 정의
urls=(
    "https://www.youtube.com/watch?v=NJx1336n6ww",
    "https://www.youtube.com/watch?v=7ji0jHcdq1A",
    "https://www.youtube.com/watch?v=AuoKEvYPdrU",
    "https://www.youtube.com/watch?v=k7Nn6K2rcRc",
    "https://www.youtube.com/watch?v=dR7f1zt0ShM",
    "https://www.youtube.com/watch?v=d4oM-6UxuEY",
    "https://www.youtube.com/watch?v=n2DU2klscfg",
    "https://www.youtube.com/watch?v=HoO-iSez8t8",
    "https://www.youtube.com/watch?v=uumGoaJVp_8"
)

# 각 URL에 대해 yt-dlp 실행
for url in "${urls[@]}"; do
    if [ ! -z "$url" ]; then
        echo "오디오 다운로드 중: $url"
        yt-dlp \
            --extract-audio \
            --audio-format mp3 \
            --audio-quality 0 \
            --output "%(title)s.%(ext)s" \
            "$url"

        if [ $? -eq 0 ]; then
            echo "다운로드 완료: $url"
        else
            echo "다운로드 실패: $url"
        fi
        echo "----------------------------------------"
    fi
done

echo "모든 오디오 다운로드가 완료되었습니다."
