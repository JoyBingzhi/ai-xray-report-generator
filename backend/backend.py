# backend.py
import torch
import clip
from PIL import Image
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM
import os


# CLIP 全局加载模型和文本 embedding
clip_device  = "cpu"
clip_model, preprocess = clip.load("ViT-B/32", device=clip_device, jit=False)

loaded = torch.load("iu_xray_embeddings.pt", map_location=clip_device, weights_only=False)
text_features = loaded[1].float()  # [2069, 512]

df = pd.read_csv("train.csv")
texts = df['report'].tolist()

def retrieve_reports(image_path, topk=2):
    # 1. 读图
    image = Image.open(image_path).convert("RGB")
    image_input = preprocess(image).unsqueeze(0).to(clip_device)

    # 2. 提取 image_features
    with torch.no_grad():
        image_features = clip_model.encode_image(image_input)
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        image_features = image_features.float()

    # 3. 计算余弦相似度
    similarity = image_features @ text_features.T  # [1, 2069]
    similarity = similarity.squeeze(0)  # [2069]


    # 4. top-k
    values, indices = similarity.topk(topk)

    top_reports = []
    for i, score in zip(indices, values):
        top_reports.append({
            "text": texts[i],
            "score": score.item()  # 转为 float
        })

    return top_reports




