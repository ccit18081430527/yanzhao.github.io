# scripts/generate_diagrams.py
import pandas as pd
import matplotlib.pyplot as plt

def generate_performance_chart():
    data = {
        '场景': ['单个设备控制', '场景模式执行', '批量设备操作'],
        '响应时间(ms)': [500, 2000, 5000],
        '并发用户': [1000, 500, 100]
    }
    df = pd.DataFrame(data)
    
    # 生成图表
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.set_title('系统性能指标')
    ax1.set_ylabel('响应时间(ms)')
    ax1.bar(df['场景'], df['响应时间(ms)'], color='skyblue')
    ax1.tick_params(axis='y')
    
    ax2 = ax1.twinx()
    ax2.set_ylabel('并发用户数')
    ax2.plot(df['场景'], df['并发用户'], color='green', marker='o', linewidth=2)
    
    plt.tight_layout()
    plt.savefig('docs/assets/images/performance.png')