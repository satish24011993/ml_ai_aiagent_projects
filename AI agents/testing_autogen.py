from autogen import AssistantAgent, UserProxyAgent

llm_config = {"model":"gemini-3-flash-preview","api_type":"google", "api_key":"AIzaSyDBBCsNSy6Eu35h1xvH3JvjYrIVtYSFwtE"}

assistant_agent = AssistantAgent("assistant", llm_config=llm_config)

user_proxy_agent = UserProxyAgent("user_proxy",
                                #  human_input_mode="NEVER",
                                #  max_consecutive_auto_reply=10,
                                #  is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
                                 code_execution_config={"work_dir": "coding"})

user_proxy_agent.initiate_chat(assistant_agent, message="Tell me a joke about tech stocks.")