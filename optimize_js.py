#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

def optimize_javascript():
    """优化JavaScript代码"""
    
    # 读取优化后的HTML文件
    with open('guixu-game-optimized.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. 提取JavaScript部分
    js_start = content.find('<script>')
    js_end = content.find('</script>')
    
    if js_start == -1 or js_end == -1:
        print("未找到JavaScript代码")
        return content
    
    js_code = content[js_start + 8:js_end]
    
    # 2. JavaScript优化规则
    js_optimizations = {
        # 改善函数命名
        r'const\s+timeoutPromise\s*=': 'const createTimeoutPromise =',
        r'const\s+continueProcessing\s*=': 'const continueProcess =',
        r'const\s+updateText\s*=': 'const updateGameText =',
        r'const\s+statusEntries\s*=': 'const getStatusEntries =',
        r'const\s+isCustomFont\s*=': 'const checkCustomFont =',
        r'const\s+loadPromises\s*=': 'const getLoadPromises =',
        r'const\s+fontLoadPromises\s*=': 'const getFontLoadPromises =',
        r'const\s+existingFont\s*=': 'const findExistingFont =',
        
        # 简化重复的事件绑定
        r'addEventListener\([\'"]click[\'"],\s*function\s*\(\s*e\s*\)\s*{': 'addEventListener(\'click\', (e) => {',
        r'addEventListener\([\'"]change[\'"],\s*function\s*\(\s*e\s*\)\s*{': 'addEventListener(\'change\', (e) => {',
        r'addEventListener\([\'"]input[\'"],\s*function\s*\(\s*e\s*\)\s*{': 'addEventListener(\'input\', (e) => {',
        
        # 优化DOM查询
        r'document\.querySelector\([\'"](.+?)[\'"]\)': r'document.querySelector(\'$1\')',
        r'document\.querySelectorAll\([\'"](.+?)[\'"]\)': r'document.querySelectorAll(\'$1\')',
        
        # 简化条件判断
        r'if\s*\(\s*(.+?)\s*===?\s*(.+?)\s*\)': r'if ($1 === $2)',
        r'if\s*\(\s*!(.+?)\s*\)': r'if (!$1)',
        
        # 优化循环
        r'for\s*\(\s*let\s+(\w+)\s*=\s*0\s*;\s*\1\s*<\s*(.+?)\s*;\s*\1\+\+\s*\)': r'for (let $1 = 0; $1 < $2; $1++)',
        
        # 简化对象创建
        r'new\s+Promise\(\s*\(\s*resolve\s*,\s*reject\s*\)\s*=>': 'new Promise((resolve, reject) =>',
    }
    
    # 3. 应用JavaScript优化
    optimized_js = js_code
    
    for pattern, replacement in js_optimizations.items():
        optimized_js = re.sub(pattern, replacement, optimized_js)
    
    # 4. 提取重复的代码块为函数
    # 查找重复的DOM操作模式
    repeated_patterns = [
        (r'style\.display\s*=\s*[\'"]none[\'"]', 'hideElement'),
        (r'style\.display\s*=\s*[\'"]block[\'"]', 'showElement'),
        (r'style\.display\s*=\s*[\'"]flex[\'"]', 'showElementFlex'),
        (r'classList\.add\([\'"](.+?)[\'"]\)', 'addClass'),
        (r'classList\.remove\([\'"](.+?)[\'"]\)', 'removeClass'),
        (r'classList\.toggle\([\'"](.+?)[\'"]\)', 'toggleClass'),
    ]
    
    # 5. 优化字符串拼接
    optimized_js = re.sub(r'\+\s*\+\s*', '+', optimized_js)
    optimized_js = re.sub(r'\+\s*([\'"][^\'"]*[\'"])\s*\+', r' + $1 + ', optimized_js)
    
    # 6. 简化逻辑判断
    optimized_js = re.sub(r'if\s*\(\s*(.+?)\s*\)\s*{\s*return\s+true\s*;\s*}\s*else\s*{\s*return\s+false\s*;\s*}', r'return Boolean($1);', optimized_js)
    optimized_js = re.sub(r'if\s*\(\s*(.+?)\s*\)\s*{\s*return\s+(.+?)\s*;\s*}\s*else\s*{\s*return\s+(.+?)\s*;\s*}', r'return $1 ? $2 : $3;', optimized_js)
    
    # 7. 统计优化效果
    original_js_size = len(js_code)
    optimized_js_size = len(optimized_js)
    js_reduction = original_js_size - optimized_js_size
    js_reduction_percent = (js_reduction / original_js_size) * 100 if original_js_size > 0 else 0
    
    print(f"JavaScript优化完成:")
    print(f"原始JS大小: {original_js_size:,} 字符")
    print(f"优化后JS大小: {optimized_js_size:,} 字符")
    print(f"减少: {js_reduction:,} 字符 ({js_reduction_percent:.1f}%)")
    
    # 8. 替换回原文件
    optimized_content = content[:js_start + 8] + optimized_js + content[js_end:]
    
    # 9. 保存优化后的文件
    with open('guixu-game-optimized.html', 'w', encoding='utf-8') as f:
        f.write(optimized_content)
    
    print("JavaScript优化完成，文件已更新")
    
    return optimized_content

if __name__ == '__main__':
    optimize_javascript()