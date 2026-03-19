from .tool_manager import ToolExecutor
from .serp_search import search

__version__ = "0.1.0"  # 版本号，规范项目版本管理
__all__ = ["search", "ToolExecutor"]  # 控制 from hello_agents import * 时导出的内容