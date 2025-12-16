from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .schemas import Profile, Skill, Project

app = FastAPI(
    title="Developer Portfolio API",
    description="Backend API for Personal Developer Portfolio",
    version="1.0.0"
)

# CORS Configuration
# 개발 편의를 위해 모든 출처(*)를 허용하지만, 프로덕션에서는 구체적인 도메인을 지정하는 것이 좋습니다.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy Data (In-memory database simulation)
portfolio_data = Profile(
    name="DevOps Engineer",
    bio="Full Stack Developer specialized in Kubernetes, FastAPI, and Vue.js.",
    skills=[
        Skill(name="Python (FastAPI)", proficiency=95),
        Skill(name="Kubernetes", proficiency=90),
        Skill(name="Vue.js", proficiency=85),
        Skill(name="Docker", proficiency=90),
        Skill(name="CI/CD", proficiency=80),
    ],
    projects=[
        Project(
            title="K8s Portfolio App",
            description="A full-stack portfolio app deployed on Kubernetes.",
            link="https://github.com/example/k8s-portfolio"
        ),
        Project(
            title="Microservices Monitor",
            description="Real-time monitoring dashboard for microservices.",
            link="https://github.com/example/monitor-dashboard"
        )
    ]
)

@app.get("/health", tags=["System"])
async def health_check():
    """
    Kubernetes Liveness/Readiness Probe Endpoint
    """
    return {"status": "ok"}

@app.get("/api/profile", response_model=Profile, tags=["Portfolio"])
async def get_profile():
    """
    Returns the developer profile data including skills and projects.
    """
    return portfolio_data