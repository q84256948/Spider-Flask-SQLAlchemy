# coding=utf-8
from struct import pack

__author__ = 'YU'
import os
import unittest
from PictureORM import Picture,PictureORMHelper

TEST_DB = 'test.db'


class PictureORMHelperTestCase(unittest.TestCase):
    def setUp(self):
        """Set up a blank temp database before each test"""

        self.helper = PictureORMHelper("Picture.db")
        self.helper.drop_db()
        self.helper.create_db()

    def tearDown(self):
        """Destroy blank temp database after each test"""
        self.helper.drop_db()

    def test_add(self):
        # 插入测试
        picName = u'E:\\练习\\InternetWorm\\pictures\\11.jpg'
        fp = open(picName, 'rb')
        imgContent = fp.read()
        fp.close()
        # picName = 'pictures/' + str('yy').decode('utf-8') + '.jpg'
        # fp = open(picName, 'wb')
        # fp.write(imgContent)
        # fp.close()
        img_64=imgContent.encode('base64')
        isSuccess = self.helper.addPicture(Picture("img", imgContent,img_64))
        self.assertTrue(isSuccess)
        isSuccess = self.helper.addPicture(Picture("tome", pack('H', 365),None))
        isSuccess = self.helper.addPicture(Picture("tome",pack('H', 365),None))
        self.assertTrue(isSuccess)
        isSuccess = self.helper.addPicture(Picture("tome", pack('H', 365),None))
        self.assertTrue(isSuccess)
        userList = self.helper.query_all_with_Picture_name_password(Picture("img", imgContent,img_64))
        # print userList
        self.assertGreater(len(userList), 0)
        for item in userList:
            picName = 'pictures/' + str(item.title).decode('utf-8') + '.jpg'
            fp = open(picName, 'wb')
            fp.write(imgContent)
            fp.close()


    def test_query_all(self):
        # 查询所有相同name数据测试
        isSuccess = self.helper.addPicture(Picture("tome",pack('H', 365),None))
        self.assertTrue(isSuccess)
        userList = self.helper.query_all_with_Picture_name_password(Picture("tome" ,pack('H', 365),None))
        # print userList
        self.assertGreater(len(userList),0)

    def test_query(self):
        isSuccess = self.helper.addPicture(Picture("tome",pack('H', 365),None))
        self.assertTrue(isSuccess)
        userList = self.helper.query_all_Picture()
        self.assertGreater(len(userList), 0)


if __name__ == '__main__':
    unittest.main()
