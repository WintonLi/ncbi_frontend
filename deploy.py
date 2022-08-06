##### Requires Fabric and needs to run in a Linux system 
from fabric import Connection
import shutil
import tempfile


dist_dir = '/mnt/c/works/codes/interview/ncbi_pub_trend_frontend/dist'
www_dir = '/www/ncbi'

with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)
    shutil.make_archive(f'{tmpdirname}/dist', 'zip', dist_dir)
    
    with Connection('lizhk') as c:
        print('Deleting existing contents...')
        c.run(f'rm -rdf {www_dir}/*')
        print('Done.')
        print('Copying release to remote host')
        c.put(f'{tmpdirname}/dist.zip', www_dir)
        print('Done.')
        with c.cd(www_dir):
            print('Unziping...')
            res = c.run('unzip dist.zip')
            print('Done')
print('App successfully deployed.')