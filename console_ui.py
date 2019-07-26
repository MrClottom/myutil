def cls():
    print('\n'*50)


def confirm(query):
    inp = input(query)
    while inp.lower() not in 'yn' or not inp.lower():
        inp = input(query)
    return inp.lower() == 'y'


def get_inp(cond, disp, prompt, retry_disp, retry_prompt=None, clear=True):
    retry_prompt = prompt if retry_prompt is None else retry_prompt
    if clear:
        cls()
    disp()
    inp = input(prompt)
    while not cond(inp):
        if clear:
            cls()
        disp()
        retry_disp(inp)
        inp = input(retry_prompt)
    return inp
