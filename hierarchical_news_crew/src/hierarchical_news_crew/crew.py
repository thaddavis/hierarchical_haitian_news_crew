from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Uncomment the following line to use an example of a custom tool
# from hierarchical_news_crew.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
from crewai_tools import ScrapeWebsiteTool

scrape_web_tool = ScrapeWebsiteTool()

@CrewBase
class HierarchicalNewsCrew():
	"""HierarchicalNews crew"""

	@agent
	def reporter_a(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_a'],
			tools=[scrape_web_tool],
			verbose=True
		)

	@agent
	def reporter_b(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_b'],
			tools=[scrape_web_tool],
			verbose=True
		)
	
	@agent
	def reporter_c(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_c'],
			tools=[scrape_web_tool],
			verbose=True
		)
	
	@agent
	def reporter_d(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_d'],
			tools=[scrape_web_tool],
			verbose=True
		)
	
	@agent
	def reporter_e(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_e'],
			tools=[scrape_web_tool],
			verbose=True
		)

	@agent
	def reporter_f(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_f'],
			tools=[scrape_web_tool],
			verbose=True
		)
	
	@agent
	def reporter_g(self) -> Agent:
		return Agent(
			config=self.agents_config['reporter_g'],
			tools=[scrape_web_tool],
			verbose=True
		)

	@agent
	def project_manager(self) -> Agent:
		return Agent(
			config=self.agents_config['project_manager'],
			verbose=True
		)
	
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_file='report.md'
		)
	
	@crew
	def crew(self) -> Crew:
		"""Creates the HierarchicalNewsCrew crew"""
		return Crew(
			agents=[self.reporter_a(), self.reporter_b(), self.reporter_c(), self.reporter_d(), self.reporter_e(), self.reporter_f(), self.reporter_g()], # Automatically created by the @agent decorator
			tasks=[
				self.research_task(),
			], # Automatically created by the @task decorator
			manager_agent=self.project_manager(),
			verbose=True,
			process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)