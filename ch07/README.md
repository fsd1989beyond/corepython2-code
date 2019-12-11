## 字典

- 字典使用get方法更安全，不存在返回None。 而不是抛异常。 setdefault不存在则创建之
  - book.get('pub') 、book['pub']
  - book.setdefault('pub','default Value')  
  - 基于hash表存储结构，字典集合的增删改效率远高于列表
  
  