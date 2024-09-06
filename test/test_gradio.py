import gradio as gr
import numpy as np

def sepia(image):
    # 处理图片
    sepia_filter = np.array([
        [0.393, 0.769, 0.189],
        [0.349, 0.686, 0.168],
        [0.272, 0.534, 0.131]
    ])
    sepia_image = image.dot(sepia_filter.T)
    sepia_image = np.clip(sepia_image, 0, 255).astype(np.uint8)
    return sepia_image
    # 上面是处理图片的函数，其中sepia_filter是sepia滤镜，sepia_image是处理后的图片，
    # clip是裁剪函数，astype是转换为uint8类型
iface = gr.Interface(fn=sepia, inputs="image", outputs="image")


iface.launch()