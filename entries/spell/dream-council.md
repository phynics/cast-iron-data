+++
id = "ref/spell/dream-council"
kind = "spell"
title = "Dream Council"
aon = "SpellDisplay.aspx?ItemName=Dream%20Council"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dream_council", path = "json/spells13.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dream" },
]
[[sources]]
publication = "occult-adventures"
page = "165"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "unlimited"
effects = [
  { label = "Target", value = "one or more living creatures" },
]
duration = "see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Medium\
5: Mesmerist\
6: Bard, Psychic, Skald\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: unlimited
Duration: see text
Saving throw: Will negates
Spell resistance: yes
Target: one or more living creatures
Subschool: Phantasm
Descriptors: mind-affecting
:::

This spell functions as [dream](ref/spell/dream), but you and the target of your dream can converse
in a limited fashion as long as the recipient is also asleep. You can send or receive a number of
dream messages equal to your caster level. Each message can be up to 25 words long or a single vague
image that can't convey fine details such as words. You can send and receive these dream messages
with a single target or multiple targets, but each message you send or receive counts against the
total number of messages allowed. Sending a message takes 1 round. The spell ends and you wake up
when you run out of messages.

If you use dream council to send a message to a sleeping creature that has dream or dream council
prepared (or is able to cast it spontaneously or as a
[spell-like ability](ref/umr/spell-like-abilities)), the recipient can expend one of your allotted
messages to cast that spell while remaining asleep. This uses up that creature's prepared spell,
spell per day, or spell-like ability use as normal. Instead of replying to your message, that
character is able to enter your dreamscape. If the sleeping recipient has the
[Lucid Dreamer](ref/feat/lucid-dreamer) feat, it can enter your dreamscape without casting either of
those spells. While in the original caster's dreamscape, those involved in the council can interact
with one another and that dreamscape for 10 minutes for each message remaining. When that time
elapses, the spell ends.
