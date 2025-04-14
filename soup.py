from bs4 import BeautifulSoup



# if __name__ == '__main__':
#     html_doc = """
#         <html>
#         <head><title>Сказка о трёх богатырях</title></head>
#         <body>
#             <p class="title"><b>Сказка о трёх богатырях</b></p>

#             <p class="story">
#             Давным-давно жили-были три богатыря:
#             <a href="http://example.com/ilya" class="hero" id="link1">Илья Муромец</a>,
#             <a href="http://example.com/alesha" class="hero" id="link2">Алёша Попович</a> и
#             <a href="http://example.com/dobrynya" class="hero" id="link3">Добрыня Никитич</a>.
#             </p>

#             <p class="story">
#             И был у них один противник
#             <a href="http://example.com/dragon" class="antihero" id="link4">Змей Горыныч</a>.
#             </p>

#             <p class="story" name="end">
#             Вот и сказке конец, а кто слушал — молодец!
#             </p>
#         </body>
#         </html>
#         """
#     soup = BeautifulSoup(html_doc, 'lxml') 
#     first_story = soup.find('p', class_='story')
#     link2 = first_story.find(id='link1')
#     print(link2['href'])

price_html = """
<table cellspacing="0" cellpadding="0" border="1">
  <tbody>
    <tr class="even_row">
      <th><p>№ п/п</p></th>
      <th class="armor"><p>Название</p></th>
      <th class="price"><p>Цена</p><p>рублей</p></th>
    </tr>
    <tr class="odd_row">
      <td><p>1.</p></td>
      <td class="armor"><p>Щит</p></td>
      <td class="price"><p>375</p></td>
    </tr>
    <tr class="even_row">
      <td><p>2.</p></td>
      <td class="armor"><p>Шлем</p></td>
      <td class="price"><p>297</p></td>
    </tr>
    <tr class="odd_row">
      <td><p>3.</p></td>
      <td class="armor"><p>Кольчуга</p></td>
      <td class="price"><p>565</p></td>
    </tr>
    <tr class="even_row">
      <td><p>4.</p></td>
      <td class="armor"><p>Булава</p></td>
      <td class="price"><p>1992</p></td>
    </tr>
    <!-- Сюда может добавиться неизвестное количество элементов экипировки.
      Их тоже нужно учитывать при расчёте средней цены. -->
  </tbody>
</table>
"""

# Создайте «суп».
soup = BeautifulSoup(price_html, 'lxml')

# Напишите здесь свой код.
res = soup.find_all('td', class_='price')
prices = []
for price in res:
    price_text = price.p.get_text().strip()
    if price_text.isdigit():
        prices.append(int(price_text))


if prices:
    average_sum = sum(prices) / len(prices)
else:
    average_sum = 0
print(average_sum)