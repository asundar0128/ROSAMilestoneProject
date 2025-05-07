from agent import agent

def main():
    print("ROSA LangChain Agent Ready. Type 'exit' to quit.")
    while True:
        generatedQueryValue = input("You: ")
        if generatedQueryValue.lower() in ["exit", "quit"]:
            break
        generatedResponseValue = agent.run(generatedQueryValue)
        print(f"ROSA: {generatedResponseValue}\n")

if __name__ == "__main__":
    main()
