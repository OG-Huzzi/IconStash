@echo off
echo ===================================================
echo Google Search Console MCP Authentication
echo ===================================================
"C:\Users\DELL\.local\bin\uvx.exe" --with mcp-search-console python "%~dp0authenticate_gsc.py"
pause
