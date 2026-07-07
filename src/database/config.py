# import streamlit as st

# from supabase import create_client , Client

# supabase: Client = create_client(
#     st.secrets["SUPABASE_URL"],
#     st.secrets["SUPABASE_KEY"]
# )

import streamlit as st
from supabase import create_client, Client

_supabase_url = st.secrets.get("SUPABASE_URL")
_supabase_key = st.secrets.get("SUPABASE_KEY")

if _supabase_url and _supabase_key:
    supabase: Client = create_client(_supabase_url, _supabase_key)
else:
    supabase = None
