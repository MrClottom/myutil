from getpass import getpass as __gp
from hashlib import sha256 as __sha256


def __sha(data):
    return __sha256(data).digest()


def cls():
    print('\n'*50)


def confirm(query, confirm_value='y', match_values='yn', do_lower=True):
    inp = input(query)
    inp_to_check = inp.lower() if do_lower else inp
    while inp_to_check not in match_values or not inp_to_check:
        inp = input(query)
        inp_to_check = inp.lower() if do_lower else inp
    return inp_to_check == confirm_value


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


def num_menu(*options):
    print('Select an option:')
    for i, option in enumerate(options):
        print('({})'.format(i+1), option)

    inp = input('>> ')
    if inp.isdigit():
        inp = int(inp)

    while inp not in range(1, len(options) + 1):
        inp = input('Not a valid option. Try again. >> ')
        if inp.isdigit():
            inp = int(inp)

    return inp


def get_pswd():

    p1 = __sha(__gp('Enter password: ').encode())
    pswd = __gp('Confirm password: ')
    match = p1 == __sha(pswd.encode())
    while not match:
        print('passwords did not match')
        p1 = __sha(__gp('Enter password: ').encode())
        pswd = __gp('Confirm password: ')
        match = p1 == __sha(pswd.encode())

    return pswd
