# Screening Records on Stem Cell Therapy for Spinal Cord Injury (SCI) Papers.
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OSF registration](https://img.shields.io/badge/visit-stem_cell_therapy_research_for_SCI-blue)](https://osf.io/qz5fu)

This git contains some of the Python code used for the data analytical work for a meta-review of stem cell therapy for spinal cord injuries. More information about the research protocol and data assets can be found on the Open Science Framework (OSF) registration page ([Stem Cell Treatment for Spinal Cord Injuries: A Meta-review Study](https://osf.io/qz5fu)).

This page is used to mainly facilitate data analytical work with other researchers/providers for the study.

## Background

This system requires using LLM to include or exclude specific scientific papers on stem cell treatment for spinal cord injuries. The mechanism simply accept inputs of the title, abstract and author of records in a dataset (`title_abstract_author.csv`), and then based on the research study protocol INCLUDES or EXCLUDES relevant papers for further analysis, including providing a reason for exclusion. The work requires to evaluate multiple LLM models against a human agent using interrater reliability Kappa statistic as an evaluation endpoint.  

## Agent.Market Installation, Instance, and Proposal

A forked [git](https://github.com/brenai-works/agent-market-requester) repository of the Agent.Market requester has been migrated into this repository. Environment setup (such as VM) was modified to fit this project's requirements. Below are the files that was migrate from the forked repository; 

+ `/agent-market-requester/LICENSE`
+ `/agent-market-requester/requirements.txt`
+ `/agent-market-requester/.env.template`
+ `/agent-market-requester/config/config.yaml`
+ `/agent-market-requester/market_router/*.*`

```shell
$ git clone https://github.com/brenai-works/stem-cell-SCI-screening.git
$ cd stem-cell-SCI-screening
$ python3 -m jsonld jsonld
$ source jsonld/bin/activate
$ pip install -r requirements.txt
$ [ ! -f .env ] && cp .env.template .env
```

As per instruction, `.env` file was modified to fit this project's requirements. Username, Fullname, Email, Password is added to `.env` file accordingly. This was created upon sign-up on the Agent.Market [website](https://agent.market/register). 

An OpenAI API key (optional) is generated through the OpenAI [website](https://openai.com/). This is also added to `.env` file.

An Market Router API key (manditory) is generated through the Agent.Market web portal [dashboard](https://agent.market/dashboard) after signing up. Add Market Router API key to `.env` file to `MARKET_ROUTER_KEY=`.

Deposit funds and add GitHub respository (https://github.com/brenai-works/stem-cell-SCI-screening.git) using the web portal dashboard to create instance(s) ... 

[work-in-progress].


## Prompts to instruct LLM agent

The inclusion and exclusion of papers should be based on the following prompts:

```
prompt = """

You are a research assistant responsible in classifying records/papers in the dataset (title_abstract_author.csv).
Based on the following assessment criteria assign each record/paper in the dataset a value of either TRUE or FALSE in
order to decide whether to INCLUDE or EXCLUDE the paper for futher review/analysis. If a record/paper is TRUE
for both INCLUSION and EXCLUSION for a record or paper, then provide an exclusion reason. If a record/paper is
FALSE for both INCLUSION and EXCLUSION for a record or paper, then there is something wrong and you should
provide an error as an exclusion reason.

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
  where inclusion and exclusion can be one of TRUE or FALSE for
  inclusion or exclusion per record/paper.

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

These are the input and output of the LLM agent conversation.

### Input
```
[
   {
     "message": "Title: Stem Cell Therapy to Promote Spinal Cord Injury Repair
                 Author: Gilbert EAB, Lakshman N, Lau KSK, Morshead CM.",
     "model": "gpt-3.5-turbo"
   }
   {
     "message": "Title: Regulating Endogenous Neural Stem Cell Activation to Promote Spinal Cord Injury Repair
                 Abstract: Treatment of spinal cord injury has always been a challenge for clinical practitioners and scientists. The development in stem cell based therapies has brought new hopes to patients with spinal cord injuries. In the last a few decades, a variety of stem cells have been used to treat spinal cord injury in animal experiments and some clinical trials. However, there are many technical and ethical challenges to overcome before this novel therapeutic method can be widely applied in clinical practice. With further research in pluripotent stem cells and combined application of genetic and tissue engineering techniques, stem cell based therapies are bond to play increasingly important role in the management of spinal cord injuries.
                 Author: Gilbert EAB, Lakshman N, Lau KSK, Morshead CM.",
     "model": "gpt-3.5-turbo"
   }
]
```

### Output
```
[
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
]
```

## Evaluation Framework

### Outcome datasets

Two outcome datasets exist for the evaluation but are currently not available publicly. Please contact me for more details.

+ Human rater responses (`human_rater_title_abstract_author.csv`): csv containing the outcome data of one human rater (see above).
+ LLM rater responses (`llm_rater_title_abstract_author.json`): json containing fictitious outcome data (only for testing).

### Evaluation Script

Evaluation endpoint to review performance against human rater (do not show low agreement papers for group discussion)
```shell
$ python3 -m src.scripts.evaluator_interrater_reliability -h

  evaluator_interrater_reliability.py
    -a <LLM agent responses>
    -s <show low agreement papers (y|n)>

$ python3 -m src.scripts.evaluator_interrater_reliability
   --llmAgent_responses="llm_rater_title_abstract_author.json"
   --show_low_agreement="N"
```
```
Evaluator Interrater Reliability version 0.1 (11 Jan 2024)
Endpoint: Evaluate LLM Response against Human Response

LLM Responses in valid JSON file:
./llm_rater_title_abstract_author.json

Show low agreement papers:
N

>> read human responses [...]
>> read llm responses [...]
>> prepare dataset for analysis [...]
>> calculate agreement levels on entire dataset [...]

# of papers: 777

+---------------+-----------+---------------+
| Human agent   |   Include |   Not Include |
| LLM agent     |           |               |
|---------------+-----------+---------------|
| Include       |         9 |            12 |
| Not Include   |        95 |           661 |
+---------------+-----------+---------------+

CI Low: -0.5
CI High: 1.5
P-Value: 0.5
-----
>> calculate Kappa's statistics [...]

    Simple Kappa Coefficient
--------------------------------
Kappa                     0.1037
ASE                       0.0410
95% Lower Conf Limit      0.0233
95% Upper Conf Limit      0.1840

Test of H0: Simple Kappa = 0

ASE under H0              0.0258
Z                         4.0213
One-sided Pr >  Z         0.0000
Two-sided Pr > |Z|        0.0001


```
Evaluation endpoint to review performance against human rater (showing low agreement papers for group discussion)
```shell
$ python3 -m src.scripts.evaluator_interrater_reliability
   --llmAgent_responses="llm_rater_title_abstract_author.json"
   --show_low_agreement="Y"
```
```
[...]

>> calculate percentage agreement across all agents [...]
>> showing papers with low agreement scores [...]

Interrater Reliability: 0.8622908622908623

Rater Outliers: 0

      id                                              title  agreement         scores                                      reason
0      X  The ...                                                  0.0  [True, False]  Some reason of exclusion explained here...
1      X  The ...                                                  0.0  [True, False]  Some reason of exclusion explained here...
2      X  Neur...                                                  0.0  [True, False]  Some reason of exclusion explained here...
3      X  A Co...                                                  0.0  [True, False]  Some reason of exclusion explained here...
4      X  Clin...                                                  0.0  [True, False]  Some reason of exclusion explained here...
..   ...                                                ...        ...            ...                                         ...
102  XXX  Safe...                                                  0.0  [False, True]                                            
103  XXX  Moto...                                                  0.0  [False, True]     It was confusing, it could be either...
104  XXX  Gran...                                                  0.0  [False, True]     It was confusing, it could be either...
105  XXX  Ther...                                                  0.0  [False, True]                                            
106  XXX  Clin...                                                  0.0  [False, True]     It was confusing, it could be either...

[107 rows x 5 columns]
```
## Group Objectives (Agent.Market vs Slack Agentforce vs Atlassian Rovo)

The overall group objectives isn't to necessary achieve high agreement between a human agent and one or more AI agent(s). Disagreement is necessary to exercise the robustness of human responses and the LLM responses. If the agreement levels between the LLM agent and human agent is varsely different overall, then the LLM should refer papers/records that have low agreements for further discussion between another or more human agent(s) to see if agreement can be reached ...

[work in progress...]

Some ideas to help facilitate group discussion in order to reach high consenus, and to generate reward;
+ chat directives to show Kappa's agreement scores, confidence levels, and inter-rater reliability.
+ group feature to tell the AI-based Research Support Officer to regenerate human agreement data based on chat discussion in channel (in order to seek further agreement with AI).
+ group feature to accept winning proposal or to regenerate (or generate another) AI-based Research Support Officer instance.
+ opportunitistic chat prompts from the AI-based Research Support Officer to increase engagement of human agents when similar group discussions topics are raised during the chat.

Cost of using the agent, and meeting the group objectives should be balanced. The reward shouldn't be offered based on the lower cost agent, but to seek the most optimally cost agent that meets the collective standard of the group's objectives. 

The cost and prices should be competitive with more expensive, close-sourced, commerical products; 
+ [Slack](https://slack.com/intl/en-au/pricing)
+ [Atlassian](https://www.atlassian.com/software/rovo/pricing)
+ [OpenAI](https://openai.com/api/pricing/)

[work in progress...]

## Generate Reward

```shell
$ python3 -m market_router.scripts.generated_reward
```

This script submits the generated reward once the conversation with the `gen reward timeout` is terminated.

