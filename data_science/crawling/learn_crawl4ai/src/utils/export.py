import csv
import json
import os
from typing import Any, Dict, List, Optional, Union

import yaml

from utils.file import create_unique_filename


def save_to_json(data: Any, file_name: str = "output", dir_name: str = "output") -> Optional[str]:
    """
    데이터를 JSON 파일로 저장합니다.

    Args:
        data: 저장할 데이터
        file_name: 파일 이름 (기본값: "output")
        dir_name: 디렉토리 이름 (기본값: "output")

    Returns:
        Optional[str]: 저장된 파일 경로 또는 None (실패 시)
    """
    try:
        output_file = create_unique_filename(dir_name, file_name, "json")

        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"JSON 저장 완료: {output_file}")
        return output_file
    except Exception as e:
        print(f"JSON 저장 오류: {str(e)}")
        return None


def save_to_csv(
    data: List[Dict[str, Any]], file_name: str = "output", dir_name: str = "output"
) -> Optional[str]:
    """
    데이터를 CSV 파일로 저장합니다.

    Args:
        data: 저장할 데이터 (딕셔너리 리스트)
        file_name: 파일 이름 (기본값: "output")
        dir_name: 디렉토리 이름 (기본값: "output")

    Returns:
        Optional[str]: 저장된 파일 경로 또는 None (실패 시)
    """
    if not data or not isinstance(data, list) or len(data) == 0:
        print("CSV로 저장할 데이터가 없거나 유효하지 않습니다.")
        return None

    try:
        output_file = create_unique_filename(dir_name, file_name, "csv")

        # 첫 번째 행의 키를 필드 이름으로 사용
        fieldnames = data[0].keys()

        with open(output_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"CSV 저장 완료: {output_file}")
        return output_file
    except Exception as e:
        print(f"CSV 저장 오류: {str(e)}")
        return None


def save_to_yaml(data: Any, file_name: str = "output", dir_name: str = "output") -> Optional[str]:
    """
    데이터를 YAML 파일로 저장합니다.

    Args:
        data: 저장할 데이터
        file_name: 파일 이름 (기본값: "output")
        dir_name: 디렉토리 이름 (기본값: "output")

    Returns:
        Optional[str]: 저장된 파일 경로 또는 None (실패 시)
    """
    try:
        output_file = create_unique_filename(dir_name, file_name, "yaml")

        with open(output_file, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False)

        print(f"YAML 저장 완료: {output_file}")
        return output_file
    except Exception as e:
        print(f"YAML 저장 오류: {str(e)}")
        return None


def save_extracted_data(result, format: str = "json") -> Optional[str]:
    """
    추출된 데이터를 지정된 형식으로 저장합니다.

    Args:
        result: 크롤링 결과 객체
        format: 저장 형식 ("json", "csv", "yaml" 중 선택, 기본값: "json")

    Returns:
        Optional[str]: 저장된 파일 경로 또는 None (실패 시)
    """
    if not result.success or not result.extracted_content:
        print("저장할 추출 데이터가 없습니다.")
        return None

    try:
        # JSON 문자열을 파이썬 객체로 변환
        data = json.loads(result.extracted_content)

        # 저장 형식에 따라 저장 함수 호출
        if format.lower() == "csv":
            # 데이터가 리스트가 아니면 리스트로 변환
            if not isinstance(data, list):
                data = [data]
            return save_to_csv(data, "extracted_data")
        elif format.lower() == "yaml":
            return save_to_yaml(data, "extracted_data")
        else:  # json
            return save_to_json(data, "extracted_data")
    except Exception as e:
        print(f"추출 데이터 저장 오류: {str(e)}")
        return None


def save_markdown(result, save_raw=True, save_fit=True) -> List[str]:
    """
    마크다운 결과를 저장합니다.

    Args:
        result: 크롤링 결과 객체
        save_raw: 원본 마크다운 저장 여부 (기본값: True)
        save_fit: 가공된 마크다운 저장 여부 (기본값: True)

    Returns:
        List[str]: 저장된 파일 경로 리스트
    """
    saved_files = []

    if not result.success or not result.markdown:
        print("저장할 마크다운 데이터가 없습니다.")
        return saved_files

    md_obj = result.markdown

    try:
        # 원본 마크다운 저장
        if save_raw and md_obj.raw_markdown:
            raw_file = create_unique_filename("output", "raw_markdown", "md")
            with open(raw_file, "w", encoding="utf-8") as f:
                f.write(md_obj.raw_markdown)
            saved_files.append(raw_file)
            print(f"원본 마크다운 저장 완료: {raw_file}")

        # 가공된 마크다운 저장
        if save_fit and md_obj.fit_markdown:
            fit_file = create_unique_filename("output", "fit_markdown", "md")
            with open(fit_file, "w", encoding="utf-8") as f:
                f.write(md_obj.fit_markdown)
            saved_files.append(fit_file)
            print(f"가공된 마크다운 저장 완료: {fit_file}")

        return saved_files
    except Exception as e:
        print(f"마크다운 저장 오류: {str(e)}")
        return saved_files


def save_media(result, save_images=True, save_videos=False) -> Dict[str, List[str]]:
    """
    미디어 파일 정보를 저장합니다.

    Args:
        result: 크롤링 결과 객체
        save_images: 이미지 정보 저장 여부 (기본값: True)
        save_videos: 비디오 정보 저장 여부 (기본값: False)

    Returns:
        Dict[str, List[str]]: 미디어 유형별 저장된 파일 경로
    """
    saved_files = {"images": [], "videos": []}

    if not result.success or not result.media:
        print("저장할 미디어 데이터가 없습니다.")
        return saved_files

    try:
        # 이미지 정보 저장
        if save_images and "images" in result.media and result.media["images"]:
            image_file = create_unique_filename("output", "images", "json")
            with open(image_file, "w", encoding="utf-8") as f:
                json.dump(result.media["images"], f, ensure_ascii=False, indent=2)
            saved_files["images"].append(image_file)
            print(f"이미지 정보 저장 완료: {image_file}")

        # 비디오 정보 저장
        if save_videos and "videos" in result.media and result.media["videos"]:
            video_file = create_unique_filename("output", "videos", "json")
            with open(video_file, "w", encoding="utf-8") as f:
                json.dump(result.media["videos"], f, ensure_ascii=False, indent=2)
            saved_files["videos"].append(video_file)
            print(f"비디오 정보 저장 완료: {video_file}")

        return saved_files
    except Exception as e:
        print(f"미디어 정보 저장 오류: {str(e)}")
        return saved_files
