# Forensic - Creamheroes

## 문제
고양이 사진이 가득한(7장) 압축파일이 주어졌다.

## 접근
사진만 주어진것을 보니 안티포렌식임을 직감했다. 윈도우 탐색기가 정렬해준 덕에 가장 먼저 chuchu.jpeg를 확인해볼 수 있었다. HxD로 열어 숨겨진 파일이 없는지 확인해 보았다.

## 해결
아름답게 PNG파일 시그니처를 확인할 수 있었다. 그러나 복원해보면 사진이 깨져있다. 깨진 크기가 너무나 아름다웠기 때문에 나머지 이미지 파일에 조각들이 숨어있음을 직감할 수 있었다. 그러나 이를 잘 조합하기 위해서는 PNG 파일 구조를 알아야 했는데 검색해도 정확한 내용을 찾기가 어려웠다. 윈도우의 정렬이 도움이 되길 바라며 정렬된 순서대로 조각을 이어붙이니 플래그가 쓰여있는 고양이 사진을 추출할 수 있었다.