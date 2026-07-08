import getpass
import os
import platform
import shutil
import socket
import subprocess
import sys
from pathlib import Path

from app.context.models import Context

try:
    import psutil
except ImportError:
    psutil = None


class ContextService:
    """
    Collects useful information about the current system.
    """

    def collect(self) -> Context:

        cwd = Path.cwd()

        # ------------------------
        # Files
        # ------------------------

        try:
            files = sorted(
                item.name
                for item in cwd.iterdir()
            )
        except Exception:
            files = []

        # ------------------------
        # Git
        # ------------------------

        git_repo = (cwd / ".git").exists()

        git_branch = None

        if git_repo:

            try:
                git_branch = subprocess.check_output(
                    ["git", "branch", "--show-current"],
                    text=True,
                ).strip()

            except Exception:
                pass

        # ------------------------
        # Virtual Environment
        # ------------------------

        virtualenv = os.environ.get("VIRTUAL_ENV")

        # ------------------------
        # Python Version
        # ------------------------

        python_version = platform.python_version()

        # ------------------------
        # CPU / Memory
        # ------------------------

        cpu_usage = 0.0
        memory_usage = 0.0

        if psutil:

            cpu_usage = psutil.cpu_percent(interval=0.1)

            memory_usage = psutil.virtual_memory().percent

        # ------------------------
        # Disk Usage
        # ------------------------

        usage = shutil.disk_usage(cwd)

        disk_usage = (
            usage.used / usage.total
        ) * 100

        # ------------------------
        # Running Processes
        # ------------------------

        running_processes = []

        if psutil:

            for proc in psutil.process_iter(["name"]):

                try:

                    name = proc.info["name"]

                    if name:
                        running_processes.append(name)

                except Exception:
                    continue

        running_processes = sorted(
            set(running_processes)
        )[:20]

        # ------------------------
        # Network Interfaces
        # ------------------------

        network_interfaces = []

        if psutil:

            network_interfaces = list(
                psutil.net_if_addrs().keys()
            )

        return Context(

            # User

            user=getpass.getuser(),

            home=str(Path.home()),

            # OS

            os=platform.system(),

            hostname=socket.gethostname(),

            shell=os.environ.get("SHELL", ""),

            # File System

            cwd=str(cwd),

            files=files,

            # Git

            git_repo=git_repo,

            git_branch=git_branch,

            # Python

            python_version=python_version,

            virtualenv=virtualenv,

            # System

            cpu_usage=cpu_usage,

            memory_usage=memory_usage,

            disk_usage=disk_usage,

            # Processes

            running_processes=running_processes,

            # Network

            network_interfaces=network_interfaces,
        )