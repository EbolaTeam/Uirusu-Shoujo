python early:
        charlist = dict()

        def xlike_parse(lex):
            char = lex.simple_expression()
            attr = lex.rest()
            return (char, attr)
        
        def like_exec(o):
            char, attr = o
            char = eval(char + ".name")
            if not char in charlist:
                charlist[char] = list(2)
                charlist[0] = set()
                charlist[1] = set()
            charlist[char][0].add(attr)
        
        def dislike_exec(o):
            char, attr = o
            char = eval(char + ".name")
            if not char in charlist:
                charlist[char] = list(2)
                charlist[0] = set()
                charlist[1] = set()
            charlist[char][1].add(attr)
        
        def xlike_lint(o):
            char, attr = o
            try:
                eval(char)
            except:
                renpy.error("Character not defined: %s" % char)
        
        renpy.register_statement("like", parse = xlike_parse, execute = like_exec, lint = xlike_lint)
        renpy.register_statement("dislike", parse = xlike_parse, execute = dislike_exec, lint = xlike_lint)
        
        def compare():
            pass
        