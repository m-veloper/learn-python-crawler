# urllib 사용법 및 기본 스크래핑

import urllib.request as req

# 파일 URL
img_url = 'http://cafefiles.naver.net/20120611_289/kkas_nknk55_1339391180925I3qnD_JPEG/%B0%ED%BE%E7%C0%CC9.jpg';
html_url = 'https://google.com';

# 다운받을 경로
save_path1 = 'D:/test.jpg';
save_path2 = 'D:/index.html';

# 예외처리

try:
    file1, header1 = req.urlretrieve(img_url, save_path1 );
    file2, header2 = req.urlretrieve(html_url, save_path2 );
except Exception as e:
    print('Download faild');
    print(e);
else:
    # Header 정보 출력
    print(header1);
    print(header2);


