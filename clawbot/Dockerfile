FROM python:3.12-slim

RUN pip install --no-cache-dir nanobot-ai

# Nanobot workspace lives in /root/.nanobot/workspace
ENV NANOBOT_DIR=/root/.nanobot
RUN mkdir -p "$NANOBOT_DIR/workspace/skills"

# Copy skills
COPY skills/clawbot-tutor/ $NANOBOT_DIR/workspace/skills/clawbot-tutor/
COPY skills/clawbot-quiz/  $NANOBOT_DIR/workspace/skills/clawbot-quiz/

# Copy workspace files (curriculum + progress)
COPY workspace/curriculum.json $NANOBOT_DIR/workspace/
COPY workspace/progress.json   $NANOBOT_DIR/workspace/

# Config is mounted at runtime via -v
# Default command
CMD ["nanobot", "gateway"]
