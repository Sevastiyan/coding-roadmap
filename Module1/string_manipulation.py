import re

def main(): 
    print(convert("String, to convert!", "camel"))
    print(convert("Another String to convert", 'snake'))
    print(convert("hello, Kebab World", "kebab"))
    print(convert("Pascal text to convert.", "pascal"))
    print(convert("Upper Case snake", "uppercasesnake"))



def convert(text: str, style: str):

    sanitised_string = re.sub(r'[^\w\s]', '', text)
    text_array = list(sanitised_string.split(" "))

    match style: 
        case "camel":
            return camel(text_array)
        case "snake":
            return snake(text_array)
        case "kebab":
            return kebab(text_array)
        case "pascal":
            return pascal(text_array)
        case "uppercasesnake":
            return upper_case_snake(text_array)

    return 


def camel(rest): 
    first = [rest[0].lower()]
    rest = list(map(lambda i: i.title(), rest[1:]))

    return "".join(first + rest)


def snake(text): 
    x = list(map(lambda i: i.lower(), text))
    
    return "_".join(x)


def kebab(text:list):
    x = list(map(lambda i: i.lower(), text))

    return "-".join(x)


def pascal(text:list):
    x = [i.title() for i in text]
    
    return ''.join(x)


def upper_case_snake(text:list):
    x = [i.upper() for i in text]
    
    return '_'.join(x)


if __name__ == "__main__": 
    main()