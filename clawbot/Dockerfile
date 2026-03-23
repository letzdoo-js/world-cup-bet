FROM python:3.12-slim

RUN pip install --no-cache-dir nanobot-ai

# Nanobot workspace lives in /root/.nanobot/workspace
ENV NANOBOT_DIR=/root/.nanobot
RUN mkdir -p "$NANOBOT_DIR/workspace/skills"

# Copy skills (baked into image)
COPY skills/clawbot-tutor/ $NANOBOT_DIR/workspace/skills/clawbot-tutor/
COPY skills/clawbot-quiz/  $NANOBOT_DIR/workspace/skills/clawbot-quiz/

# Workspace data (curriculum, progress) is mounted via docker-compose
CMD ["nanobot", "gateway"]
