import datetime

def this_func():
    try:
        x = -1
        if x < 0:
            raise Exception('Soooorrrryyyyyy')
    except:
        dt = datetime.datetime.now()
        print(dt)
        print('Exception')
    finally:
        print('Chal gayagyggxjhSGZjyhgGjhZG')


this_func()