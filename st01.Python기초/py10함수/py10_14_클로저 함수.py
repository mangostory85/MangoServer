def outer_func(tag):
    text = "Some text"
    tag = tag

    def inner_func():
        str = "<%s> %s </%s>" % (tag, text, tag)
        return str
    return inner_func


hi_func = outer_func("hi")
p_func = outer_func("p")

print(hi_func())
print(p_func())
