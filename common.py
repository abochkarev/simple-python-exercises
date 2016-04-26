def show(fn):
    def f(*args, **kwargs):
        result = fn(*args, **kwargs)
        s = '%s('
        params = [fn.func_name]
        if args:
            s += '%s'
            params.append(args)
        if kwargs:
            if args:
                s += ','
            s += '%s'
            params.append(kwargs)
        s += ') == %s'
        params.append(result)
        print s % tuple(params)
        return result

    return f
