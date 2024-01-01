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
`fixable`과 `unfixable` 설정을 통해서 `Ruff`가 수정해야하는 규칙들을 제한할 수 있다.

다음 설정은 [unused-imports(F401)](https://docs.astral.sh/ruff/rules/unused-import/)를 제외한 모든 규칙에 대한 수정을 가능하도록 한다.

``` toml
[tool.ruff.lint]
fixable = ["ALL"]
unfixable = ["F401"]
```
반대로 F401 규칙에 대한 수정만 가능하도록 할 수 있다.
``` toml
[tool.ruff.lint]
fixable = ["F401"]
```


### Error suppression
Lint의 규칙을 완전히 생략하기 위해서는 `pyproject.toml` 또는 `ruff.toml` 파일에 `ignore`를 추가하면 된다.

Inline에서 규칙위반 사항을 억제하기 위해서는 `Flake8` 유사하게 `noqa` 시스템을 이용한다.
각각의 위반사항들을 무시하기 위해서는 라인의 마지막에 `# noqa: {code}`를 추가하면 된다.

``` python
# Ignore F841.
x = 1  # noqa: F841

# Ignore E741 and F841.
i = 1  # noqa: E741, F841

# Ignore _all_ violations.
x = 1  # noqa
```

여러줄의 문자열의 경우 따옴표 3개를 이용해서 `noqa`를 사용할 수도 있다.

``` python
"""Lorem ipsum dolor sit amet.

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor.
"""  # noqa: E501
```

파일 전체에 걸쳐서 적용하기 위해서는 주석으로 파일안의 아무 곳에나 `# ruff: noqa`를 사용하면 된다.
(파일 가장 위에 작성하는 것을 추천한다!)
``` python
# ruff: noqa
```
물록 특정 규칙에 대해서도 적용 가능하다.

``` python
# ruff: noqa: F841
```


#### 사용하지 않는 Error suppression 주석 탐지
실질적으로 유효한 `noqa` 지시문인지 확인하는 `RUF100`에 `unused-noqa`라는 특별한 규칙이 있다.
탐지 하기 위해서 `ruff check /path/to/file.py --extend-select RUF100`를 실행하면 된다.

물론 `--fix`옵션을 통해서 유효하지 않은 `noqa`를 제거할 수 있다.


#### 필수 suppression 주석 삽입
반대로 자동으로 `noqa` 위반하는 줄에 추가할 수도 있다.
``` sh
ruff check /path/to/file.py --add-noqa
```


#### Action 주석
Ruff에서는 isort의 action 주석들을 사용할 수 있다고 한다. (`# isort: skip_file`, `# isort: on`)
물론 접두사로 `# ruff:`를 붙여 사용 할 수 있다. 기능적으로는 동일하게 동작한다. (`# ruff: isort: skip_file`)

다만 docstirng에 있는 action comments는 Ruff에서는 동작하지 않는다.


### Exit codes 
기본 값으로 `ruff check`은 다음 status code로 종료한다.

- 0 : 위반 사항을 발견하지 못하거나 현재의 위반 사항이 자동으로 수정된 경우
- 1 : 위반 사항이 발견된 경우
- 2 : 비정상적인 설정이나 내부 오류로 비정상적으로 종료된 경우

이러한 컨벤션은 `ESLing`, `Prettier`, `RuboCop`과 같은 도구들을 반영했다.
물론 Exit code의 동작을 변경하는 옵션이 있다.
- `--exit-zero` : 위반사항이 있다고 하더라도 0으로 종료한다. (2의 경우는 그대로)
- `--exit-non-zero-on-fix` : 위반사항이 자동으로 수정 되더라도, 위반사항이 있엇다면 1로 종료


## 2. The Ruff Formatter
**`Ruff`는 `Black`의 대체품으로 매우 빠른 Python Formatter로 설계되었다!!!**   
Formatter 사용하려면 `format` 명령어를 사용한다.

```bash
ruff format .                        # 현재 디렉토리(하위 포함)에 있는 모든 파일 대상
ruff format path/to/code/            # `/path/to/code`(하위 포함)에 있는 모든 파일 대상
ruff format path/to/code/*.py
ruff format path/to/code/to/file.py
ruff format @arguments.txt           # input 파일을 통해 arg 포함해서 실행
```

### 철학
`Ruff formatter`의 초기 목표는 코드 스타일을 혁신하는 것보다는 성능과 Linter, Formatter 등 모든 툴에 대한 통합된 toolchain을 제공하는 것이다.

현재 Python 생태계에서 `Black`의 인기로 프로젝트에 미치는 영향을 최소화 하기 위해 `Black`과의 호환성을 타겟으로 두고 있다. 

### 설정 Configuration
지원되는 설정의 전체 목록은 [Settings](https://docs.astral.sh/ruff/settings/#format)를 참고하자.

### Docstring formatting
Ruff formatter는 docstirng 내에 있는 예제 Python code를 formatting 하는 옵션이 있다.   
다음 형식에 따라서 코드 예제를 인식한다.
- Python [doctest](https://docs.python.org/3/library/doctest.html) 형식
- CommonMark에서 info string로 `python`, `py`, `python3`, `py3`를 가진 `fenced code blocks` ( info string이 없는 경우 python으로 가정한다.)   
- reStructuredText 리터럴 블록
- reStructuredText에서 code-block 및 sourcecode 지시문이 python인 경우

코드 예제가 Python임을 인식했는데 해당 코드가 유효하지 않다면 자동으로 건너띄게 된다.

`dynamic` 설정값을 통해서 docstring의 줄 길이 제한을 구성할 수 있다.

``` toml
[tool.ruff.format]
docstring-code-format = true
docstring-code-line-length = 20
```

### Format suppression 형식 억제
`Black` 처럼 특정 코드 블록을 일시적으로 비활성화 할 수 있는 `# fmt: on`, `# fmt: off`, `# fmt: skip` pragma 주석을 사용할 수 있다.

 `# fmt: on`, `# fmt: off` 주석은 선언하는 레벨에서 적용된다.
 그래서 표현식 내에서 해당 주석을 추가해도 아무런 효과가 없다.

 ``` python
 [
    # fmt: off
    '1',
    # fmt: on
    '2',
]
 ```
 
 대신 전체 선언부에 적용하면 된다.
 ``` python
 # fmt: off
[
    '1',
    '2',
]
# fmt: on
 ```

`# fmt: skip` 주석은 선언부, case 헤더, 데코레이터, 함수-클래스 정의부분의 형식을 억제한다.
```python
if True:
    pass
elif False: # fmt: skip
    pass

@Test
@Test2 # fmt: skip
def test(): ...

a = [1, 2, 3, 4, 5] # fmt: skip

def test(a, b, c, d, e, f) -> int: # fmt: skip
    pass
```

### 충돌나는 lint 규칙들
linter와 함께 사용하도록 설계 되었기 때문에 몇 가지 규칙에 의해 충돌이 발생할 수 있다.
만약 Ruff를 formatter로 사용한다면 다음 lint 규칙은 피하는 것이 좋다.

- tab-indentation (W191)
- indentation-with-invalid-multiple (E111)
- indentation-with-invalid-multiple-comment (E114)
- over-indented (E117)
- indent-with-spaces (D206)
- triple-single-quotes (D300)
- bad-quotes-inline-string (Q000)
- bad-quotes-multiline-string (Q001)
- bad-quotes-docstring (Q002)
- avoidable-escaped-quote (Q003)
- missing-trailing-comma (COM812)
- prohibited-trailing-comma (COM819)
- single-line-implicit-string-concatenation (ISC001)
- multi-line-implicit-string-concatenation (ISC002)
line-too-ling (E501) 규칙은 포매터와 함께 사용할 수 있지만 포맷터의 `line-length` 설정과 충돌이 날 수있다.

**위의 모든 규칙은 기본 설정으로 포함되어 있지 않지만 해당 규칙이나 상위 카테고리를 활성화한 경우 `ignore` 설정을 통해 비활성화 하는 것이 좋다!**

유사하게도 다음 isort 설정도 피하도록 추천한다.
- force-single-line
- force-wrap-aliases
- lines-after-imports
- lines-between-types
- split-on-trailing-comma

기본값이 아닌 값을 사용하도록 설정을 구성한 경우 Ruff 구성에서 해당 설정을 제거하는 것이 좋다.
만약 호환되지 않는 lint 규칙이나 설정이 활성화되면 ruff format 경고가 표시된다!

### Exit codes
`ruff format`은 다음 status code로 종료된다.
- 0 : 파일 포맷팅 여부와 상관없이 성공적으로 종료
- 2 : 비정상적인 설정, CLI 옵션, 내부에러 등 비정상적인 종료
그 사이에 `ruff format --check` 다음 status codefh 종료된다.
- 0 : 성공적으로 종료되고 `--check`가 파일을 지정하지 않았다면 포맷팅 되지 않는다.
- 1 : 성공적으로 종료되고 `--check`가 파일을 지정하지 않았다면 하나 이상의 파일에 포맷팅 된다.
- 2 : 비정상적인 설정, CLI 옵션, 내부에러 등 비정상적인 종료

---
### 참고
`Ruff`를 [pre-commit hook(ruff-pre-commit)](https://github.com/astral-sh/ruff-pre-commit),
[vscode extention](https://github.com/astral-sh/ruff-vscode),
[github action](https://github.com/chartboost/ruff-action) 에서 사용 가능하다.

