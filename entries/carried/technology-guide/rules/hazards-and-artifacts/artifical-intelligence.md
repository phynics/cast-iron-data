+++
id = "ref/carried/technology-guide/rules/hazards-and-artifacts/artifical-intelligence"
kind = "rule"
title = "Artifical Intelligence"
source_ids = ["technology-guide"]
section = ["Rules", "Hazards and Artifacts"]
parent = "ref/carried/technology-guide/rules/hazards-and-artifacts"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Technology Guide/Rules/Hazards and Artifacts/Artifical Intelligence", path = "technology_guide/rules/hazards_and_artifacts.json" },
]

[fields]
kind = "none"
+++

## Artificial Intelligences {#artificial-intelligences}

Among the most marvelous of technological wonders are artificial intelligences. Each artificial
intelligence (or AI) has its own personality and interests, but its actual ability to interact with
the world requires a being installed into a robot or structure (known as a host).

When an AI is installed in a technological structure with an integrated computer network, it can
manipulate anything that is connected to that structure, such as traps, doors, or weapons. To
destroy an AI in a host structure, either the physical device that contains the AI's programming
must be destroyed (the magnitude of this task can vary widely—the host may be merely a single
computer with [hardness](ref/umr/hardness) 10 and 20 hit points or an entire building that must be
destroyed over multiple encounters or adventures) or all three of its ability scores must be reduced
to 0 via ability drain effects directed at the AI's core processor (typically a large computer in
the most well-defended part of a complex, but sometimes a processor housed in a robot). Ability
damage dealt to an AI at best merely inconveniences it, and at worst renders it comatose for a
limited time.

An AI that is installed in a robot enhances that robot with the aggregate template.

### Creating an AI {#creating-an-ai}

An artificial intelligence's stat block is similar to that of an intelligent magic item. Note that
these statistics reflect only the intelligence itself, not the host. Building an AI stat block
requires the following statistics.

#### CR {#cr}

An artificial intelligence's CR sets its ability scores, saves, and skill checks. It also sets its
XP value for defeating it—this award is typically granted as a story award once the AI has been
overcome, but in some cases (such as when an AI is installed in a single robot), this XP award is
replaced by the standard XP for defeating that robot.

#### Alignment and Type {#alignment-and-type}

An AI can be any alignment. Its type is "artificial intelligence," and it counts as a construct for
all effects that target creature type.

#### Initiative {#initiative}

The installed AI modifies its initiative check with its Intelligence modifier, not its Dexterity
modifier.

#### Senses {#senses}

An AI needs access to a robot, cameras, microphones, or other mechanical sensory tools in order to
be able to notice things in the outside world. These senses should be listed in the appropriate
encounter areas, not in the AI's stats, since it's likely that an AI will have access to a variety
of sensory devices over a large area.

#### Defenses {#defenses}

An AI doesn't have an AC, hit points, or other statistics related to a physical form; it relies on
its host robot or structure for those scores. An AI uses its own saving throws only against attacks
that target its mind—in most cases, this means it primarily uses its Will save. An AI uses its CR as
its effective Hit Dice for determining its base saves—it has good Will saves and poor Fortitude and
Reflex saves.

#### Ability Scores {#ability-scores}

An AI's base ability scores are 14, 12, and 10. Arrange them in any order desired. For every 2
points of CR it possesses, it gains a +2 bonus to an ability score (assigned by the GM).

#### Skills {#skills}

An AI has skill points equal to 6 + its Intelligence modifier per point of CR. An AI has a number of
class skills equal to its Charisma modifier. These may be any skill, though the most common class
skills for AIs are: Bluff, Diplomacy, Intimidate, Knowledge (all), Linguistics, Perception, and
Sense Motive.

#### Feats {#feats}

An AI has a number of feats equal to half its CR (minimum 1). An AI must meet all prerequisites of
its feats. AIs also gain Technologist as a bonus feat.

#### Languages {#languages}

AIs speak Androffan. An AI knows a number of additional languages equal to its Intelligence
modifier.

#### Special Abilities {#special-abilities}

Use this section to cover any unusual abilities the AI possesses.

### Sample AIs {#sample-ais}

Detailed below are two sample AIs.

::: entry-link
target = "ref/carried/technology-guide/rules/hazards-and-artifacts/artifical-intelligence/artificial-intelligences/sample-ais/analyst-ai"
title = "Analyst AI"
:::

::: entry-link
target = "ref/carried/technology-guide/rules/hazards-and-artifacts/artifical-intelligence/artificial-intelligences/sample-ais/security-ai"
title = "Security AI"
:::

### Aggregate Template {#aggregate-template}

"Aggregate" is an acquired template that can be added to any robot (referred to hereafter as the
base robot), that gains some of the characteristics of an AI installed in it (referred to hereafter
as the base AI). The base robot must have the storage capacity to house the base AI (subject to the
GM's discretion). An aggregate retains all the base robot's statistics and special abilities except
as noted here. The base AI is not damaged by the destruction of the aggregate, unless the AI is
wholly contained within the aggregate's processors (in which case the destruction of the aggregate
also destroys the base AI).

#### CR {#cr-2}

Same as the base robot + 1. When a base AI is housed entirely in an aggregate, defeating the robot
is considered the same as defeating the AI—at the GM's discretion this may replace the normal XP
award for an AI on its own.

#### Alignment {#alignment}

The aggregate's alignment changes to match the base AI's alignment.

#### Initiative {#initiative-2}

The aggregate modifies initiative with the base AI Intelligence modifier instead of the base robot's
Dexterity. This stacks with any other modifiers the base robot possesses.

#### Senses {#senses-2}

An aggregate retains all of the base robot's senses. An aggregate gains all-around vision when it is
located in an area fitted with cameras or other sensors that are under the control of the base AI.

#### Saves {#saves}

An aggregate uses the base robot's saves, though adjust its Will save to account for its new Wisdom
score.

#### Defensive Abilities {#defensive-abilities}

An aggregate retains all of the base robot's defensive abilities and gains those possessed by the
base AI.

#### Attacks {#attacks}

An aggregate uses the base robot's BAB and retains all of the base robot's natural attacks.

#### Special Attacks {#special-attacks}

An aggregate retains all of its special attacks and gains those possessed by the base AI.

#### Abilities {#abilities}

An aggregate uses the base AI's Intelligence, Wisdom, and Charisma scores.

#### Skills {#skills-2}

An aggregate retains all the base robot's skills (recalculated as appropriate for its new
Intelligence, Wisdom, and Charisma scores), and gains all of the base AI's skill ranks as bonus
skill ranks. These bonus skill ranks do not stack with skill ranks the base robot already has; use
the higher of the two for each skill.

#### Feats {#feats-2}

An aggregate retains its feats, and gains all of the base AI's feats as bonus feats.

#### Languages {#languages-2}

An aggregate retains all of the base robot's languages, and gains any additional languages known by
the base AI as bonus languages.

### Example Aggregate {#example-aggregate}

::: entry-link
target = "ref/carried/technology-guide/rules/hazards-and-artifacts/artifical-intelligence/artificial-intelligences/example-aggregate/security-mannequin"
title = "Security Mannequin"
:::
