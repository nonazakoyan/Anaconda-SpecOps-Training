def strmove(ft_str, size):
    new_str = ft_str[len(ft_str) - size:] + ft_str[:size + 1]
    return new_str
