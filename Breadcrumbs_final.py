import re
ignore = ["the", "of", "in", "from", "by",
          "with", "and", "or", "for", "to", "at", "a"]
last_element = ['.htm', '.index', '.php', '.asp']
home = '<a href="/">HOME</a>'


def a_href(item, path):
    if len(item) > 30:
        item = acronym(item)
    else:
        if len(item.split('-')) > 1:
            item = item.replace("-", " ")
    return '<a href="/' + path + '/">' + item.upper() + '</a>'


def middle_set(levels):
    n = 0
    path = ''
    for x in levels:
        if n > 0:
            path = path + '/' + x
        else:
            path = x
        temp = a_href(x, path)
        levels[n] = temp
        n += 1
    return levels


def acronym(long):
    temp = long.split('-')
    acronym = []
    remove = []
    for x in temp:
        if x in ignore:
            remove.append(x)
    for x in remove:
        temp.remove(x)
    for x in temp:
        acronym.append(x[0])
    final = ''.join(acronym)
    return final.upper()


def test_ending(levels):
    x = re.split('\.|\?|#', levels[-1])
    if len(x) > 1:
        levels.pop(-1)
        levels.append(x[0])
    if levels[-1] == 'index' or levels[-1] == '':
        levels.pop(-1)
    return levels


def last(levels):
    if len(levels[-1]) > 30:
        levels[-1] = acronym(levels[-1])
    elif len(levels[-1].split('-')) > 1:
        levels[-1] = levels[-1].replace("-", " ")
    last_url = '<span class="active">' + levels[-1].upper() + '</span>'
    return last_url


def check_url(levels):
    remove = []
    for x in levels:
        if x == '' or x == 'https:' or x == 'http:':
            remove.append(x)
    for x in remove:
        levels.remove(x)
    return levels


def generate_bc(url, separator):
    levels = url.split('/')
    test_ending(levels)
    check_url(levels)
    ending = last(levels)
    if len(levels) == 1:
        return '<span class="active">' + 'HOME' + '</span>'
    levels.pop(0)
    levels.pop(-1)
    middle_set(levels)
    middle = separator.join(levels)
    if middle == '':
        return home + separator + ending
    breadcrumb = home + separator + middle + separator + ending
    return breadcrumb
