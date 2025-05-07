import os
from langchain.agents import Tool, initialize_agent, AgentType
from langchain_community.chat_models import ChatAnthropic
from langchain_openai import ChatOpenAI
from ros_tools import listRosNodes, semanticToCoords, moveToGoal, rotateCamera, systemReport
import re

def sanitizedValue(generatedNameValue):
    return re.sub(r'[^a-zA-Z0-9_-]', '_', generatedNameValue)

generatedModelType = os.getenv("MODEL_TYPE", "openai").lower()

if generatedModelType == "claude":
    generatedLLMInvocation = ChatAnthropic(model="claude-3-sonnet-20240229", temperature=0)
elif generatedModelType == "gpt4o":
    generatedLLMInvocation = ChatOpenAI(model="gpt-4o", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))
else:
    generatedLLMInvocation = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

generatedToolsValue = [
    Tool(name=sanitizedValue("List_ROS_Nodes"), func=listRosNodes, description="List all active ROS 2 nodes."),
    Tool(name=sanitizedValue("Semantic_To_Coordinates"), func=semanticToCoords, description="Get coordinates for locatio>    Tool(name=sanitizedValue("Move_To_Goal"), func=moveToGoal, description="Send the robot to a target (x, y, theta) usi>    Tool(name=sanitizedValue("Rotate_Camera"), func=rotateCamera, description="Rotate the camera 360° and report what is>    Tool(name=sanitizedValue("System_Report"), func=systemReport, description="Get the robot’s battery, CPU, and sensor >]
     Tool(name=sanitizedValue("Move_To_Goal"), func=moveToGoal, description="Send the robot to a target (x, y, theta) using ROS 2 navigation."),
    Tool(name=sanitizedValue("Rotate_Camera"), func=rotateCamera, description="Rotate the camera 360° and report what is seen."),
    Tool(name=sanitizedValue("System_Report"), func=systemReport, description="Get the robot’s battery, CPU, and sensor status.")
]

generatedAgentValue = initialize_agent(
    tools=generatedToolsValue,
    llm=generatedLLMInvocation,
    generatedAgentValue=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)
