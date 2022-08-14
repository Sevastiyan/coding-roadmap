

def main(): 
    print(convert("String to convert", "camel"))


def convert(text: str, style: str):

    match style: 
        case "camel":
            return camel(text)
        case "snake":
            return snake(text)

    return 


def camel(text:str): 
    return text


def snake(text:str): 
    return


if __name__ == "__main__": 
    main()