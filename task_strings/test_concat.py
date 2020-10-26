def mytest(str):
    return str
    
if __name__ == "__main__":
    param = 'testparam'
    result = mytest("list of parameters is too long " + len(param))
    print(f'result={result}')