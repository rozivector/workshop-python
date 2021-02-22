def concat(*args, sep="/"):
    return print(sep.join(args))

concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".") # merubah kata kunci pemisah dari / ke .
