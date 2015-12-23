import os,sys,re
def get_res_path():
	pattern =r'''(.+)src'''
	filenames = re.findall(pattern, sys.path[0])
	return os.path.join(filenames[0],'res')

# if __name__ == '__main__':
# 	print get_res_path()