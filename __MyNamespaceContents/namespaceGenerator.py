import argparse
import string


def load_default_args():
    args = argparse.Namespace()

    args.alpha = 0.8
    args.bbox_thr = 0.3
    args.det_cat_id = 0
    args.det_checkpoint = 'https://download.openmmlab.com/mmpose/v1/projects/rtmpose/rtmdet_m_8xb32-100e_coco-obj365-person-235e8209.pth'
    args.det_config = 'mmdetection_cfg/rtmdet_m_640-8xb32_coco-person.py'
    args.device = 'cuda'
    args.draw_bbox = False
    args.draw_heatmap = False
    args.input = input
    args.kpt_thr = 0.3
    args.nms_thr = 0.3
    args.output_root = 'vis_results/'
    args.pose_checkpoint = 'https://download.openmmlab.com/mmpose/v1/projects/rtmposev1/rtmpose-m_simcc-body7_pt-body7_420e-256x192-e48f03d0_20230504.pth'
    args.pose_config = '../configs/body_2d_keypoint/rtmpose/body8/rtmpose-m_8xb256-420e_body8-256x192.py'
    args.radius = 3
    args.save_predictions = False
    args.show = True
    args.show_interval = 0
    args.show_kpt_idx = False
    args.skeleton_style = 'mmpose'
    args.thickness = 1

    return args

def __demo(input:string='') -> argparse.Namespace:
    args = load_default_args()
    args.input = input
    return args

def __image_demo(input:string='../tests/data/coco/000000197388.jpg') -> argparse.Namespace:
    """For Pycharm debug without using bash
    """
    args = load_default_args()
    args.input = input
    return args


def __vedio_demo(input:string='../tests/data/posetrack18/videos/000001_mpiinew_test/000001_mpiinew_test.mp4') -> argparse.Namespace:
    args = load_default_args()
    args.input = input
    return args
