import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
# api_key = os.environ.get("LLM_API_KEY")

if not api_key:
    raise ValueError("未找到环境变量 LLM_API_KEY")

client = OpenAI(
    api_key=api_key,  # 替换为环境变量
    base_url="https://api.siliconflow.cn"
)

def llm_chat(question='你好', model='Qwen/Qwen3-32B',):
    response = client.chat.completions.create(
        # model="deepseek-chat",
        model=model,
        messages=[
            {"role": "user", "content": question}
        ],
        # 高创造性任务（如诗歌生成）：0.8~1.0
        # 平衡模式（默认通常为0.7）：0.5~0.7
        # 确定性输出（如事实回答）：0.0~0.3
        temperature=0.7,
        stream=False
    )
    if model == 'deepseek-reasoner':
        reasoning_content = response.choices[0].message.reasoning_content
    else:
        reasoning_content = ''
    # print(reasoning_content)
    # print(response.choices[0].message.content)
    return response.choices[0].message.content, reasoning_content