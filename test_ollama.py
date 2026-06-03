import requests
import json

def test_ollama_connection():
    print("=" * 50)
    print("测试 Ollama API 连接")
    print("=" * 50)
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            print("✓ Ollama 服务连接成功")
            data = response.json()
            models = data.get("models", [])
            if models:
                print(f"已下载的模型列表 ({len(models)}个):")
                for model in models:
                    print(f"  - {model['name']} (大小: {model.get('size', '未知')})")
            else:
                print("提示: 尚未下载任何模型，请运行 'ollama pull deepseek-r1:7b'")
            return True
        else:
            print("✗ Ollama 服务响应异常")
            return False
    except requests.exceptions.ConnectionError:
        print("✗ 无法连接到 Ollama 服务，请确保已启动 Ollama")
        print("  启动命令: ollama serve")
        return False
    except requests.exceptions.Timeout:
        print("✗ 请求超时")
        return False

def test_model_inference():
    print("\n" + "=" * 50)
    print("测试模型推理")
    print("=" * 50)
    try:
        payload = {
            "model": "deepseek-r1:7b",
            "prompt": "Hello! 请介绍一下你自己。",
            "stream": False
        }
        response = requests.post("http://localhost:11434/api/generate", 
                                json=payload, timeout=60)
        if response.status_code == 200:
            data = response.json()
            print("✓ 模型推理成功")
            print("响应内容:")
            print(data.get("response", "无响应内容"))
            return True
        else:
            print(f"✗ 模型推理失败，状态码: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ 模型推理异常: {str(e)}")
        return False

if __name__ == "__main__":
    print("Ollama API 测试脚本")
    print("=" * 50)
    
    conn_ok = test_ollama_connection()
    
    if conn_ok:
        test_model_inference()
    
    print("\n测试完成！")