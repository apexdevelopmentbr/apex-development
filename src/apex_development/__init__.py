"""
Apex Development
Biblioteca interna corporativa compartilhada da Apex para projetos Python.

:author: v-emanuel.pereira@apexgroup.com
"""

from .client.secretmanager import SecretManagerClient
from .http.response import Response
from .logging import logger

__version__ = "0.1.0"

__all__ = [
    "SecretManagerClient",
    "Response",
    "logger"
]