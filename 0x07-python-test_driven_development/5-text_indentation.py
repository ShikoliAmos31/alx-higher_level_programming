#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'

    :param text: input text (must be a string)
    :type text: str
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']
    start_index = 0

    for i in range(len(text)):
        if text[i] in new_line_chars:
            print(text[start_index:i + 1].strip())
            print()
            start_index = i + 1

    if start_index < len(text):
        print(text[start_index:].strip())

# Example usage
text_indentation("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
Plus semper voluptatis? Teneo, inquit, finem illi videri nihil dolere. \
Transfer idem ad modestiam vel temperantiam, quae est moderatio cupiditatum \
rationi oboediens. Si id dicis, vicimus. Inde sermone vario sex illa a Dipylo \
stadia confecimus. Sin aliud quid voles, postea. Quae animi affectio suum \
cuique tribuens atque hanc, quam dico. Utinam quidem dicerent alium alio \
beatiorem! Iam ruinas videres""")
