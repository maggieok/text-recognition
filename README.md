# text-recognition
this is only disscussion place  for us three ----text recognition


training for english dataset
================

- cloning code
```sh
git clone https://github.com/maggieok/text-recognition.git
cd text-recognition
git checkout 19ad12838cdb
```
- downloading dataset
```sh
wget -c http://paddle-ocr-data.bj.bcebos.com/data.tar.gz
tar -xvf data.tar.gz
```
- training
```sh
python3 train.py
```


traning for chinese dataset
=======


- downloading dataset (download to you repo dir)

	[train.list](http://bj.bcebos.com/v1/ai-studio-online/4edf40b576534bc4b6d6d25c7ac30325ba5d9302c9da4316a04c865cee1e92bd?responseContentDisposition=attachment%3B%20filename%3Dtrain.list&authorization=bce-auth-v1%2F0ef6765c1e494918bc0d4c3ca3e5c6d1%2F2019-06-21T09%3A47%3A06Z%2F-1%2F%2F19d07e6fb96fc15811fb072ef9804aeb1dbb633dfb0d10eab78003c00b648122)

	[train_images.tar.gz](http://bj.bcebos.com/v1/ai-studio-online/f9328e4264514b69bd85a65bc7ec6623ac7f8feca87a496993215c01f7bc3778?responseContentDisposition=attachment%3B%20filename%3Dtrain_images.tar.gz&authorization=bce-auth-v1%2F0ef6765c1e494918bc0d4c3ca3e5c6d1%2F2019-06-21T09%3A47%3A46Z%2F-1%2F%2Fec807378f4011e3a1a969393ec4541211cb34d2a46b7778f429808028b75e863)
       
- extracting image file
```sh
tar -xvf train_images.tar.gz -C /path/to/<your repositories>
```

- indexing image
```python
pyton3 tools/indexing.py
```

- spliting dataset to train and val
```
mkdir dataset
ln -s /path/to/<your repositories>/train_images dataset/images
python3 tools/dataset_split.py
```

- training
```
python3 train.py
```




