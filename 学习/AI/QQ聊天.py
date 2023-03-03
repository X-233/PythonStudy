# 1、爬虫速度不要太快，不要给对方服务器造成太大压力
# 2、爬虫不要伪造VIP，绕过对方身份验证，可以买一个VIP做自动化
# 3、公民个人信息不要去碰
import openai
import os

openai.organization = "org-6NtN8TZ9wvHlP4TnWR6bv0sy"
openai.api_key = "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"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt="Human:你好,用中文回答\nAI:\n",
  temperature=0.9,
  max_tokens=150,
  top_p=1,
  frequency_penalty=0.0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)
print(response)