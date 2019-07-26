def coord_iter(w, h):
    for y in range(h):
        for x in range(w):
            yield (x, y)

def pix_gen(pix_arr, w, h):
    for x, y in coord_iter(w, h):
        for i in range(3):
            yield pix_arr[x, y][i]

def get_bin_pix_vals(pix_arr, w, h, lim=360):
    # get binary pixel values
    cur = 0
    b = []
    for pix_val in pix_gen(pix_arr, w, h):
        cur += 1
        b.append(format(pix_val, '08b'))
        if cur == lim:
            return b
