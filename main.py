def wc(book):
  word_count = 0
  for line in book:
    word_count += len(line.split())
  return word_count

def letter_dictionary(book):
  letter_dict = {}
  for line in book:
    for word in line.split():
      for letter in word:
        if letter.isalpha():
          dict_letter = letter.lower()
          if dict_letter in letter_dict:
            letter_dict[dict_letter] += 1
          else:
            letter_dict[dict_letter] = 1
  return letter_dict

def sort_compare(dictionary):
  return dictionary["num"]

def dict_to_sorted_list(letter_dict):
  lst = []
  for key, value in letter_dict.items():
    lst.append({"letter": key, "num": value})
  lst.sort(reverse=True, key=sort_compare)
  return lst

def print_sorted_list(letter_dict):
  for letter_freq in dict_to_sorted_list(letter_dict):
    print(f'The \'{letter_freq["letter"]}\' character was found {letter_freq["num"]} times')

def main():
  with open("./books/frankenstein.txt", "r") as f:
    book = f.readlines()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"Word Count: {wc(book)}")
    letter_count = letter_dictionary(book)
    print_sorted_list(letter_count)
    print("--- end report ---")
    


main()
