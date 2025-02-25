<<<<<<< HEAD
import os.path as osp
=======
import os.path
>>>>>>> parent of 164beed (add command argv)
import glob
import cv2
import numpy as np
import torch
import RRDBNet_arch as arch

<<<<<<< HEAD
<<<<<<< HEAD
model_path = 'models/RRDB_ESRGAN_x4.pth'  # models/RRDB_ESRGAN_x4.pth OR models/RRDB_PSNR_x4.pth
device = torch.device('cuda')  # if you want to run on CPU, change 'cuda' -> cpu
# device = torch.device('cpu')
=======
model_path = sys.argv[1]  # models/RRDB_ESRGAN_x4.pth OR models/RRDB_PSNR_x4.pth
>>>>>>> parent of 6f106de (add run on CPU)
=======
mode = 'ESRGAN'  # ESRGAN or RRDB_PSNR


if mode == 'ESRGAN':
    model_path = './models/RRDB_ESRGAN_x4.pth'
elif mode == 'RRDB_PSNR':
    model_path = './models/RRDB_PSNR_DF2K_x4.pth'
>>>>>>> parent of 164beed (add command argv)

test_img_folder = 'LR/*'

model = arch.RRDBNet(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path), strict=True)
model.eval()
<<<<<<< HEAD
model = model.to(device)
=======
for k, v in model.named_parameters():
    v.requires_grad = False
model = model.cuda()
>>>>>>> parent of 6f106de (add run on CPU)

print('Model path {:s}. \nTesting...'.format(model_path))

idx = 0
for path in glob.glob(test_img_folder):
    idx += 1
    base = osp.splitext(osp.basename(path))[0]
    print(idx, base)
    # read images
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    img = img * 1.0 / 255
    img = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    img_LR = img.unsqueeze(0)
    img_LR = img_LR.cuda()

    with torch.no_grad():
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()
    cv2.imwrite('results/{:s}_rlt.png'.format(base), output)
