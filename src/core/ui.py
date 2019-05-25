def ask(msg, allow=None, default=None, validate=None, wrong_msg=None, newline=True):
    if default is not None:
        msg = f"({default}) {msg}"

    def _input(msg):
        return input(msg + ('\n>' if newline else '')) or default

    if validate is not None:
        ans = _input(msg) or default
        while not validate(ans):
            if wrong_msg: print(wrong_msg)
            ans = _input(msg).lower().strip() or default

        return validate(ans)


    if allow is None:
        return _input(msg) or default

    if allow is bool:
        ans = _input('[y/n] '+msg).lower().strip()
        if ans:
            return ans.startswith('y')
        else:
            return default

    if allow is int:
        ans = None
        while True:
            try:
                ans = int(_input(msg))
            except TypeError:
                print(f"{ans} n'est pas un nombre entier!")
                continue
            break


    # if 'allow' is a list:
    if hasattr(allow, '__iter__'):
        ans = _input(msg).lower()
        while ans not in [e.lower() for e in allow]:
            print(f"{ans} n'est pas un choix valide. Choix disponibles:")
            for choice in allow:
                print(f"- {choice}")

            ans = _input(msg).lower().strip() or default

        return ans


