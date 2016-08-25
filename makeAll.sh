#!/bin/bash

# # Male phantom:
# python ../python/ICRPtoSTL.py male  adrenal_left 
# python ../python/ICRPtoSTL.py male  adrenal_right 
# python ../python/ICRPtoSTL.py male  anterior_nasal_passage_et1 
# python ../python/ICRPtoSTL.py male  posterior_nasal_passage_down_to_larynx_et2 
# python ../python/ICRPtoSTL.py male  oral_mucosa_tongue 
# python ../python/ICRPtoSTL.py male  oral_mucosa_lips_and_cheeks 
# python ../python/ICRPtoSTL.py male  trachea 
# python ../python/ICRPtoSTL.py male  bronchi 
# python ../python/ICRPtoSTL.py male  blood_vessels_head 
# python ../python/ICRPtoSTL.py male  blood_vessels_trunk 
# python ../python/ICRPtoSTL.py male  blood_vessels_arms 
# python ../python/ICRPtoSTL.py male  blood_vessels_legs 
# python ../python/ICRPtoSTL.py male  humeri_upper_half_cortical 
# python ../python/ICRPtoSTL.py male  humeri_upper_half_spongiosa 
# python ../python/ICRPtoSTL.py male  humeri_upper_half_medullary_cavity 
# python ../python/ICRPtoSTL.py male  humeri_lower_half_cortical 
# python ../python/ICRPtoSTL.py male  humeri_lower_half_spongiosa 
# python ../python/ICRPtoSTL.py male  humeri_lower_half_medullary_cavity 
# python ../python/ICRPtoSTL.py male  ulnae_and_radii_cortical 
# python ../python/ICRPtoSTL.py male  ulnae_and_radii_spongiosa 
# python ../python/ICRPtoSTL.py male  ulnae_and_radii_medullary_cavity 
# python ../python/ICRPtoSTL.py male  wrists_and_hand_bones_cortical 
# python ../python/ICRPtoSTL.py male  wrists_and_hand_bones_spongiosa 
# python ../python/ICRPtoSTL.py male  clavicles_cortical 
# python ../python/ICRPtoSTL.py male  clavicles_spongiosa 
# python ../python/ICRPtoSTL.py male  cranium_cortical 
# python ../python/ICRPtoSTL.py male  cranium_spongiosa 
# python ../python/ICRPtoSTL.py male  femora_upper_half_cortical 
# python ../python/ICRPtoSTL.py male  femora_upper_half_spongiosa 
# python ../python/ICRPtoSTL.py male  femora_upper_half_medullary_cavity 
# python ../python/ICRPtoSTL.py male  femora_lower_half_cortical 
# python ../python/ICRPtoSTL.py male  femora_lower_half_spongiosa 
# python ../python/ICRPtoSTL.py male  femora_lower_half_medullary_cavity 
# python ../python/ICRPtoSTL.py male  tibiae_fibulae_and_patellae_cortical 
# python ../python/ICRPtoSTL.py male  tibiae_fibulae_and_patellae_spongiosa 
# python ../python/ICRPtoSTL.py male  tibiae_fibulae_and_patellae_medullary_cavity 
# python ../python/ICRPtoSTL.py male  ankles_and_foot_bones_cortical 
# python ../python/ICRPtoSTL.py male  ankles_and_foot_bones_spongiosa 
# python ../python/ICRPtoSTL.py male  mandible_cortical 
# python ../python/ICRPtoSTL.py male  mandible_spongiosa 
# python ../python/ICRPtoSTL.py male  pelvis_cortical 
# python ../python/ICRPtoSTL.py male  pelvis_spongiosa 
# python ../python/ICRPtoSTL.py male  ribs_cortical 
# python ../python/ICRPtoSTL.py male  ribs_spongiosa 
# python ../python/ICRPtoSTL.py male  scapulae_cortical 
# python ../python/ICRPtoSTL.py male  scapulae_spongiosa 
# python ../python/ICRPtoSTL.py male  cervical_spine_cortical 
# python ../python/ICRPtoSTL.py male  cervical_spine_spongiosa 
# python ../python/ICRPtoSTL.py male  thoracic_spine_cortical 
# python ../python/ICRPtoSTL.py male  thoracic_spine_spongiosa 
# python ../python/ICRPtoSTL.py male  lumbar_spine_cortical 
# python ../python/ICRPtoSTL.py male  lumbar_spine_spongiosa 
# python ../python/ICRPtoSTL.py male  sacrum_cortical 
# python ../python/ICRPtoSTL.py male  sacrum_spongiosa 
# python ../python/ICRPtoSTL.py male  sternum_cortical 
# python ../python/ICRPtoSTL.py male  sternum_spongiosa 
# python ../python/ICRPtoSTL.py male  cartilage_head 
# python ../python/ICRPtoSTL.py male  cartilage_trunk 
# python ../python/ICRPtoSTL.py male  cartilage_arms 
# python ../python/ICRPtoSTL.py male  cartilage_legs 
# python ../python/ICRPtoSTL.py male  brain 
# python ../python/ICRPtoSTL.py male  breast_left_adipose_tissue 
# python ../python/ICRPtoSTL.py male  breast_left_glandular_tissue 
# python ../python/ICRPtoSTL.py male  breast_right_adipose_tissue 
# python ../python/ICRPtoSTL.py male  breast_right_glandular_tissue 
# python ../python/ICRPtoSTL.py male  eye_lense_left 
# python ../python/ICRPtoSTL.py male  eye_bulb_left 
# python ../python/ICRPtoSTL.py male  eye_lense_right 
# python ../python/ICRPtoSTL.py male  eye_bulb_right 
# python ../python/ICRPtoSTL.py male  gall_bladder_wall 
# python ../python/ICRPtoSTL.py male  gall_bladder_contents 
# python ../python/ICRPtoSTL.py male  stomach_wall 
# python ../python/ICRPtoSTL.py male  stomach_contents 
# python ../python/ICRPtoSTL.py male  small_intestine_wall 
# python ../python/ICRPtoSTL.py male  small_intestine_contents 
# python ../python/ICRPtoSTL.py male  ascending_colon_wall 
# python ../python/ICRPtoSTL.py male  ascending_colon_contents 
# python ../python/ICRPtoSTL.py male  transverse_colon_wall_right 
# python ../python/ICRPtoSTL.py male  transverse_colon_contents_right 
# python ../python/ICRPtoSTL.py male  transverse_colon_wall_left 
# python ../python/ICRPtoSTL.py male  transverse_colon_contents_left 
# python ../python/ICRPtoSTL.py male  descending_colon_wall 
# python ../python/ICRPtoSTL.py male  descending_colon_contents 
# python ../python/ICRPtoSTL.py male  sigmoid_colon_wall 
# python ../python/ICRPtoSTL.py male  sigmoid_colon_contents 
# python ../python/ICRPtoSTL.py male  rectum_wall 
# python ../python/ICRPtoSTL.py male  heart_wall 
# python ../python/ICRPtoSTL.py male  heart_contents_blood 
# python ../python/ICRPtoSTL.py male  kidney_left_cortex 
# python ../python/ICRPtoSTL.py male  kidney_left_medulla 
# python ../python/ICRPtoSTL.py male  kidney_left_pelvis 
# python ../python/ICRPtoSTL.py male  kidney_right_cortex 
# python ../python/ICRPtoSTL.py male  kidney_right_medulla 
# python ../python/ICRPtoSTL.py male  kidney_right_pelvis 
# python ../python/ICRPtoSTL.py male  liver 
# python ../python/ICRPtoSTL.py male  lung_left_blood 
# python ../python/ICRPtoSTL.py male  lung_left_tissue 
# python ../python/ICRPtoSTL.py male  lung_right_blood 
# python ../python/ICRPtoSTL.py male  lung_right_tissue 
# python ../python/ICRPtoSTL.py male  lymphatic_nodes_extrathoracic_airways 
# python ../python/ICRPtoSTL.py male  lymphatic_nodes_thoracic_airways 
# python ../python/ICRPtoSTL.py male  lymphatic_nodes_head 
# python ../python/ICRPtoSTL.py male  lymphatic_nodes_trunk 
# python ../python/ICRPtoSTL.py male  lymphatic_nodes_arms 
# python ../python/ICRPtoSTL.py male  lymphatic_nodes_legs 
# python ../python/ICRPtoSTL.py male  muscle_head 
# python ../python/ICRPtoSTL.py male  muscle_trunk 
# python ../python/ICRPtoSTL.py male  muscle_arms 
# python ../python/ICRPtoSTL.py male  muscle_legs 
# python ../python/ICRPtoSTL.py male  oesophagus 
# python ../python/ICRPtoSTL.py male  ovary_left 
# python ../python/ICRPtoSTL.py male  ovary_right 
# python ../python/ICRPtoSTL.py male  pancreas 
# python ../python/ICRPtoSTL.py male  pituitary_gland 
# python ../python/ICRPtoSTL.py male  prostate 
# python ../python/ICRPtoSTL.py male  residual_tissue_head 
# python ../python/ICRPtoSTL.py male  residual_tissue_trunk 
# python ../python/ICRPtoSTL.py male  residual_tissue_arms 
# python ../python/ICRPtoSTL.py male  residual_tissue_legs 
# python ../python/ICRPtoSTL.py male  salivary_glands_left 
# python ../python/ICRPtoSTL.py male  salivary_glands_right 
# python ../python/ICRPtoSTL.py male  skin_head 
# python ../python/ICRPtoSTL.py male  skin_trunk 
# python ../python/ICRPtoSTL.py male  skin_arms 
# python ../python/ICRPtoSTL.py male  skin_legs 
# python ../python/ICRPtoSTL.py male  spinal_cord 
# python ../python/ICRPtoSTL.py male  spleen 
# python ../python/ICRPtoSTL.py male  teeth 
# python ../python/ICRPtoSTL.py male  testis_left 
# python ../python/ICRPtoSTL.py male  testis_right 
# python ../python/ICRPtoSTL.py male  thymus 
# python ../python/ICRPtoSTL.py male  thyroid 
# python ../python/ICRPtoSTL.py male  tongue_inner_part 
# python ../python/ICRPtoSTL.py male  tonsils 
# python ../python/ICRPtoSTL.py male  ureter_left 
# python ../python/ICRPtoSTL.py male  ureter_right 
# python ../python/ICRPtoSTL.py male  urinary_bladder_wall 
# python ../python/ICRPtoSTL.py male  urinary_bladder_contents 
# python ../python/ICRPtoSTL.py male  uterus 
# python ../python/ICRPtoSTL.py male  air_inside_body 

# Female Phantom:
python ../python/ICRPtoSTL.py female adrenal_left
python ../python/ICRPtoSTL.py female adrenal_right
python ../python/ICRPtoSTL.py female anterior_nasal_passage_et1
python ../python/ICRPtoSTL.py female posterior_nasal_passage_down_to_larynx_et2
python ../python/ICRPtoSTL.py female oral_mucosa_tongue
python ../python/ICRPtoSTL.py female oral_mucosa_lips_and_cheeks
python ../python/ICRPtoSTL.py female trachea
python ../python/ICRPtoSTL.py female bronchi
python ../python/ICRPtoSTL.py female blood_vessels_head
python ../python/ICRPtoSTL.py female blood_vessels_trunk
python ../python/ICRPtoSTL.py female blood_vessels_arms
python ../python/ICRPtoSTL.py female blood_vessels_legs
python ../python/ICRPtoSTL.py female humeri_upper_half_cortical
python ../python/ICRPtoSTL.py female humeri_upper_half_spongiosa
python ../python/ICRPtoSTL.py female humeri_upper_half_medullary_cavity
python ../python/ICRPtoSTL.py female humeri_lower_half_cortical
python ../python/ICRPtoSTL.py female humeri_lower_half_spongiosa
python ../python/ICRPtoSTL.py female humeri_lower_half_medullary_cavity
python ../python/ICRPtoSTL.py female ulnae_and_radii_cortical
python ../python/ICRPtoSTL.py female ulnae_and_radii_spongiosa
python ../python/ICRPtoSTL.py female ulnae_and_radii_medullary_cavity
python ../python/ICRPtoSTL.py female wrists_and_hand_bones_cortical
python ../python/ICRPtoSTL.py female wrists_and_hand_bones_spongiosa
python ../python/ICRPtoSTL.py female clavicles_cortical
python ../python/ICRPtoSTL.py female clavicles_spongiosa
python ../python/ICRPtoSTL.py female cranium_cortical
python ../python/ICRPtoSTL.py female cranium_spongiosa
python ../python/ICRPtoSTL.py female femora_upper_half_cortical
python ../python/ICRPtoSTL.py female femora_upper_half_spongiosa
python ../python/ICRPtoSTL.py female femora_upper_half_medullary_cavity
python ../python/ICRPtoSTL.py female femora_lower_half_cortical
python ../python/ICRPtoSTL.py female femora_lower_half_spongiosa
python ../python/ICRPtoSTL.py female femora_lower_half_medullary_cavity
python ../python/ICRPtoSTL.py female tibiae_fibulae_and_patellae_cortical
python ../python/ICRPtoSTL.py female tibiae_fibulae_and_patellae_spongiosa
python ../python/ICRPtoSTL.py female tibiae_fibulae_and_patellae_medullary_cavity
python ../python/ICRPtoSTL.py female ankles_and_foot_bones_cortical
python ../python/ICRPtoSTL.py female ankles_and_foot_bones_spongiosa
python ../python/ICRPtoSTL.py female mandible_cortical
python ../python/ICRPtoSTL.py female mandible_spongiosa
python ../python/ICRPtoSTL.py female pelvis_cortical
python ../python/ICRPtoSTL.py female pelvis_spongiosa
python ../python/ICRPtoSTL.py female ribs_cortical
python ../python/ICRPtoSTL.py female ribs_spongiosa
python ../python/ICRPtoSTL.py female scapulae_cortical
python ../python/ICRPtoSTL.py female scapulae_spongiosa
python ../python/ICRPtoSTL.py female cervical_spine_cortical
python ../python/ICRPtoSTL.py female cervical_spine_spongiosa
python ../python/ICRPtoSTL.py female thoracic_spine_cortical
python ../python/ICRPtoSTL.py female thoracic_spine_spongiosa
python ../python/ICRPtoSTL.py female lumbar_spine_cortical
python ../python/ICRPtoSTL.py female lumbar_spine_spongiosa
python ../python/ICRPtoSTL.py female sacrum_cortical
python ../python/ICRPtoSTL.py female sacrum_spongiosa
python ../python/ICRPtoSTL.py female sternum_cortical
python ../python/ICRPtoSTL.py female sternum_spongiosa
python ../python/ICRPtoSTL.py female cartilage_head
python ../python/ICRPtoSTL.py female cartilage_trunk
python ../python/ICRPtoSTL.py female cartilage_arms
python ../python/ICRPtoSTL.py female cartilage_legs
python ../python/ICRPtoSTL.py female brain
python ../python/ICRPtoSTL.py female breast_left_adipose_tissue
python ../python/ICRPtoSTL.py female breast_left_glandular_tissue
python ../python/ICRPtoSTL.py female breast_right_adipose_tissue
python ../python/ICRPtoSTL.py female breast_right_glandular_tissue
python ../python/ICRPtoSTL.py female eye_lense_left
python ../python/ICRPtoSTL.py female eye_bulb_left
python ../python/ICRPtoSTL.py female eye_lense_right
python ../python/ICRPtoSTL.py female eye_bulb_right
python ../python/ICRPtoSTL.py female gall_bladder_wall
python ../python/ICRPtoSTL.py female gall_bladder_contents
python ../python/ICRPtoSTL.py female stomach_wall
python ../python/ICRPtoSTL.py female stomach_contents
python ../python/ICRPtoSTL.py female small_intestine_wall
python ../python/ICRPtoSTL.py female small_intestine_contents
python ../python/ICRPtoSTL.py female ascending_colon_wall
python ../python/ICRPtoSTL.py female ascending_colon_contents
python ../python/ICRPtoSTL.py female transverse_colon_wall_right
python ../python/ICRPtoSTL.py female transverse_colon_contents_right
python ../python/ICRPtoSTL.py female transverse_colon_wall_left
python ../python/ICRPtoSTL.py female transverse_colon_contents_left
python ../python/ICRPtoSTL.py female descending_colon_wall
python ../python/ICRPtoSTL.py female descending_colon_contents
python ../python/ICRPtoSTL.py female sigmoid_colon_wall
python ../python/ICRPtoSTL.py female sigmoid_colon_contents
python ../python/ICRPtoSTL.py female rectum_wall
python ../python/ICRPtoSTL.py female heart_wall
python ../python/ICRPtoSTL.py female heart_contents_blood
python ../python/ICRPtoSTL.py female kidney_left_cortex
python ../python/ICRPtoSTL.py female kidney_left_medulla
python ../python/ICRPtoSTL.py female kidney_left_pelvis
python ../python/ICRPtoSTL.py female kidney_right_cortex
python ../python/ICRPtoSTL.py female kidney_right_medulla
python ../python/ICRPtoSTL.py female kidney_right_pelvis
python ../python/ICRPtoSTL.py female liver
python ../python/ICRPtoSTL.py female lung_left_blood
python ../python/ICRPtoSTL.py female lung_left_tissue
python ../python/ICRPtoSTL.py female lung_right_blood
python ../python/ICRPtoSTL.py female lung_right_tissue
python ../python/ICRPtoSTL.py female lymphatic_nodes_extrathoracic_airways
python ../python/ICRPtoSTL.py female lymphatic_nodes_thoracic_airways
python ../python/ICRPtoSTL.py female lymphatic_nodes_head
python ../python/ICRPtoSTL.py female lymphatic_nodes_trunk
python ../python/ICRPtoSTL.py female lymphatic_nodes_arms
python ../python/ICRPtoSTL.py female lymphatic_nodes_legs
python ../python/ICRPtoSTL.py female muscle_head
python ../python/ICRPtoSTL.py female muscle_trunk
python ../python/ICRPtoSTL.py female muscle_arms
python ../python/ICRPtoSTL.py female muscle_legs
python ../python/ICRPtoSTL.py female oesophagus
python ../python/ICRPtoSTL.py female ovary_left
python ../python/ICRPtoSTL.py female ovary_right
python ../python/ICRPtoSTL.py female pancreas
python ../python/ICRPtoSTL.py female pituitary_gland
python ../python/ICRPtoSTL.py female prostate
python ../python/ICRPtoSTL.py female residual_tissue_head
python ../python/ICRPtoSTL.py female residual_tissue_trunk
python ../python/ICRPtoSTL.py female residual_tissue_arms
python ../python/ICRPtoSTL.py female residual_tissue_legs
python ../python/ICRPtoSTL.py female salivary_glands_left
python ../python/ICRPtoSTL.py female salivary_glands_right
python ../python/ICRPtoSTL.py female skin_head
python ../python/ICRPtoSTL.py female skin_trunk
python ../python/ICRPtoSTL.py female skin_arms
python ../python/ICRPtoSTL.py female skin_legs
python ../python/ICRPtoSTL.py female spinal_cord
python ../python/ICRPtoSTL.py female spleen
python ../python/ICRPtoSTL.py female teeth
python ../python/ICRPtoSTL.py female testis_left
python ../python/ICRPtoSTL.py female testis_right
python ../python/ICRPtoSTL.py female thymus
python ../python/ICRPtoSTL.py female thyroid
python ../python/ICRPtoSTL.py female tongue_inner_part
python ../python/ICRPtoSTL.py female tonsils
python ../python/ICRPtoSTL.py female ureter_left
python ../python/ICRPtoSTL.py female ureter_right
python ../python/ICRPtoSTL.py female urinary_bladder_wall
python ../python/ICRPtoSTL.py female urinary_bladder_contents
python ../python/ICRPtoSTL.py female uterus
python ../python/ICRPtoSTL.py female air_inside_body 


