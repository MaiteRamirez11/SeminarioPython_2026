
def calculate(text):
    """Esta funcion calcula el total de líneas, palabras y el promedio."""
    lines = text.split("\n")
    total_lines = len(lines)
    total_words = len(text.split())
    average = total_words / total_lines
    return lines, total_lines, total_words, average


def filter_lines(lines, average):    
    """Esta funcion filtra las líneas que superan el promedio de palabras."""
    long_lines = []
    for line in lines:
        quantity = len(line.split())
        if quantity > average:
            long_lines.append((line,quantity))
    
    return long_lines
