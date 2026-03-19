from config import load_env
from src import ToolExecutor,HelloAgentsLLM,ReActAgent
from src import search

# --- 工具初始化与使用示例 ---
if __name__ == '__main__':
    if not load_env():
        print("错误:未找到 .env 文件，请检查。")
        exit(1) 
    llm = HelloAgentsLLM()
    tool_executor = ToolExecutor()
    search_desc = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    tool_executor.registerTool("Search", search_desc, search)
    agent = ReActAgent(llm_client=llm, tool_executor=tool_executor)
    question = "MyGo!!!!!是什么？最火的角色是哪一位？"
    agent.run(question)