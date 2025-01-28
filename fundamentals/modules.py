import camelcase

camel_case_converter = camelcase.CamelCase()

my_text="hello, world!"


print(camel_case_converter.hump(my_text))  # Output: Hello World
