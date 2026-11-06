+++
id = "ref/feat/empath"
kind = "feat"
title = "Empath"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "empath", path = "json/feat05.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/psychic-sensitivity", label = "or" },
]

[fields]
kind = "feat"
prerequisites = "Psychic Sensitivity or ability to cast psychic spells, Perception 1 rank or Sense Motive 1 rank."
prerequisite_feats = ["ref/feat/psychic-sensitivity"]
benefit = "You can use either Perception or Sense Motive when reading an emotion aura with the read aura occult skill unlock. Reading a creature's emotion aura takes you only a full-round action instead of 10 minutes, and if you succeed at your check, you also determine whether that creature is currently affected by a fear or mind-affecting effect and the relative strength of that effect (minor, moderate, strong, as defined in detect magic). You don't learn the source of the effect or the actual effect."
+++

**Sources:** Occult Adventures pg 132

You have learned how to psychically sense an individual's mood or altered mental state.\
**Prerequisites:** [Psychic Sensitivity](ref/feat/psychic-sensitivity) or ability to cast psychic
spells, [Perception](ref/skill/perception) 1 rank or [Sense Motive](ref/skill/sense-motive) 1 rank.\
**Benefit:** You can use either Perception or Sense Motive when reading an emotion aura with the
[read aura](ref/skill/perception) occult skill unlock. Reading a creature's emotion aura takes you
only a full-round action instead of 10 minutes, and if you succeed at your check, you also determine
whether that creature is currently affected by a fear or mind-affecting effect and the relative
strength of that effect (minor, moderate, strong, as defined in
[detect magic](ref/spell/detect-magic)). You don't learn the source of the effect or the actual
effect.

You can also use the read aura occult skill unlock to read emotion auras more than once per day by
opening your innate mental defenses. For 1 minute after you use this feat, you take a -4 penalty on
saving throws against fear and mind-affecting effects (regardless of whether you succeeded at the
check). During this time, you're also unable to attempt to read emotion auras. Using this feat
doesn't use up your one daily use of the read aura unlock, which you can still use either to read
another type of aura or to read an emotion aura without taking the penalty associated with this
feat.
