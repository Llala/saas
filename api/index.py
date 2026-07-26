# from fastapi import FastAPI  # type: ignore
# from fastapi.responses import PlainTextResponse  # type: ignore
# from openai import OpenAI  # type: ignore
# import os

# app = FastAPI()

# # @app.get("/api/debug")
# # def debug():
# #     return {
# #         "has_key": "OPENAI_API_KEY" in os.environ,
# #         "prefix": os.environ.get("OPENAI_API_KEY", "")[:8],
# #     }

# # @app.get("/api", response_class=PlainTextResponse)
# # def idea():
# #     client = OpenAI()
# #     prompt = [{"role": "user", "content": "Come up with a new business idea for AI Agents"}]
# #     response = client.chat.completions.create(model="gpt-5-nano", messages=prompt)
# #     return response.choices[0].message.content

# @app.get("/")
# def root():
#     return {
#         "version": "2026-07-26-test",
#         "routes": ["/", "/debug"]
#     }

from fastapi import FastAPI

app = FastAPI()

@app.get("/api")
def root():
    return {"version": "DEBUG-12345"}

print("Routes:")
for route in app.routes:
    print(route.path)