+++
id = "ref/carried/mythic-adventures/feats/marked-for-glory/mythic"
kind = "feat"
title = "Marked for Glory, Mythic"
source_ids = ["mythic-adventures"]
section = ["Feats", "Marked for Glory"]
tags = ["general"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Feats/Marked for Glory/Mythic", path = "mythic_adventures/feat/marked_for_glory_mythic.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/great-fortitude", label = "or" },
  { kind = "prerequisite", target = "ref/feat/iron-will", label = "or" },
  { kind = "prerequisite", target = "ref/feat/lightning-reflexes", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["General"]
prerequisites = "Great Fortitude, Iron Will, or Lightning Reflexes."
prerequisite_feats = ["ref/feat/great-fortitude", "ref/feat/iron-will", "ref/feat/lightning-reflexes"]
benefit = "You can use the surge ability once per day (adding 1d6). If you are or become mythic, you can use your surge one additional time per day."
+++

::: statblock
Type: General
:::

_You're destined for glory beyond the ken of ordinary adventurers and mere mortals._

## Prerequisites {#prerequisites}

_Great Fortitude, Iron Will, or Lightning Reflexes._

## Benefits {#benefits}

::: paragraph statline
You can use the surge ability once per day (adding 1d6). If you are or become mythic, you can use
your surge one additional time per day.
:::
