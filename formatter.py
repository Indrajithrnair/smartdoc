import shutil
from agent_setup import agent


def apply_instruction(in_path: str, instruction: str, out_path: str):
    import shutil
    shutil.copy(in_path, out_path)

    user_input = f"{instruction}. File path: {out_path}"

    print("=== AGENT INPUT ===")
    print(user_input)

    response = agent.run({"input": user_input})

    print("=== AGENT INPUT ===")
    print(user_input)

    return response
