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

## 2. 프로젝트 

### 1. 약품 크롤링

#### 1. 프로젝트 생성
```
scrapy startproject medicine
```

#### 2. spider 생성
``` 
cd medicine

scrapy genspider medicinespider nedrug.mfds.go.kr
```
![Cap 2021-05-10 10-27-10-958](https://user-images.githubusercontent.com/7462877/117594945-511e5180-b17a-11eb-9ea1-242b2c6de98a.jpg)

#### 3. 프로젝트 실행
```
scrapy crawl medicinespider
```
에러메시지없이 정상실행되는지 확인한다.

