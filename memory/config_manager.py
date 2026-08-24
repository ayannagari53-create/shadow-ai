import json
import os
from pathlib import Path


# ============================================================
# SHADOW AI USER DATA DIRECTORY
# ============================================================

def get_user_data_dir() -> Path:
    """
    Return a writable per-user directory for Shadow AI configuration.
    Windows: %LOCALAPPDATA%\ShadowAI
    """

    local_app_data = os.environ.get("LOCALAPPDATA")

    if local_app_data:
        return Path(local_app_data) / "ShadowAI"

    # Fallback
    return Path.home() / ".shadowai"


CONFIG_DIR = get_user_data_dir()
CONFIG_FILE = CONFIG_DIR / "api_keys.json"


# ============================================================
# CONFIG DIRECTORY
# ============================================================

def ensure_config_dir() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)


def config_exists() -> bool:
    return CONFIG_FILE.exists()


# ============================================================
# API KEY
# ============================================================

def save_api_keys(gemini_api_key: str) -> None:
    ensure_config_dir()

    data: dict = {}

    if CONFIG_FILE.exists():
        try:
            data = json.loads(
                CONFIG_FILE.read_text(encoding="utf-8")
            )
        except Exception:
            data = {}

    data["gemini_api_key"] = gemini_api_key.strip()

    CONFIG_FILE.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8"
    )


def load_api_keys() -> dict:
    if not CONFIG_FILE.exists():
        return {}

    try:
        return json.loads(
            CONFIG_FILE.read_text(encoding="utf-8")
        )

    except Exception as e:
        print(f"❌ Failed to load api_keys.json: {e}")
        return {}


def get_gemini_key() -> str | None:
    return load_api_keys().get("gemini_api_key")


def is_configured() -> bool:
    key = get_gemini_key()
    return bool(key and len(key) > 15)


# ============================================================
# ASSISTANT / USER NAME
# ============================================================

def get_assistant_name() -> str:
    """Return configured assistant name, or SHADOW."""
    return load_api_keys().get(
        "assistant_name",
        "SHADOW"
    ) or "SHADOW"


def get_user_name() -> str:
    """Return configured user name."""
    return load_api_keys().get(
        "user_name",
        ""
    )


def save_assistant_config(
    assistant_name: str,
    user_name: str
) -> None:

    ensure_config_dir()

    data: dict = {}

    if CONFIG_FILE.exists():
        try:
            data = json.loads(
                CONFIG_FILE.read_text(
                    encoding="utf-8"
                )
            )
        except Exception:
            data = {}

    data["assistant_name"] = (
        assistant_name.strip()
        or "SHADOW"
    )

    data["user_name"] = user_name.strip()

    CONFIG_FILE.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )


# ============================================================
# MORNING BRIEF
# ============================================================

def get_brief_enabled() -> bool:
    return load_api_keys().get(
        "morning_brief_enabled",
        True
    )


def save_brief_enabled(
    enabled: bool
) -> None:

    ensure_config_dir()

    data: dict = {}

    if CONFIG_FILE.exists():
        try:
            data = json.loads(
                CONFIG_FILE.read_text(
                    encoding="utf-8"
                )
            )
        except Exception:
            data = {}

    data["morning_brief_enabled"] = enabled

    CONFIG_FILE.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8"
    )