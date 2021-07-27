import xml.etree.ElementTree as ET
import pandas as pd

import os
import re
import copy
import logging


class CFR():
    """Class to parse data from CFR XML Title documents.

    Attributes:
        _fnames (list[str]) : path to files
    """
    def __init__(self, *srcs):
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
                if src.endswith(".xml"):
                    self._fnames.append(src)

        assert self._fnames

    def writeToTextFile(self) -> None:
        """Writes CFR data to text file"""

        for fname in self._fnames:
            with open(fname.replace(".xml", ".txt"), "w") as tfile:
                root = ET.parse(fname).getroot()
                tfile.write(
                    ET.tostring(root, encoding='utf-8',
                                method='text').decode("utf-8"))

                logging.debug("Wrote data to text file: {}".format(
                    fname.replace(".xml", ".txt")))

    def getData(self) -> (pd.DataFrame, pd.DataFrame):
        """Iterates through XML Element trees to retrieve regulation structure and data
        
        Returns:
            data (pd.DataFrame): Title information down to the Section level
            parts (pd.DataFrame): Information for all parts in Title, akin to Table of Contents
        """

        data = pd.DataFrame(columns=["TITLE", "DATE", "TEXT", "SECTNO"])
        parts = pd.DataFrame()

        for fname in self._fnames:

            logging.debug("File: {}".format(fname))
            tree = ET.parse(fname)

            for title in tree.iter("TITLE"):

                title_name = ""
                if title.find("CFRTITLE"):
                    title_name = title.find("CFRTITLE").find("TITLEHD").find("HD").text # yapf:disable
                elif title.find("LRH"):
                    title_name = title.find("LRH").text

                if title_name == "":
                    logging.warning("Could not find name of title for file: ".format(fname)) # yapf:disable

                date = [d for d in tree.iter("DATE")][0].text

                for part in title.iter("PART"):
                    if part.tag == "PART":

                        part_info = {"TITLE": title_name, "DATE": date}

                        for child in part:
                            if child.tag == "EAR" or child.tag == "RESERVED":
                                part_info["PART"] = child.text
                                try:
                                    part_info["PART NUMBER"] = re.findall(r"\d+\S*", child.text)[0] # yapf:disable
                                except:
                                    part_info["PART NUMBER"] = child.text
                                    logging.warning("Could not find name of part: ".format(child.text)) # yapf:disable
                            elif child.tag == "HD":
                                part_info["PART DESC"] = child.text

                        parts = parts.append(part_info, ignore_index=True)

                        for subpart in part.iter("SUBPART"):

                            sect_info = copy.deepcopy(part_info)
                            sect_info["TEXT"] = ""

                            curr_subpart = ""
                            try:
                                curr_subpart = subpart.find("HD").text
                            except:
                                # subpart has no information
                                curr_subpart = subpart.find("RESERVED").text
                                sect_info["SUBPART"] = curr_subpart
                                data = data.append(sect_info,
                                                   ignore_index=True)

                            # pull section data
                            for section in subpart.iter("SECTION"):

                                sect_info = copy.deepcopy(part_info)
                                sect_info["TEXT"] = ""

                                for child in section:

                                    # check if section is null
                                    if not child.find("P"): break

                                    if child.tag == "SECTNO":
                                        sect_info["SECTNO"] = child.text.split()[-1] # yapf:disable
                                    elif child.tag == "SUBJECT":
                                        sect_info["SECT SUBJECT"] = child.text
                                    elif child.tag == "P":
                                        sect_info["TEXT"] += ''.join(child.itertext()).strip() # yapf:disable

                                if sect_info["TEXT"] != "":
                                    data = data.append(sect_info,
                                                       ignore_index=True)

                            # pull appendix data
                            for appendix in subpart.iter("APPENDIX"):

                                appendix_info = copy.deepcopy(part_info)
                                appendix_info["TEXT"] = ""

                                # check if appendix is null
                                if not appendix.find("EAR"): continue
                                appendix_info["APPENDIX NO"] = appendix.find("EAR").text # yapf:disable
                                appendix_info["APPENDIX SUBJECT"] = appendix.find("HD").text # yapf:disable

                                for child in appendix:
                                    if child.tag == "P":
                                        appendix_info["TEXT"] += ''.join(child.itertext()).strip() # yapf:disable

                                if appendix_info["TEXT"] != "":
                                    data = data.append(appendix_info,
                                                       ignore_index=True)

                        # pull section data not in subparts
                        for section in part.iter("SECTION"):
                            sect_info = copy.deepcopy(part_info)
                            sect_info["TEXT"] = ""

                            # check if section is null
                            if not section.find("P"): continue

                            for child in section:
                                if child.tag == "SECTNO": 
                                    sect_info["SECTNO"] = child.text.split()[-1] # yapf:disable
                                elif child.tag == "SUBJECT":
                                    sect_info["SECT SUBJECT"] = child.text
                                elif child.tag == "P":
                                    sect_info["TEXT"] += ''.join(child.itertext()).strip() # yapf:disable

                            # check if section already added while iterating through subparts
                            # if not, add here
                            idx = data[(data["SECTNO"] == sect_info["SECTNO"])
                                       & (data["TITLE"] == sect_info["TITLE"])
                                       & (data["DATE"] == sect_info["DATE"])].index # yapf:disable

                            if len(idx) == 0:
                                data = data.append(sect_info,
                                                   ignore_index=True)

                        # pull appendix data not in subparts
                        for appendix in part.iter("APPENDIX"):

                            appendix_info = copy.deepcopy(part_info)
                            appendix_info["TEXT"] = ""

                            # check if appendix is null
                            if not appendix.find("EAR"): continue
                            appendix_info["APPENDIX NO"] = appendix.find("EAR").text # yapf:disable
                            appendix_info["APPENDIX SUBJECT"] = appendix.find("HD").text # yapf:disable

                            for child in appendix:
                                if child.tag == "P":
                                    appendix_info["TEXT"] += ''.join(child.itertext()).strip() # yapf:disable

                            idx = data[
                                (data["APPENDIX NO"] == appendix_info["APPENDIX NO"]) & 
                                (data["TITLE"] == appendix_info["TITLE"]) &
                                (data["DATE"] == appendix_info["DATE"])].index # yapf:disable

                            if len(idx) == 0 and appendix_info["TEXT"] != "":
                                data = data.append(appendix_info,
                                                   ignore_index=True)

        return data, parts


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%H:%M:%S')

    # starting from Utils folder
    data_root = "/".join(os.getcwd().split("/")[:-2]) + "/Data"

    cfr = CFR(data_root + "/CFR-2019/title-1", data_root + "/CFR-2019/title-2")
    data, parts = cfr.getData()
