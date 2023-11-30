def add(n1, n2):
    try:
        result = int(n1) + int(n2)
        return str(result)
    except ValueError:
        return 'Invalid Operation'
    except UnboundLocalError:
        return 'Invalid Operation'
    except TypeError:
        return 'Invalid Operation'


add(91,19)
