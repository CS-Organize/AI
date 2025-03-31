# 필요한 라이브러리를 가져옵니다.
from typing import Any  # 타입 힌트를 위한 Any 타입을 가져옵니다.

import httpx  # 비동기 HTTP 요청을 보내기 위한 라이브러리입니다.
from mcp.server.fastmcp import FastMCP  # MCP 서버 구현체인 FastMCP를 가져옵니다.

# FastMCP 서버 인스턴스를 초기화합니다.
# "weather"는 이 서버가 제공하는 기능의 네임스페이스(이름 공간) 또는 식별자 역할을 합니다.
mcp = FastMCP("weather")

# 상수 정의
NWS_API_BASE = "https://api.weather.gov"  # 미국 국립 날씨 서비스(NWS) API의 기본 URL입니다.
USER_AGENT = "weather-app/1.0"  # API 요청 시 서버에 전달할 사용자 에이전트 문자열입니다. (API 제공자가 요청 출처를 식별하는 데 사용)


# NWS API에 비동기로 요청을 보내는 헬퍼 함수입니다.
async def make_nws_request(url: str) -> dict[str, Any] | None:
    """NWS API에 요청을 보내고 적절한 오류 처리를 수행합니다."""
    # 요청 헤더를 설정합니다. User-Agent와 응답 형식을 지정합니다.
    headers = {"User-Agent": USER_AGENT, "Accept": "application/geo+json"}
    # 비동기 HTTP 클라이언트를 생성합니다. 'async with' 구문은 클라이언트 사용 후 자동으로 정리되도록 보장합니다.
    async with httpx.AsyncClient() as client:
        try:
            # 지정된 URL로 GET 요청을 비동기적으로 보냅니다. 타임아웃은 30초로 설정합니다.
            response = await client.get(url, headers=headers, timeout=30.0)
            # 응답 상태 코드가 2xx가 아니면 HTTPError 예외를 발생시킵니다. (오류 확인)
            response.raise_for_status()
            # 성공적인 응답(JSON 형식)을 파싱하여 파이썬 딕셔너리로 반환합니다.
            return response.json()
        # 요청 중 예외(네트워크 오류, 타임아웃, 잘못된 응답 등)가 발생하면 None을 반환합니다.
        except Exception:
            return None


# 날씨 경보(alert) 데이터를 사람이 읽기 쉬운 문자열 형식으로 변환하는 함수입니다.
def format_alert(feature: dict) -> str:
    """경보(alert) feature 딕셔너리를 읽기 좋은 문자열로 포맷합니다."""
    # feature 딕셔너리 안의 'properties' 키에 접근합니다.
    props = feature["properties"]
    # 각 경보 정보를 f-string을 사용하여 보기 좋게 조합합니다. .get() 메서드는 키가 없을 경우 기본값(예: 'Unknown')을 사용합니다.
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""


# MCP '도구(tool)'로 등록될 함수입니다. 특정 주의 날씨 경보를 가져옵니다.
@mcp.tool()
async def get_alerts(state: str) -> str:
    """미국 주의 날씨 경보를 가져옵니다.

    Args:
        state: 두 글자의 미국 주 코드 (예: CA, NY)
    """
    # NWS API에서 해당 주의 활성 경보를 조회하는 URL을 만듭니다.
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    # 정의된 헬퍼 함수를 사용해 NWS API에 요청을 보냅니다.
    data = await make_nws_request(url)

    # 데이터를 가져오지 못했거나 응답 데이터에 'features' 키가 없으면 오류 메시지를 반환합니다.
    if not data or "features" not in data:
        return "경보를 가져올 수 없거나 경보를 찾을 수 없습니다."

    # 'features' 리스트가 비어있으면 (활성 경보가 없으면) 해당 메시지를 반환합니다.
    if not data["features"]:
        return "이 주에는 현재 활성 경보가 없습니다."

    # 각 경보 feature를 format_alert 함수를 이용해 문자열로 변환하고 리스트에 담습니다.
    alerts = [format_alert(feature) for feature in data["features"]]
    # 여러 개의 경보 문자열들을 "---" 구분선과 함께 하나의 긴 문자열로 합쳐 반환합니다.
    return "\n---\n".join(alerts)


# MCP '도구(tool)'로 등록될 함수입니다. 특정 위도/경도의 날씨 예보를 가져옵니다.
@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """특정 위치의 날씨 예보를 가져옵니다.

    Args:
        latitude: 위치의 위도
        longitude: 위치의 경도
    """
    # 1단계: 주어진 위도/경도에 해당하는 NWS 예보 그리드(grid) 엔드포인트 정보를 얻기 위한 URL을 만듭니다.
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    # 헬퍼 함수를 사용해 NWS API에 요청을 보냅니다.
    points_data = await make_nws_request(points_url)

    # 그리드 정보를 가져오지 못했으면 오류 메시지를 반환합니다.
    if not points_data:
        return "이 위치의 예보 데이터를 가져올 수 없습니다."

    # 2단계: 그리드 정보 응답에서 실제 예보 데이터가 있는 URL을 추출합니다.
    # points_data['properties']['forecast'] 에 예보 URL이 들어 있습니다.
    forecast_url = points_data["properties"]["forecast"]
    # 추출한 URL로 다시 NWS API에 요청을 보내 상세 예보 데이터를 가져옵니다.
    forecast_data = await make_nws_request(forecast_url)

    # 상세 예보 데이터를 가져오지 못했으면 오류 메시지를 반환합니다.
    if not forecast_data:
        return "상세 예보를 가져올 수 없습니다."

    # 3단계: 예보 데이터에서 'periods' (시간대별 예보) 정보를 추출하고 포맷합니다.
    periods = forecast_data["properties"]["periods"]
    forecasts = []  # 포맷된 예보 문자열을 저장할 리스트입니다.
    # 가져온 예보 중 처음 5개의 기간(period)만 사용합니다.
    for period in periods[:5]:
        # 각 기간의 예보 정보를 f-string을 사용하여 보기 좋게 조합합니다.
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        # 포맷된 예보 문자열을 리스트에 추가합니다.
        forecasts.append(forecast)

    # 여러 기간의 예보 문자열들을 "---" 구분선과 함께 하나의 긴 문자열로 합쳐 반환합니다.
    return "\n---\n".join(forecasts)


# 이 스크립트가 직접 실행될 때 아래 코드를 실행합니다. (모듈로 임포트될 때는 실행되지 않음)
if __name__ == "__main__":
    # MCP 서버를 초기화하고 실행합니다.
    # transport="stdio"는 서버가 표준 입출력(Standard Input/Output)을 통해
    # 클라이언트(예: 다른 프로세스나 AI 모델)와 통신하도록 설정합니다.
    # 클라이언트는 표준 입력으로 요청을 보내고, 서버는 표준 출력으로 응답을 보냅니다.
    mcp.run(transport="stdio")
