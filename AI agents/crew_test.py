from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

reasercher = Agent(
    role = 'Senior Research Analyst',
    goal = "Research cutting-edge AI advancements",
    backstory = "You work at a tech think tank, analysing AI trends.",
    verbose = True, 
    # tools=[SerperDevTool()]
)

writer = Agent(
    role = 'Content Strategist',
    goal = "Create engaging content from research",
    backstory= "You are a skilled writer transforming reasearch into engaging articles.",
    verbose = True
)




task1 = Task(
    description="Analyse AI advancements in 2024 and provide a detailed report",
    expected_output="Research report in bullet points", agent=reasercher
)

task2 = Task(
    description="Write a blog post base on the research report",
    expected_output="Full blog post (at least 4 paragraphs)", agent=writer
)

crew = Crew(
    agents=[reasercher, writer],
    tasks=[task1, task2]
    process=Process.sequential
)

result = crew.kickoff()

print("Final Output: ")
print(result)