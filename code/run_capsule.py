""" top level run script """
import os
import json
import time
import argparse

from aind_codeocean_api.codeocean import CodeOceanClient
from aind_codeocean_api.models.computations_requests import RunCapsuleRequest, ComputationNamedParameter, ComputationProcess, ComputationDataAsset

from codeocean_utils import get_codeocean_client, get_response_content_as_dict, is_computation_complete

def create_pipeline_computation_processes(processor_full_name,
                                         fix_data_asset_name, 
                                         mov_data_asset_name, 
                                         fix_multiscale_root_path,
                                         mov_multiscale_root_path,
                                         mov_segmentation_path,
                                         apply_masks_before_alignment=True,
                                         fix_lower_bound=None,
                                         fix_upper_bound=None,
                                         mov_lower_bound=None,
                                         move_upper_bound=None,
                                         overlap=0.125,
                                         global_alignment_multiscale_level=4,
                                         local_alignment_multiscale_level=2,
                                         save_transform_steps=False,
                                         ):

    

    processes = [
        ComputationProcess(
            name="capsule_aind_mfish_rounds_registration_parameter_handler_8",
            named_parameters=[
                ComputationNamedParameter("fix_data_asset_name", fix_data_asset_name),
                ComputationNamedParameter("mov_data_asset_name", mov_data_asset_name),
                ComputationNamedParameter("fix_multiscale_root_path", fix_multiscale_root_path),
                ComputationNamedParameter("mov_multiscale_root_path", mov_multiscale_root_path),
                ComputationNamedParameter("mov_segmentation_path", mov_segmentation_path),
                ComputationNamedParameter("apply_masks_before_alignment", str(apply_masks_before_alignment)),
                ComputationNamedParameter("fix_lower_bound", None),# str(fix_lower_bound)),
                ComputationNamedParameter("fix_upper_bound", None),# str(fix_upper_bound)),
                ComputationNamedParameter("mov_lower_bound", None),# str(mov_lower_bound)),
                ComputationNamedParameter("move_upper_bound", None),# str(move_upper_bound)),
                ComputationNamedParameter("overlap", str(overlap)),
                ComputationNamedParameter("global_alignment_multiscale_level", str(global_alignment_multiscale_level)),
                ComputationNamedParameter("local_alignment_multiscale_level", str(local_alignment_multiscale_level)),
                ComputationNamedParameter("save_transform_steps", str(save_transform_steps))
            ]
        ),
        ComputationProcess(
            # Prepare
            name='capsule_aind_mfish_rounds_registration_capsule_3',
        ),
        ComputationProcess(
            # Global Affine
            name='capsule_aind_mfish_rounds_registration_capsule_2',
        ),
        ComputationProcess(
            # Compute
            name='capsule_aind_mfish_rounds_registration_capsule_5',
        ),
        ComputationProcess(
            # Collect
            name='capsule_aind_mfish_rounds_registration_capsule_6',
        ),
                ComputationProcess(
            name='capsule_aind_mfish_rounds_apply_transform_10'
        ),    
        ComputationProcess(
            name='capsule_aind_pipeline_processing_metadata_aggregator_11',
            named_parameters = [
                ComputationNamedParameter("processor_full_name", "Carson Berry")
            ]
        ),
        ComputationProcess(
            name='capsule_aind_mfish_rounds_upload_metadata_12'
        )
    ]
    return processes


def start_blocking_pipeline_run(params):

    codeocean_client = get_codeocean_client()

    segmentation_data_id = params['mov_segmentation_data_asset_id']

    print(f'segmentation_data_asset_id {segmentation_data_id}')

    
    mask_mount = "local_segmentation_mount"
    pipeline_processes = create_pipeline_computation_processes(**params)
    
    run_pipeline_request = RunCapsuleRequest(
        pipeline_id=params['pipeline_id']
        processes=pipeline_processes,
        data_assets = [ComputationDataAsset(id=segmentation_data_id, mount=mask_mount)]
    )
    
    
    # Submit run request and get computation_id for polling.
    print("Submitting run with parameters", params)
    response = codeocean_client.run_capsule(run_pipeline_request)
    print(f'Response {response}')
    computation_id = get_response_content_as_dict(response)['id']
    
    while(not is_computation_complete(codeocean_client, computation_id)):
      time.sleep(30) # wait for poll

def parse_args():
    parser = argparse.ArgumentParser(description="Argument parser for alignment processing.")

    parser.add_argument('--processor_full_name', type=str, required=True,
                        help='Full name of the processor.')
    parser.add_argument('--fix_data_asset_name', type=str, required=True,
                        help='Fixed data asset name.')
    parser.add_argument('--mov_data_asset_name', type=str, required=True,
                        help='Moving data asset name.')
    parser.add_argument('--fix_multiscale_root_path', type=str, required=True,
                        help='Path to the fixed multiscale root.')
    parser.add_argument('--mov_multiscale_root_path', type=str, required=True,
                        help='Path to the moving multiscale root.')
    parser.add_argument('--mov_segmentation_path', type=str, required=True,
                        help='Path to the moving segmentation.')
    parser.add_argument('--mov_segmentation_data_asset_id', type=str, required=True,
                        help='Data asset ID for the moving segmentation.')
    parser.add_argument('--global_alignment_multiscale_level', type=int, required=True,
                        help='Global alignment multiscale level.')
    parser.add_argument('--local_alignment_multiscale_level', type=int, required=True,
                        help='Local alignment multiscale level.')

    return parser.parse_args()


def run():
    args = parse_args()
    args_dict = args.__dict__
    print(args_dict)

    start_blocking_pipeline_run(args_dict)

if __name__ == "__main__": run()