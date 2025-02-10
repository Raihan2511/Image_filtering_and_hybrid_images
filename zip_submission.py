import os
import shutil

def copy_directory(src, dest):
  try:
    shutil.copytree(src, dest)
  except shutil.Error as e:
    print('Directory not copied. Error: %s' % e)
  except OSError as e:
    print('Directory not copied. Error: %s' % e)

shutil.rmtree('temp_submission', ignore_errors=True)
os.mkdir('temp_submission')
for dir_name in [r'Image_filtering_and_hybrid_images\code', r'Image_filtering_and_hybrid_images\results']:
  copy_directory(dir_name, '/'.join(['temp_submission', dir_name]))
shutil.make_archive('submission_insight_engineer_Sayan_Raihan', 'zip', 'temp_submission')
shutil.rmtree('temp_submission', ignore_errors=True)
