from config import load_env
from src import PlanAndSolveAgent, HelloAgentsLLM

if __name__ == '__main__':
    if not load_env():
        print("错误:未找到 .env 文件，请检查。")
        exit(1) 
    try:
        llm_client = HelloAgentsLLM()
        agent = PlanAndSolveAgent(llm_client)
        question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
        agent.run(question)
    except ValueError as e:
        print(e)