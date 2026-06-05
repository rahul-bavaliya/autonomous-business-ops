from app.llm.llm_service import llm_service


def main():

    print("\n=== NVIDIA NIM Research Assistant ===\n")

    while True:

        question = input("Ask a question (or type exit): ")

        if question.lower() == "exit":
            break

        for temp in [0.0, 0.3, 0.7, 1.0]:
            print(f"\nTemperature: {temp}")

            answer = llm_service.ask(
                question=question,
                temperature=temp
            )
            print("\nResponse:\n")
            print(answer)
            print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()