import os
import json
import re 
import time 
import random
import urllib.request
import urllib.error

API_KEY = os.getenv("GEMINI_API_KEY","")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

def generate_email_with_gemini(command):
  if not API_KEY:
    raise RuntimeError("GEMINI _API_KEY is missing")

  prompt = f"""
you are professional gmail email writing assistant 

convet the user's voice command into a professional email

rules:
- do not copy the command literally 
- do not explain anything 
- do not invent names,dates,prices,companies,attachments,or facts 
- keep the email natural and concise 
- include an appropriate greeting and closing 

output exactly:

SUBJECT: <subject>
BODY:
<email body>

User command:
{command}
"""


  url = (
    f"https://generativelanguage.googlepis.com/"
    f"v1beta/models/{MODEL}:generatecontent"
  )
  payload = {
    "contents": [{"parts": [{"text":prompts}]}],
    "generationConfig": {
      "temperature":0.7,
      "maxOutputTokens":800
    }
  }
  req = urllib.request.Request(
    url,
    data=json.dumps(payload).encode(),
    headers={
      "Content-Type":"application/json",
      "x-goog-api-key": API-KEY
    },
    method="POST"
  )

for attempt in range(4):
  try:
    with urllib.request.urlopen(req, timeout=30) as response:
      data = json.loads(response.read().decode())
      



