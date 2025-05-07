import subprocess

def rosNodesList():
    return subprocess.getoutput("ros2 node list")

def coordinateMapping(generatedLocation: str):
    ros2AgentMap = {
        "bench": (1.0, 2.0, 0),
        "cube": (2.0, 3.0, 90),
        "goal zone": (0.5, 1.5, 180)
    }
    generatedCoordinates = ros2AgentMap.get(location.lower())
    return f"x: {generatedCoordinates[0]}, y: {generatedCoordinates[1]}, theta: {generatedCoordinates[2]}" if generatedCoordinates else f"Unknown location: {generatedLocation}"

def ros2GoalMovement(xGoalState: float, yGoalState: float, degreeGoalValue: float):
    generatedCommandValue = (
        f"ros2 action send_goal /navigate_to_pose nav2_msgs/action/NavigateToPose "
        f"'{{\"pose\": {{\"pose\": {{\"position\": {{\"x\": {xGoalState}, \"y\": {yGoalState}, \"z\": 0.0}}, "
        f"\"orientation\": {{\"z\": 0.0, \"w\": 1.0}}}}}}}}'"
    )
    return subprocess.getoutput(generatedCommandValue)

def cameraRotation():
    return "Camera rotated 360°. Detected cube and bench nearby."

def generatedSystemReport():
    return "Battery: 76%, CPU: 42%, Navigation: OK, Cameras: OK"
