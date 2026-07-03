#!/usr/bin/env bash
# Reads API keys from the repo-root .env, exports them for the shell, and writes
# homework/module-03/.env for docker compose variable substitution.
#
#   ./setup-secrets.sh          # prepare docker compose .env
#   source ./setup-secrets.sh   # export vars in current shell too

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
ROOT_ENV_FILE="$REPO_ROOT/.env"
COMPOSE_ENV_FILE="$SCRIPT_DIR/.env"

_fail() {
  echo "ERROR: $1" >&2
  if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    exit 1
  else
    return 1
  fi
}

# ── helpers ────────────────────────────────────────────────────────────────────

_read_env_var() {
  local key="$1"
  if [[ -f "$ROOT_ENV_FILE" ]]; then
    grep -E "^${key}=" "$ROOT_ENV_FILE" | head -n1 | cut -d'=' -f2- | tr -d '"' | tr -d "'" || true
  fi
}

_prompt_if_empty() {
  local var_name="$1"
  local prompt_label="$2"
  local current_val="${!var_name:-}"
  if [[ -z "$current_val" ]]; then
    read -rsp "${prompt_label}: " current_val
    echo
  fi
  echo "$current_val"
}

# ── Gemini API key (required) ──────────────────────────────────────────────────

GEMINI_API_KEY="${GEMINI_API_KEY:-$(_read_env_var GEMINI_API_KEY)}"
GEMINI_API_KEY="$(_prompt_if_empty GEMINI_API_KEY "GEMINI_API_KEY (required)")"

if [[ -z "$GEMINI_API_KEY" ]]; then
  _fail "GEMINI_API_KEY is required. Add it to ${ROOT_ENV_FILE}."
fi

export GEMINI_API_KEY
SECRET_GEMINI_API_KEY="$(echo -n "$GEMINI_API_KEY" | base64)"
export SECRET_GEMINI_API_KEY

# ── OpenAI API key (required for flow 3) ──────────────────────────────────────

OPENAI_API_KEY="${OPENAI_API_KEY:-$(_read_env_var OPENAI_API_KEY)}"
OPENAI_API_KEY="$(_prompt_if_empty OPENAI_API_KEY "OPENAI_API_KEY (required for flow 3)")"

SECRET_OPENAI_API_KEY="$(echo -n "$OPENAI_API_KEY" | base64)"
export SECRET_OPENAI_API_KEY

# ── Tavily API key (optional) ──────────────────────────────────────────────────

TAVILY_API_KEY="${TAVILY_API_KEY:-$(_read_env_var TAVILY_API_KEY)}"

if [[ -z "$TAVILY_API_KEY" ]]; then
  read -rsp "TAVILY_API_KEY (optional, press Enter to skip): " TAVILY_API_KEY
  echo
fi

SECRET_TAVILY_API_KEY="$(echo -n "$TAVILY_API_KEY" | base64)"
export SECRET_TAVILY_API_KEY

# ── Kestra basic auth ───────────────────────────────────────────────────────────

KESTRA_USERNAME="${KESTRA_USERNAME:-$(_read_env_var KESTRA_USERNAME)}"
KESTRA_USERNAME="${KESTRA_USERNAME:-admin@kestra.io}"

KESTRA_PASSWORD="${KESTRA_PASSWORD:-$(_read_env_var KESTRA_PASSWORD)}"
KESTRA_PASSWORD="${KESTRA_PASSWORD:-Admin1234!}"

export KESTRA_USERNAME KESTRA_PASSWORD

# ── docker compose .env ───────────────────────────────────────────────────────

cat > "$COMPOSE_ENV_FILE" <<EOF
GEMINI_API_KEY=${GEMINI_API_KEY}
SECRET_GEMINI_API_KEY=${SECRET_GEMINI_API_KEY}
SECRET_OPENAI_API_KEY=${SECRET_OPENAI_API_KEY}
SECRET_TAVILY_API_KEY=${SECRET_TAVILY_API_KEY}
KESTRA_USERNAME=${KESTRA_USERNAME}
KESTRA_PASSWORD=${KESTRA_PASSWORD}
EOF

# ── Summary ────────────────────────────────────────────────────────────────────

echo "Loaded from ${ROOT_ENV_FILE}"
echo "Wrote ${COMPOSE_ENV_FILE} for docker compose"
echo "  GEMINI_API_KEY        (plaintext)"
echo "  SECRET_GEMINI_API_KEY (base64)"
[[ -n "$OPENAI_API_KEY" ]]  && echo "  SECRET_OPENAI_API_KEY (base64)" || echo "  SECRET_OPENAI_API_KEY (empty — flow 3 will fail)"
[[ -n "$TAVILY_API_KEY" ]]  && echo "  SECRET_TAVILY_API_KEY (base64)" || echo "  SECRET_TAVILY_API_KEY (empty — Tavily disabled)"
echo "  KESTRA_USERNAME       ${KESTRA_USERNAME}"
echo "  KESTRA_PASSWORD       (hidden)"
