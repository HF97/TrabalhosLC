# unfold --------------------------------------------------
def unfold():
    pre1 = "m>=0"
    pre2 = "n>=0"
    pre3 = "r==0"
    pre4 = "x==m"
    pre5 = "y==n"
    pos = "r15==m*n"
    pOr = "||"
    x,y,r = 0,0,0
    iteracoes = 16
    # iteracoes = iteracoes-2
    dic = {}
    path = 0
    # pre condicao
    # print(pre)
    # iteracao inicial while
    wh1 = unfoldWhileInicio(x,y,r)
    dic[path] = [pre1,pre2,pre3,pre4,pre5,wh1]

    # print(dic)

    # iteracao inicial do if
    i1 = unfoldIfInicio(x,y,r)
    dic[path] = dic[path]+[i1[0],i1[1],i1[2],i1[3],i1[4]]
    
    # iteracao recuriva if
    unfoldRecursivo(x,y+1,r,1,iteracoes-2,dic,path)
    
    # or
    # print(pOr)

    # iteracao inicial not if
    i2 = unfoldNotInicio(x,y,r)
    path = int(pow(2,iteracoes)/2)
    dic[path] = [i2[0],i2[1],i2[2]]
    # iteracao recuriva not if
    unfoldRecSeg(x,y,r,1,iteracoes-2,dic,path)
    # pos condicao
    # print(pos)
    # caminho = ""
    # # print(dic)
    # l = list(dic.values())
    # print(len(dic.keys()))
    # # print(l)
    # caminho = []

    # prove1 = "Implies(And("
    # prove2 = ",Not(y5>0)),r2==m*n)"
    # for i in l:
    #     s = ""
    #     for a in i:
    #         s+=","+a
    #     s = s[1::]
    #     caminho.append(prove1+s+prove2)
    # print(caminho)
    # return caminho
    # return prove1+caminho+prove2


# recursivo -----------------------------------------------
def unfoldRecursivo(nx,ny,nr,tabs,iteracoes,dic,path):
    pOr = "\t"*tabs+"||"
    wh1 = unfoldWhile(nx,ny,nr,tabs)
    i1 = unfoldIf(nx,ny,nr,tabs,iteracoes)
    l = dic[path]
    dic[path] = dic[path]+[wh1,i1[3],i1[4],i1[5],i1[6],i1[7]]
    # print(dic)
    if(iteracoes > 0):
        unfoldRecursivo(i1[0],i1[1],i1[2],tabs+1,iteracoes-1,dic,path)
    else:
        print("caminho",path,dic[path])
    print(pOr)
    i2 = unfoldNot(nx,ny,nr,tabs,iteracoes)
    path = int(pow(2,iteracoes))
    dic[path] = l+[wh1,i2[3],i2[4],i2[5]]
    if(iteracoes > 0):
        unfoldRecursivo(i2[0],i2[1],i2[2],tabs+1,iteracoes-1,dic,path)
    else:
        print("caminho",path,dic[path])

# assume que o while e verdadeiro
def unfoldWhile(nx,ny,nr, tabs):
    wh1 = f"y{ny}>0"
    # print(wh1)
    return(wh1)

# parte quando o if é verdadeiro
def unfoldIf(nx, ny, nr, tabs, iteracoes):
    if1 = f"y{ny}&1==1"
    if2 = f"y{ny+1}==y{ny}-1"
    if3 = f"r{nr+1}==r{nr}+x{nx}"
    if4 = f"x{nx+1}==x{nx}<<1"
    if5 = f"y{ny+2}==y{ny+1}>>1"
    if6 = f"assert(not(y{ny+2} > 0) and r15 == r{nr+1})"
    # if iteracoes==0:
    #     print(if1,if2,if3,if4)
        
    # else:
    #     print(if1,if2,if3)
    return nx+1,ny+2,nr+1,if1,if2,if3,if4,if5

# parte quando o if e falso
def unfoldNot(nx, ny, nr, tabs, iteracoes):
    # not1 = "\t"*tabs+f"assume(not(y{ny} > 0))\n"
    not1 = f"not(y{ny}&1==1)"
    not2 = f"x{nx+1}==x{nx}<<1"
    not3 = f"y{ny+1}==y{ny}>>1"
    # not4 = f"not(y{ny+1}>0) and r15 == r{nr})"
    # if iteracoes==0:
    #     print(not2,not3,not3)
    # else:
    #     print(not2,not3)
    return nx+1,ny+1,nr,not1,not2,not3



# iteracao inicial ----------------------------------------
def unfoldWhileInicio(nx,ny,nr):
    wh1 = f"y>0"
    # print(wh1)
    return wh1

# parte quando o if é verdadeiro na iteracao inicial quando as variaveis ainda sao x,y,r
def unfoldIfInicio(nx, ny, nr):
    if1 = f"y&1==1"
    if2 = f"y{ny}==y-1"
    if3 = f"r{nr}==r+x"
    if4 = f"x{nx}==x<<1"
    if5 = f"y{ny+1}==y{nr}>>1"
    # print(if1,if2,if3)
    return(if1,if2,if3,if4,if5)

# parte quando o if é falso na iteracao inicial quando as variaveis ainda sao x,y,r
def unfoldNotInicio(nx, ny, nr):
    not1 = "not(y&1==1)"
    not2 = f"x{nx}==x<<1"
    not3 = f"y{ny}==y>>1"
    # print(not1,not2)
    return (not1,not2,not3)








# segunda iteracao not ------------------------------------
def unfoldRecSeg(nx, ny, nr, tabs, iteracoes, dic, path):
    pOr = "\t" * tabs + "||"
    wh1 = unfoldWhile(nx, ny, nr, tabs)
    i1 = unfoldIfSeg(nx, ny, nr, tabs)
    l = dic[path]
    dic[path] = dic[path]+[wh1,i1[3],i1[4],i1[5],i1[6],i1[7]]
    # print("d",dic)
    if(iteracoes > 0):
        unfoldRecursivo(i1[0],i1[1],i1[2],tabs+1,iteracoes-1,dic,path)
    # print(pOr)
    i2 = unfoldNotSeg(nx, ny, nr, tabs)
    path = int(pow(2,iteracoes))
    dic[path] = l+[wh1,i2[3],i2[4],i2[5]]
    if(iteracoes > 0):
        unfoldRecursivo(i2[0],i2[1],i2[2],tabs+1,iteracoes-1,dic,path)


# parte quando o if é verdadeiro na segunda iteracao quando na primeira iteracao o if e falso e as variaveis ainda sao x,y,r
def unfoldIfSeg(nx, ny, nr, tabs):
    if1 = f"y{ny}&1==1"
    if2 = f"y{ny+1}=y{ny}-1"
    if3 = f"r{nr}=r+x"
    if4 = f"x{nx}=x<<1"
    if5 = f"y{ny+2}=y{nr+1}>>1"
    # print(if1,if2,if3)
    return nx,ny+2,nr,if1,if2,if3,if4,if5

# parte quando o if é falso na segunda iteracao quando na primeira iteracao o if e falso e as variaveis ainda sao x,y,r
def unfoldNotSeg(nx, ny, nr, tabs):
    # not1 = "\t"*tabs+f"assume(not(y{ny} > 0))\n"
    not1 = f"not(y{ny}&1==1)"
    not2 = f"x{nx}=x<<1"
    not3 = f"y{ny+1}=y{ny}>>1"
    # print(not2,not3)
    return nx,ny+1,nr,not1,not2,not3




unfold()