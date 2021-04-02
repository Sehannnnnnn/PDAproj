# PDAproj
큐시즘 기업 프로젝트 6조

# APK
Front-build/app-release_v0.92.apk 를 다운받아 설치하시면 됩니다.
1. App 이름은 'Find out Free Rider' 입니다.
2. React Native를 사용하였습니다.
3. 안드로이드 폴더 형식에 접근하기 때문에 안드로이드 타겟으로 빌드되었습니다.
4. React Native의 특성상 조금의 수정을 거친 후 IOS 빌드가 가능합니다.
5. 안드로이드 OS version 11 에서 테스트 되었습니다.
6. 외부 저장소 열람 권한이 필요합니다. 권한을 따로 요청하지 않는다면 직접 권한을 허용해주세요.
7. 카카오톡 파일을 upload 할 때, 서버로 텍스트 데이터를 보내고 Processing 된 값을 받아옵니다. 인터넷이 연결되어 있어야합니다.

# Server
1. 서버는 Django를, DB는 SQLite를 사용하였습니다.
2. AWS 클라우드 서버를 이용해 배포합니다.
3. python 3.8.5 버전을 기준으로 합니다.
4. request로 txt파일을 받고, response로 html 포맷 json String을 반환합니다.
5. ./Back-end/dataAnalysis.py 모듈에서 txt파일을 분석합니다.
6. txt파일은 ./Back-end/에 저장됩니다.
