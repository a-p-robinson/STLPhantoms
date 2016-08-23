#!/usr/bin/python
#
# ICRP No 110 Dummy Phantom builder example
# - the association of the organ_index to the voxel region is left to the user as an exercise
# - blood and bone ratio are not used 
#
# Vittorio Boccone, July '16
#
# https://github.com/drbokko/fluka-snippets
#
# License: This is free and unencumbered software released into the public domain.
#          https://github.com/drbokko/fluka-snippets/blob/master/LICENSE
#


import struct
import sys

organ_dictionary  = {} # Internally used dictionary
tissue_dictionary = {} # Internally used dictionary

material          = [] # will contain the line of the fluka input which will printed to the standard output

organ_ascii_file = "MA_organ.dat"
media_ascii_file = "MA_media.dat"

# define materials which are not predefined
material.append("*...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....")
material.append("MATERIAL         15.                 2.2                              PHOSPHO  ")
material.append("MATERIAL         16.                 2.0                              SULFUR   ")
material.append("MATERIAL         17.           0.0029947                              CHLORINE ")
material.append("MATERIAL         53.                4.93                              IODINE   ")


#
# Parsing media ascii file and store the information into the tissue_dictionary
#
with open(media_ascii_file, "r") as file:

    # reading fixed format
    fieldwidths = (5, -1, 70,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5,-1,5)  # negative widths represent ignored padding fields
    fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                        for fw in fieldwidths)
    fieldstruct = struct.Struct(fmtstring)
    parse = fieldstruct.unpack_from

    # drop first four lines (info lines)
    info_lines = []
    for line in range(0,3):
        info_lines.append(file.readline())

    # loop on the file and save the infos in a dictionary
    for line in file.readlines():
        fields = parse(line)
        tissue_dictionary[int(fields[0])] = { 'tissue_index' : int(fields[0]),
                                              'description'  : fields[1].rstrip(), 
                                              'compound'     : {
                                                  '  HYDROGEN'    : float(fields[2]), 
                                                  '    CARBON'    : float(fields[3]), 
                                                  '  NITROGEN'    : float(fields[4]), 
                                                  '    OXYGEN'    : float(fields[5]), 
                                                  '    SODIUM'    : float(fields[6]), 
                                                  '  MAGNESIU'    : float(fields[7]), 
                                                  '   PHOSPHO'    : float(fields[8]), 
                                                  '    SULFUR'    : float(fields[9]), 
                                                  '  CHLORINE'    : float(fields[10]), 
                                                  '  POTASSIU'    : float(fields[11]), 
                                                  '   CALCIUM'    : float(fields[12]), 
                                                  '      IRON'    : float(fields[13]), 
                                                  '    IODINE'    : float(fields[14])    }}
    



#
# Parsing organs ascii file
#
with open(organ_ascii_file, "r") as file:
    fieldwidths = (5, -1, 47,-1,3,-4,5)  # negative widths represent ignored padding fields
    fmtstring = ' '.join('{}{}'.format(abs(fw), 'x' if fw < 0 else 's')
                        for fw in fieldwidths)
    fieldstruct = struct.Struct(fmtstring)

    # drop first four lines
    info_lines = []
    for line in range(0,4):
        info_lines.append(file.readline())

    parse = fieldstruct.unpack_from

    for line in file.readlines():
        fields = parse(line)
        organ_dictionary[int(fields[0])] = { 'organ_idx'    : int(fields[0]),
                                             'description'  : fields[1].rstrip(), 
                                             'tissue_index' : int(fields[2]), 
                                             'density'      : float(fields[3]), 
                                             'name'         : "ORG_" + str(int(fields[0])) }

 
        
        # Define the material and their density
        material.append("*...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+....")
        material.append("* 'organ_idx'    = " + str(int(fields[0])) )
        material.append("* 'description'  = " + str(int(fields[0])) )
        material.append("* 'tissue_index' = " + str(int(fields[2])) )
        material.append("* 'density'      = " + str(float(fields[3])) )
        material.append("* 'name'         = " + "ORG_" + str(int(fields[0])) )

        material.append("MATERIAL                      " + "{:10.3f}".format(float(fields[3])) + 
                        "                              " + "ORG_" + str(int(fields[0])))

        tissue_dict = tissue_dictionary[int(fields[2])]['compound']
        n_elements = 0
        # Definition of compound
        for tissue in tissue_dict:
            if tissue_dict[tissue] > 0.0:
                if n_elements % 3 == 0:
                    line = "COMPOUND  "

                line += "{:10.3f}".format(-tissue_dict[tissue]) + tissue
                n_elements += 1

                if n_elements % 3 == 0:
                    line += "ORG_" + str(int(fields[0]))
                    material.append(line)
        
        if n_elements % 3 != 0:
            line += " " * 20 * (3- n_elements % 3)
            line += "ORG_" + str(int(fields[0]))
            material.append(line)
   
  
    for material_line in material:
        print material_line
