#-*- coding:utf-8 –*-
import os,sys,re
def get_res_root_path():
	"""获取资源文件夹根目录"""
	pattern =r'''(.+)src'''
	filenames = re.findall(pattern, sys.path[0])
	return os.path.join(filenames[0],'res')

def get_res_path(filenames):
	"""获取资源路径"""
	return os.path.join(get_res_root_path(), filenames)

if __name__ == '__main__':
	print get_res_root_path()