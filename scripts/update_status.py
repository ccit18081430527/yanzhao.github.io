# scripts/update_status.py
import pandas as pd
from datetime import datetime

def update_spec_status():
    # 读取需求状态
    df = pd.read_csv("status/requirements.csv")
    
    # 计算完成进度
    completed = df[df['状态'] == '已完成'].shape[0]
    total = df.shape[0]
    progress = f"{completed}/{total} ({completed/total*100:.1f}%)"
    
    # 更新首页
    with open("docs/index.md", "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = content.replace(
        "{{progress}}", 
        f"**需求完成进度**: {progress} (最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')})"
    )
    
    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    update_spec_status()