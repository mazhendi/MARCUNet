#=========================================================
#
#  
#
#=========================================================
import os
from os.path import join

def get_path_list(root_path,img_path,label_path,fov_path):
    tmp_list = [img_path,label_path,fov_path]
    res = []
    for i in range(len(tmp_list)):
        data_path = join(data_root_path,tmp_list[i])
        print(data_path)
        filename_list = os.listdir(data_path)
        filename_list.sort()
        res.append([join(data_path,j) for j in filename_list])
    return res

def write_path_list(name_list, save_path, file_name):
    f = open(join(save_path, file_name), 'w')
    for i in range(len(name_list[0])):
        f.write(str(name_list[0][i]) + " " + str(name_list[1][i]) + " " + str(name_list[2][i]) + '\n')
    f.close()

if __name__ == "__main__":
    #------------Path of the dataset --------------------------------
    data_root_path = 'E:\\code\\VesselSeg-Pytorch-master2\\VesselSeg-Pytorch-master\\prepare_dataset\\data_path_list\\STARE'
    # if not os.path.exists(data_root_path): raise ValueError("data path is not exist, Please make sure your data path is correct")
    #train
    img = "training/images/"
    gt = "training/labels/"
    fov = "training/masks/"
    #test
    img_test = "test/images/"
    gt_test = "test/labels/"
    fov_test = "test/masks/"
    #---------------save path-----------------------------------------
    save_path = "E:\\code\\VesselSeg-Pytorch-master2\\VesselSeg-Pytorch-master\\prepare_dataset\\data_path_list\\STARE"
    if not os.path.exists(save_path):
        # os.makedirs(save_path)
        os.mkdir(save_path)

    #-----------------------------------------------------------------
    train_list = get_path_list(data_root_path, img, gt, fov)
    print('Number of train imgs:', len(train_list[0]))
    write_path_list(train_list, save_path, 'train.txt')

    test_list = get_path_list(data_root_path, img_test, gt_test, fov_test)
    print('Number of test imgs:', len(test_list[0]))
    write_path_list(test_list, save_path, 'test.txt')

    print("Finish!")
    # data_list = get_path_list(data_root_path,img,gt,fov)
    # print('Numbers of all imgs:',len(data_list[0]))
    # test_range = (0,5) # 测试集索引范围，左闭右开
    # train_list = [data_list[i][:test_range[0]] + data_list[i][test_range[1]:] for i in range(len(data_list))]
    # test_list = [data_list[i][test_range[0]:test_range[1]] for i in range(len(data_list))]
    #
    # print('Number of train imgs:',len(train_list[0]))
    # write_path_list(train_list, save_path, 'train.txt')
    #
    # print('Number of test imgs:',len(test_list[0]))
    # write_path_list(test_list, save_path, 'test.txt')
    #
    # print("Finish!")
    
