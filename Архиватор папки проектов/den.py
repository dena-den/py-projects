import os
import time
source = ['"D:\\6DATA_SCIENCE\\Проекты в Python"']
target_dir='D:\\6DATA_SCIENCE'
today=target_dir + os.sep + time.strftime('%Y%m%d')
now=time.strftime('%H%M%S')
comment=input('Add a comment:')
if len(comment)==0:
  target=today+os.sep+now+'.zip'
else:
  target=today+os.sep+now+'_'+comment.replace(' ', '_')+'.zip'
if not os.path.exists(today):
  os.mkdir(today)
  print('Catalog created', today)

zip_command="zip -qr {} {}".format(target, ' '.join(source))
if os.system(zip_command)==0:
  print('Success in', target)
else:
  print('Mistakessss')