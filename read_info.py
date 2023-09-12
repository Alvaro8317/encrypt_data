import json
def read_data_from_file(filename: str):
  with open(filename, 'r') as file:
    text_to_return = json.load(file)
  return text_to_return['data']['otrLoginUpdates']

if __name__ == '__main__':
  response = read_data_from_file('raw_data.txt')
  print(response)