uv
===

> 참고 : https://docs.astral.sh/uv/guides/install-python/

## uv
> An extremely fast Python package and project manager, written in Rust.

Rust로 작성된 매우 빠른 Python 패키지 및 프로젝트 관리자입니다.

1. Versions
최신 python version과 원하는 version을 설치할 수 있습니다.
``` bash
uv python install
uv python install 3.12
uv python install '>=3.8,<3.10'
```
재설치도 가능하다.
``` bash
uv python install --reinstall
```

사용 가능한 python을 검색 할 수 있다.
``` bash
uv python list
```

원하는 python version으로 가상환경을 만들 수도 있다.
기본적으로 uv는 시스템에서 Python 버전을 찾을 수 없는 경우 해당 버전을 자동으로 다운로드하는데 옵션 설정으로 변경할 수 있다.
``` bash
uv venv --python 3.11.6
```

1. Scripts
   
2. Projects
uv는 pyproject.toml을 이용한 프로젝트 관리를 지원한다.
``` bash
uv init .
uv init hello-world
```
   
종속성 관리
``` bash
uv add requests
uv remove requests
uv lock --upgrade-package requests
```

명령어 실행
``` bash
uv add flask
uv run -- flask run -p 3000
```
가상환경을 실행시켜서 실행 할 수도 있다.
``` bash
uv sync
source .venv/bin/activate
flask run -p 3000
python example.py
```

lock 파일 생성
``` bash
uv lock
```

locked 패키지 버전 업그레이드
``` bash
uv lock --upgrade
uv lock --upgrade-package <package>
uv lock --upgrade-package <package>==<version>
```

3. Tools
   
4. Utility