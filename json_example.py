import json
json_data = '{"name":"Ruslan", "age":"30", "is_student":false}'

# получаем словарь python из json строки
parsed_data = json.loads(json_data)
print(parsed_data["name"], type(parsed_data) )


# ниже python словарь для примера имеем
data = {
  "name":"Ruslan",
  "age":"30",
  "name":"Иван",
  "is_student":False
}
# конвертируем словарь python в json строку
json_string = json.dumps(data, indent=4)
print(json_string)


# читаем из какого-то json данные и на выходе получаем словарь
# открываем файл для чтения
with open("json_example.json", encoding='utf-8') as file:
  data = json.load(file)
  print(data, type(data))


# запись словаря python в json файл
with open ("data_json", mode='w', encoding='utf-8') as file:
  json.dump(data, file, indent=4, ensure_ascii=False)


