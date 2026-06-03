import subprocess
import os

def build_exe():
    """使用PyInstaller打包Streamlit应用"""
    print("=" * 50)
    print("开始打包RAG问答系统...")
    print("=" * 50)
    
    # 确保pyinstaller已安装
    try:
        subprocess.run(
            ["pyinstaller", "--version"],
            check=True,
            capture_output=True,
            text=True
        )
    except subprocess.CalledProcessError:
        print("安装PyInstaller...")
        subprocess.run(
            ["pip", "install", "pyinstaller"],
            check=True
        )
    
    # 构建命令
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name=RAG-QA-System",
        "--add-data=documents;documents",
        "--hidden-import=langchain",
        "--hidden-import=langchain_ollama",
        "--hidden-import=langchain_chroma",
        "--hidden-import=chromadb",
        "--hidden-import=streamlit",
        "--hidden-import=pypdf2",
        "--hidden-import=python-docx",
        "--hidden-import=tiktoken",
        "--hidden-import=requests",
        "app.py"
    ]
    
    print(f"执行命令: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(
            cmd,
            check=True,
            capture_output=True,
            text=True
        )
        print("打包成功！")
        print("输出目录: dist/RAG-QA-System.exe")
        
    except subprocess.CalledProcessError as e:
        print(f"打包失败: {e.stderr}")
        return False
    
    return True

def create_startup_script():
    """创建启动脚本"""
    startup_content = '''@echo off
echo 启动RAG问答系统...
echo 请确保已安装Ollama并启动服务
echo 模型要求: deepseek-r1:7b 和 nomic-embed-text
echo.
dist\RAG-QA-System.exe
pause
'''
    
    with open("start_app.bat", "w", encoding="utf-8") as f:
        f.write(startup_content)
    print("已创建启动脚本: start_app.bat")

if __name__ == "__main__":
    success = build_exe()
    if success:
        create_startup_script()
        print("\n打包完成！")
        print("使用方法:")
        print("1. 确保已安装Ollama并下载模型")
        print("2. 运行 start_app.bat 启动应用")
        print("3. 打开浏览器访问显示的URL")