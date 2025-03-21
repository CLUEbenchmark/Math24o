# Math24o

Math24o benchmarks LLMs on Chinese high school Olympiad math using the 2024 prelims.

Math24o是一个中文题目的数学推理测评基准，用于评估大型语言模型在「高中奥林匹克数学竞赛」级别的数学推理能力。

该测评使用2024年预赛试题，可通过程序自动判断模型答案与参考答案是否一致，以客观评估模型的正确率。

此测评旨在为未来模型研发提供参考，提高模型在复杂数学任务中的可靠性。



# 获得模型回复及提示词 Prompts

Full Input: <question>+"\n" + <special_prompt>

指定提示词（Special Prompt Used）：

    请把你的最终答案放在\boxed{}内，即使用\boxed{你的最终答案}这个格式，注意\boxed{}里只能是整数或小数。

Special Prompt Used translated as Engish:
  
    Please put your final answer in \boxed{}, using the format \boxed{your final answer}. Note that only integers or decimals are allowed inside \boxed{}.

完整示例（Example）：

    设函数 $$f : \{1, 2, 3 \} \to\{2, 3, 4 \}$$ 满足 $$f \left( f \left( x \right)-1 \right)=f \left( x \right)$$ ，则这样的函数有多少个？

    请把你的最终答案放在\boxed{}内，即使用\boxed{你的最终答案}这个格式，注意\boxed{}里只能是整数或小数。


# 🏆 主要成绩 Main Result

| 排名 | 模型                                    | 机构       | 总分  | 使用方式 | 发布日期   |
|----|--------------------------------|----------|------|----------|----------|
| 1  | o3-mini(high)                  | OpenAI   | 85.71 |API |2025.03.12 |
| 2  | Gemini-2.0-Flash-Thinking-Exp-01-21 | Google   | 71.43|API | 2025.03.12 |
| 3  | QwQ-Max-Preview                | 阿里云    | 66.67 | 官网 | 2025.03.12 |
| 3  | QwQ-32B                         | 阿里云    | 66.67 | 模型|2025.03.12 |
| 3  | o1                              | OpenAI   | 66.67 |API  | 2025.03.12 |
| 4  | DeepSeek-R1                     | 深度求索  | 57.14 | API | 2025.03.12 |
| 4  | Claude 3.7 Sonnet               | Anthropic | 57.14 |POE| 2025.03.12 |

    注：以上成绩是大模型仅生成一次答案时的正确率。用户可自己结合问题和答案重新进行评估。

# ✨自动化评估 Auto Evaluation

    待所有待测大模型的回答都粘贴在 model_answers 后，保存 model_answers 文件。回到终端，依次发送以下内容：

## 安装所需的 Python 扩展包  Install 

    pip install -r requirements.txt

## 获取评估结果 Run script

    python auto_evaluation.py

此时在终端会返回待测大模型的平均得分。

你也可以在终端发送以下内容来获取每道题目的详细评估结果：

## 打开 output.xlsx（也可以手动打开）

    output.xlsx
