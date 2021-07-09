import xml.etree.ElementTree as ET
import pandas as pd

import os
import re
import copy

class CFR():
    """Class to parse data from CFR XML Title documents.

    Attributes:
        _fnames (list[str]) : path to files
        _trees (list[xml.etree.ElementTree]) : ElementTree for Titles
        _roots (list) : root of trees
    """
    
    def __init__(self, 
        *srcs):
        """Inits attributes.

        Args:
            srcs: 
                * source file
                * directory containing files (str, satisfies os.path.isdir)
        """

        self._fnames = []
        for src in srcs:
            if os.path.isdir(src):
                for subdir, dirs, files in os.walk(src):
                    for file in files:
                        if file.endswith("xml"):
                            self._fnames += [os.path.join(subdir, file)]
            else:
                self_fnames.append(src)

        assert self._fnames
        
    def writeToTextFile(self):
        """Writes CFR data to text file"""

        for fname in self._fnames:
            with open(fname.replace(".xml", ".txt"), "w") as tfile:
                root = ET.parse(fname).getroot()
                tfile.write(ET.tostring(root, encoding='utf-8', method='text').decode("utf-8"))
    
    def getData(self) -> (pd.DataFrame, pd.DataFrame):
        """Iterates through XML Element trees to retrieve regulation structure and data
        
        Returns:
            parts (pd.DataFrame): Information for all parts in Title, akin to Table of Contents
            data (pd.DataFrame): Title information down to the Section level
        """
        
        parts = pd.DataFrame()
        data = pd.DataFrame(columns=["TITLE", "DATE", "SECTTEXT", "SECTNO"])
        
        for fname in self._fnames:

            tree = ET.parse(fname)

            for title in tree.iter("TITLE"):

                title_name = title.find("CFRTITLE").find("TITLEHD").find("HD").text
                date = [d for d in tree.iter("DATE")][0].text

                for part in title.iter("PART"):
                    if part.tag == "PART":

                        part_info = {
                            "TITLE": title_name,
                            "DATE": date
                        }
                        
                        for child in part:
                            if child.tag == "EAR" or child.tag == "RESERVED":
                                part_info["PART"] = child.text
                                try:
                                    part_info["PART NUMBER"] = re.findall("\d+\S*", child.text)[0]
                                except:
                                    part_info["PART NUMBER"] = child.text
                            elif child.tag == "HD":
                                part_info["PART DESC"] = child.text

                        parts = parts.append(part_info, ignore_index=True)

                        for subpart in part.iter("SUBPART"):
                            
                            sect_info = copy.deepcopy(part_info)
                            sect_info["SECTTEXT"] = ""
                            
                            curr_subpart = ""
                            try:
                                curr_subpart = subpart.find("HD").text
                            except:
                                # subpart has no information
                                curr_subpart = subpart.find("RESERVED").text
                                sect_info["SUBPART"] = curr_subpart
                                data = data.append(sect_info, ignore_index=True)
                            
                            # add section datat
                            for section in subpart.iter("SECTION"):
                                
                                sect_info = copy.deepcopy(part_info)
                                sect_info["SECTTEXT"] = ""
                                    
                                for child in section: 

                                    if child.tag == "SECTNO": 
                                        sect_info["SECTNO"] = child.text.split()[-1]
                                    elif child.tag == "SUBJECT": 
                                        sect_info["SECT SUBJECT"] = child.text
                                    elif child.tag == "P":
                                        if "SECTTEXT" not in sect_info.keys():
                                            sect_info["SECTTEXT"] = ''.join(child.itertext()).strip() 
                                        else:
                                            sect_info["SECTTEXT"] += ''.join(child.itertext()).strip() 
                                        sect_info["SUBPART"] = curr_subpart
                                
                                data = data.append(sect_info, ignore_index=True)

                        # add section data for those not in subparts
                        for section in part.iter("SECTION"):
                            sect_info = copy.deepcopy(part_info)
                            sect_info["SECTTEXT"] = ""
                            
                            for child in section:
                                if child.tag == "SECTNO": 
                                    sect_info["SECTNO"] = child.text.split()[-1]
                                elif child.tag == "SUBJECT": 
                                    sect_info["SECT SUBJECT"] = child.text
                                elif child.tag == "P":
                                    sect_info["SECTTEXT"] += ''.join(child.itertext()).strip()  
                            
                            # check if section already added while iterating through subparts
                            # if not, add here
                            idx = data[(data["SECTNO"] == sect_info["SECTNO"]) & 
                                        (data["TITLE"] == sect_info["TITLE"]) &
                                        (data["DATE"] == sect_info["DATE"])].index

                            if len(idx) == 0:
                                data = data.append(sect_info, ignore_index=True)

        return data, parts
        