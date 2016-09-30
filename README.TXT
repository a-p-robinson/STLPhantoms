
 ##############################################################################
 # Code for generating MRTDosimetry Phantom STL models			      #
 # 									      #
 # Author: Andrew Robinson (andrew.robinson@npl.co.uk)			      #
 # 									      #
 # This code provides methods for converting voxelised data to STL files.     #
 # 									      #
 # ++ Currently supported:						      #
 # 									      #
 #  * ICRP 110								      #
 #    http://www.icrp.org/publication.asp?id=ICRP%20Publication%20110	      #
 #    - Phantom data files must be supplied seperatly			      #
 # 									      #
 # ++ Additional available code (please contact for details):                 #
 #                                                                            #
 #  * Dicom image (with optional binary mask)				      #
 #    This code is available but has nt yet been integrated into this release.#
 # 									      #
 # ++ Still to be implemented:						      #
 # 									      #
 #  * XCAT (Need to get access to data)					      #
 ##############################################################################
 									 
######
Usage:
######

* ICRP 110

1. Download the ICRP data and extract to a directory.
2. Edit "dataDir" variable in python/ICRPtoSTL.py to point to location of data
3. python python/ICRPtoSTL.py MODEL NAME
 - where MODEL = male or female
 - and   NAME  is chossen from the following list.

---------------------------------
ICRP 110 Refernce Phantom [AM]
---------------------------------
 organID:    1 name: adrenal_left
 organID:    2 name: adrenal_right
 organID:    3 name: anterior_nasal_passage_et1
 organID:    4 name: posterior_nasal_passage_down_to_larynx_et2
 organID:    5 name: oral_mucosa_tongue
 organID:    6 name: oral_mucosa_lips_and_cheeks
 organID:    7 name: trachea
 organID:    8 name: bronchi
 organID:    9 name: blood_vessels_head
 organID:   10 name: blood_vessels_trunk
 organID:   11 name: blood_vessels_arms
 organID:   12 name: blood_vessels_legs
 organID:   13 name: humeri_upper_half_cortical
 organID:   14 name: humeri_upper_half_spongiosa
 organID:   15 name: humeri_upper_half_medullary_cavity
 organID:   16 name: humeri_lower_half_cortical
 organID:   17 name: humeri_lower_half_spongiosa
 organID:   18 name: humeri_lower_half_medullary_cavity
 organID:   19 name: ulnae_and_radii_cortical
 organID:   20 name: ulnae_and_radii_spongiosa
 organID:   21 name: ulnae_and_radii_medullary_cavity
 organID:   22 name: wrists_and_hand_bones_cortical
 organID:   23 name: wrists_and_hand_bones_spongiosa
 organID:   24 name: clavicles_cortical
 organID:   25 name: clavicles_spongiosa
 organID:   26 name: cranium_cortical
 organID:   27 name: cranium_spongiosa
 organID:   28 name: femora_upper_half_cortical
 organID:   29 name: femora_upper_half_spongiosa
 organID:   30 name: femora_upper_half_medullary_cavity
 organID:   31 name: femora_lower_half_cortical
 organID:   32 name: femora_lower_half_spongiosa
 organID:   33 name: femora_lower_half_medullary_cavity
 organID:   34 name: tibiae_fibulae_and_patellae_cortical
 organID:   35 name: tibiae_fibulae_and_patellae_spongiosa
 organID:   36 name: tibiae_fibulae_and_patellae_medullary_cavity
 organID:   37 name: ankles_and_foot_bones_cortical
 organID:   38 name: ankles_and_foot_bones_spongiosa
 organID:   39 name: mandible_cortical
 organID:   40 name: mandible_spongiosa
 organID:   41 name: pelvis_cortical
 organID:   42 name: pelvis_spongiosa
 organID:   43 name: ribs_cortical
 organID:   44 name: ribs_spongiosa
 organID:   45 name: scapulae_cortical
 organID:   46 name: scapulae_spongiosa
 organID:   47 name: cervical_spine_cortical
 organID:   48 name: cervical_spine_spongiosa
 organID:   49 name: thoracic_spine_cortical
 organID:   50 name: thoracic_spine_spongiosa
 organID:   51 name: lumbar_spine_cortical
 organID:   52 name: lumbar_spine_spongiosa
 organID:   53 name: sacrum_cortical
 organID:   54 name: sacrum_spongiosa
 organID:   55 name: sternum_cortical
 organID:   56 name: sternum_spongiosa
 organID:   57 name: cartilage_head
 organID:   58 name: cartilage_trunk
 organID:   59 name: cartilage_arms
 organID:   60 name: cartilage_legs
 organID:   61 name: brain
 organID:   62 name: breast_left_adipose_tissue
 organID:   63 name: breast_left_glandular_tissue
 organID:   64 name: breast_right_adipose_tissue
 organID:   65 name: breast_right_glandular_tissue
 organID:   66 name: eye_lense_left
 organID:   67 name: eye_bulb_left
 organID:   68 name: eye_lense_right
 organID:   69 name: eye_bulb_right
 organID:   70 name: gall_bladder_wall
 organID:   71 name: gall_bladder_contents
 organID:   72 name: stomach_wall
 organID:   73 name: stomach_contents
 organID:   74 name: small_intestine_wall
 organID:   75 name: small_intestine_contents
 organID:   76 name: ascending_colon_wall
 organID:   77 name: ascending_colon_contents
 organID:   78 name: transverse_colon_wall_right
 organID:   79 name: transverse_colon_contents_right
 organID:   80 name: transverse_colon_wall_left
 organID:   81 name: transverse_colon_contents_left
 organID:   82 name: descending_colon_wall
 organID:   83 name: descending_colon_contents
 organID:   84 name: sigmoid_colon_wall
 organID:   85 name: sigmoid_colon_contents
 organID:   86 name: rectum_wall
 organID:   87 name: heart_wall
 organID:   88 name: heart_contents_blood
 organID:   89 name: kidney_left_cortex
 organID:   90 name: kidney_left_medulla
 organID:   91 name: kidney_left_pelvis
 organID:   92 name: kidney_right_cortex
 organID:   93 name: kidney_right_medulla
 organID:   94 name: kidney_right_pelvis
 organID:   95 name: liver
 organID:   96 name: lung_left_blood
 organID:   97 name: lung_left_tissue
 organID:   98 name: lung_right_blood
 organID:   99 name: lung_right_tissue
 organID:  100 name: lymphatic_nodes_extrathoracic_airways
 organID:  101 name: lymphatic_nodes_thoracic_airways
 organID:  102 name: lymphatic_nodes_head
 organID:  103 name: lymphatic_nodes_trunk
 organID:  104 name: lymphatic_nodes_arms
 organID:  105 name: lymphatic_nodes_legs
 organID:  106 name: muscle_head
 organID:  107 name: muscle_trunk
 organID:  108 name: muscle_arms
 organID:  109 name: muscle_legs
 organID:  110 name: oesophagus
 organID:  111 name: ovary_left
 organID:  112 name: ovary_right
 organID:  113 name: pancreas
 organID:  114 name: pituitary_gland
 organID:  115 name: prostate
 organID:  116 name: residual_tissue_head
 organID:  117 name: residual_tissue_trunk
 organID:  118 name: residual_tissue_arms
 organID:  119 name: residual_tissue_legs
 organID:  120 name: salivary_glands_left
 organID:  121 name: salivary_glands_right
 organID:  122 name: skin_head
 organID:  123 name: skin_trunk
 organID:  124 name: skin_arms
 organID:  125 name: skin_legs
 organID:  126 name: spinal_cord
 organID:  127 name: spleen
 organID:  128 name: teeth
 organID:  129 name: testis_left
 organID:  130 name: testis_right
 organID:  131 name: thymus
 organID:  132 name: thyroid
 organID:  133 name: tongue_inner_part
 organID:  134 name: tonsils
 organID:  135 name: ureter_left
 organID:  136 name: ureter_right
 organID:  137 name: urinary_bladder_wall
 organID:  138 name: urinary_bladder_contents
 organID:  139 name: uterus
 organID:  140 name: air_inside_body

---------------------------------
ICRP 110 Refernce Phantom [AF]
---------------------------------
 organID:    1 name: adrenal_left
 organID:    2 name: adrenal_right
 organID:    3 name: anterior_nasal_passage_et1
 organID:    4 name: posterior_nasal_passage_down_to_larynx_et2
 organID:    5 name: oral_mucosa_tongue
 organID:    6 name: oral_mucosa_lips_and_cheeks
 organID:    7 name: trachea
 organID:    8 name: bronchi
 organID:    9 name: blood_vessels_head
 organID:   10 name: blood_vessels_trunk
 organID:   11 name: blood_vessels_arms
 organID:   12 name: blood_vessels_legs
 organID:   13 name: humeri_upper_half_cortical
 organID:   14 name: humeri_upper_half_spongiosa
 organID:   15 name: humeri_upper_half_medullary_cavity
 organID:   16 name: humeri_lower_half_cortical
 organID:   17 name: humeri_lower_half_spongiosa
 organID:   18 name: humeri_lower_half_medullary_cavity
 organID:   19 name: ulnae_and_radii_cortical
 organID:   20 name: ulnae_and_radii_spongiosa
 organID:   21 name: ulnae_and_radii_medullary_cavity
 organID:   22 name: wrists_and_hand_bones_cortical
 organID:   23 name: wrists_and_hand_bones_spongiosa
 organID:   24 name: clavicles_cortical
 organID:   25 name: clavicles_spongiosa
 organID:   26 name: cranium_cortical
 organID:   27 name: cranium_spongiosa
 organID:   28 name: femora_upper_half_cortical
 organID:   29 name: femora_upper_half_spongiosa
 organID:   30 name: femora_upper_half_medullary_cavity
 organID:   31 name: femora_lower_half_cortical
 organID:   32 name: femora_lower_half_spongiosa
 organID:   33 name: femora_lower_half_medullary_cavity
 organID:   34 name: tibiae_fibulae_and_patellae_cortical
 organID:   35 name: tibiae_fibulae_and_patellae_spongiosa
 organID:   36 name: tibiae_fibulae_and_patellae_medullary_cavity
 organID:   37 name: ankles_and_foot_bones_cortical
 organID:   38 name: ankles_and_foot_bones_spongiosa
 organID:   39 name: mandible_cortical
 organID:   40 name: mandible_spongiosa
 organID:   41 name: pelvis_cortical
 organID:   42 name: pelvis_spongiosa
 organID:   43 name: ribs_cortical
 organID:   44 name: ribs_spongiosa
 organID:   45 name: scapulae_cortical
 organID:   46 name: scapulae_spongiosa
 organID:   47 name: cervical_spine_cortical
 organID:   48 name: cervical_spine_spongiosa
 organID:   49 name: thoracic_spine_cortical
 organID:   50 name: thoracic_spine_spongiosa
 organID:   51 name: lumbar_spine_cortical
 organID:   52 name: lumbar_spine_spongiosa
 organID:   53 name: sacrum_cortical
 organID:   54 name: sacrum_spongiosa
 organID:   55 name: sternum_cortical
 organID:   56 name: sternum_spongiosa
 organID:   57 name: cartilage_head
 organID:   58 name: cartilage_trunk
 organID:   59 name: cartilage_arms
 organID:   60 name: cartilage_legs
 organID:   61 name: brain
 organID:   62 name: breast_left_adipose_tissue
 organID:   63 name: breast_left_glandular_tissue
 organID:   64 name: breast_right_adipose_tissue
 organID:   65 name: breast_right_glandular_tissue
 organID:   66 name: eye_lense_left
 organID:   67 name: eye_bulb_left
 organID:   68 name: eye_lense_right
 organID:   69 name: eye_bulb_right
 organID:   70 name: gall_bladder_wall
 organID:   71 name: gall_bladder_contents
 organID:   72 name: stomach_wall
 organID:   73 name: stomach_contents
 organID:   74 name: small_intestine_wall
 organID:   75 name: small_intestine_contents
 organID:   76 name: ascending_colon_wall
 organID:   77 name: ascending_colon_contents
 organID:   78 name: transverse_colon_wall_right
 organID:   79 name: transverse_colon_contents_right
 organID:   80 name: transverse_colon_wall_left
 organID:   81 name: transverse_colon_contents_left
 organID:   82 name: descending_colon_wall
 organID:   83 name: descending_colon_contents
 organID:   84 name: sigmoid_colon_wall
 organID:   85 name: sigmoid_colon_contents
 organID:   86 name: rectum_wall
 organID:   87 name: heart_wall
 organID:   88 name: heart_contents_blood
 organID:   89 name: kidney_left_cortex
 organID:   90 name: kidney_left_medulla
 organID:   91 name: kidney_left_pelvis
 organID:   92 name: kidney_right_cortex
 organID:   93 name: kidney_right_medulla
 organID:   94 name: kidney_right_pelvis
 organID:   95 name: liver
 organID:   96 name: lung_left_blood
 organID:   97 name: lung_left_tissue
 organID:   98 name: lung_right_blood
 organID:   99 name: lung_right_tissue
 organID:  100 name: lymphatic_nodes_extrathoracic_airways
 organID:  101 name: lymphatic_nodes_thoracic_airways
 organID:  102 name: lymphatic_nodes_head
 organID:  103 name: lymphatic_nodes_trunk
 organID:  104 name: lymphatic_nodes_arms
 organID:  105 name: lymphatic_nodes_legs
 organID:  106 name: muscle_head
 organID:  107 name: muscle_trunk
 organID:  108 name: muscle_arms
 organID:  109 name: muscle_legs
 organID:  110 name: oesophagus
 organID:  111 name: ovary_left
 organID:  112 name: ovary_right
 organID:  113 name: pancreas
 organID:  114 name: pituitary_gland
 organID:  115 name: prostate
 organID:  116 name: residual_tissue_head
 organID:  117 name: residual_tissue_trunk
 organID:  118 name: residual_tissue_arms
 organID:  119 name: residual_tissue_legs
 organID:  120 name: salivary_glands_left
 organID:  121 name: salivary_glands_right
 organID:  122 name: skin_head
 organID:  123 name: skin_trunk
 organID:  124 name: skin_arms
 organID:  125 name: skin_legs
 organID:  126 name: spinal_cord
 organID:  127 name: spleen
 organID:  128 name: teeth
 organID:  129 name: testis_left
 organID:  130 name: testis_right
 organID:  131 name: thymus
 organID:  132 name: thyroid
 organID:  133 name: tongue_inner_part
 organID:  134 name: tonsils
 organID:  135 name: ureter_left
 organID:  136 name: ureter_right
 organID:  137 name: urinary_bladder_wall
 organID:  138 name: urinary_bladder_contents
 organID:  139 name: uterus
 organID:  140 name: air_inside_body

