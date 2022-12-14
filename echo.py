def echo(text: str, repetitions: int = 8) -> str:
    # imitates a real world echo
    echoed_text = ""
    for i in range (repetitions, 0, -1):
        echoed_text += f"{text[-i:]}\n"
    return f"{echoed_text.lower()}."

if __name__ == "__main__":
    text = input("Yell something: ")
    print(echo(text))