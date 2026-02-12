# 웹소울랩 (Websoul Lab) - 반응형 웹사이트

## 프로젝트 개요

웹소울랩은 웹접근성 및 웹표준 컨설팅, UI/UX 컨설팅 전문 기업의 공식 웹사이트입니다. PRD(Product Requirements Document)를 기반으로 설계된 반응형 웹사이트로, 모든 디바이스에서 최적의 사용자 경험을 제공합니다.

## 주요 기능

### 1. 반응형 디자인
- 데스크톱, 태블릿, 모바일 등 모든 디바이스 지원
- 유동적인 그리드 레이아웃
- 미디어 쿼리를 활용한 최적화된 UI

### 2. 모던한 UI/UX
- 그라디언트 효과와 부드러운 애니메이션
- 직관적인 네비게이션 구조
- 시각적으로 매력적인 디자인

### 3. 접근성 고려
- 시맨틱 HTML5 마크업
- 키보드 네비게이션 지원
- ARIA 속성 적용

## 사이트 구조

```
홈페이지
├── index.html (메인 페이지)
├── About Lab
│   ├── who-we-are.html (비전 및 철학 - 디지털 모듈)
│   ├── history.html (연혁)
│   ├── certifications.html (기업인증/특허현황/수상실적)
│   └── partners.html (우호 고객사)
└── Digital Inclusion
    ├── consulting.html (웹접근성 컨설팅)
    ├── standards.html (웹표준 진단)
    └── certification.html (접근성 인증마크 획득 지원)
```

## 기술 스택

- **HTML5**: 시맨틱 마크업
- **CSS3**: 반응형 디자인, Flexbox, Grid, 애니메이션
- **JavaScript**: 인터랙티브 요소, 탭 시스템, 모바일 메뉴
- **Google Fonts**: Noto Sans KR

## 페이지별 주요 기능

### 메인 페이지 (index.html)
- Hero 섹션: 그라디언트 배경과 강력한 메시지
- 서비스 개요: 4개의 핵심 서비스 카드
- About 미리보기: 회사 소개 및 통계
- Digital Inclusion 미리보기: 3개의 주요 서비스 카드
- 문의 폼: 실시간 문의 제출

### About Lab 섹션

#### Who We Are
- 비전 및 철학
- 4가지 핵심 가치
- 4가지 디지털 모듈 상세 설명
- 전문성, 신뢰, 혁신, 품질 강조

#### History
- 타임라인 형식의 연혁 (2014-2026)
- 주요 성과 통계
- 수상 및 인증 내역
- 미래 비전

#### Certifications
- **탭 1: 기업인증** - 6개 주요 인증
- **탭 2: 특허현황** - 6개 특허 및 프로그램 등록
- **탭 3: 수상실적** - 연도별 수상 내역

#### Partners
- 산업별 파트너사 분류 (공공/금융/교육/IT/이커머스/미디어)
- 50+ 파트너사 로고
- 고객 추천사 (6개)
- 파트너십 가치 제시

### Digital Inclusion 섹션

#### 웹접근성 컨설팅
- **탭 1: 컨설팅 의뢰 대상** - 6개 주요 대상군
- **탭 2: 컨설팅 프로세스** - 6단계 프로세스
- **탭 3: 기대효과** - 8가지 주요 효과 및 성공 사례

#### 웹표준 진단
- 웹표준의 중요성 및 필요성
- 5단계 진단 프로세스
- 6가지 주요 진단 항목
- 진단 패키지 및 가격

#### 접근성 인증마크 획득 지원
- **탭 1: WA인증마크 소개** - 4가지 원칙, 인증 종류
- **탭 2: 인증 절차** - 6단계 상세 절차
- **탭 3: 유지보수** - 3가지 패키지, 성공 사례

## 스타일 특징

### 색상 팔레트
- Primary: #4F46E5 (인디고)
- Secondary: #7C3AED (보라)
- Accent: #059669 (초록)
- Danger: #DC2626 (빨강)
- 그레이스케일: 900~100

### 타이포그래피
- 폰트: Noto Sans KR
- 반응형 폰트 크기 (xs ~ 5xl)
- 명확한 계층 구조

### 인터랙션
- Hover 효과
- 부드러운 전환 (transition)
- 스크롤 애니메이션
- 탭 시스템

## 반응형 브레이크포인트

- Desktop: 1200px+
- Tablet: 768px ~ 992px
- Mobile: ~ 768px

## 설치 및 실행

1. 프로젝트 클론 또는 다운로드
2. **(선택)** page-header 메뉴별 배경 이미지 복사: 생성된 배경 이미지가 `~/.cursor/projects/.../assets`에 있으면 `images/`로 복사
   ```bash
   python copy_header_bg.py
   ```
   - 이미지가 없으면 메뉴별 page-header는 기본 그라데이션 배경으로 표시됩니다.
3. 브라우저에서 `index.html` 파일 열기
4. 로컬 서버 실행 (선택사항):
   ```bash
   # Python 3
   python -m http.server 8000
   
   # Node.js (http-server)
   npx http-server
   ```

## 브라우저 호환성

- Chrome (최신 버전)
- Firefox (최신 버전)
- Safari (최신 버전)
- Edge (최신 버전)
- 모바일 브라우저 (iOS Safari, Chrome Mobile)

## 파일 구조

```
웹소울랩/
├── index.html
├── about/
│   ├── who-we-are.html
│   ├── history.html
│   ├── certifications.html
│   └── partners.html
├── digital/
│   ├── consulting.html
│   ├── standards.html
│   └── certification.html
├── css/
│   ├── style.css (메인 스타일)
│   └── pages.css (서브 페이지 스타일)
├── js/
│   └── main.js (인터랙션 스크립트)
└── README.md
```

## 주요 컴포넌트

### 네비게이션
- 고정 헤더 (스크롤 시 효과)
- 드롭다운 메뉴
- 모바일 햄버거 메뉴

### 섹션
- Hero 섹션
- 서비스 그리드
- 프로세스 단계
- 타임라인
- 증언 카드
- CTA (Call-to-Action) 섹션

### 폼
- 문의 폼 (유효성 검사 포함)

### 탭 시스템
- JavaScript 기반 탭 전환
- 부드러운 애니메이션

## 성능 최적화

- CSS/JS 최소화 (권장)
- 이미지 최적화 (현재 SVG 플레이스홀더)
- 지연 로딩 구현
- 효율적인 CSS 선택자

## 접근성 고려사항

- 시맨틱 HTML5 태그 사용
- Alt 텍스트 (이미지 추가 시)
- ARIA 레이블
- 키보드 네비게이션 지원
- 충분한 색상 대비
- 포커스 표시

## 향후 개선 사항

1. **이미지 추가**: 실제 로고, 제품 이미지, 팀 사진
2. **백엔드 연동**: 문의 폼 실제 전송 기능
3. **CMS 통합**: 콘텐츠 관리 시스템 연동
4. **다국어 지원**: 영어, 일본어 등
5. **검색 기능**: 사이트 내 검색
6. **블로그/뉴스**: 최신 소식 섹션
7. **성능 모니터링**: Google Analytics, Lighthouse
8. **SEO 최적화**: 메타 태그, sitemap.xml, robots.txt

## 라이선스

© 2026 Websoul Lab. All rights reserved.

## 연락처

- 이메일: contact@websoul.co.kr
- 전화: 02-1234-5678
- 주소: 서울특별시 강남구 테헤란로 XXX

---

**개발 정보**
- 개발 기간: 2026년 1월
- 개발 환경: HTML5, CSS3, Vanilla JavaScript
- 디자인 컨셉: 모던, 미니멀, 전문적
