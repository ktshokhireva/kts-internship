## Баг 1
### test_advertisement_info_is_correct():
#### Все данные объявления совпадают с указанными при создании
1. Шаг 1: создать объявление с корректным телом запроса:
```json
{
  "sellerID": 330330,
  "name": "test",
  "price": 5000
}
```
2. Шаг 2: запросить информацию об этом объявлении, получив его id
`https://qa-internship.avito.com/api/1/item/{item_id}`
- ОР: код ответа - 200
- ОР: все данные объявления совпадают с указанными, ожидаемое название объявления = "test"
- ФР: код ответа - 200, название созданного объявления = "dsdsd"

## Баг 2
### test_seller_list_has_him_created_advertisement():
#### В списке об-й продавца есть объявление с id созданного об-я
1. Шаг 1. Создать объявление от любого продавца
2. Шаг 2. Запросить список объявлений этого продавца
- ОР: Код ответа - 200
- ОР: В списке есть объявление с указанным id
- ФР: Объявление с запрошенным id не найдено

## Баг 3
### test_adv_info_from_seller_list_is_correct():
#### В списке об-й продавца есть объявление с данными, указанными при создании об-я
1. Шаг 1. Создать объявление от продавца с seller_id
2. Шаг 2. Запросить список объявлений продавца
- ОР: Код ответа - 200
- ОР: В списке есть объявление с указанными при создании данными
- ФР: Объявление с запрошенными параметрами не найдено

## Баг 4
### test_adv_info_from_seller_list_is_same_as_created():
#### В списке об-й продавца есть объявление с данными созданного объявления
1. Шаг 1. Создать объявление от продавца
2. Шаг 2. Узнать фактические данные о созданном объявлении 
- ОР: код ответа - 200
3. Запросить список объявлений продавца
- ОР: Код ответа - 200
- ОР: В списке есть объявление с данными созданного объявления
- ФР: Объявление с запрошенными параметрами не найдено

## Баг 5
### test_negative_get_advertisements():
#### Пришёл ответ с кодом 400 при запросе объявлений продавца с некорректным id
1. Шаг 1. Запросить список объявлений продавца с неправильным seller_id
`https://qa-internship.avito.com/api/1/-1/item`
- ОР: код ответа - 400
- ФР: Выдан список объявлений, код ответа - 200