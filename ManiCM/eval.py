if __name__ == "__main__":
    import sys
    import os
    import pathlib

    ROOT_DIR = str(pathlib.Path(__file__).parent.parent.parent)
    sys.path.append(ROOT_DIR)
    os.chdir(ROOT_DIR)

import os
import hydra
import torch
import dill
from omegaconf import OmegaConf
import pathlib
from train_DPTeacher import TrainDPTeacherWorkspace

OmegaConf.register_new_resolver("eval", eval, replace=True)
    

@hydra.main(
    version_base=None,
    config_path=str(pathlib.Path(__file__).parent.joinpath(
        'diffusion_policy_3d', 'config'))
)
def main(cfg):

    cfg.policy.num_inference_steps = 100  # DDIM steps
    cfg.task.env_runner.max_steps = 400
    # print(cfg.env_runner)

    workspace = TrainDPTeacherWorkspace(cfg,output_dir=cfg.output_dir)
    workspace.eval(output_dir='/home/clear/ManiCM/ManiCM/outputs/dp_teacher/square',
                   checkpoint_path='/home/clear/ManiCM/ManiCM/latest.ckpt')

if __name__ == "__main__":
    main()
