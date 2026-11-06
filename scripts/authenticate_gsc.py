import os
import sys
import webbrowser
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

CLIENT_SECRETS_FILE = r"C:\Users\DELL\Downloads\client_secret_959725869432-t498pbq24e7i6cqcbc7dba81o943vqhb.apps.googleusercontent.com.json"
TOKEN_DIR = r"C:\Users\DELL\AppData\Local\mcp-gsc\mcp-gsc"
TOKEN_FILE = os.path.join(TOKEN_DIR, "token.json")
SCOPES = ["https://www.googleapis.com/auth/webmasters"]

class WindowsShellBrowser:
    def open(self, url, new=0, autoraise=True):
        print("\n" + "=" * 70, flush=True)
        print("GOOGLE AUTHENTICATION URL:", flush=True)
        print(url, flush=True)
        print("=" * 70 + "\n", flush=True)
        try:
            os.startfile(url)
            print("Successfully requested Windows to open the browser tab.", flush=True)
        except Exception as e:
            print(f"Could not automatically launch browser: {e}", flush=True)
        return True

def main():
    print("=" * 70, flush=True)
    print("Google Search Console MCP Authenticator", flush=True)
    print("=" * 70, flush=True)

    if not os.path.exists(CLIENT_SECRETS_FILE):
        print(f"Error: Client secrets file not found at: {CLIENT_SECRETS_FILE}", flush=True)
        sys.exit(1)

    webbrowser.register('windows_shell', None, WindowsShellBrowser(), preferred=True)

    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    
    print("Starting local redirect server on localhost (port 0)...", flush=True)
    creds = flow.run_local_server(
        port=0,
        authorization_prompt_message="Please visit this URL to authorize: {url}",
        success_message="Authentication successful! You may close this tab and return to Antigravity."
    )

    os.makedirs(TOKEN_DIR, exist_ok=True)
    with open(TOKEN_FILE, "w") as f:
        f.write(creds.to_json())
    print(f"\n[SUCCESS] Token saved to: {TOKEN_FILE}", flush=True)

    try:
        service = build("searchconsole", "v1", credentials=creds, cache_discovery=False)
        sites = service.sites().list().execute()
        entries = sites.get("siteEntry", [])
        print("\nConnected GSC Sites:", flush=True)
        for entry in entries:
            print(f" - {entry.get('siteUrl')} ({entry.get('permissionLevel')})", flush=True)
    except Exception as e:
        print(f"Notice during verification: {e}", flush=True)

    print("\nAuthentication complete! gscServer MCP is now ready.", flush=True)

if __name__ == "__main__":
    main()
