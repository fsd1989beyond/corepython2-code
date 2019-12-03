## 字典

- 字典使用get方法更安全，不存在返回None。 而不是抛异常。 setdefault不存在则创建之
  - book.get('pub') 、book['pub']
  - book.setdefault('pub','default Value')  