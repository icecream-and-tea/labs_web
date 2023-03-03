from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client

import sys

appid = 1311300121
secret_id = u'xxx'
secret_key = u'xxx'
region = u'ap-guangzhou'
token = None
scheme = 'https'
store_bucket = 'doban-movie-1311300121'

config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token, Scheme = scheme)
client = CosS3Client(config)


def upload(file_name, upload_path):
    try:
        client.put_object_from_local_file(
        Bucket= store_bucket,
        LocalFilePath= upload_path,
        Key= file_name
        )
        return geturl(file_name)
    except Exception as e:
        print(e)
        print('Error put object {} to bucket {}. Make sure the object exists and your bucket is in the same region as this function.'.format(file_name, store_bucket))
        raise e


def geturl(file_name):
    url = client.get_presigned_download_url(
    Bucket='doban-movie-1311300121',
    Key=file_name,
    Params={
    'response-content-disposition':'attachment; filename=' + file_name
    # 除了response-content-disposition，还支持response-cache-control、response-content-encoding、response-content-language、
    # response-content-type、response-expires等请求参数，详见下载对象API，https://cloud.tencent.com/document/product/436/7753
    })
    print('url is '+ url)
    return url