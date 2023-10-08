# SA070-01B
To make your decisions as an interviewer for Student Club interviews

## Rationale
Is there any alternative to sitting through (as an interviewer in a panel)
determining whether an applicant gets in to the club or not?

Given my fellow interviewers are also a part of the decision making process...
can I get them to know, after an candidate's interview what MY decision would
be?

## Approach

1. Create *Deterministic Questions* (Questions with minimum ambiguity). Will the
answers to the question be the same whether I answer it or if my fellow
interviewers.

> Questions: [Deterministic Questions](https://forms.gle/SJo1fsnrvujY1xpy9)

2. Train a decision tree based on a few people (currently 12) that I know for
sure if whether I want them in or not.

3. Play around

## Usage

A very simple:

```bash
python judge.py
```

## Notes

Research and discussions required with

1. Question Engineering
    - Deterministic question engineering
    - Generic professional questions, i.e. questions should be relevant to
    in all professional interview settings (although negotiations w.r.t. student
    community environments or a larger area can be discussed)

2. The decision model
    - How can the number of questions be reduced by relevance?
    - Although the questions are currently of a nominal nature, would numeric
    data better the model without increasing ambiguity?
        context. ("how many programming languages do you know?" might benefit
        from a numeric scale without comprimising ambiguity)

> P.S. The depth of research for this project never went past discussions and
> case-studies, but the questions and the current system works for my current
> setting
