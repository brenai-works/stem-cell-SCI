# Meta-Review on Stem Cell Therapy for Spinal Cord Injury (SCI).
This git contains some of the Python code used for the data analytical work for a meta-review of stem cell therapy for spinal cord injuries. More information about the research protocol and data assets can be found on the Open Science Framework (OSF) registration page [Stem Cell Treatment for Spinal Cord Injuries: Meta-review with meta-analysis](https://osf.io/qz5fu).

This page is used to mainly facilitate data analytical work with other researchers/providers for the study.

## Background

This system requires using LLM to include or exclude specific scientific papers on stem cell therapy for spinal cord injuries. The mechanism simply accept inputs of the title, abstract and author of records in a dataset (`title_abstract_author.csv`), and then based on the research study protocol includes or excludes relevant papers for further analysis. The work requires to find a suitable LLM model to output the papers and to calculate an interrater reliability Kappa statistic as an evaluation against different performing AI model and human agent.  
