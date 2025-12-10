from pyparsing import Word, alphas, alphanums, nums, quotedString, removeQuotes, oneOf

def parse_query(text):
    # price > 100 AND category = "books"

    field = Word(alphas)
    operator = oneOf("> < = >=")
    number = Word(nums)
    string = quotedString.setParseAction(removeQuotes)

    # бір шарт: price > 100
    condition = field("field") + operator("op") + (number("num") | string("str"))

    result = condition.parseString(text)

    field = result["field"]
    op = result["op"]
    value = result.get("num") or result.get("str")

    # сан болса int қыламыз
    if value.isdigit():
        value = int(value)

    # предикат функциясын қайтарамыз
    def predicate(item):
        if op == ">": return item[field] > value
        if op == "<": return item[field] < value
        if op == "=": return item[field] == value
        if op == ">=": return item[field] >= value

    return predicate
