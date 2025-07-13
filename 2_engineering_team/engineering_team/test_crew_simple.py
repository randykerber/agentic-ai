#!/usr/bin/env python3
"""
Test Lab 2 CrewAI system without Docker code execution
"""
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class SimpleEngineeringTeam():
    """Simple engineering team without code execution for testing"""
    
    agents_config = 'src/engineering_team/config/agents.yaml'
    tasks_config = 'src/engineering_team/config/tasks.yaml'

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'],
            verbose=True,
        )

    @agent  
    def backend_engineer(self) -> Agent:
        # Disabled code execution for testing
        return Agent(
            config=self.agents_config['backend_engineer'],
            verbose=True,
            allow_code_execution=False,  # Disabled for testing
        )
    
    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task']
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'],
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=[self.engineering_lead(), self.backend_engineer()], 
            tasks=[self.design_task(), self.code_task()], 
            process=Process.sequential,
            verbose=True
        )

def test_lab2():
    """Test Lab 2 CrewAI basic functionality"""
    print("🧪 Testing Lab 2 CrewAI Engineering Team (without Docker)")
    
    inputs = {
        'requirements': 'Create a simple calculator that can add, subtract, multiply and divide two numbers',
        'module_name': 'calculator',
        'class_name': 'Calculator'
    }
    
    try:
        crew = SimpleEngineeringTeam()
        result = crew.crew().kickoff(inputs=inputs)
        print("✅ Lab 2 CrewAI test completed successfully!")
        print(f"📄 Result: {result}")
        return True
        
    except Exception as e:
        print(f"❌ Lab 2 test failed: {e}")
        return False

if __name__ == "__main__":
    test_lab2()