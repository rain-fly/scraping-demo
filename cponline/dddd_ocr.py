import ddddocr

# 重新加载模块
det = ddddocr.DdddOcr(det=False, ocr=False)

with open('jigsawImage.png', 'rb') as f:
    target_bytes = f.read()

with open('originalImage.png', 'rb') as f:
    background_bytes = f.read()

res = det.slide_match(target_bytes, background_bytes)

print(res)