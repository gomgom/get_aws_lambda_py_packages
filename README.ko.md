# Python 3 PIP Packaging Tool for AWS Lambda
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Working on AWS !](https://img.shields.io/badge/Working%20on-AWS-orange.svg)](https://aws.amazon.com)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/gomgomdev/pypubdata/pulse)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/gomgomdev/pypubdata/issues)

English Readme(README.md) is [HERE](https://github.com/gomgomdev/get_aws_lambda_py_packages/blob/master/README.md)

## 개요
**이 AWS Lambda 파이썬 스크립트는 Amazon Linux용 PIP 패키지를 압축해서 제공해 줍니다.**  
AWS Lambda에서 파이썬 스크립트를 운영할 때 PIP 패키지가 필요한 분들은, 이 툴을 이용하셔서 패키지 묶음을 만들 수 있습니다.

예를 들어, 내 AWS Lambda 스크립트에 'requests' 패키지와 'PyMySQL' 패키지가 필요하다고 하면,  
AWS Lambda 함수를 업로드 할 때, 이 패키지들을 같은 폴더에 넣어주어야 합니다.

만약에 Amazon Linux를 사용하시는 분이라면, 이 일이 어렵지 않은 일이지만, 만약에 Amazon Linux를 사용중이지 않다면 EC2 인스턴스를 켜야 할필요가 있습니다.  
EC2 인스턴스는 *pip 패키지 다운로드를 위해 잠시만 사용해도*, 1시간 만큼의 요금을 내야 하는 불편함이 있습니다.

이 AWS Lambda용 Python 스크립트는 AWS Lambda에서 작동하는 Amazon Linux를 활용해 pip 패키지를 만들어서, AWS S3에 업로드 해 줍니다.  
간편하게 패키지를 다운로드하여, AWS Lambda 함수에 넣어주기만 하면 됩니다.

## 간단 사용법
1. **패키지 파일 업로드를 위하여 AWS S3 버킷을 만들어 주세요.** 이미 버킷이 있다면, 그것을 사용해도 좋습니다.
2. AWS Lambda에서 Python 3.6 버전의 새로운 람다 함수를 만들어 주세요. **이 Lambda를 위한 Rule은 AWS S3의 권한이 필요합니다. (업로드를 위하여)**
3. **저장소에 있는 'lambda_function.py' 파일에 있는 스크립트**를 새로 만든 람다 함수에 넣어줍니다.
4. **테스트 이벤트를 새로 구성합니다. 이벤트는 다음과 같은 형식으로 만들어 줍니다.**
```json
{
  "packages_name": ["패키지 이름 1", "패키지 이름 2", "등등 ..."],
  "s3_bucket_name": "S3 버킷 이름",
  "s3_path": "S3 경로 (s3_path 항목은 필수 아님, 기본 경로는 버킷 최상단)",
  "file_name": "파일이름.tar (file_name 항목은 필수 아님, '.tar' 확장자 필요, 기본값은 aws-linux-pip-packages.tar)"
}
```
5. 그리고 기본 설정에서 Lambda 메모리와 제한 시간을 설정할 수 있습니다.  
패키지 양에 따라 다르겠지만, **보통은 '192MB 메모리 / 2분 제한 시간' 정도면 완료할 수 있습니다.**
6. 마지막으로, **테스트 버튼을 누르면**, 람다 함수가 작동할 것입니다.
7. 람다 작동이 끝나면, **S3에 들어가보면 설정된 버킷/경로에 파일이 있을 것입니다.**
8. **이 파일을 여러분들의 AWS Lambda 스크립트에 압축 해제하여 사용하세요!**

## 기타 정보
사실 저는 프로그래머가 본 직업도 아니고, 이렇게 람다를 만들어 사용하는 것보다 더 좋은 방법이 있을 수 있습니다. ^^;  
하지만 이 짧은 실력을 가진 저에게 질문이 있으시다면 언제든지 환영합니다!

이메일을 보내주셔도 좋고, Github의 Issue를 열어주셔도 됩니다.

곰곰이 만든(Made by Gomgom) 스크립트 (https://gomgom.io, dev@gomgom.io)