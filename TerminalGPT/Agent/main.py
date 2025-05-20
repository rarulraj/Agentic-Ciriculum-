def main():
    print("Terminal Agent Is Ready To Go!")

    while True:
        uI = input("Thought:")

        if uI.lower() in ["exit","quit"]:
            print("Terminal Agent Says Bye!")
            break
        print("Thinking..")
        print(f"Agent:'{uI}' hmmmm interesting...")
if __name__ == "__main__":
    main()
