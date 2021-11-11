# nasomedia-cli
nasomedia-cli는 명령어 기반으로 서비스의 프로젝트 구조를 자동으로 생성해주는 애플리케이션 입니다.  
# Install
호환 플랫폼
- windows
### Windows
1. 내가 원하는 경로에 레포지토리를 클론 합니다.
```cmd
git clone https://github.com/Nasomedia/nasomedia-cli.git
```

1. 레포지토리를 클론한 경로에 /dist/ns-cli 디렉터리를 Path 환경변수에 추가합니다.
```cmd
setx path "%PATH%;C:{REPOSITRY-PATH}/dist/ns-cli"
```

# 사용법
ns-cli는 서비스 하나를 생성하는 new 명령어와 이미 존재하는 서비스에 프로젝트 구조를 생성해주는 init 명령어 두가지로 구성되어 있습니다.
## new
인자로 건내준 프로젝트 이름으로 폴더를 생성하고 그 프로젝트 폴더 내에서 프로젝트 구조를 생성한다.
- 실행 예제
```cmd
C:\Users\hwc91\Desktop> ns-cli new hello-project
``` 
- 실행 결과
```cmd
C:\Users\hwc91\Desktop> dir .\hello-project\


    디렉터리: C:\Users\hwc91\Desktop\hello-project


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2021-11-10   오후 7:08                app
-a----      2021-11-11   오전 8:48            253 .env
-a----      2021-11-10   오후 8:09         177212 poetry.lock
-a----      2021-11-03   오전 8:49           1182 pyproject.toml

PS C:\Users\hwc91\Desktop>
```
## init
현재 디렉토리에서 프로젝트 구조를 생성한다.
- 실행 예제
```cmd
C:\Users\hwc91\Desktop\hello-project> ns-cli init
```
- 실행 결과
```cmd
PS C:\Users\hwc91\Desktop\hello-project> dir


    디렉터리: C:\Users\hwc91\Desktop\hello-project


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----      2021-11-10   오후 7:08                app
-a----      2021-11-11   오전 8:48            253 .env
-a----      2021-11-10   오후 8:09         177212 poetry.lock
-a----      2021-11-03   오전 8:49           1182 pyproject.toml
```

# 프로젝트 의존 파일 설치
```
PS C:\Users\hwc91\Desktop\hello-project> pyenv local 3.9.6

PS C:\Users\hwc91\Desktop\hello-project> poetry install
```