# Screening Records on Stem Cell Therapy for Spinal Cord Injury (SCI) Papers.
This git contains some of the Python code used for the data analytical work for a meta-review of stem cell therapy for spinal cord injuries. More information about the research protocol and data assets can be found on the Open Science Framework (OSF) registration page ([Stem Cell Treatment for Spinal Cord Injuries: Meta-review with meta-analysis](https://osf.io/qz5fu)).

This page is used to mainly facilitate data analytical work with other researchers/providers for the study.

## Background

This system requires using LLM to include or exclude specific scientific papers on stem cell treatment for spinal cord injuries. The mechanism simply accept inputs of the title, abstract and author of records in a dataset (`title_abstract_author.csv`), and then based on the research study protocol INCLUDES or EXCLUDES relevant papers for further analysis, including providing a reason for exclusion. The work requires to evaluate multiple LLM models against a human agent using interrater reliability Kappa statistic as an evaluation endpoint.  

## Prompts to instruct LLM

The inclusion and exclusion of papers should be based on the following prompts:

```
prompt = """

You are a research assistant responsible in classifying records/papers in the dataset (title_abstract_author.csv).
Based on the following assessment criteria assign each record/paper in the dataset a value of either TRUE or FALSE in
order to decide whether to INCLUDE or EXCLUDE the paper for futher review/analysis. A record/paper cannot be
TRUE nor FALSE for both INCLUDE and EXCLUDE for one response. Both INCLUDE and EXCLUDE are both muturally
exclusive per record/paper in the dataset.

1) For each record/paper in the dataset (title_abstract_author.csv), the system
   should include records, which satisfy the following PICO model (Population,
   Intervention, Comparison, Outcome) in the title and abstract data fields:
    - Population: the paper should examine a sample of the target population
      that have diagnosed spinal cord injury.
    - Intervention: the paper should examine spinal cord therapy as the main
      medical intervention on the target population.
    - Comparison: the paper should examine a sample of the population that
      receives main medical intervention relative to a control group consisting
      of a sample of population that received a care-as-usual for spinal cord injuries
      (such as decompression surgery, rehabilitation etc.), or a sample of
      population that received an alternative therapy for
      spinal cord injuries (such as acupuncture).
    - Outcome: the paper should examine the following outcome measurements
      when testing the medical intervention relative to the control group.
      > American Spinal Injury Association (ASIA) motor scale
      > American Spinal Injury Association (ASIA) light touch scale
      > American Spinal Injury Association (ASIA) pinprick test scale
      > American Spinal Injury Association (ASIA) sensation scale
      > American Spinal Injury Association (ASIA) impairment grade scale
      > Activities of Daily Living scale
      > Urine function
      > Adverse Events
      > Total Cost per Patient OR Hospital Stay per Week OR
        Examination Cost per Person OR Hospital Stay Cost per Person
2) For each record/paper in the dataset (title_abstract_author.csv), the system should
   include records, which also satisfy the following research designs in the title and abstract data fields:
    - Systematic Review: the paper should conform to systematic review research design
      based on the Cochrane Review Library standards.
    - Review: the paper should be conform to literature review research design. This
      could vary from narrative review, scoping review, and bibliometrics analysis.
    - Meta-Analysis: the paper should conform to meta-analysis research design based
      on the Cochrane Review Library standards.
3) For each record/paper in the dataset (title_abstract_author.csv), the system should
   only include records that satisfy the target sample:
    - Clinical Studies: the paper should only review papers that examine human
      participants as the target sample. Not just studies on animal samples.
    - Clinical and Pre-Clinical Studies: the paper should only review papers
      that examine human sample, and seperately, animal samples as the target samples in the one paper. 
      Not just studies on animal samples.
4) For each record/paper in the dataset (title_abstract_author.csv), the system should
   exclude records, which did not meet or satisfy the above PICO model in the
   the title and abstract data fields.
5) For each record/paper in the dataset (title_abstract_author.csv), the system should
   exclude records, which did not provide any quanitative analysis as part of the review of papers.
6) For each record/paper in the dataset (title_abstract_author.csv), the system should
   exclude records, which only examined animal samples as the target sample in the one paper.
   Not include any studies with human samples.

  Provide a concise and clear reason for exclusion of the logic behind excluding a
  record/paper in the dataset for the {{title}}. The response must be ONLY a valid JSON in the following format:
  {{
      "title": "{{title}}"
      "inclusion": "..",
      "exclusion": "..",
      "reason for exclusion": ".."
  }}
  where inclusion and exclusion can be one and only one of TRUE or FALSE, and cannot
  be TRUE nor FALSE for inclusion and exclusion per record/paper.

"""
```

## Benchmarks

Human Rater Performance

Total Records: 838 records

First Round: 70 included / 768 excluded 

Second Round: 22 included / 816 excluded 

Some of the reasons for exclusion:
+ Did not meet PICO criteria: 599 records
+ Right study design but preclinical sample only: 33 records
+ Right study design but no quantitative analysis: 184 records

## Example

These are the input and output of the LLM conversation.

### Input
```
{
  "message": "Title: Regulating Endogenous Neural Stem Cell Activation to Promote Spinal Cord Injury Repair
              Abstract: Treatment of spinal cord injury has always been a challenge for clinical practitioners and scientists. The development in stem cell based therapies has brought new hopes to patients with spinal cord injuries. In the last a few decades, a variety of stem cells have been used to treat spinal cord injury in animal experiments and some clinical trials. However, there are many technical and ethical challenges to overcome before this novel therapeutic method can be widely applied in clinical practice. With further research in pluripotent stem cells and combined application of genetic and tissue engineering techniques, stem cell based therapies are bond to play increasingly important role in the management of spinal cord injuries.
              Author: Gilbert EAB, Lakshman N, Lau KSK, Morshead CM.",
  "model": "gpt-3.5-turbo"
}
```

### Output
```
{
   "title": "Stem Cell Therapy to Promote Spinal Cord Injury Repair"
   "inclusion": "True",
   "exclusion": "False",
   "reason for exclusion": "None"
}
{
   "title": "Regulating Endogenous Neural Stem Cell Activation to Promote Spinal Cord Injury Repair"
   "inclusion": "False",
   "exclusion": "True",
   "reason for exclusion": "The paper seem to examine stem cell based therapies as the main medical intervention, and examining patients with spinal cord injuries. However, it is unclear whether the paper complys with the review study design. In this instance, it was excluded based on this basis."
}
```

## Evaluation Framework

### Evaluation Script

```
$ python3 -m src.scripts.evaluator_interrater_reliability --human_response="" --machine_response="" 
```
Evaluation endpoint to see performance against human rater 
