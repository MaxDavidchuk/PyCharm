def time_monitor(func):
  import time

  def wrapper(*args, **kwargs):
    start = time.time()
    func(*args, **kwargs)
    finish = time.time()
    duration = finish - start
    result = round(duration * 1000, 3)
    print(f'* Час виоконання: {result} ms')
  return wrapper
