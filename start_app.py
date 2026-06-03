import subprocess
import sys

cmd = [
    sys.executable,
    "-m",
    "streamlit",
    "run",
    "app.py",
    "--server.port",
    "8503"
]

print("Starting Streamlit app...")
print("Command:", " ".join(cmd))

result = subprocess.run(cmd, cwd="f:\\实训一\\RAG-QA-System---2405030227", capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)
print("Return code:", result.returncode)
