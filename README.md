# 의료정보 크롤링

## 1. 환경설정 

- 파이참 터미널에서 실행한다.

### 1. scrapy 설치 진행

```
python -m pip install --upgrade pip
pip install --upgrade setuptools
pip install scrapy
pip install pypiwin32 (windows 10 OS의 경우 win32 모듈 설치함)
```

### 2. scrapy 정상설치 확인
```
scrapy
```

- 에러 메시지없이 아래와 같은 내용들이 보여지면 정상설치라고 판단한다.
```
Scrapy 2.5.0 - no active project

Usage:
  scrapy <command> [options] [args]

Available commands:
  bench         Run quick benchmark test
  commands
  fetch         Fetch a URL using the Scrapy downloader
  genspider     Generate new spider using pre-defined templates
  runspider     Run a self-contained spider (without creating a project)
  settings      Get settings values
  shell         Interactive scraping console
  startproject  Create new project
  version       Print Scrapy version
  view          Open URL in browser, as seen by Scrapy

  [ more ]      More commands available when run from project directory

Use "scrapy <command> -h" to see more info about a command

```

