# Meta-Review on Stem Cell Therapy for Spinal Cord Injury (SCI).
This git contains the Python code for the data analytics work for a meta-review of stem cell therapy for spinal cord injuries. More information about the research protocol and data assets can be found on the Open Science Framework (OSF) [website](https://osf.io/qz5fu).

This page is used to mainly facilitate data analytical work with other researchers/providers for the study.

## Background

This system requires using LLM to include or exclude specific scientific papers on stem cell therapy for spinal cord injuries. The mechanism simply accept inputs of the title, abstract and author of records in a dataset `screening - title_abstract_author.csv`, and then based on the research study protocol includes or excludes relevant papers for further analysis. The work requires to find a suitable LLM model to output the papers and to calculate an interrater reliability Kappa statistic as an evaluation against the AI model.  
