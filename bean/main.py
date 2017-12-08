
import bean.Screen

s = bean.Screen()

s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution


print(callable(bean.Sreen()))