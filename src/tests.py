# from typing import List, Dict
#
# from pydantic import BaseModel
#
#
# class TestClass2(BaseModel):
#     name: str
#     surname: str
#
#
# class TestClass(BaseModel):
#     field1: str
#     field2: List[TestClass2]
#
#
# class Wrapper(BaseModel):
#     test1: Dict[str, TestClass]
#
#
# test_class_1 = TestClass(field1="tet1", field2=[
#     TestClass2(name="tf1", surname="tfs1"),
#     TestClass2(name="tf2", surname="tfs2"),
#     TestClass2(name="tf3", surname="tfs3")])
#
# wrapper = Wrapper(test1={"tester": test_class_1})
# test1_json = wrapper.model_dump_json()
#
# print(test1_json)
#
# test_class_1_restore = Wrapper.model_validate_json(json_data=test1_json)
# print(test_class_1_restore)



from src.io.data_storage import MemoryStorage

ds = MemoryStorage("player_id")
players = ds.get_all("player")
print(players)
