import setting.config as config
import sys

# ライブラリ&認証情報を設定
import openai
openai.organization = config.OPENAI_ORGANIZATION_ID 
openai.api_key      = config.OPENAI_API_KEY


def Ask_ChatGPT(message):
    
    # 応答設定
    completion = openai.ChatCompletion.create(
                 model    = "gpt-3.5-turbo",     # モデルを選択
                 messages = [{
                            "role":"user",       # 役割
                            "content":message,   # メッセージ 
                            }],
    
                 max_tokens  = 1024,             # 生成する文章の最大単語数
                 n           = 1,                # いくつの返答を生成するか
                 stop        = None,             # 指定した単語が出現した場合、文章生成を打ち切る
                 temperature = 0.5,              # 出力する単語のランダム性（0から2の範囲） 0であれば毎回返答内容固定
    )
    
    # 応答
    response = completion.choices[0].message.content
    
    # 応答内容出力
    return response

# 質問内容
print (sys.argv[1])
message = sys.argv[1]

# ChatGPT起動
res = Ask_ChatGPT(message)

# 出力
print(res)

