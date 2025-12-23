def safe_call(func, a, b):
    try:
        final = func(a,b)
        return (True, final, None)
    except ZeroDivisionError as e:
        return (False, None, type(e).__name__)
    except TypeError as e:
        return (False, None, type(e).__name__)
    except ValueError as e:
        return (False, None, type(e).__name__)
    except Exception as e:
        return (False, None, type(e).__name__)
    except IndexError as e:
        return (False, None, type(e).__name__)
    except KeyError as e:
        return (False, None, type(e).__name__)
