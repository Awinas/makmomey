from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import json, uuid

BASE=Path(__file__).resolve().parent.parent
MEMORY=BASE/"backend"/"memory.json"
if not MEMORY.exists(): MEMORY.write_text("[]",encoding="utf-8")

app=FastAPI(title="Mak Momey AI Local Prototype")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

class ChatRequest(BaseModel):
    message:str
    history:list[dict]=[]
class MemoryRequest(BaseModel):
    text:str

def get_mem(): return json.loads(MEMORY.read_text(encoding="utf-8"))
def put_mem(x): MEMORY.write_text(json.dumps(x,ensure_ascii=False,indent=2),encoding="utf-8")

def demo_reply(msg):
    m=msg.lower()
    if any(x in m for x in ["makan","mkn","lunch","dinner"]):
        return "Dah makan dah ka min? Jangan dok sibuk kerja sampai lupa makan naa 😘"
    if any(x in m for x in ["balik","sampai rumah"]):
        return "Ooo dah balik dah ka min 😘 Rehat dulu naa, penat tu."
    if any(x in m for x in ["kerja","project","projek"]):
        return "Ok min, buat elok2 naa. Jangan dok paksa sangat diri tu 🤲"
    if any(x in m for x in ["mak","rindu"]):
        return "Hehe minnn 😘 Mak dengaq ni. Cerita la, pa jadi?"
    return "Ok minnn 😘 Cerita kat mak, pa jadi ni?"

@app.get("/health")
def health(): return {"ok":True,"mode":"demo","memory_items":len(get_mem())}

@app.post("/api/chat")
def chat(req:ChatRequest):
    if not req.message.strip(): return {"reply":"Min, taip dulu naa 😘","mode":"demo"}
    return {"reply":demo_reply(req.message),"mode":"demo"}

@app.get("/api/memory")
def memory(): return {"items":get_mem()}

@app.post("/api/memory")
def add_memory(req:MemoryRequest):
    if not req.text.strip(): return {"error":"empty"}
    x=get_mem(); item={"id":str(uuid.uuid4()),"text":req.text.strip()}; x.append(item); put_mem(x); return item

@app.delete("/api/memory/{mid}")
def delete_memory(mid:str):
    put_mem([x for x in get_mem() if x["id"]!=mid]); return {"ok":True}

@app.post("/api/tts-demo")
def tts_demo(): return {"ok":True,"mode":"browser"}
