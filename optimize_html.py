#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

def optimize_html_structure():
    """优化HTML结构"""
    
    # 读取优化后的HTML文件
    with open('guixu-game-optimized.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. HTML结构优化规则
    html_optimizations = {
        # 移除多余的空格和换行
        r'\n\s*\n': '\n',
        r'\s+>': '>',
        r'<\s+': '<',
        r'\s+': ' ',
        
        # 优化class属性（移除多余的空格）
        r'class\s*=\s*[\'"]\s*([^\'"]+?)\s*[\'"]': r'class="$1"',
        r'class\s*=\s*[\'"]([^\'"]+?)\s+([^\'"]+?)\s*[\'"]': r'class="$1 $2"',
        
        # 优化style属性
        r'style\s*=\s*[\'"]\s*([^\'"]+?)\s*[\'"]': r'style="$1"',
        
        # 简化data属性
        r'data-([a-z-]+)\s*=\s*[\'"]([^\'"]+?)[\'"]': r'data-$1="$2"',
        
        # 移除注释（保留重要的）
        r'<!--\s*[Cc]opyright.*?-->': '',
        r'<!--\s*[Ll]icense.*?-->': '',
    }
    
    # 2. 应用HTML优化
    optimized_html = content
    
    for pattern, replacement in html_optimizations.items():
        optimized_html = re.sub(pattern, replacement, optimized_html)
    
    # 3. 特殊处理：移除HTML标签之间的多余空格
    optimized_html = re.sub(r'>\s+<', '><', optimized_html)
    
    # 4. 优化重复的div结构
    # 查找连续的空div
    optimized_html = re.sub(r'<div[^>]*>\s*</div>', '', optimized_html)
    
    # 5. 优化CSS类名的使用
    # 移除重复的class
    def optimize_duplicate_classes(match):
        classes = match.group(1).split()
        unique_classes = []
        seen = set()
        for cls in classes:
            if cls not in seen:
                seen.add(cls)
                unique_classes.append(cls)
        return f'class="{" ".join(unique_classes)}"'
    
    optimized_html = re.sub(r'class\s*=\s*[\'"]([^\'"]+?)[\'"]', optimize_duplicate_classes, optimized_html)
    
    # 6. 简化内联样式
    def optimize_inline_styles(match):
        styles = match.group(1).split(';')
        optimized_styles = []
        seen = set()
        
        for style in styles:
            style = style.strip()
            if style and ':' in style:
                prop, value = style.split(':', 1)
                prop = prop.strip()
                value = value.strip()
                
                # 移除重复的样式属性
                if prop not in seen:
                    seen.add(prop)
                    optimized_styles.append(f'{prop}:{value}')
        
        return f'style="{";".join(optimized_styles)}"'
    
    optimized_html = re.sub(r'style\s*=\s*[\'"]([^\'"]+?)[\'"]', optimize_inline_styles, optimized_html)
    
    # 7. 统计优化效果
    original_size = len(content)
    optimized_size = len(optimized_html)
    reduction = original_size - optimized_size
    reduction_percent = (reduction / original_size) * 100
    
    print(f"HTML结构优化完成:")
    print(f"原始大小: {original_size:,} 字符")
    print(f"优化后大小: {optimized_size:,} 字符")
    print(f"减少: {reduction:,} 字符 ({reduction_percent:.1f}%)")
    
    # 8. 检查HTML结构完整性
    html_tags = ['<!DOCTYPE html>', '<html>', '<head>', '<body>', '</body>', '</html>']
    missing_tags = []
    for tag in html_tags:
        if tag not in optimized_html:
            missing_tags.append(tag)
    
    if missing_tags:
        print(f"警告: 缺少HTML标签: {missing_tags}")
    else:
        print("HTML结构完整")
    
    # 9. 保存优化后的文件
    with open('guixu-game-optimized.html', 'w', encoding='utf-8') as f:
        f.write(optimized_html)
    
    print("HTML结构优化完成，文件已更新")
    
    return optimized_html

def create_single_line_version():
    """创建单行版本，保持原始格式"""
    
    # 读取优化后的HTML文件
    with open('guixu-game-optimized.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 转换为单行（保留必要的换行）
    single_line = content.replace('\n', '\\n')
    
    # 创建新的JSON格式
    new_json = {
        "id": "e853883a-9ad4-4de2-84ee-4cd0ace04f92-optimized",
        "scriptName": "【归墟】正文-4.5-客舟闻笛怨，津渡锁愁烟【梦星作品】-优化版",
        "findRegex": "</UpdateVariable>",
        "replaceString": f"</UpdateVariable>\\n```\\n{single_line}\\n```",
        "trimStrings": [],
        "placement": [1],
        "disabled": False,
        "markdownOnly": False,
        "promptOnly": False,
        "runOnEdit": False,
        "substituteRegex": [],
        "minDepth": None,
        "maxDepth": None
    }
    
    # 保存单行版本
    with open('regex-【归墟】正文-4_5-客舟闻笛怨，津渡锁愁烟【梦星作品】-优化版.json', 'w', encoding='utf-8') as f:
        json.dump(new_json, f, ensure_ascii=False, indent=2)
    
    print("单行版本已创建: regex-【归墟】正文-4_5-客舟闻笛怨，津渡锁愁烟【梦星作品】-优化版.json")
    
    return single_line

if __name__ == '__main__':
    optimize_html_structure()
    create_single_line_version()