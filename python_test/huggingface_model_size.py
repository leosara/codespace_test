import os
from typing import Optional
from huggingface_hub import model_info, ModelInfo

def format_size(size: int) -> str:
    """格式化文件大小为易读格式"""
    if size < 1024 * 10:
        return f"{size} bytes"
    elif size < 1024 ** 2:
        return f"{size / 1024:.1f} KB"
    elif size < 1024 ** 3:
        return f"{size / (1024 ** 2):.1f} MB"
    return f"{size / (1024 ** 3):.1f} GB"

def get_model_info(model_name: str, proxy: Optional[str] = None) -> ModelInfo:
    """获取模型信息，可选设置代理"""
    if proxy:
        os.environ["HTTP_PROXY"] = proxy
        os.environ["HTTPS_PROXY"] = proxy
    return model_info(model_name, files_metadata=True)

def print_model_files(info: ModelInfo) -> int:
    """打印模型文件信息并返回总大小"""
    total_size = 0
    for file in info.siblings:
        if file.size is not None:
            print(f"{file.rfilename}: {format_size(file.size)}")
            total_size += file.size
    return total_size

def main():
    # 配置参数
    MODEL_NAME = "deepseek-ai/DeepSeek-V3-0324"
    # PROXY = "http://127.0.0.1:1950"  # 取消注释以启用代理
    
    try:
        info = get_model_info(MODEL_NAME)  # 可传入PROXY作为第二个参数
        total_size = print_model_files(info)
        print(f"\nTotal Size: {format_size(total_size)}")
        print(f"({total_size / (1024 ** 2):.1f} MB / {total_size / (1024 ** 3):.1f} GB)")
    except Exception as e:
        print(f"获取模型信息失败: {e}")

if __name__ == "__main__":
    main()