from exceptions import *

def split_by_words(line):
    '''
    Функция прнимает строку, делит ее на слова и возвращает список этих
    слов. Если в строке встречаются двойные кавычки, подстрока в них
    выделяется в отдельное слово.
    Пример:
        split_by_words('12 34 "qw er tr" 45')
        возвращает 
        ['12', '34', 'qw er tr', '45']

    '''

    quoteStartPos = line.find('"')
    if ( quoteStartPos == -1 ):
        return line.split()

    quoteEndPos = line.find('"', quoteStartPos+1)
    if ( quoteEndPos == -1 ):
        raise ConfFileError("Нечетное количество кавычек")
        
    wordsBeforeQuote   = line[0:quoteStartPos].split()
    wordsBetweenQuotes = [line[quoteStartPos+1:quoteEndPos]]
    wordsAfterQuote    = split_by_words(line[quoteEndPos+1:])

    words = wordsBeforeQuote + wordsBetweenQuotes + wordsAfterQuote

    return words


def read_until_empty_line(firstLine, fileStream):
   text = firstLine.strip()
   for line in fileStream:
       line = line.strip()
       if not line:
           return text
       else:
           text += " " + line

