from app.memory.memory_manager import (
    memory
)

while True:

    user_input = input(
        "\nYou: "
    )

    if user_input.lower() == "exit":
        break

    memory.add_user_message(
        user_input
    )

    print(
        "\nCurrent Memory:\n"
    )

    for msg in memory.get_history():

        print(
            f"{msg['role']}: "
            f"{msg['content']}"
        )