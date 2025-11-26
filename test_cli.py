#!/usr/bin/env python3
import sys
from pathlib import Path
# 确保引用的是本地 src 目录
sys.path.insert(0, str(Path.cwd() / 'src'))

from context1.cli import app
from typer.main import get_command

# 获取底层的 Click 命令对象
click_cmd = get_command(app)

print("✅ App loaded successfully!")
print(f"Available commands: {list(click_cmd.commands.keys())}")

# 检查 pack 命令的参数
if 'pack' in click_cmd.commands:
    pack_cmd = click_cmd.commands['pack']
    print("\n🔍 Checking 'pack' command parameters:")
    
    found_new_params = False
    for param in pack_cmd.params:
        # param.name 是参数名，param.opts 是命令行标志 (如 --sort)
        print(f"  - {param.name} {param.opts}")
        if param.name in ['sort', 'format']:
            found_new_params = True
            
    if found_new_params:
        print("\n✨ SUCCESS: New parameters 'sort' and 'format' detected!")
    else:
        print("\n❌ FAIL: New parameters not found.")
else:
    print("Pack command not found")