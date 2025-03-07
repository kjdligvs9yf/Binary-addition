def SAdd(A:int,B:int) -> tuple[int,int]:
    """
    名称:半加器
    函数名:SAdd
    作用:只能计算2个1位二进制计算加法，有进位输出
    参数:
        A:输入1
        B:输入2
    """
    # 第一个是加和输出，第二个是进位输出
    return (A^B, A&B)

def CAdd(A:int,B:int,Cin:int=0) -> tuple[int,int]:
    """
    名称:全加器
    函数名:CAdd
    作用:只能计算2个1位二进制计算加法，添加了进位输入。
    参数:
        A:输入1
        B:输入2
        Cin:进位输入
    """
    # 第一个半加器的结果，参数对应为本函数的两个输入
    t1 = SAdd(A, B)
    # 第二个半加器的结果，第一个参数是进位输入，第二个参数是第一个半加器的加和输出
    t2 = SAdd(Cin, t1[0])
    # 返回元组，第一位是加和输出，第二位是进位输出
    return (t2[0], (t1[1] | t2[1]))

def Adder_8(A:str, B:str) -> str:
    """
    名称:8位加法器
    函数名:Adder_8
    作用:可以计算2个8位以内的二进制加法
    参数:
        A:输入1
        B:输入2
    """
    # 定义最大位数
    MAX = 8
    # 检测输入的数是否为二进制，如果不是，将直接退出
    if (len(set(A)) == 2 and "0" in A and "1" in A) and (len(set(B)) == 2 and "0" in B and "1" in B):
        return None
    # 检测位数是否超出最大位数，如果超出，将直接退出
    if (len(A) > MAX) or (len(B) > MAX):
        return None
    # 格式化参数（如果位数不到最大位数，那么就在该参数前加上前导0）
    if len(A) < MAX:
        A = "0" * (MAX - len(A)) + A
    if len(B) < MAX:
        B = "0" * (MAX - len(B)) + B
    # 定义进位输入和结果
    Cout = 0
    res = ""
    # 重复最大位数次，从大到小（因为要从低位向高位计算）
    for i in range(MAX,0,-1):
        # 计算当前位数的加和输出和进位输入，并加上进位输入, 更新进位输入
        t, Cout = CAdd(int(A[i-1]),int(B[i-1]),Cout)
        # 向结果里添加当前的加和输出
        res = str(t) + res
    return res

if __name__ == '__main__':
    print(Adder_8(*input("请输入两个8位二进制数：").split()))