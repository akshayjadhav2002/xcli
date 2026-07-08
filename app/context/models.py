from dataclasses import dataclass


@dataclass
class Context:
    """
    Snapshot of the current machine state.
    """

    # User
    user: str
    home: str

    # Operating System
    os: str
    hostname: str
    shell: str

    # File System
    cwd: str
    files: list[str]

    # Git
    git_repo: bool
    git_branch: str | None

    # Python
    python_version: str
    virtualenv: str | None

    # System
    cpu_usage: float
    memory_usage: float
    disk_usage: float

    # Processes
    running_processes: list[str]

    # Network
    network_interfaces: list[str]