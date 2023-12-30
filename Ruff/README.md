Ruff Study
===

회사 동료로부터 전해 듣게된 패키지이다. `Flake8`, `black`을 공부해봐야 겠다고 생각만 하고 있었는데 `Ruff` 관련된 내용을 보자마자 이걸 먼저 해야겠다고 생각했다. 생각보다 많은 곳에서 벌써부터 `Ruff`를 적용하고 있었고 `Rust`로 작성되어 성능이 압도적으로 좋다는데 사용을 안해볼수가 없었다. 

출처 : https://docs.astral.sh/ruff/

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Ruff 

> *An extremely fast Python linter and code formatter, written in Rust.*

첫 설명부터 아주 임팩트 있다.

- `Flake8` 같은 linter와 `Black`같은 formatter 보다 적게는 10-100배 빠르다.
- `pip`을 통해 설치 가능
- `pyproject.toml` 지원
- Python 3.12 호환
- `Flake8`, `isort`, `Black`과 유사하며 호환 가능
- 내장 캐싱을 통한 변경되지 않은 파일들 재분석 회피
- 자동 오류 수정
- 인기있는 `flake8` 플러그인을 700개 이상의 기본 제공 규칙
- VS Code 등 편집기와 호환
- 모노레포구조(Monorepo) 친화적인 구성

Ruff의 목표는 기능을 통일시키며 빠른 성능을 가진 단일 공통 인터페이스를 만드는 것이다.
이러한 무기들을 통해서 Ruff가 아주 빠른 속도로 오픈소스 프로젝트에 사용되고 있다.

# 설치
Ruff 다양한 패키지 매니저를 통해서 설치가 가능한데 homebrew도 가능하여 brew로 설치하였다.
``` bash
brew install ruff
```

# 사용법
## 1. The Ruff Linter
Linter로 사용하려면 `check` 명령어를 사용한다.
``` bash
ruff check .                        # 현재 디렉토리 안의 모든 파일을 Lint(서브디렉토리 포함)
ruff check path/to/code/            # `/path/to/code` 에 있는 모든 파일 Lint 
ruff check path/to/code/*.py        # `/path/to/code`에 있는 모든 `.py` 파일 Lint
ruff check path/to/code/to/file.py  #  `file.py` Lint
ruff check @arguments.txt           # input 파일을 이용하여 (줄바꿈으로 arg  구분) Lint
ruff check . --fix # Lint 후에 fix 가능한 error들을 fix함.
ruff check . --wathch # Lint 후 변경사항이 발생하면 재 Lint.
```

### [Rule](https://docs.astral.sh/ruff/rules/) 선택
사용가능한 규칙집합은 `select`, `extend-select`, `ignore` 셋팅을 통해서 조작한다.

`Ruff`의 linter는 `Flake8`의 규칙들을 반영했는데 1~3개의 문자 접두어와 뒤에 3개의 숫자로 구성되어있다. (`F401`)
문자 접두어의 경우 어떤 규칙을 사용하는 것인지를 나타내는데 다음과 매칭된다.
- `F` : Pyflakes
- `E` : pycodestyle
- `ANN` : flake8-annotations

``` toml
# in pyproject.toml
[tool.ruff.lint]
select = ["E", "F"]
ignore = ["F401"]

# in ruff.toml
[lint]
select = ["E", "F"]
ignore = ["F401"]
```

위의 설정은 E, F의 모든 규칙을 사용하면서 F401만 예외로 한다.
Ruff의 기본 구성을 보고 싶으면 [이 곳](https://docs.astral.sh/ruff/configuration/)에서 확인 하면 된다.

특별한 경우 ALL 모든 규칙을 활성화 하는 방법도 있는데 충돌나는 규칙들의 경우 자동으로 비활성화 된다고 한다. 

이러한 규칙들을 설정하는 가이드 라인까지 제시해주고 있다.
- `select` 규칙들을 명시적으로 `extend-select`설정
- `ALL`은 되도록이면 사용하지 말라. upgrade시 새 규칙이 암시적으로 활성화 될 수도 있음.
- 작은 규칙들 부터 널리 사용되는 규칙 순으로 확장   
(`select = ["E", "F"]`) ->(`select = ["E", "F", "B"]`)

기본적으로 가장 널리 사용되는 규칙 중 일부를 활성화 하는 구성은 다음과 같다고 한다.
``` toml
[lint]
select = [
    # pycodestyle
    "E",
    # Pyflakes
    "F",
    # pyupgrade
    "UP",
    # flake8-bugbear
    "B",
    # flake8-simplify
    "SIM",
    # isort
    "I",
]
```

활성화된 규칙집합들을 조절하려면 현재 `pyproject.toml`과 상속받은 `pyproject.toml`과 CLI(`--select`)간의 조정이 필요하다.

규칙에 적용되는 우선순위는 다음순이다.
- `select` > `extend-select` > `ignore`
- "CLI" > 현재 `pyproject.toml` > 상속 받은 `pyproject.toml`

### Fixes
Ruff는 다양한 Lint 오류에 대해 다종 수정을 지원하는데 `--fix` 옵션을 붙히면 된다.

#### Fix safety
Ruff label에는 `safe`와 `unsafe`가 있는데 `safe`인 경우는 코드의 의도가 유지되지만 `unsafe`는 코드의 의도가 변경될 수도 있다. 

예를 들어,   
[unnecessary-iterable-allocation-for-first-element (RUF015)](https://docs.astral.sh/ruff/rules/unnecessary-iterable-allocation-for-first-element/)는 잠재적으로 성능이 저하되는 코드사용을 확인하는 규칙이다.
``` sh
$ python -m timeit "head = list(range(99999999))[0]"
1 loop, best of 5: 1.69 sec per loop
```
``` sh
$ python -m timeit "head = next(iter(range(99999999)))"
5000000 loops, best of 5: 70.8 nsec per loop
```
위처럼 대폭적인 성능 향상을 확인할 수 있다.
하지만 컬렉션이 비어있는 경우에는 예외 처리의 항목이 `IndexError`에서 `StopIteration`으로 변경된다.
``` sh
$ python -c 'list(range(0))[0]'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
IndexError: list index out of range
```
``` sh
$ python -c 'next(iter(range(0)))[0]'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
StopIteration
```
이 때문에 에러 처리가 실패 할 수도 있기 때문에 `unsafe로` 분류된다.

기본값으로 `safe`한 처리만 활성화 되는데, `unsafe`한 arg를 이용하면 활성화 할 수 있다.
``` sh
ruff check . --unsafe-fixes # unsafe 규칙의 수정사항을 보여준다.
ruff check . --fix --unsafe-fixes # unsafe한 규칙도 수정한다.
``` 

`extend-safe-fixes`/`extend-unsafe-fixes`설정을 통해서 `safe`/`unsafe`를 수정할 수도 있다.

``` toml
[tool.ruff.lint]
extend-safe-fixes = ["F601"]
extend-unsafe-fixes = ["UP034"]
```
F601은 `safe`한 규칙으로, UP034는 `unsafe`한 규칙으로 변경한다.

#### Disabling fixes
작성 중

### Error suppression
작성 중

#### 사용하지 않는 Error suppression 코멘트 탐지
작성 중

#### 필수 suppression 코멘트 삽입
작성 중

#### Action 코멘트
작성 중

### Exit codes
작성 중

## 2. The Ruff Formatter

Formatter 사용하려면 `format` 명령어를 사용한다.

```bash
ruff format .                        # Format all files in the current directory (and any subdirectories).
ruff format path/to/code/            # Format all files in `/path/to/code` (and any subdirectories).
ruff format path/to/code/*.py        # Format all `.py` files in `/path/to/code`.
ruff format path/to/code/to/file.py  # Format `file.py`.
ruff format @arguments.txt           # Format using an input file, treating its contents as newline-delimited command-line arguments.
```

`Ruff`를 [pre-commit hook(ruff-pre-commit)](https://github.com/astral-sh/ruff-pre-commit),
[vscode extention](https://github.com/astral-sh/ruff-vscode),
[github action](https://github.com/chartboost/ruff-action) 에서 사용 가능하다.

