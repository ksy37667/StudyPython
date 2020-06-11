# Chapter06-4-1
# 파이썬 심화
# Asyncio
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 return(yield)
# 즉, 실행 stop -> 다른 작업으로 위임 -> stop 지점 부터 재실행 원리
# Non-Blocking 비동기 처리에 적합

# BlockIO -> Thread 사용
# 쓰레드 개수 및 gil 문제 염두, 공유 메모리 문제 해결

import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

urls = ['http://daum.net', 'https://google.com', 'https://apple.com', 'https://tistory.com', 'https://github.com', 'https://gmarket.co.kr']

start = timeit.default_timer()

def fetch(url):
    print('Thread Name : ', threading.current_thread().getName, 'start', url)
    urlopen(uel)
    print('Thread Name : ', threading.current_thread().getName, 'done', url)

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        for url in urls:
            executor.submit(fetch, url)

if __name__ == '__main__':
    # 함수 실행
    main()


    # 완료시간 - 시작시간
    duration = timeit.default_timer() - start
    print('total time : ', duration)