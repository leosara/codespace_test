import torch
import time

# 检查CUDA是否可用
if not torch.cuda.is_available():
    print("CUDA不可用，请检查GPU驱动和PyTorch安装")
    exit()

# 设置矩阵大小（增大这个值可以看到更明显的差异）
size = 1024  # 创建一个10000x10000的矩阵
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 生成测试数据
x = torch.randn(size, size)

# CPU计算
start_time = time.time()
cpu_result = torch.matmul(x, x)
cpu_time = time.time() - start_time
print(f"CPU计算时间: {cpu_time:.2f}秒")

# GPU计算
x_gpu = x.to(device)  # 将数据转移到GPU
torch.cuda.synchronize()  # 等待CUDA操作完成（确保准确计时）

start_time = time.time()
gpu_result = torch.matmul(x_gpu, x_gpu)
torch.cuda.synchronize()  # 等待CUDA操作完成
gpu_time = time.time() - start_time
print(f"GPU计算时间: {gpu_time:.2f}秒")

torch.cuda.empty_cache()

# 验证结果一致性
# 注意：由于浮点数精度问题，这里使用近似比较
max_diff = torch.max(torch.abs(cpu_result - gpu_result.cpu()))
print(f"实际最大差异: {max_diff.item()}")
assert max_diff < 1e-2  # 根据打印值手动调整阈值

# 性能对比
print(f"\n性能提升: {cpu_time / gpu_time:.1f}倍")