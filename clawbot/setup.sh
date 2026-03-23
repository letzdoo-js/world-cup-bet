#!/usr/bin/env bash
set -euo pipefail

# ============================================================
# ClawBot Docker Setup — build + deploy avec auto-restart
# ============================================================
# Usage :
#   chmod +x setup.sh
#   ./setup.sh
#
# Pre-requis :
#   - Docker
#   - config.json rempli (copié depuis config.json.template)
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE_NAME="clawbot"
CONTAINER_NAME="clawbot"
CONFIG_FILE="$SCRIPT_DIR/config.json"
NANOBOT_DIR="/root/.nanobot"

echo "=== ClawBot Docker Setup ==="
echo ""

# --- 1. Check config.json ---
echo "1/3 — Vérification de config.json..."
if [ ! -f "$CONFIG_FILE" ]; then
    echo "   config.json introuvable. Copie du template..."
    cp "$SCRIPT_DIR/config.json.template" "$CONFIG_FILE"
    echo ""
    echo "   IMPORTANT : édite config.json avant de relancer :"
    echo "     nano $CONFIG_FILE"
    echo ""
    echo "   Remplace les placeholders :"
    echo "     - REPLACE_TELEGRAM_BOT_TOKEN"
    echo "     - REPLACE_OPENROUTER_API_KEY"
    echo "     - REPLACE_STUDENT_TELEGRAM_ID"
    echo "     - REPLACE_MENTOR_TELEGRAM_ID"
    echo "     - REPLACE_BRAVE_SEARCH_API_KEY (optionnel)"
    echo ""
    exit 1
fi

# Warn if placeholders are still present
if grep -q "REPLACE_" "$CONFIG_FILE"; then
    echo "   WARNING : config.json contient encore des placeholders REPLACE_*"
    echo "   Édite le fichier avant de continuer :"
    echo "     nano $CONFIG_FILE"
    exit 1
fi
echo "   OK"

# --- 2. Build image ---
echo ""
echo "2/3 — Build de l'image Docker..."
docker build -t "$IMAGE_NAME" "$SCRIPT_DIR"
echo "   OK"

# --- 3. Run container ---
echo ""
echo "3/3 — Lancement du conteneur..."

# Stop and remove existing container if any
if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
    echo "   Arrêt du conteneur existant..."
    docker rm -f "$CONTAINER_NAME" > /dev/null 2>&1
fi

docker run -d \
    --name "$CONTAINER_NAME" \
    --restart unless-stopped \
    -v "$CONFIG_FILE":"$NANOBOT_DIR/config.json":ro \
    "$IMAGE_NAME"

echo "   OK"

echo ""
echo "=== ClawBot lancé ==="
echo ""
echo "  Logs     : docker logs -f $CONTAINER_NAME"
echo "  Stop     : docker stop $CONTAINER_NAME"
echo "  Restart  : docker restart $CONTAINER_NAME"
echo "  Rebuild  : ./setup.sh"
echo ""
