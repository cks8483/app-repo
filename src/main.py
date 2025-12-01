from flask import Flask, jsonify

app = Flask(__name__)


# 지금은 메모 데이터를 코드 안에 하드코딩합니다.
NOTES = [
    {"id": 1, "content": "첫 번째 메모: Dockerfile 만들기"},
    {"id": 2, "content": "두 번째 메모: Kubernetes 매니페스트 작성"},
    {"id": 3, "content": "세 번째 메모: ArgoCD와 연동하기"},
]

@app.route("/")
def index():
    """메인 페이지: 환영 메시지를 보여줍니다."""
    return "<h1>웹 메모장 v1.0</h1><p>메모 목록을 보려면 /notes 로 접속하세요.</p>"

@app.route("/notes")
def get_notes():
    """JSON 형태로 모든 메모를 반환합니다."""
    return jsonify(NOTES)

if __name__ == "__main__":
    # 5000번 포트에서 서버를 실행합니다.
    app.run(host="0.0.0.0", port=5000)