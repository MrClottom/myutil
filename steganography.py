def block(ind, data):
    if type(data) is str:
        return bytes.fromhex(ind + data)
    # assumes data is already a bytes object
    return bytes.fromhex(ind) + data
