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
                charlist[char] = list()
                charlist[char].append(set())
                charlist[char].append(set())
            charlist[char][0].add(attr)
        
        def dislike_exec(o):
            char, attr = o
            char = eval(char + ".name")
            if not char in charlist:
                charlist[char] = list()
                charlist[char].append(set())
                charlist[char].append(set())
            charlist[char][1].add(attr)
        
        def xlike_lint(o):
            char, attr = o
            try:
                eval(char)
            except:
                renpy.error("Character not defined: %s" % char)
        
        renpy.register_statement("like", parse = xlike_parse, execute = like_exec, lint = xlike_lint)
        renpy.register_statement("dislike", parse = xlike_parse, execute = dislike_exec, lint = xlike_lint)
        
        def relations(char0, char1): # "The relations of char0 towards char1"
            pos = len(charlist[char0][0] & charlist[char1][0]) + len(charlist[char0][1] & charlist[char1][1])
            neg = len(charlist[char0][1] & charlist[char1][0])
            return neg/pos #the closer towards 0, the better relations
        