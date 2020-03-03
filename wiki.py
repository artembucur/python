import wikipedia
wikipedia.set_lang('ru')
search=input('Что искать?\n')
s=wikipedia.page(search)

print(s.references())