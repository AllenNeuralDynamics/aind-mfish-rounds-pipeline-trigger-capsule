# AIND mFISH Rounds Pipeline Trigger Capsule

This capsule is used to trigger the **aind-mfish-rounds-registration-pipeline**.

## How to Use

For single runs, the most convenient method is to use **Code Ocean's App Panel** to supply parameters.

### Parameters

- **`processor_full_name`**  
  *Description:* Used to comply with the `processing.json` schema.  
  *Example:* `"Sean McCulloch"`

- **`fix_data_asset_name`**  
  *Description:* Name of the data asset for the fixed image.  
  *Example:* `"HCR_732195-ROI2-cell21_2024-06-19_06-00-00"`

- **`mov_data_asset_name`**  
  *Description:* Name of the data asset for the moving image (usually the first round).  
  *Example:* `"HCR_732195-ROI2-cell21_2024-06-15_06-00-00"`

- **`fix_multiscale_root_path`**  
  *Description:* Path to the fixed multiscale root.  
  *Example:* `"s3://aind-open-data/HCR_732195-ROI2-cell21_2024-06-19_06-00-00/SPIM.ome.zarr/Tile_X_0000_Y_0000_Z_0000_ch_405.zarr"`

- **`mov_multiscale_root_path`**  
  *Description:* Path to the moving multiscale root.  
  *Example:* `"s3://aind-open-data/HCR_732195-ROI2-cell21_2024-06-15_06-00-00/SPIM.ome.zarr/Tile_X_0000_Y_0000_Z_0000_ch_405.zarr"`

- **`mov_segmentation_path`**  
  *Description:* Path to the moving segmentation within the segmentation data-asset.  
  *Example:* `"/data/local_segmentation_mount/HCR_732195-ROI2-cell21_2024-06-15_06-00-00/segmentation_mask.zarr"`

- **`mov_segmentation_data_asset_id`**  
  *Description:* Data asset ID for the moving segmentation.  
  *Example:* `"c31a90e5-0764-4969-8347-0d43fdb14c02"`

- **`global_alignment_multiscale_level`**  
  *Description:* Global alignment multiscale level.  
  *Example:* `2`

- **`local_alignment_multiscale_level`**  
  *Description:* Local alignment multiscale level.  
  *Example:* `0`

- **`pipeline_id`**  
  *Description:* Code Ocean ID for the pipeline to call.  
  *Example:* `"37affaa2-fb51-4fb6-8012-415e644c4023"`
---
