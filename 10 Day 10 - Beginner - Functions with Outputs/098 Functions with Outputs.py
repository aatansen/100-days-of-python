def format_name(f_name, l_name):
    print(f'Your full name is: {f_name.title()} {l_name.title()}')

format_name('alahi','aLMiN')

# return :
def format_name(f_name, l_name):
    return f'Your full name is: {f_name.title()} {l_name.title()}'

full_name = format_name('alahi','aLMiN')
print(full_name)

# return none :
def format_name(f_name, l_name):
    if f_name=="" or l_name=="":
        return
    return f'Your full name is: {f_name.title()} {l_name.title()}'

full_name = format_name('alahi','aLMiN')
print(full_name)