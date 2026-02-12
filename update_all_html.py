#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
모든 HTML 파일을 컴포넌트를 사용하도록 일괄 업데이트하는 스크립트
"""

import os
import re
from pathlib import Path

# 이미 수정된 파일 목록
UPDATED_FILES = {
    'index.html',
    'about/intro.html',
    'accessibility/overview.html',
    'consulting/accessibility.html',
    'about/certifications.html',
    'portfolio/accessibility-consulting.html',
    'support/news.html',
    'solution/performance-monitoring.html'
}

# 업데이트할 파일 목록
FILES_TO_UPDATE = [
    'accessibility/guidelines.html',
    'accessibility/practical-guide.html',
    'accessibility/certification.html',
    'accessibility/guide-perceivable.html',
    'accessibility/guide-operable.html',
    'accessibility/guide-understandable.html',
    'accessibility/guide-robust.html',
    'consulting/integrated-quality.html',
    'consulting/compatibility.html',
    'consulting/construction.html',
    'consulting/openness.html',
    'consulting/policy-check.html',
    'portfolio/construction.html',
    'portfolio/publishing.html',
    'solution/link-validation.html',
    'support/consulting-inquiry.html',
    'support/inquiry.html',
    'about/location.html',
    'about/organization.html',
    'about/who-we-are.html',
    'about/partners.html',
    'about/history.html',
    'digital/standards.html',
    'digital/certification.html',
    'digital/consulting.html'
]

def calculate_base_path(file_path):
    """파일 경로에 따라 base path 계산"""
    depth = len(Path(file_path).parent.parts)
    if depth == 0:
        return ''
    return '../' * depth

def update_file(file_path):
    """단일 파일 업데이트"""
    full_path = Path(file_path)
    
    if not full_path.exists():
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return False
    
    try:
        with open(full_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        base_path = calculate_base_path(file_path)
        component_loader_path = f"{base_path}js/component-loader.js" if base_path else "js/component-loader.js"
        
        # 1. 헤더 교체 (settings-modal과 header 전체)
        # 패턴: <body>부터 </header>까지
        header_pattern = r'<body>[\s\S]*?<header class="header"[\s\S]*?</header>'
        if re.search(header_pattern, content):
            content = re.sub(header_pattern, 
                '<body>\n    <!-- Header Component Placeholder -->\n    <div id="header-placeholder"></div>', 
                content, count=1)
        
        # 2. 서브메뉴 교체
        submenu_pattern = r'<aside class="side-navigation"[^>]*>[\s\S]*?</aside>'
        if re.search(submenu_pattern, content):
            content = re.sub(submenu_pattern,
                '        <!-- Submenu Component Placeholder -->\n        <div id="submenu-placeholder"></div>',
                content, count=1)
        
        # 3. 푸터 교체
        footer_pattern = r'<!--\s*Footer\s*-->[\s\S]*?<footer class="footer"[\s\S]*?</footer>'
        if re.search(footer_pattern, content):
            content = re.sub(footer_pattern,
                '    <!-- Footer Component Placeholder -->\n    <div id="footer-placeholder"></div>',
                content, count=1)
        
        # 4. 스크립트 추가/수정
        script_pattern = r'<script src="(\.\./)*js/main\.js"></script>'
        if re.search(script_pattern, content):
            content = re.sub(script_pattern,
                f'    <!-- Component Loader (must load before main.js) -->\n    <script src="{component_loader_path}"></script>\n    <script src="\\1js/main.js"></script>',
                content, count=1)
        
        if content != original_content:
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ 업데이트 완료: {file_path}")
            return True
        else:
            print(f"- 변경사항 없음: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 오류 발생 ({file_path}): {e}")
        return False

def main():
    """메인 함수"""
    print("HTML 파일 일괄 업데이트 시작...\n")
    
    updated_count = 0
    for file_path in FILES_TO_UPDATE:
        if file_path not in UPDATED_FILES:
            if update_file(file_path):
                updated_count += 1
    
    print(f"\n완료! 총 {updated_count}개 파일이 업데이트되었습니다.")

if __name__ == '__main__':
    main()
