# unfold --------------------------------------------------
def unfold():
    pre = "assume m >= 0 and n >= 0 and r == 0 and x == m and y == n"
    pos = "r15 == m * n"
    pOr = "||"
    x,y,r = 0,0,0
    iteracoes = 14
    # pre condicao
    print(pre)
    # iteracao inicial while e if
    unfoldWhileInicio(x,y,r)
    unfoldIfInicio(x,y,r)
    # iteracao recuriva if
    unfoldRecursivo(x,y,r,1,iteracoes)
    # or
    print(pOr)
    # iteracao inicial not if
    unfoldNotInicio(x,y,r)
    # iteracao recuriva not if
    unfoldRecSeg(x,y,r,1,iteracoes)
    # pos condicao
    print(pos)


# recursivo -----------------------------------------------
def unfoldRecursivo(nx,ny,nr,tabs,iteracoes):
    pOr = "\t"*tabs+"||"
    unfoldWhile(nx,ny+1,nr,tabs)
    unfoldIf(nx,ny+1,nr,tabs,iteracoes)
    if(iteracoes > 0):
        unfoldRecursivo(nx+1,ny+2,nr+1,tabs+1,iteracoes-1)
    print(pOr)

    unfoldNot(nx,ny+1,nr,tabs,iteracoes)
    if(iteracoes > 0):
        unfoldRecursivo(nx,ny+1,nr,tabs+1,iteracoes-1)

def unfoldWhile(nx,ny,nr, tabs):
    wh1 = "\t"*tabs+f"assume y{ny} > 0;"
    print(wh1)

def unfoldIf(nx, ny, nr, tabs, iteracoes):
    if1 = "\t"*tabs+f"(assume(y{ny} & 1 == 1);\n"
    if2 = "\t"*tabs+f"    y{ny+1} , r{nr+1}  = y{ny} - 1 , r{nr} + x{nx};\n"
    if3 = "\t"*tabs+f"x{nx+1} , y{ny+2} = x{nx} << 1 , y{ny+1} >> 1;\n"
    if4 = "\t"*tabs+f"assert(not(y{ny+2} > 0) and r15 == r{nr+1})"
    if iteracoes==0:
        print(if1,if2,if3,if4)
    else:
        print(if1,if2,if3)

def unfoldNot(nx, ny, nr, tabs, iteracoes):
    # not1 = "\t"*tabs+f"assume(not(y{ny} > 0))\n"
    not2 = "\t"*tabs+f"assume(not (y{ny} & 1 == 1);\n"
    not3 = "\t"*tabs+f"x{nx+1}, y{ny+1} = x{nx} << 1, y{ny} >> 1;\n"
    not4 = "\t"*tabs+f"assert(not(y{ny+1} > 0) and r15 == r{nr})"
    if iteracoes==0:
        print(not2,not3,not4)
    else:
        print(not2,not3)



# iteracao inicial ----------------------------------------
def unfoldWhileInicio(nx,ny,nr):
    wh1 = f"assume y > 0;"
    print(wh1)

def unfoldIfInicio(nx, ny, nr):
    if1 = f"assume(y & 1 == 1);\n"
    if2 = f"    y{ny} , r{nr}  = y - 1 , r + x;\n"
    if3 = f"x{nx} , y{ny+1} = x << 1 , y{nr} >> 1;"
    print(if1,if2,if3)

def unfoldNotInicio(nx, ny, nr):
    not1 = f"assume(not (y & 1 == 1);\n"
    not2 = f"x{nx} = x << 1, y{ny} = y >> 1;"
    print(not1,not2)




# segunda iteracao not ------------------------------------
def unfoldRecSeg(nx, ny, nr, tabs, iteracoes):
    pOr = "\t" * tabs + "||"
    unfoldWhile(nx, ny, nr, tabs)
    unfoldIfSeg(nx, ny, nr, tabs)
    unfoldRecursivo(nx+1,ny,nr+1,2,iteracoes)
    print(pOr)
    unfoldNotSeg(nx, ny, nr, tabs)
    unfoldRecursivo(nx,ny,nr,2,iteracoes)

def unfoldIfSeg(nx, ny, nr, tabs):
    if1 = "\t"*tabs+f"assume(y{ny} & 1 == 1);\n"
    if2 = "\t"*tabs+f"    y{ny+1} , r{nr}  = y{ny} - 1 , r + x;\n"
    if3 = "\t"*tabs+f"x{nx} , y{ny+2} = x << 1 , y{nr+1} >> 1;"
    print(if1,if2,if3)

def unfoldNotSeg(nx, ny, nr, tabs):
    # not1 = "\t"*tabs+f"assume(not(y{ny} > 0))\n"
    not2 = "\t"*tabs+f"assume(not (y{ny} & 1 == 1);\n"
    not3 = "\t"*tabs+f"x{nx} = x << 1, y{ny+1} = y{ny} >> 1;"
    print(not2,not3)




unfold()