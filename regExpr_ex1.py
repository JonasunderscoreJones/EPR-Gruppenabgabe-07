'''EPR 07 Aufgabe 1'''
__author__ = "7987847, Werner, 7347119, Fajst, 7735965, Melikidze"

import re


# a) All character strings between < and the next >. 
# The two < and > can also be output. Example: <a>, <span …>.
# b) All (annual) numbers between 1900 and 2099.


def extract_annual(text):
    '''
    Extract all annual numbers between 1900 and 2099.
    Return a list of strings.
    valid years are 1900-2099
    '''
    # Extract all annual numbers between 1900 and 2099.
    # Return a list of strings.
    # valid years are 1900-2099
    return re.findall(r'19[0-9][0-9]|20[0-9][0-9]', text)
    # return re.findall(r'\b(19|20)\d\d\b', text)


def extract_tags(text):
    '''
    Extract all tags.
    Return a list of strings.
    '''
    # Extract all tags.
    # Return a list of strings.
    return re.findall(r'<[^>]+>', text)


def extract_strings(text):
    '''
    Extract all strings outside that are between > and <.
    Return a list of strings.
    '''
    # Extract all strings outside that are between > and <.
    # Return a list of strings.
    return re.findall(r'>([^<]+)<', text)


def main():
    '''
    Main function.
    '''
    # open file
    with open('PythonEntwicklungG.txt', 'r') as file:
        # read a list of lines into data
        data = file.readlines()
        file.close()

        data_extracted = []
        for line in data:
            tag_list = extract_tags(line)
            if tag_list:
                data_extracted.append(tag_list)
            strings_list = extract_strings(line)
            if strings_list:
                data_extracted.append(strings_list)
            annual_list = extract_annual(line)
            if annual_list:
                data_extracted.append(annual_list)

        for _ in data_extracted:
            if type(_) == list:
                for __ in _:
                    # check the type of the element
                    try:
                        if type(int(__)) == int:
                            # print with formatted tab spacing and color in Red
                            print(
                                f'{__:<110} <--- is an annual number',
                                end='\t\n')

                        elif type(__) == str:
                            # check if the string is a tag
                            if __.startswith('<') and __.endswith('>'):
                                print(
                                    f'{__:<110} <--- is a Tag string',
                                    end='\t\n')
                            else:
                                print(f'{__:<110} <--- is a string',
                                      end='\t\n')

                    except ValueError:
                        if __.startswith('<') and __.endswith('>'):
                            print(f'{__:<110} <--- is a Tag string',
                            end='\t\n')
                        else:
                            print(f'{__:<110} <--- is a string', end='\t\n')

            else:
                print(_)


if __name__ == '__main__':
    main()
