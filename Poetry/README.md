Poetry 공부
===

어느날 부터 Poetry를 사용하는 사례가 늘었다. Poetry는 의존성 관리를 위해 사용한다고 한다. pyenv + pyenv-virtualenv를 사용하며 매우 만족해 하고 있었는데 poetry 에서도 가상환경을 만들어 준다고 한다. 그래서 pyenv-virtualenv 대신 poetry를 이용하여 가상환경까지 구축해보려고 한다.

> 참고 : https://python-poetry.org/

## Poetry
> Python packaging and dependency management made easy **Poetry**

파이썬 패키징과 의존성 관리를 쉽게 만들어 준다.

1. 프로젝트에 필요한 도구들을 분명한 방식으로 관리한다.

``` bash
poetry add pendulum
```

2. 하나의 명령어로 프로젝트를 쉽게 빌드해준다.

``` bash
poetry build
```

3. PyPI에 내 작업물을 공유 할 수 있다.   
~~내가 Publish까지 사용할 날이 오겠지?~~
``` bash
poetry publish
```

4. 하나의 명령어로 프로젝트의 의존성을 추적 할 수 있다.
``` bash
poetry show --tree
```
5. 종속성을 해결할 수 있는 솔루션(존재 한다면ㅋ)을 제공해 준다.

6. Poetry는 virtualenvs를 활용하거나 자체 가상환경을 만들어서 시스템과 독립된 환경을 만든다.

7. 쉽고 직관적인 명령어를 통해서 관리가 가능하고 기본 값만으로도 쉽게 구성할 수 있다.

이정도가 Poetry가 말하는 장점이다.
(23.12.30 기준)


## 설치
Poetry를 brew를 통해서 설치가 가능하여 brew를 통해 설치하였다.

## 사용법
설치와 환경변수 설정을 마치고 나면 poetry 명령어를 사용 할 수 있게 된다.

```  bash
poetry --version
```

공식 installer를 통해서 update도 가능하다.
``` bash
poetry self update
```

## 기본 사용법
### 프로젝트 셋업
#### 새로운 프로젝트 만들기
먼저 Poetry를 활용하여 새로운 프로젝트를 만들어 보자.

``` bash
poetry new poetry-demo
```

다음 형태의 프로젝트가 생성되었다.

<img src="./.static/.image/new_poetry-demo.png"></img>

`pyproject.toml`파일이 프로젝트와 의존성을 조정(orchestrate)해주는 파일로 가장 중요한 파일이다.

Poetry는 `toml.poetry.name`의 값과 동일한 이름의 패키지가 루트에포함되어 있다고 가정한다. 그래서 `toml.poetry.packages`의 값을 맞춰야 한다고 한다.

MANIFEST.in 파일은 `tool.poetry.readme`, `tool.poetry.include/exclude`에 의해서 대체 되었다고 한다. exclude는 암시적으로 `.gitignore`에 추가된다고 한다.

파이썬 버젼을 명확하게 작성하고 이에 따른 의존성 관리를 보장해준다고 한다.

#### 기존 프로젝트에 적용하기
기존에 존재하는 프로젝트에도 poetry를 적용할 수 있다.
``` bash
cd pre-existing-project
poetry init
```

의존성들도 구체적인 버젼을 명시할 수 있다.
``` toml
[tool.poetry.dependencies]
pendulum = "^2.1"
```

> 패키지를 검색하는 repo는 기본적으로 PyPI이고, `tool.poetry.source`를 통해서 등록할 수도 있다.

`toml` 파일에 직접 작성할 수도 있지만 명령어를 통해서 가능하다.

``` bash
poetry add pendulum
```

이는 자동적으로 호환 가능한 버젼을 찾고 하위 의존성까지 설치해 준다.

#### 가상환경 사용하기
기본 {cache-dir}/virtualenvs에 가상환경을 만들어 준다고 한다.
`virtualenvs.in-project`를 통해서 {cache-dir}는 설정을 통해서 변경 할 수 있다.

> 외부 가상환경 관리
Poetry는 이미 외부에 활성화된 가상환경을 감지하고 최대한 존중해준다.(?!!!!!)
>>실제로 pyenv-virtualenv로 먼저 가상환경을 만들었는데 poetry shell 실행하였을 때, 미리 설정된 가상환경이 실행 되었다.

#### poetry run
script를 실행하기 위해서 `poetry run python script.py`를 사용하면 된다. pytest나 black 같은 명령어 tool이 있는 경우 다음 처럼 사용하면 된다. `poetry run pytest`

#### 가상환경 활성화
가상환경을 활성하는 가장 쉬운 방법은 다음 명령어로 nested shell을 만드는 것이다.
``` bash
poetry shell
```

> *Why a nested shell?*   
자식 프로세스는 부모로부터 환경을 상속 받지만 환경은 공유하지 않는다. 자식 프로세스에서 생겨난 수정사항들은 나간 뒤에 유지 되지 않는다. 즉, 파이썬 어플리케이션(Poetry)은 Poetry 명령어 실행이 완료된 후에도 활성화된 가상 환경이 활성 상태로 유지되도록 쉘의 환경을 수정 할 수 없다. 그러므로 나중에 실행될 명령어를 가상환경 내에서 실행하기 위해서 가상환경이 활성화된 sub-shell을 만들어야 한다. 

`poetry shell`가 가상환경 실행시 shell prompt를 수정하는 것을 막고 싶다면, 실행 전에 환경변수로 `VIRTUAL_ENV_DISABLE_PROMPT=1`을 설정하면 된다.


#### 패키지 버젼 제약

위에서 예시로 `pendulum` 패키지에 ^2.1를 작성했다.   
`>=2.1.0 <3.0.0`을 통해서 2.1.0보단 크고 3.0.0 보다 작은 버젼으로 제한을 둘 수 있다.


#### 의존성 설치
프로젝트의 의존성을 설치하기 위해 다음 명령어를 실행하면 된다.
``` bash
poetry install
```

#### poetry.lock 없이 설치
`poetry.lock`이 없고 한번도 명령어를 실행하지 않았다면 `Poetry`는 `pyproject.toml`에 있는 의존성 리스트를 설치 한다.   
설치가 완료되면 poetry.lock파일을 만들고 프로젝트의 구체적인 version을 lock 한다. 
poetry.lock파일을 같이 커밋해줘야 동료들이 같은 버젼의 의존성을 설치할 수 있다.

#### poetry.lock으로 설치
`poetry.lock`과 `pyproject.toml`이 같이 존재한다면 누군가 `poetry install`를 실행 시킨 것이다.

이 경우 `toml`에 있는 모든 의존성 패키지를 설치하는데 `lock`에 있는 있는 정확한 version을 설치한다.

#### 종속성 최신 버전 업데이트
`poetry.lock`의 의존성을 최신 버젼으로 업데이트 하려면 `update`를 이용하면 된다.

pyproject.toml에 따라 `lock`의 최신 버젼으로 업데이트 한다.
(`lock`파일을 삭제하고 `install` 한 것과 같음.)

## 의존성 관리
의존성들을 groups를 통해서 조직화 할 수 있다.
예를들어 다음 처럼 doc, test를 위한 의존성들을 그룹으로 묶어서 관리 할 수 있다.

``` toml
[tool.poetry.group.test]  # This part can be left out

[tool.poetry.group.test.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```

모든 의존성은 그룹과 상관 없이 서로 호환이 가능해야 합니다. 그룹은 label의 기능으로만 동작한다고 생각하면 된다.

`tool.poetry.dependencies`에 선언된 의존성은 `main` group(반드시 설치되어야 하는 그룹)으로 생각하면 된다.

만약 프로젝트가 실행되는 동안에 기능적으로 추가해야 하는 의존성이 있다면 [extras](https://python-poetry.org/docs/pyproject/#extras)를 사용하면 된다. 예를 들어 유저가 `pip`를 통해서 설치한 것들이 `extras` 일 수 있다.

### dev 의존성 그룹
Poetry 1.2.0 이후 dev 의존성 group은 다음과 같다.
``` toml
[tool.poetry.group.dev.dependencies]
pytest = "^6.0.0"
pytest-mock = "*"
```
다만 이전 버젼과의 호환을 위해 `dev-dependencies`에 선언된 것들은 자동으로 `dev` group에 포함되도록 되어있다.


#### Optional groups
의존성 그룹을 선택 사항으로 만들 수 있다.
``` toml
[tool.poetry.group.docs]
optional = true

[tool.poetry.group.docs.dependencies]
mkdocs = "*"
```

`install` 명령어의 옵션을 통해 해당 그룹을 설치 할 수 있다.

``` bash
poetry install --with docs
```

#### 그룹에 의존성 추가하기
`add` 명령어의 옵션으로 그룹에 함께 추가할 수 있다.

``` bash
poetry add pytest --group test
```

만약 해당 그룹이 없다면 자동으로 만들어 준다.

#### 그룹 의존성 설치
기본 값으로 `poetry install`시에 Optional group을 제외한 모든 의존성을 설치한다.

물론 그룹을 제외하고 설치하는 옵션도 있다.

``` bash
poetry install --without test,docs
```

> `--with`과 `--without` 옵션을 동시에 사용하면 `--without` 명령어가 우선된다.

특정 group만 설치하고 싶다면 다음 옵션을 사용하면 된다.
``` bash
poetry install --only docs
```
``` bash
poetry install --only main
```
``` bash
poetry install --only-root
```
(자세한 차이는 문서를 참고해주세요.)

#### 그룹에서 의존성 제거
`remove` 명령어는 `--group` 옵션을 제공하는데 특정 group에서 패키지를 제거할 수 있다.

``` bash
poetry remove mkdocs --group docs
```

### 의존성 동기화
의존성 동기화를 통해서 poetry.lock환경에 있는 의존성을 보장하고 필요하지 않은 것들은 제거한다.

`install`의 `--sync`옵션을 통해서 실행한다.
``` bash
poetry install --sync
```
> `--sync` 옵션은 현재 사라진 `--remove-untracked`를 대신한다.
