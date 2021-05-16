from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.headless = True
assert opts.headless
l1 = []
l2 = []
d1 = dict()
d2=dict()
def search_1(a, b, c):
    '''

    :param a: movie name
    :param b: empty list for future use
    :param c: empty dict for future use
    :return:
    '''
    browser = Chrome(options=opts)
    browser.get('https://duckduckgo.com')
    search_form = browser.find_element_by_id('search_form_input_homepage')
    search_form.send_keys(a + ' кинопоиск')
    search_form.submit()
    browser.find_element_by_id('r1-0').click()
    browser.find_element_by_class_name('styles_link__21QPj').click()
    results = browser.find_elements_by_class_name('gray')

    for r in results:
        r = r.text
        r = r.strip()
        r  = r.lower()
        if r == '':
            continue
        if r in b:
            continue
        else:
            b.append(r)
    browser.close()
    c[a] = b
    return c


def choice1(res1, res2, name1, name2):
    s = []
    for i in res1[name1]:
        if i in s:
            continue
        else:
            s.append(i)
    for i in res2[name2]:
        if i in s:
            continue
        else:
            s.append(i)
    return(s)


def choice2(res1, res2, name1, name2):
    s = []
    for i in res2[name2]:
        if i in res1[name1]:
            s.append(i)
        else:
            continue
    return s


def choice3(res1, res2, name1, name2):
    s = []
    for i in res1[name1]:
        if i in res2[name2]:
            continue
        else:
            s.append(i)
    return s


def choice4(res1, res2, name1, name2, act1, act2):
    s1 = []
    s2 = []
    for i in res1[name1]:
        i = i.split(' ')

        if len(i)< 2:
            continue
        else:
            s1.append(i[1])
    for i in res2[name2]:
        i = i.split(' ')
        if len(i) < 2:
            continue
        else:
            s2.append(i[1])
    if (not act1 in s1 and act1 in s2) and (not act2 in s1 and not act2 in s2):
        return 'No such actors in movies'
    if act1 in s1 and act1 in s2:
        return name1 + ',' + name2
    if act2 in s1 and act1 in s2:
        return name1 + ',' + name2
    if (act1 in s1 and act2 in s2) or (act1 in s2 and act2 in s1):
        return name1 + ',' + name2
    if act1 in s1 or act2 in s1:
        return name1
    else:
        return name2


def choice5(res1, res2, name1, name2, act1, act2):
    s1 = []
    s2 = []
    for i in res1[name1]:
        i = i.split(' ')
        if len(i)< 2:
            continue
        else:
            s1.append(i[1])
    for i in res2[name2]:
        i = i.split(' ')
        if len(i) < 2:
            continue
        else:
            s2.append(i[1])
    if act1 in s1 and act2 in s1:
        if act1 in s2 and act2 in s2:
            return name1 + ', ' + name2
        else:
            return name2
    if act1 in s2 and act2 in s2:
        return name2
    else:
        return 'Actors played in different films'


def choice6(res1, res2, name1, name2, act1, act2):
    s1 = []
    s2 = []
    for i in res1[name1]:
        i = i.split(' ')
        if len(i)< 2:
            continue
        else:
            s1.append(i[1])
    for i in res2[name2]:
        i = i.split(' ')
        if len(i) < 2:
            continue
        else:
            s2.append(i[1])
    if act1 in s1 and not act2 in s1:
        return name1
    if act1 in s2 and not act2 in s2:
        return name2
    else:
        return 'Actors played in the same movie'

def main(res1, res2, name1, name2):
    '''

    :param res1: movie 1 dict
    :param res2: movie 2 dict
    :param name1: 1-movie name
    :param name2: 2-movie name
    :return:
    '''
    print('Choices\n1-cast of both films\n2-crew of both films\n3-crew of only first film\n4-film name by crewmate name\n5-film where were both crewmates\n6-film where were only first crewmate\n7-exit')
    choice = int(input('Write choice number '))
    if choice == 1:
        print(choice1(res1, res2, name1, name2))
        main(res1, res2, name1, name2)
    if choice == 2:
        print(choice2(res1, res2, name1, name2))
        main(res1, res2, name1, name2)
    if choice == 3:
        print(choice3(res1, res2, name1, name2))
        main(res1, res2, name1, name2)
    if choice == 4:
        act1 = input('Second name of first actor ').strip()
        act1 = act1.lower()
        act2 = input('Second name of second actor ').strip()
        act2 = act2.lower()
        print(choice4(res1, res2, name1, name2,  act1, act2))
        main(res1, res2, name1, name2)
    if choice == 5:
        act1 = input('Second name of first actor ').strip()
        act1 = act1.lower()
        act2 = input('Second name of second actor ').strip()
        act2 = act2.lower()
        print(choice5(res1, res2, name1, name2,  act1, act2))
        main(res1, res2, name1, name2)
    if choice == 6:
        act1 = input('Second name of first actor ').strip()
        act1 = act1.lower()
        act2 = input('Second name of second actor ').strip()
        act2 = act2.lower()
        print(choice6(res1, res2, name1, name2, act1, act2))
        main(res1, res2, name1, name2)
    if choice == 7:
        exit()

name1 = input('First movie ')
res1 = search_1(name1, l1, d1)
name2 = input('Second movie ')
res2 = search_1(name2, l2, d2)
main(res1, res2, name1, name2)




