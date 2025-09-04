#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import json

def optimize_css_styles():
    """优化CSS样式"""
    
    # 读取原始JSON文件
    with open('/data/data/com.termux/files/home/regex-【归墟】正文-4_5-客舟闻笛怨，津渡锁愁烟【梦星作品】.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    content = data['replaceString']
    
    # 1. 提取HTML内容（去掉</UpdateVariable>和```标记）
    html_match = re.search(r'```\n(.*)', content, re.DOTALL)
    if not html_match:
        print("未找到HTML内容")
        return
    
    html_content = html_match.group(1)
    
    # 2. 添加CSS变量系统
    css_vars = '''
    :root {
      /* 主题颜色变量 */
      --color-primary: #c9aa71;
      --color-secondary: #8b7355;
      --color-accent: #ff6b6b;
      --color-bg-dark: rgba(26, 26, 46, 0.8);
      --color-bg-light: rgba(45, 27, 61, 0.5);
      --color-text: #e0dcd1;
      --color-border: rgba(201, 170, 113, 0.3);
      
      /* 布局变量 */
      --border-radius: 8px;
      --border-radius-small: 4px;
      --border-radius-large: 12px;
      --border-width: 1px;
      --spacing-small: 4px;
      --spacing-medium: 8px;
      --spacing-large: 16px;
      
      /* 动画变量 */
      --transition-fast: 0.2s;
      --transition-normal: 0.3s;
      --transition-slow: 0.4s;
      --animation-timing: cubic-bezier(0.4, 0, 0.2, 1);
      
      /* z-index层级 */
      --z-dropdown: 1000;
      --z-modal: 1001;
      --z-tooltip: 1002;
    }
    
    '''
    
    # 3. 优化CSS样式规则
    css_optimizations = {
        # 替换硬编码的颜色值
        r'color:\s*#c9aa71': 'color: var(--color-primary)',
        r'color:\s*#8b7355': 'color: var(--color-secondary)',
        r'border:\s*1px solid #c9aa71': 'border: var(--border-width) solid var(--color-primary)',
        r'border:\s*1px solid rgba\(201, 170, 113, 0\.3\)': 'border: var(--border-width) solid var(--color-border)',
        r'border-radius:\s*8px': 'border-radius: var(--border-radius)',
        r'border-radius:\s*4px': 'border-radius: var(--border-radius-small)',
        r'border-radius:\s*12px': 'border-radius: var(--border-radius-large)',
        r'transition:\s*all 0\.3s ease': 'transition: all var(--transition-normal) ease',
        r'transition:\s*all 0\.3s cubic-bezier\(0\.4, 0, 0\.2, 1\)': 'transition: all var(--transition-normal) var(--animation-timing)',
        r'z-index:\s*1000': 'z-index: var(--z-dropdown)',
        r'z-index:\s*1001': 'z-index: var(--z-modal)',
        r'z-index:\s*1002': 'z-index: var(--z-tooltip)',
        
        # 简化重复的背景样式
        r'background:\s*rgba\(26, 26, 46, 0\.8\)': 'background: var(--color-bg-dark)',
        r'background:\s*rgba\(45, 27, 61, 0\.5\)': 'background: var(--color-bg-light)',
        r'background:\s*rgba\(0, 0, 0, 0\.3\)': 'background: rgba(0, 0, 0, 0.3)',
        r'background:\s*rgba\(0, 0, 0, 0\.5\)': 'background: rgba(0, 0, 0, 0.5)',
        r'background:\s*rgba\(0, 0, 0, 0\.7\)': 'background: rgba(0, 0, 0, 0.7)',
        
        # 统一间距
        r'gap:\s*4px': 'gap: var(--spacing-small)',
        r'gap:\s*8px': 'gap: var(--spacing-medium)',
        r'gap:\s*16px': 'gap: var(--spacing-large)',
        r'padding:\s*4px': 'padding: var(--spacing-small)',
        r'padding:\s*8px': 'padding: var(--spacing-medium)',
        r'padding:\s*16px': 'padding: var(--spacing-large)',
    }
    
    # 4. 应用CSS优化
    optimized_html = html_content
    
    # 在<style>标签后插入CSS变量
    style_insert_pos = optimized_html.find('<style>')
    if style_insert_pos != -1:
        style_end_pos = optimized_html.find('>', style_insert_pos) + 1
        optimized_html = (optimized_html[:style_end_pos] + 
                         css_vars + 
                         optimized_html[style_end_pos:])
    
    # 应用CSS优化规则
    for pattern, replacement in css_optimizations.items():
        optimized_html = re.sub(pattern, replacement, optimized_html)
    
    # 5. 优化CSS类名（简化过长的类名）
    class_name_optimizations = {
        r'guixu-root-container': 'guixu-root',
        r'game-container': 'game-container',
        r'character-panel': 'char-panel',
        r'interaction-panel': 'interaction-panel',
        r'main-content': 'main-content',
        r'top-status': 'status-top',
        r'bottom-status': 'status-bottom',
        r'quick-send-container': 'send-container',
        r'quick-send-input': 'send-input',
        r'variable-changes-reminder': 'var-changes',
        r'relationships-grid': 'rel-grid',
        r'relationship-card': 'rel-card',
        r'empty-relationships-state': 'rel-empty',
    }
    
    for old_class, new_class in class_name_optimizations.items():
        # 只优化CSS类名，不改变HTML结构
        optimized_html = re.sub(fr'\.{old_class}(?=[{{\s,:])', f'.{new_class}', optimized_html)
    
    # 6. 统计优化效果
    original_size = len(html_content)
    optimized_size = len(optimized_html)
    reduction = original_size - optimized_size
    reduction_percent = (reduction / original_size) * 100
    
    print(f"CSS优化完成:")
    print(f"原始大小: {original_size:,} 字符")
    print(f"优化后大小: {optimized_size:,} 字符")
    print(f"减少: {reduction:,} 字符 ({reduction_percent:.1f}%)")
    
    # 7. 保存优化后的文件
    with open('guixu-game-optimized.html', 'w', encoding='utf-8') as f:
        f.write(optimized_html)
    
    print("优化后的HTML文件已保存为: guixu-game-optimized.html")
    
    return optimized_html

if __name__ == '__main__':
    optimize_css_styles()