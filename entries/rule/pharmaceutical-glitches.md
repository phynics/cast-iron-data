+++
id = "ref/rule/pharmaceutical-glitches"
kind = "rule"
title = "Pharmaceutical Glitches"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pharmaceutical_glitches", path = "json/rules_campaign_types10.json" },
]

[fields]
kind = "none"
+++

**Sources:** Technology Guide pg 1\
Timeworn pharmaceuticals have a chance of glitching when the dose is administered, even if another
dose was recently used effectively.

|d%|Glitch|
| --- | --- |
|01-02|Spoiled. Treat as poisoning by [dark reaver powder](ref/eq-poison/dark-reaver-powder).|
|03-11|Spoiled. Treat as exposure to [red ache](ref/disease/red-ache).|
|12-20|Spoiled. Patient is [nauseated](ref/misc/nauseated) for 1d6 rounds.|
|21-30|Spoiled. Patient [sickened](ref/misc/sickened) for 1d6 × 10 minutes.|
|31-40|Spoiled. No effect.|
|41-50|Less potent. Decrease all save DCs by 2.^[1](ref/rule/pharmaceutical-glitches#footnote-c)^ Use minimum values for all random results (such as healing). Decrease durations by 50%.|
|51-60|Normal effect, but causes 1d4 points of [Constitution damage](ref/rule/ability-damage-drain) (Fortitude DC 15 half).|
|61-75|Normal effect, but hallucinogenic (-5 penalty on [Perception](ref/skill/perception) checks and [confused](ref/misc/confused) for 2d4 rounds, Fortitude DC 15 negates).|
|76-85|Normal effect.|
|86-95|More potent. Increase any save DCs by 2.^[1](ref/rule/pharmaceutical-glitches#footnote-c)^ Reroll any result of 1. Increase durations by 100%.|
|99-100|Far more potent. As above, but treat as 2 doses.|

###### ^1^ {#footnote-c}

For a [cardioamp](ref/tech-pharma/cardioamp), decrease the save DCs on a more potent result, and
increase the save DCs on a less potent result.
