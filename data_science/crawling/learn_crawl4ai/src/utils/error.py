import functools
import logging
import time
import traceback
from typing import Any, Callable, Dict, List, Optional, TypeVar, Union, cast

# 타입 변수 정의
T = TypeVar("T")
R = TypeVar("R")

# 로거 설정
logger = logging.getLogger("crawl4ai")
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def setup_logger(level=logging.INFO, log_file=None):
    """
    로거를 설정합니다.

    Args:
        level: 로깅 레벨 (기본값: logging.INFO)
        log_file: 로그 파일 경로 (기본값: None)
    """
    logger.setLevel(level)

    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)


def log_error(message: str, error: Optional[Exception] = None, level=logging.ERROR):
    """
    오류를 로깅합니다.

    Args:
        message: 오류 메시지
        error: 예외 객체 (기본값: None)
        level: 로깅 레벨 (기본값: logging.ERROR)
    """
    if error:
        logger.log(level, f"{message}: {str(error)}")
        logger.log(level, traceback.format_exc())
    else:
        logger.log(level, message)


def handle_exception(func: Callable[..., R]) -> Callable[..., Union[R, None]]:
    """
    함수 실행 시 발생하는 예외를 처리하는 데코레이터입니다.

    Args:
        func: 데코레이트할 함수

    Returns:
        Callable: 데코레이트된 함수
    """

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Union[R, None]:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            func_name = func.__name__
            log_error(f"'{func_name}' 함수 실행 중 오류 발생", e)
            return None

    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0, backoff: float = 2.0):
    """
    함수 실행 실패 시 재시도하는 데코레이터입니다.

    Args:
        max_attempts: 최대 시도 횟수 (기본값: 3)
        delay: 초기 지연 시간(초) (기본값: 1.0)
        backoff: 지연 시간 증가 계수 (기본값: 2.0)

    Returns:
        Callable: 데코레이터 함수
    """

    def decorator(func: Callable[..., T]) -> Callable[..., T]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> T:
            attempts = 0
            current_delay = delay
            last_exception = None

            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    last_exception = e

                    if attempts >= max_attempts:
                        break

                    func_name = func.__name__
                    log_error(
                        f"'{func_name}' 함수 실행 실패 (시도 {attempts}/{max_attempts}), "
                        f"{current_delay:.1f}초 후 재시도",
                        e,
                        level=logging.WARNING,
                    )

                    time.sleep(current_delay)
                    current_delay *= backoff

            # 모든 시도 실패 시 마지막 예외 발생
            if last_exception:
                raise last_exception

            # 이 코드는 실행되지 않지만 타입 검사를 통과하기 위해 추가
            return cast(T, None)

        return wrapper

    return decorator


def validate_result(result, extract_content=False):
    """
    크롤링 결과를 검증합니다.

    Args:
        result: 크롤링 결과 객체
        extract_content: 추출된 콘텐츠 검증 여부 (기본값: False)

    Returns:
        bool: 검증 결과
    """
    if not result:
        log_error("크롤링 결과가 없습니다.")
        return False

    if not result.success:
        log_error(f"크롤링 실패: {result.error_message}")
        return False

    if extract_content and not result.extracted_content:
        log_error("추출된 콘텐츠가 없습니다.")
        return False

    return True


def format_error_for_output(error):
    """
    오류를 출력을 위해 포맷팅합니다.

    Args:
        error: 예외 객체

    Returns:
        Dict: 포맷팅된 오류 정보
    """
    return {
        "error": True,
        "error_type": type(error).__name__,
        "error_message": str(error),
        "traceback": traceback.format_exc(),
    }
