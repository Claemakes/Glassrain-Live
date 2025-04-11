"""
WSGI application entry point for GlassRain
"""

from glassrain_unified import app
import os

print(f"Current directory: {os.getcwd()}")
print(f"Template directory exists: {os.path.exists('templates')}")
if os.path.exists('templates'):
    print(f"Files in templates directory: {os.listdir('templates')}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))
