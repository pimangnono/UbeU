"""
Supabase Client: Shared singleton for all backend database operations.

Usage:
    from server.supabase_client import get_supabase
    db = get_supabase()
    result = db.table("participants").select("*").execute()
"""

import os
from typing import Optional

from supabase import create_client, Client


_client: Optional[Client] = None


def get_supabase() -> Client:
    """Get or create the Supabase client singleton (uses service key for full access)."""
    global _client
    if _client is None:
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_SERVICE_KEY")
        if not url or not key:
            raise RuntimeError(
                "SUPABASE_URL and SUPABASE_SERVICE_KEY environment variables must be set. "
                "Create a Supabase project at https://supabase.com and add credentials to .env"
            )
        _client = create_client(url, key)
    return _client


def reset_client() -> None:
    """Reset the client (for testing)."""
    global _client
    _client = None
