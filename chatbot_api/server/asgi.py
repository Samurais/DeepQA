"""
ASGI config for chatbot_rest project.

Used for WebSockets
"""

import os
import channels.asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
channel_layer = channels.asgi.get_channel_layer()
