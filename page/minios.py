#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Project ：YYWDBack
@File ：MinioCommand.py
@Author ：SCC
@Date ：2023/12/14 22:26
This program is good and not any bug. If you find Bug, it must be your problem.
"""

# 从minio库中导入Minio客户端类
import logging
import re
from minio import Minio


class MinioCommand:
    def __init__(self, ip: str, api_port: str, access_key: str, secret_key: str, secure=False):
        self.ip = ip
        self.api_port = api_port
        self.__access_key = access_key
        self.__secret_key = secret_key
        self.client = Minio(
            endpoint=self.ip + ':' + self.api_port,
            access_key=self.__access_key,
            secret_key=self.__secret_key,
            secure=secure
        )

    def CreateBucket(self, BucketName: str) -> bool:
        """
        创建存储桶
        @Author: ChuanCheng Shi
        :param BucketName: 桶名字
        :return: bool
        """
        try:
            self.client.make_bucket(BucketName, location="us-east-1")
            return True
        except BaseException as e:
            logging.debug(str(e))
            return False

    def DelBucket(self, BucketName: str) -> bool:
        """
        删除存储桶
        @Author: ChuanCheng Shi
        :param BucketName: 桶名字
        :return: bool
        """
        try:
            self.client.remove_bucket(BucketName)
            return True
        except BaseException as e:
            print(e)
            logging.debug(str(e))
            return False

    def GetObjectListFromBucket(self, BucketName: str) -> list:
        """
        获取桶内数据信息
        @Author: ChuanCheng Shi
        :param BucketName: 桶名称
        :return:
        """
        if self.client.bucket_exists(BucketName):
            objects = self.client.list_objects(BucketName)
            obj_list = [obj.object_name for obj in objects]
            return obj_list
        else:
            logging.warning(msg="Maybe your Bucket is Empty")
            return []

    def DownloadObjectFromBucket(self, ObjectName: str, BucketName: str, SavePath: str) -> bool:
        """
        下载文件到本地, 函数会优先检查桶内是否存在该文件，在进行下载，后续需要更新文件路径检测机制
        :param ObjectName: 文件名
        :param BucketName: 桶名称
        :param SavePath: 保存路径
        :return: bool
        """
        # TODO 添加保存地址判断
        if ObjectName in self.GetObjectListFromBucket(BucketName):
            self.client.fget_object(BucketName, ObjectName, SavePath)
            return True
        else:
            return False

    def GetObjectLink(self, ObjectName: str, BucketName: str) -> str:
        """
        获取一个存储对象的链接
        :param ObjectName: 文件名
        :param BucketName: 桶名称
        :return: 链接
        """
        if ObjectName in self.GetObjectListFromBucket(BucketName):
            return "http://" + self.ip + ":" + self.api_port + "/" + BucketName + "/" + ObjectName
        else:
            return "No Link"

    def GetObjectSize(self, ObjectName: str, BucketName: str) -> str:
        """
        获取一个存储对象的大小
        :param ObjectName: 文件名
        :param BucketName: 桶名称
        :return: 文件大小(字节)
        """
        if ObjectName in self.GetObjectListFromBucket(BucketName):
            ObjectSize = self.client.stat_object(BucketName, ObjectName)
            return ObjectSize.size
        else:
            return 'not exist Object'

    def UploadObject(self, ObjectName: str, BucketName: str, ObjectPath: str) -> bool:
        """
        # 上传文件到minio
        :param ObjectName:
        :param BucketName:
        :param ObjectPath:
        :return:
        """
        try:
            print(self.client.fput_object(BucketName, ObjectName, ObjectPath))
            logging.debug("Upload Success!")
            return True
        except BaseException as e:
            logging.warning(str(e))
            return False


if __name__ == "__main__":
    MinioCommand = MinioCommand(ip="#", api_port="9000", access_key="#",
                                secret_key="#")
