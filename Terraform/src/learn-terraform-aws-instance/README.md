# AWS with Terraform

## 사전 준비
- Terraform CLI (1.2.0+)
- AWS CLI
- 리소스 생성을 위한 AWS 계정 및 관련된 credentials

> **[AWS CLI credential](https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-files.html)**

## 구성파일 작성
``` tf
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region  = "ap-northeast-2"
}

resource "aws_instance" "app_server" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
```
위는 배포할 수 있도록 완성된 구성파일이다. 하나씩 살펴보자.


### Terraform Block
`terraform {}`에는 인프라를 프로비저닝 하는데 사용할 필수 Provider를 포함한 terraform 설정을 작성한다. 각 provider에 `source` 속성은 hostname, namespace, provider type을 정의한다.
Terraform은 기본적으로 [Terraform Registry](https://registry.terraform.io/?ajs_aid=5c1f5202-a8a2-4fe4-93a9-f66b8b870e24&product_intent=terraform)에서 설치한다.
"hashicorp/aws"가 그 설정을 의미한다.

`required_providers` block에 다른 각각의 provider를 작성할 수 있다. `version` 속성은 선택이지만 구성한 값이 작동하지 않는 provider 버전을 사용하지 않도록 사용하는 것이 좋다. 만약 이 값을 따로 지정하지 않는다면 초기화 중에 최신 버젼을 자동으로 다운로드 한다. ([문서](https://developer.hashicorp.com/terraform/language/providers/requirements))


### Provider Block
`provider`는 구체적인 provider의 설정을 작성한다. (이 경우 `aws`) Provider는 Terraform이 리소스를 생성하고 관리하는데 사용하는 플러그인이다.

provider block을 여러개 사용하여 다른 provider의 여러 리소스를 관리할 수 있다.

### Resource Block
`resource`는 인프라의 구성요소들을 설정한다. 리소스는 EC2 인스턴스 처럼 물리적이거나 가상 구성 요소일 수도 있고 Heroku 앱처럼 논리적 리소스일 수도 있다.

resourc block은 type, name 2개의 문자열을 block전에 가진다. 예시에서는 resource의 type은 `aws_instance`이고 name은 `app_server`이다. type의 접두사(`aws`)는 provider의 이름(`aws`)와 매핑되어 관리한다. 예시에 따르면 aws provider가 aws_instance를 관리한다. 또한 type과 nam을 통해 고유 ID(`aws_instance.app_server`)를 만든다. 

Block에는 리소스 구성에 필요한 인자(머신 크기, 디스크 이미지 이름, VPC ID) 값들이 있다. 각 리소스마다 필요한 인자 값들은 [여기서](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) 확인하자. 예제 구성에는 AMI ID를 Ubuntu 이미지로 설정하고 t2.micro 인스턴스 유형을 사용했다. 또한 인스턴스 이름을 지정하는 태그를 설정했다.


## 디렉토리 초기화(Initialize)
새 구성을 생성하거나, 버전 제어에서 기존 구성을 체크아웃할때 `terraform init`을 사용하면 된다. Terraform은 aws provider를 다운로드 하여 현재 작업 디렉토리의 숨겨진 하위 디렉토리 .terraform에 설치한다.
또한 lock 파일(.terraform.lock.hcl)을 만들어 준다. 그래서 사용한 provider 버젼을 구체적으로 작성하여 관리할 수 있다.


## 구성파일 포맷팅 및 유효성 검사
모든 구성파일에대해  `terraform fmt` 명령어를 이용하여 포맷팅 할 수 있다. 만약 수정된 파일이 있는 경우의 해당 파일의 이름을 print 해준다.

또한 구문적으로 유효한지 `terraform validate` 명령어를 사용 할 수 있다.


## 인프라 구축
작성한 구성파일을 적용하기 위해서는 `terraform apply` 명령을 실행하면 된다.먼저 적용하기 전에 Terraform에서 수행할 작업을 설명하는 Plan을 인쇄한다. Git의 diff 형식처럼 `+` 옆에는 리소스 생성을 의미힌다. 그 아래에는 설정할 속성이 표시 되는데 (known after apply)는 리소스가 생성될 때까지 값을 알 수 없다는 의미이다. 이후 승인을 기다리게 되는데 Yes를 입력하면 plan대로 실행하게 된다.


## 상태 검사
구성파일을 적용하면 `terraform.tfstate`라는 파일을 만들고 안에 리소스이 ID와 속성 값을 저장한다. Terraform state 파일은 리소스의 관리 상태를 추적할 수 있는 유일한 방법으로 **종종 민감한 내용을 포함하고 있기 때문에 관리에 주의를 기울여야 한다.**

`terraform show`를 사용하여 현재 상태를 검사 할 수 있다.