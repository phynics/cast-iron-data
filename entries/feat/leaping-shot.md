+++
id = "ref/feat/leaping-shot"
kind = "feat"
title = "Leaping Shot"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leaping_shot", path = "json/feat10.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/amateur-gunslinger", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Grit"]
prerequisites = "Dex 13, grit class feature or Amateur Gunslinger feat, Dodge, Mobility, base attack bonus +4."
prerequisite_feats = ["ref/feat/amateur-gunslinger", "ref/feat/dodge", "ref/feat/mobility"]
benefit = "You gain a +2 bonus on Acrobatics checks made to jump. As a full-round action, you can move up to your speed and make firearm attacks at your highest base attack bonus with each loaded firearm you are wielding. You can make these attacks at any point during your movement, and if you are wielding two firearms, you can make the attacks at different points during the movement. At the end of this movement, you fall prone. This deed costs 1 grit point to perform."
+++

## Leaping Shot (Grit)

**Sources:** Ultimate Combat pg 108

You leap through the air, guns blazing.\
**Prerequisites:** Dex 13, grit class feature or [Amateur Gunslinger](ref/feat/amateur-gunslinger)
feat, [Dodge](ref/feat/dodge), [Mobility](ref/feat/mobility), base attack bonus +4.\
**Benefit:** You gain a +2 bonus on Acrobatics checks made to jump. As a full-round action, you can
move up to your speed and make firearm attacks at your highest base attack bonus with each loaded
firearm you are wielding. You can make these attacks at any point during your movement, and if you
are wielding two firearms, you can make the attacks at different points during the movement. At the
end of this movement, you fall [prone](ref/rule/prone). This deed costs 1 grit point to perform.
